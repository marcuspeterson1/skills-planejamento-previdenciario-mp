#!/usr/bin/env python3
"""
tempo.py — apuração de tempo de contribuição e projeção de requisitos.

Por que este script existe: somar períodos à mão é onde nascem as divergências entre o parecer,
os slides e a planilha. Aqui a união com desconto de concomitância, a conversão em anos/meses/dias
e a projeção da data em que cada requisito é atingido saem de uma fonte só.

Uso:
    python3 tempo.py caso.json                 # relatório legível
    python3 tempo.py caso.json --json          # saída JSON, para alimentar o parecer/slides

Formato do caso.json:
{
  "nome": "Maria da Silva",
  "nascimento": "1971-03-15",
  "sexo": "F",                        # "F" ou "M"
  "data_base": "2026-09-09",          # opcional; default = hoje
  "periodos": [
    {"inicio": "1996-02-01", "fim": "2003-12-31", "rotulo": "Escola X",
     "regime": "RGPS", "magisterio": true},
    {"inicio": "2004-02-01", "fim": null, "rotulo": "Prefeitura Y",
     "regime": "RPPS-MUN", "magisterio": true, "ativo": true}
  ],
  "projetar_contribuicao": true,      # opcional; assume que os vínculos "ativo" seguem ativos
  "contribuicao_futura_em_magisterio": true   # opcional; false = segue contribuindo FORA da sala
}

O requisito de tempo das regras do professor é medido sobre o tempo de MAGISTÉRIO (campo
"magisterio": true nos períodos), nunca sobre o tempo total — só a pontuação do art. 15 soma a
idade com o tempo TOTAL de contribuição. Se nenhum período estiver marcado como magistério, o
script cai no tempo total e diz isso em `base_do_requisito`.

Um período com "fim": null e "ativo": true é tratado como em curso até a data-base (e, na
projeção, adiante). Um período com "fim": null e sem "ativo" NÃO é medido: o script o devolve na
lista `sem_fim_determinavel` e o deixa fora do total, porque presumir uma data de encerramento é
exatamente o que não se pode fazer num planejamento.
"""

import json
import sys
from datetime import date, timedelta

# --------------------------------------------------------------------------- util

def d(s):
    if s is None:
        return None
    if isinstance(s, date):
        return s
    y, m, dd = (int(x) for x in str(s).split("-"))
    return date(y, m, dd)


def amd(dias):
    """Converte dias em (anos, meses, dias) no padrão previdenciário (365 / 30).

    Como 365 = 12 × 30 + 5, o resto pode chegar a 364 e produzir "12 meses" — "32a 12m 1d" num
    parecer é erro que qualquer revisor vê. Normalizado para o ano seguinte.
    """
    anos, resto = divmod(int(dias), 365)
    meses, dd = divmod(resto, 30)
    if meses >= 12:
        anos, meses = anos + 1, meses - 12
    return anos, meses, dd


def fmt(dias):
    a, m, dd = amd(dias)
    return f"{a}a {m}m {dd}d ({int(dias)} dias)"


def idade_em(nascimento, quando):
    anos = quando.year - nascimento.year
    if (quando.month, quando.day) < (nascimento.month, nascimento.day):
        anos -= 1
    return anos


def idade_em_meses(nascimento, quando):
    meses = (quando.year - nascimento.year) * 12 + (quando.month - nascimento.month)
    if quando.day < nascimento.day:
        meses -= 1
    return meses


def dias_entre(ini, fim):
    """Dias contados de forma inclusiva, como faz a contagem previdenciária."""
    return (fim - ini).days + 1

# ------------------------------------------------------------------- união de períodos

def uniao(intervalos):
    """Recebe [(ini, fim)] e devolve a união, descontando concomitâncias."""
    ivs = sorted((a, b) for a, b in intervalos if a and b and b >= a)
    out = []
    for ini, fim in ivs:
        if out and ini <= out[-1][1] + timedelta(days=1):
            out[-1] = (out[-1][0], max(out[-1][1], fim))
        else:
            out.append((ini, fim))
    return out


def total_dias(intervalos):
    return sum(dias_entre(a, b) for a, b in intervalos)


def recortar(intervalos, ate=None, desde=None):
    out = []
    for a, b in intervalos:
        if ate and b > ate:
            b = ate
        if desde and a < desde:
            a = desde
        if b >= a:
            out.append((a, b))
    return out

# ------------------------------------------------------- tabelas de requisitos (professor)

def pontos_exigidos_professor(ano, sexo):
    """EC 103, art. 15, § 3º: 81/91 em 2019, +1 por ano, teto 92/100."""
    base, teto = (81, 92) if sexo.upper() == "F" else (91, 100)
    return min(base + max(0, ano - 2019), teto)


def idade_exigida_art16_professor(ano, sexo):
    """EC 103, art. 16, § 2º: 51/56 em 2019, +6 meses por ano, teto 57/60. Em meses."""
    base, teto = (51 * 12, 57 * 12) if sexo.upper() == "F" else (56 * 12, 60 * 12)
    return min(base + 6 * max(0, ano - 2019), teto)


def tempo_minimo_professor(sexo):
    """25 anos (mulher) / 30 (homem), em dias."""
    return (25 if sexo.upper() == "F" else 30) * 365

# ------------------------------------------------------------------------- projeção

def projetar(intervalos_magisterio, intervalos_totais, nascimento, sexo, inicio_projecao,
             contribuindo, limite_anos=40, contribuicao_futura_em_magisterio=True):
    """
    Caminha dia a dia a partir de inicio_projecao e devolve a primeira data em que cada regra
    de transição do professor é atingida. Só considera as regras cujos requisitos são
    apuráveis aritmeticamente (pontos e idade progressiva). Pedágio e direito adquirido dependem
    de dados da data da reforma e são calculados à parte, no corpo do planejamento.

    DUAS BASES, DE PROPÓSITO (corrigido após relatório de validação com caso real
    — antes disso o requisito era testado contra o tempo TOTAL):
      • `intervalos_magisterio` — tempo QUALIFICADO. É ele, e só ele, que cumpre o requisito de
        tempo mínimo do professor (EC 103, arts. 15, § 3º, e 16, § 2º: "exclusivamente tempo de
        efetivo exercício das funções de magistério"). Uma professora com 25 anos de contribuição
        dos quais 18 em magistério NÃO cumpre a regra, e o script não pode dizer que cumpre.
      • `intervalos_totais` — tempo TOTAL de contribuição, que é o que soma com a idade na
        pontuação do art. 15.

    `contribuicao_futura_em_magisterio=False` projeta quem continua contribuindo FORA da sala de
    aula: o tempo total cresce, o de magistério não — e as datas do professor podem nunca chegar.
    """
    fim = inicio_projecao + timedelta(days=365 * limite_anos)
    res = {"art15_pontos": None, "art16_idade": None, "tempo_minimo": None,
           "base_do_requisito": ("magisterio" if total_dias(intervalos_magisterio)
                                 else "tempo total (nenhum periodo marcado como magisterio)")}
    tmin = tempo_minimo_professor(sexo)

    dia = inicio_projecao
    acumulado = total_dias(intervalos_totais)
    qualificado = total_dias(intervalos_magisterio) or acumulado
    while dia <= fim:
        cumpre_tempo = qualificado >= tmin
        if res["tempo_minimo"] is None and cumpre_tempo:
            res["tempo_minimo"] = dia.isoformat()

        idade_dias = (dia - nascimento).days
        pontos = (idade_dias + acumulado) / 365.0
        idade_meses = idade_em_meses(nascimento, dia)

        if res["art15_pontos"] is None and cumpre_tempo:
            if pontos >= pontos_exigidos_professor(dia.year, sexo):
                res["art15_pontos"] = {
                    "data": dia.isoformat(),
                    "pontos": round(pontos, 2),
                    "exigido": pontos_exigidos_professor(dia.year, sexo),
                    "idade": idade_em(nascimento, dia),
                    "tempo": fmt(acumulado),
                    "tempo_magisterio": fmt(qualificado),
                }
        if res["art16_idade"] is None and cumpre_tempo:
            if idade_meses >= idade_exigida_art16_professor(dia.year, sexo):
                res["art16_idade"] = {
                    "data": dia.isoformat(),
                    "idade": idade_em(nascimento, dia),
                    "idade_exigida_meses": idade_exigida_art16_professor(dia.year, sexo),
                    "tempo": fmt(acumulado),
                    "tempo_magisterio": fmt(qualificado),
                }
        if res["art15_pontos"] and res["art16_idade"] and res["tempo_minimo"]:
            break

        dia += timedelta(days=1)
        if contribuindo:
            acumulado += 1
            if contribuicao_futura_em_magisterio:
                qualificado += 1
    return res

# ---------------------------------------------------------------------------- núcleo

MARCOS = {
    "ate_EC20_15-12-1998": "1998-12-15",
    "ate_EC41_31-12-2003": "2003-12-31",
    "ate_EC103_13-11-2019": "2019-11-13",
}


def analisar(caso):
    nasc = d(caso["nascimento"])
    sexo = caso.get("sexo", "F")
    base = d(caso.get("data_base")) or date.today()

    medidos, sem_fim = [], []
    for p in caso["periodos"]:
        ini = d(p["inicio"])
        if p.get("fim"):
            fim = d(p["fim"])
        elif p.get("ativo"):
            fim = base
        else:
            sem_fim.append(p.get("rotulo", "sem rótulo"))
            continue
        medidos.append({**p, "_ini": ini, "_fim": fim})

    todos = uniao([(p["_ini"], p["_fim"]) for p in medidos])
    mag = uniao([(p["_ini"], p["_fim"]) for p in medidos if p.get("magisterio")])

    por_regime = {}
    for p in medidos:
        por_regime.setdefault(p.get("regime", "NAO_IDENTIFICADO"), []).append(
            (p["_ini"], p["_fim"])
        )
    por_regime = {k: total_dias(uniao(v)) for k, v in por_regime.items()}

    out = {
        "cliente": caso.get("nome"),
        "data_base": base.isoformat(),
        "idade_na_data_base": idade_em(nasc, base),
        "tempo_total": fmt(total_dias(todos)),
        "tempo_total_dias": total_dias(todos),
        "tempo_magisterio": fmt(total_dias(mag)),
        "tempo_magisterio_dias": total_dias(mag),
        "tempo_comum": fmt(total_dias(todos) - total_dias(mag)),
        "por_regime": {k: fmt(v) for k, v in por_regime.items()},
        "por_marco": {
            k: fmt(total_dias(recortar(todos, ate=d(v)))) for k, v in MARCOS.items()
        },
        "magisterio_por_marco": {
            k: fmt(total_dias(recortar(mag, ate=d(v)))) for k, v in MARCOS.items()
        },
        "sem_fim_determinavel": sem_fim,
        "pontos_na_data_base": round(
            ((base - nasc).days + total_dias(todos)) / 365.0, 2
        ),
        "pontos_exigidos_no_ano": pontos_exigidos_professor(base.year, sexo),
    }

    if caso.get("projetar_contribuicao", True):
        # A regra do professor exige tempo EXCLUSIVAMENTE em magistério: o requisito de tempo se
        # mede sobre `mag`; o total só entra na pontuação do art. 15. Ver docstring de projetar().
        futuro_mag = caso.get("contribuicao_futura_em_magisterio", True)
        out["projecao_contribuindo"] = projetar(mag, todos, nasc, sexo, base, True,
                                                contribuicao_futura_em_magisterio=futuro_mag)
        out["projecao_parando_de_contribuir"] = projetar(mag, todos, nasc, sexo, base, False)

    if sem_fim:
        out["_alerta"] = (
            "Há vínculo(s) sem data de fim determinável. Eles ficaram FORA do total. "
            "O tempo apurado é um piso, não um teto — diga isso no parecer."
        )
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    caso = json.load(open(sys.argv[1], encoding="utf-8"))
    res = analisar(caso)
    if "--json" in sys.argv:
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return
    for k, v in res.items():
        if isinstance(v, dict):
            print(f"\n{k}:")
            for kk, vv in v.items():
                print(f"  {kk}: {vv}")
        elif isinstance(v, list):
            print(f"\n{k}: {', '.join(map(str, v)) if v else '(nenhum)'}")
        else:
            print(f"{k}: {v}")


if __name__ == "__main__":
    main()
