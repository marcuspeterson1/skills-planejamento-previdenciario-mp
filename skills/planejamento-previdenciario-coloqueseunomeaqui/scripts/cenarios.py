#!/usr/bin/env python3
"""
cenarios.py — comparação econômica entre cenários de aposentadoria.

Monta a tabela obrigatória do planejamento e calcula o que transforma a tabela em decisão:
ponto de equilíbrio, custo de postergar e valor projetado até a expectativa de vida.

Uso:
    python3 cenarios.py cenarios.json [--markdown] [--json]

Formato do cenarios.json:
{
  "cliente": "Maria da Silva",
  "expectativa_sobrevida_anos": 24.3,     # tábua do IBGE vigente, para o sexo e a IDADE
  "fonte_expectativa": "IBGE, Tábuas Completas de Mortalidade 2024, mulheres, 57 anos",
  "pagamentos_por_ano": 13,
  "referencia": "A",                       # cenário usado como base de comparação
  "cenarios": [
    {"id": "A", "nome": "Permanecer no vínculo até a regra de pontos",
     "data": "2029-04-10", "idade": 57, "rmi": 3120.55, "investimento": 0},
    {"id": "E", "nome": "Sair e contribuir como CI sobre R$ 3.000",
     "data": "2028-01-15", "idade": 55, "rmi": 2890.10, "investimento": 12600.00}
  ]
}

A expectativa de sobrevida é a da tábua do IBGE **na idade em que o cliente se aposenta**, não a
expectativa ao nascer. Se os cenários têm idades diferentes, informe a sobrevida por cenário no
campo opcional "sobrevida_anos" de cada um.
"""

import argparse
import json
from datetime import date


def d(s):
    y, m, dd = (int(x) for x in str(s).split("-"))
    return date(y, m, dd)


def calcular(cfg):
    ppa = cfg.get("pagamentos_por_ano", 13)
    padrao = cfg.get("expectativa_sobrevida_anos")
    cens = []
    for c in cfg["cenarios"]:
        sobrevida = c.get("sobrevida_anos", padrao)
        if sobrevida is None:
            raise SystemExit(
                f"Cenário {c['id']}: falta a expectativa de sobrevida. Consulte a tábua do IBGE "
                "vigente para o sexo e a idade de aposentadoria — não use número memorizado."
            )
        pagamentos = sobrevida * ppa
        cens.append({
            **c,
            "sobrevida_anos": sobrevida,
            "pagamentos_estimados": round(pagamentos, 1),
            "valor_projetado": round(c["rmi"] * pagamentos, 2),
            "liquido_projetado": round(c["rmi"] * pagamentos - c.get("investimento", 0), 2),
        })

    # Horizonte comum: sem ele, cada cenário é medido a partir da sua própria data e o
    # cenário mais tardio parece melhor só porque a conta ignora os anos que o cliente
    # passou sem receber nada. Aqui todos são medidos até a mesma data final.
    terminal = max(d(c["data"]).toordinal() + c["sobrevida_anos"] * 365.25 for c in cens)
    for c in cens:
        anos_recebendo = (terminal - d(c["data"]).toordinal()) / 365.25
        c["anos_recebendo_no_horizonte"] = round(anos_recebendo, 1)
        c["valor_no_horizonte"] = round(c["rmi"] * ppa * anos_recebendo, 2)
        c["liquido_no_horizonte"] = round(
            c["rmi"] * ppa * anos_recebendo - c.get("investimento", 0), 2
        )

    ref = next((c for c in cens if c["id"] == cfg.get("referencia")), cens[0])
    nasc = cfg.get("nascimento")
    for c in cens:
        dif_rmi = c["rmi"] - ref["rmi"]
        dif_inv = c.get("investimento", 0) - ref.get("investimento", 0)
        c["dif_rmi_mensal"] = round(dif_rmi, 2)
        c["dif_rmi_anual"] = round(dif_rmi * ppa, 2)
        c["dif_investimento"] = round(dif_inv, 2)
        if dif_rmi > 0 and dif_inv > 0:
            c["payback_meses"] = round(dif_inv / dif_rmi, 1)
        elif dif_inv <= 0 and dif_rmi >= 0:
            c["payback_meses"] = 0.0
        else:
            c["payback_meses"] = None
        dias = (d(c["data"]) - d(ref["data"])).days
        c["meses_vs_referencia"] = round(dias / 30.44, 1)
        if dias > 0:
            # O que a referência já teria recebido enquanto este cenário ainda espera.
            atraso = round(ref["rmi"] * (dias / 365.25) * ppa, 2)
            c["custo_de_postergar"] = atraso
            # Quando o benefício maior finalmente compensa esse atraso.
            if dif_rmi > 0:
                anos = atraso / (dif_rmi * ppa)
                cruz = d(c["data"]).toordinal() + anos * 365.25
                c["anos_ate_compensar_o_atraso"] = round(anos, 1)
                c["data_de_cruzamento"] = date.fromordinal(int(cruz)).isoformat()
                if nasc:
                    c["idade_no_cruzamento"] = round(
                        (cruz - d(nasc).toordinal()) / 365.25, 1
                    )
            else:
                c["anos_ate_compensar_o_atraso"] = None
        elif dias < 0:
            c["antecipacao_recebida"] = round(c["rmi"] * (-dias / 365.25) * ppa, 2)

    # Empate no investimento é a regra, não a exceção (quase sempre todos zerados): anunciar um
    # "vencedor" aí é `min()` decidindo pela ordem da lista, e vira slide dizendo que A é mais
    # barato que B, C e D quando nenhum custa nada.
    invs = [c.get("investimento", 0) for c in cens]
    menor_investimento = (
        min(cens, key=lambda c: c.get("investimento", 0))["id"] if len(set(invs)) > 1 else
        "empate — " + ("nenhum cenário exige desembolso" if invs[0] == 0 else
                       f"todos exigem o mesmo desembolso (R$ {invs[0]:,.2f})") +
        "; a comparação se desloca para o custo de postergar"
    )
    destaques = {
        "mais_rapido": min(cens, key=lambda c: d(c["data"]))["id"],
        "maior_beneficio": max(cens, key=lambda c: c["rmi"])["id"],
        "menor_investimento": menor_investimento,
        "melhor_custo_beneficio": max(cens, key=lambda c: c["liquido_no_horizonte"])["id"],
    }
    return {
        "cliente": cfg.get("cliente"),
        "fonte_expectativa": cfg.get("fonte_expectativa", "NÃO INFORMADA — registrar no parecer"),
        "pagamentos_por_ano": ppa,
        "referencia": ref["id"],
        "cenarios": cens,
        "destaques": destaques,
        "ressalva": (
            "A expectativa de vida é ferramenta estatística de comparação entre cenários, não "
            "previsão individual. Registre esta ressalva no parecer e nos slides."
        ),
    }


def markdown(res):
    linhas = [
        "| Cenário | Data | Idade | RMI | Investimento até aposentar | Valor projetado |",
        "|---|---|---|---|---|---|",
    ]
    for c in res["cenarios"]:
        linhas.append(
            f"| {c['id']} — {c['nome']} | {c['data']} | {c['idade']} | "
            f"R$ {c['rmi']:,.2f} | R$ {c.get('investimento', 0):,.2f} | "
            f"R$ {c['valor_projetado']:,.2f} |"
        )
    linhas.append("")
    linhas.append(
        "Medido num horizonte comum (todos os cenários até a mesma data final), para que os "
        "anos em que o cliente ainda não recebe nada apareçam na conta:"
    )
    linhas.append("")
    linhas.append("| Cenário | Anos recebendo | Valor no horizonte comum |")
    linhas.append("|---|---|---|")
    for c in res["cenarios"]:
        linhas.append(
            f"| {c['id']} | {c['anos_recebendo_no_horizonte']} | "
            f"R$ {c['valor_no_horizonte']:,.2f} |"
        )
    linhas.append("")
    linhas.append(f"Referência de comparação: cenário {res['referencia']}")
    for c in res["cenarios"]:
        if c["id"] == res["referencia"]:
            continue
        partes = [
            f"RMI {c['dif_rmi_mensal']:+,.2f}/mês ({c['dif_rmi_anual']:+,.2f}/ano)",
        ]
        if c["dif_investimento"]:
            partes.append(f"investimento {c['dif_investimento']:+,.2f}")
            if c["payback_meses"] is not None:
                partes.append(f"ponto de equilíbrio do investimento: {c['payback_meses']} meses")
        if "custo_de_postergar" in c:
            partes.append(f"deixa de receber R$ {c['custo_de_postergar']:,.2f} até lá")
            if c.get("anos_ate_compensar_o_atraso"):
                partes.append(
                    f"só compensa o atraso em {c['anos_ate_compensar_o_atraso']} anos "
                    f"({c['data_de_cruzamento']}"
                    + (f", aos {c['idade_no_cruzamento']} anos)" if c.get("idade_no_cruzamento") else ")")
                )
            elif c.get("anos_ate_compensar_o_atraso") is None and "custo_de_postergar" in c:
                partes.append("nunca compensa o atraso (RMI igual ou menor)")
        if "antecipacao_recebida" in c:
            partes.append(f"antecipa R$ {c['antecipacao_recebida']:,.2f} de benefício")
        linhas.append(f"- **{c['id']}**: " + " · ".join(partes))
    dq = res["destaques"]
    linhas += [
        "",
        f"- **Cenário mais rápido:** {dq['mais_rapido']}",
        f"- **Maior benefício:** {dq['maior_beneficio']}",
        f"- **Menor investimento:** {dq['menor_investimento']}",
        f"- **Melhor custo-benefício (líquido projetado):** {dq['melhor_custo_beneficio']}",
        "",
        f"_Fonte da expectativa de vida: {res['fonte_expectativa']}._",
        f"_{res['ressalva']}_",
    ]
    return "\n".join(linhas)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("config")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--markdown", action="store_true")
    a = ap.parse_args()
    res = calcular(json.load(open(a.config, encoding="utf-8")))
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print(markdown(res))


if __name__ == "__main__":
    main()
