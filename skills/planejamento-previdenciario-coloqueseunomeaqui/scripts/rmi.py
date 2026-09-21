#!/usr/bin/env python3
"""
rmi.py — média dos salários de contribuição, coeficiente e teste de descarte.

Por que existe: o parecer precisa mostrar a conta, não o resultado de uma calculadora. Aqui a
média, o coeficiente e o descarte do art. 26, § 6º da EC 103 saem explícitos e reproduzíveis.

Uso:
    python3 rmi.py salarios.csv --tempo-dias 9500 --limiar 15 [--fatores fatores.csv]
                               [--sem-teto | --teto 8157.41] [--json]
                               [--descarte [--competencias-magisterio mag.txt]
                                           [--folga-magisterio-dias N]]

--limiar é OBRIGATÓRIO (15 mulher no RGPS / 20 caso geral): o default silencioso de 20 já produziu
76% onde o correto era 86%, sem aviso nenhum.

DESCARTE E TEMPO DE MAGISTÉRIO: o descarte confere o tempo TOTAL contra --tempo-minimo-dias. Ele
só conhece o tempo QUALIFICADO se você passar --competencias-magisterio (lista das competências de
magistério) e --folga-magisterio-dias (quanto tempo de magistério sobra acima do exigido). Sem
isso, ele avisa em stderr que a conferência do tempo de professor é MANUAL — e continua sendo.

salarios.csv:  competencia,valor           (competencia no formato AAAA-MM)
fatores.csv:   competencia,fator           (fator de atualização monetária daquela competência)

IMPORTANTE — atualização monetária: sem --fatores, o script calcula sobre valores NOMINAIS e
marca o resultado como `atualizado: false`. Um número não atualizado NÃO vai para o parecer.
Puxe a tabela de atualização vigente (INSS/Dataprev) e passe-a em --fatores, registrando a
data-base no relatório.

TETO — histórico embutido: por padrão o script aplica o TETO DO RGPS VIGENTE NA PRÓPRIA
COMPETÊNCIA (tabela `tetos_historicos.csv`, ao lado deste arquivo — ver
`references/teto-inss-historico.md` para a fonte e a data da última conferência) ao valor
NOMINAL, antes de corrigir monetariamente. Essa ordem importa: a lei limita o salário de
contribuição pelo teto vigente NA ÉPOCA, não pelo teto de hoje. Aplicar o teto de hoje sobre o
valor já corrigido (como uma versão anterior deste script fazia) capa errado qualquer competência
antiga com remuneração alta — use --sem-teto só para depuração, nunca para o número do parecer.
Passe --teto para forçar um valor único fixo em todas as competências (raro; documente o motivo).

--limiar 15 ou 20: o número de anos a partir do qual incidem os 2 pontos percentuais do art. 26,
§ 2º e § 5º da EC 103. Confira o § 5º na fonte antes de escolher — é ele que define se o
professor homem parte de 15 ou de 20 anos.
"""

import argparse
import csv
import json
import os
import sys

PBC_INICIO = "1994-07"
TETOS_PADRAO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tetos_historicos.csv")


def num(s):
    """Aceita 1.234,56 (pt-BR) e 1234.56 (ponto decimal) sem confundir os dois."""
    s = str(s).strip()
    if "," in s:                      # pt-BR: ponto é separador de milhar
        s = s.replace(".", "").replace(",", ".")
    return float(s)


def ler_csv(caminho, campo):
    out = {}
    with open(caminho, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            out[row["competencia"].strip()] = num(row[campo])
    return out


def ler_competencias(caminho):
    """Lê uma lista de competências: uma AAAA-MM por linha (aceita CSV — usa a 1ª coluna e
    ignora cabeçalho e qualquer linha que não tenha a cara de competência)."""
    out = set()
    with open(caminho, encoding="utf-8") as f:
        for linha in f:
            c = linha.strip().split(",")[0].strip()
            if len(c) == 7 and c[4] == "-" and c[:4].isdigit() and c[5:].isdigit():
                out.add(c)
    return out


def ler_tetos(caminho):
    """Lê tetos_historicos.csv (competencia de VIGÊNCIA -> teto) e devolve lista ordenada
    [(vigencia, valor), ...] para lookup por competência (usa o último teto com vigencia <=
    competência)."""
    out = []
    with open(caminho, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            out.append((row["vigencia"].strip(), num(row["teto"])))
    out.sort(key=lambda t: t[0])
    return out


def teto_da_competencia(comp, tetos):
    """Teto vigente numa competência: o último valor cuja vigência é <= comp. Competência
    anterior à primeira vigência da tabela não tem teto aplicável (retorna None)."""
    aplicavel = None
    for vigencia, valor in tetos:
        if vigencia <= comp:
            aplicavel = valor
        else:
            break
    return aplicavel


def coeficiente(tempo_dias, limiar_anos):
    """60% + 2 p.p. por ano completo que exceder o limiar, LIMITADO A 100% da média.

    A EC 103 não escreve o teto de 100%, mas o benefício é uma fração do salário de benefício:
    não existe RMI maior que a própria média. Sem o cap, tempo − limiar >= 20 anos (com limiar 15,
    a partir de 35 anos de contribuição — caso comum de professora veterana) imprimia coeficientes
    de 102%, 106%... e uma RMI que o INSS não paga. Corrigido a partir de relatório
    de validação com caso real: o cenário de aposentadoria por idade saía com 106%.
    """
    anos = tempo_dias / 365.0
    excedente = max(0, int(anos) - limiar_anos)
    return min(1.00, 0.60 + 0.02 * excedente), int(anos), excedente


def calcular(salarios, fatores, tempo_dias, limiar, tetos=None, teto_fixo=None):
    itens, sem_fator = [], []
    for comp, val in sorted(salarios.items()):
        if comp < PBC_INICIO:
            continue
        # teto sobre o valor NOMINAL, com o teto vigente NA COMPETÊNCIA (histórico) — ou um
        # valor fixo, só se --teto foi passado explicitamente. Correção monetária vem depois.
        val_limitado = val
        if teto_fixo is not None:
            val_limitado = min(val, teto_fixo)
        elif tetos is not None:
            teto_comp = teto_da_competencia(comp, tetos)
            if teto_comp is not None:
                val_limitado = min(val, teto_comp)
        fator = fatores.get(comp, 1.0) if fatores else 1.0
        if fatores and comp not in fatores:
            sem_fator.append(comp)      # entrou NOMINAL: a média não está integralmente corrigida
        atualizado = val_limitado * fator
        itens.append({"competencia": comp, "nominal": val, "teto_aplicado": round(val_limitado, 2),
                      "fator": fator, "atualizado": round(atualizado, 2)})
    if not itens:
        raise SystemExit("Nenhuma competência a partir de 07/1994 — confira o CSV.")
    media = sum(i["atualizado"] for i in itens) / len(itens)
    coef, anos, exc = coeficiente(tempo_dias, limiar)
    return {
        "competencias": len(itens),
        "media": round(media, 2),
        "tempo_anos_completos": anos,
        "limiar_anos": limiar,
        "anos_excedentes": exc,
        "coeficiente": round(coef, 4),
        "rmi": round(media * coef, 2),
        # "parcial" = há tabela de fatores, mas competência sem fator entrou pelo valor NOMINAL.
        # A média fica silenciosamente baixa e não pode ir ao parecer sem fechar a tabela.
        "atualizado": ("parcial" if sem_fator else True) if fatores else False,
        "competencias_sem_fator": sem_fator,
        "itens": itens,
    }


def testar_descarte(salarios, fatores, tempo_dias, limiar, tetos, teto_fixo, tempo_minimo_dias,
                    competencias_magisterio=None, folga_magisterio_dias=0):
    """
    Remove as competências de menor valor atualizado, uma a uma, enquanto (a) o benefício final
    subir, (b) o tempo TOTAL restante não cair abaixo do mínimo exigido pela regra escolhida e
    (c) o tempo de MAGISTÉRIO sacrificado couber na folga informada.

    A trava (b) é o ponto que costuma ser esquecido: descartar melhora a média mas reduz o tempo,
    e o tempo derruba tanto o requisito quanto o coeficiente. O ganho tem que ser no VALOR FINAL.

    A trava (c) nasceu de um relatório de validação com caso real: das 5
    competências que o script mandava descartar, 4 eram de magistério, e a cliente chegava ao
    pedágio de 100% com folga ZERO — o descarte "melhorava" a RMI de uma aposentadoria que deixava
    de existir. Sem `competencias_magisterio`, o script NÃO sabe distinguir tempo qualificado de
    tempo comum e diz isso na saída, em vez de deixar o operador supor que conferiu.
    """
    mag = set(competencias_magisterio or ())
    atual = dict(salarios)
    base = calcular(atual, fatores, tempo_dias, limiar, tetos, teto_fixo)
    melhor, descartadas, tempo, mag_gasto = base, [], tempo_dias, 0
    while True:
        # Competência de magistério só entra na disputa enquanto couber na folga (default 0).
        candidatos = [c for c in atual if c >= PBC_INICIO
                      and (c not in mag or mag_gasto + 30 <= folga_magisterio_dias)]
        if not candidatos:
            break

        def valor_corrigido(c):
            v = atual[c]
            if teto_fixo is not None:
                v = min(v, teto_fixo)
            elif tetos is not None:
                t = teto_da_competencia(c, tetos)
                if t is not None:
                    v = min(v, t)
            return v * (fatores.get(c, 1.0) if fatores else 1.0)

        pior = min(candidatos, key=valor_corrigido)
        novo_tempo = tempo - 30
        if novo_tempo < tempo_minimo_dias:
            break
        teste_sal = {k: v for k, v in atual.items() if k != pior}
        try:
            teste = calcular(teste_sal, fatores, novo_tempo, limiar, tetos, teto_fixo)
        except SystemExit:
            break
        if teste["rmi"] <= melhor["rmi"]:
            break
        atual, tempo, melhor = teste_sal, novo_tempo, teste
        descartadas.append(pior)
        if pior in mag:
            mag_gasto += 30
    return {
        "base": {k: base[k] for k in ("media", "coeficiente", "rmi", "competencias")},
        "com_descarte": {k: melhor[k] for k in ("media", "coeficiente", "rmi", "competencias")},
        "competencias_descartadas": descartadas,
        "descartadas_de_magisterio": [c for c in descartadas if c in mag],
        "magisterio_informado": bool(mag),
        "dias_magisterio_consumidos": mag_gasto,
        "folga_magisterio_dias": folga_magisterio_dias,
        "ganho_mensal": round(melhor["rmi"] - base["rmi"], 2),
        "ganho_anual_13x": round((melhor["rmi"] - base["rmi"]) * 13, 2),
        "tempo_restante_dias": tempo,
        "observacao": (
            "Descarte só é recomendável se o ganho no VALOR FINAL compensar a perda de tempo e "
            "de coeficiente, e se nenhum requisito da regra escolhida (tempo, carência, pontos, "
            "idade) for derrubado. Confira a leitura antes de levar ao parecer."
        ) + (
            " Tempo de magistério conferido: nenhuma competência qualificada foi descartada além "
            f"da folga de {folga_magisterio_dias} dias informada."
            if mag else
            " *** ATENÇÃO: --competencias-magisterio NÃO foi informado. O script conferiu apenas o "
            "tempo TOTAL contra --tempo-minimo-dias; ele NÃO sabe quais competências são de "
            "magistério. Em regra de professor, confira À MÃO se alguma competência descartada é "
            "de magistério e se a folga do tempo qualificado suporta a perda. ***"
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("salarios")
    ap.add_argument("--fatores")
    ap.add_argument("--tempo-dias", type=int, required=True)
    # Obrigatório de propósito: o default silencioso de 20 dava 76% onde o correto era 86%
    # (centenas de reais por mês a menos num caso de validação), sem erro, sem aviso. Escolher é do operador.
    ap.add_argument("--limiar", type=int, required=True, choices=[15, 20],
                     help="Anos a partir dos quais incidem os 2 p.p. (art. 26, §§ 2º e 5º, da "
                          "EC 103): 15 para mulher no RGPS, 20 no caso geral. Confira na fonte.")
    ap.add_argument("--teto", type=float,
                     help="Força um teto FIXO em todas as competências (raro; documente o motivo "
                          "no relatório). Sem esta flag, usa o histórico de tetos por competência.")
    ap.add_argument("--sem-teto", action="store_true",
                     help="Desliga o teto por completo. Só para depuração — nunca para o parecer.")
    ap.add_argument("--tetos-historico", default=TETOS_PADRAO,
                     help="CSV vigencia,teto — por padrão usa tetos_historicos.csv desta pasta.")
    ap.add_argument("--descarte", action="store_true")
    ap.add_argument("--tempo-minimo-dias", type=int, default=25 * 365)
    ap.add_argument("--competencias-magisterio",
                     help="Arquivo com as competências de MAGISTÉRIO (uma AAAA-MM por linha, ou "
                          "CSV com a competência na 1ª coluna). Sem ele o descarte não distingue "
                          "tempo qualificado de tempo comum — e avisa isso.")
    ap.add_argument("--folga-magisterio-dias", type=int, default=0,
                     help="Dias de tempo de MAGISTÉRIO que sobram acima do exigido pela regra "
                          "escolhida. O descarte nunca consome mais do que isso. Default 0: "
                          "nenhuma competência de magistério pode ser descartada.")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    salarios = ler_csv(a.salarios, "valor")
    fatores = ler_csv(a.fatores, "fator") if a.fatores else None
    tetos = None if a.sem_teto or a.teto is not None else ler_tetos(a.tetos_historico)

    mag = ler_competencias(a.competencias_magisterio) if a.competencias_magisterio else None

    res = calcular(salarios, fatores, a.tempo_dias, a.limiar, tetos, a.teto)
    if a.descarte:
        res["teste_descarte"] = testar_descarte(
            salarios, fatores, a.tempo_dias, a.limiar, tetos, a.teto, a.tempo_minimo_dias,
            mag, a.folga_magisterio_dias
        )

    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return

    print(f"Competências no PBC (desde 07/1994): {res['competencias']}")
    if a.sem_teto:
        print("Teto: DESLIGADO (--sem-teto) — não usar este número no parecer.")
    elif a.teto is not None:
        print(f"Teto: fixo em R$ {a.teto:,.2f} para todas as competências.")
    else:
        print(f"Teto: histórico por competência ({a.tetos_historico}).")
    print(f"Média: R$ {res['media']:,.2f}")
    print(f"Tempo: {res['tempo_anos_completos']} anos completos "
          f"(limiar {res['limiar_anos']}, excedente {res['anos_excedentes']})")
    print(f"Coeficiente: {res['coeficiente']*100:.0f}%"
          + (" (limitado a 100% da média)" if res["coeficiente"] >= 1.0 else ""))
    print(f"RMI estimada: R$ {res['rmi']:,.2f}")
    if tetos and res["rmi"] > tetos[-1][1]:
        print(f"\n*** ATENÇÃO: a RMI calculada supera o teto do RGPS mais recente da tabela "
              f"(R$ {tetos[-1][1]:,.2f}, vigência {tetos[-1][0]}). O benefício será pago limitado "
              f"ao teto vigente na DER. ***", file=sys.stderr)
    if res["atualizado"] is False:
        print("\n*** ATENÇÃO: cálculo sobre valores NOMINAIS (sem tabela de atualização). "
              "Este número não pode ir para o parecer. ***", file=sys.stderr)
    elif res["atualizado"] == "parcial":
        faltam = res["competencias_sem_fator"]
        print(f"\n*** ATENÇÃO: {len(faltam)} competência(s) sem fator na tabela entraram pelo "
              f"valor NOMINAL — a média está SUBESTIMADA e o número não pode ir para o parecer "
              f"antes de fechar a tabela: {', '.join(faltam)} ***", file=sys.stderr)
    if a.descarte:
        t = res["teste_descarte"]
        print(f"\nDescarte — competências removidas: {len(t['competencias_descartadas'])}")
        if t["competencias_descartadas"]:
            print(f"  Quais: {', '.join(t['competencias_descartadas'])}")
        print(f"  RMI sem descarte: R$ {t['base']['rmi']:,.2f}")
        print(f"  RMI com descarte: R$ {t['com_descarte']['rmi']:,.2f}")
        print(f"  Ganho mensal: R$ {t['ganho_mensal']:,.2f} "
              f"| anual (13x): R$ {t['ganho_anual_13x']:,.2f}")
        if t["magisterio_informado"]:
            print(f"  Magistério: {len(t['descartadas_de_magisterio'])} competência(s) "
                  f"qualificada(s) descartada(s), {t['dias_magisterio_consumidos']} dia(s) de "
                  f"{t['folga_magisterio_dias']} de folga.")
        else:
            print("\n*** ATENÇÃO: sem --competencias-magisterio, o descarte conferiu apenas o "
                  "tempo TOTAL. Ele NÃO sabe quais competências são de magistério. Em regra de "
                  "professor, confira à mão antes de recomendar. ***", file=sys.stderr)


if __name__ == "__main__":
    main()
