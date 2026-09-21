#!/usr/bin/env python3
"""
check_scripts.py — trava dos 3 defeitos GRAVES achados em relatório de validação com caso real. Roda offline, sem dependência nenhuma:

    python3 check_scripts.py        # silencioso = tudo certo; qualquer falha estoura AssertionError

Não é suíte de teste: é o menor conjunto de asserts que falha se algum dos três bugs voltar.
"""

import datetime
import rmi
import tempo

# ---------------------------------------------------------------- 1. coeficiente capado em 100%
# Antes: 38 anos com limiar 15 dava 106% e RMI MAIOR que a média — benefício que o INSS não paga.
assert rmi.coeficiente(13870, 15)[0] == 1.00, "coeficiente passou de 100%"
assert rmi.coeficiente(10531, 15)[0] == 0.86, "coeficiente correto do caso real mudou"
assert rmi.coeficiente(10531, 20)[0] == 0.76, "coeficiente com limiar 20 mudou"
assert rmi.coeficiente(3650, 15)[0] == 0.60, "piso de 60% quebrou"

# ------------------------------------------------- 2. requisito do professor = tempo de MAGISTÉRIO
# Professora com 26a de contribuição mas só 18a em magistério NÃO cumpre a regra do professor.
caso = {
    "nascimento": "1974-05-03", "sexo": "F", "data_base": "2026-09-15",
    "contribuicao_futura_em_magisterio": False,
    "periodos": [
        {"inicio": "2000-09-16", "fim": "2018-09-15", "regime": "RGPS", "magisterio": True},
        {"inicio": "2018-09-16", "fim": None, "ativo": True, "regime": "RGPS", "magisterio": False},
    ],
}
r = tempo.analisar(caso)
assert r["tempo_total_dias"] == 9496 and r["tempo_magisterio_dias"] == 6574
for p in ("projecao_contribuindo", "projecao_parando_de_contribuir"):
    assert r[p]["tempo_minimo"] is None, f"{p}: requisito cumprido com magistério insuficiente"
    assert r[p]["art15_pontos"] is None and r[p]["art16_idade"] is None, f"{p}: data indevida"
    assert r[p]["base_do_requisito"] == "magisterio"

# Quem tem magistério de sobra continua alcançando as regras (não é trava cega).
caso_ok = dict(caso, periodos=[{"inicio": "1996-05-02", "fim": None, "ativo": True,
                                "regime": "RGPS", "magisterio": True}],
               contribuicao_futura_em_magisterio=True)
assert tempo.analisar(caso_ok)["projecao_contribuindo"]["art16_idade"] is not None

# ------------------------------------------------- 3. descarte não come tempo de magistério
sal = {f"2003-{m:02d}": 1000.0 for m in range(1, 13)}
sal["2003-04"] = sal["2003-05"] = 100.0        # as duas piores, ambas de magistério
sal["2003-10"] = 200.0                          # a pior fora do magistério
mag = {c for c in sal if c not in ("2003-10",)}
t = rmi.testar_descarte(sal, None, 9200, 15, None, None, 9125, mag, 0)
assert not t["descartadas_de_magisterio"], "descartou magistério com folga zero"
assert t["magisterio_informado"] and t["dias_magisterio_consumidos"] == 0
t60 = rmi.testar_descarte(sal, None, 9200, 15, None, None, 9125, mag, 60)
assert len(t60["descartadas_de_magisterio"]) <= 2, "estourou a folga de magistério (60d = 2 comp.)"
t_cego = rmi.testar_descarte(sal, None, 9200, 15, None, None, 9125, None, 0)
assert not t_cego["magisterio_informado"] and "ATENÇÃO" in t_cego["observacao"], \
    "sem a lista de magistério o script tem que avisar que NÃO conferiu"

# ------------------------------------------------- menores: amd() 12 meses, fator faltando
assert tempo.amd(12041) == (33, 0, 1), 'amd() voltou a imprimir "12m"'
assert tempo.amd(364) == (0, 12, 4) or tempo.amd(364) == (1, 0, 4), "amd() inconsistente"
assert tempo.fmt(12041).startswith("33a 0m 1d")
res = rmi.calcular({"2003-01": 1000.0, "2003-02": 1000.0}, {"2003-01": 1.5}, 9200, 15)
assert res["atualizado"] == "parcial" and res["competencias_sem_fator"] == ["2003-02"]
assert rmi.calcular({"2003-01": 1000.0}, {"2003-01": 1.5}, 9200, 15)["atualizado"] is True

print("ok — 3 bugs graves travados + menores (amd, fator parcial).",
      datetime.date.today().isoformat())
