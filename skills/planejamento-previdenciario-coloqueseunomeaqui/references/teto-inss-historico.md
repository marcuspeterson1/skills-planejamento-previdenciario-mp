# Teto do RGPS — histórico de vigências (1994–2026)

`scripts/tetos_historicos.csv`, ao lado deste arquivo, é a tabela usada por `scripts/rmi.py` para
limitar cada salário de contribuição ao teto vigente **na própria competência**, antes da correção
monetária — não ao teto de hoje.

## Por que a ordem importa

O art. 28, § 5º da Lei 8.212/1991 limita a base de contribuição ao teto do RGPS **vigente na
competência**. Aplicar o teto de hoje sobre um valor já corrigido monetariamente é diferente — e
errado: uma remuneração antiga que hoje pareceria "acima do teto atual" só depois de multiplicada
pelo fator de correção pode nunca ter excedido o teto real da época. A ordem certa é: **teto
histórico sobre o nominal primeiro, correção monetária depois.** `rmi.py` já faz isso por padrão.

**Sinal de alerta que essa correção pega sozinha:** uma competência isolada com valor muito acima
das vizinhas (ex.: dezembro com 13º somado, ou um mês com verba retroativa) pode, sem o teto
histórico certo, inflar a média mais do que deveria — o script agora aplica o teto real daquele ano,
não o de hoje, reduzindo essa distorção. **Isso não substitui a auditoria da competência em si** —
uma remuneração muito acima das vizinhas continua sendo, sempre, motivo para conferir a ficha
financeira daquele ano antes de aceitar o valor (ver `calculo-e-cenarios.md`, seção 1, item (i)).

## Fonte e conferência

A tabela abaixo foi compilada de
[previdenciarista.com](https://previdenciarista.com/tabela-historica-de-tetos-previdenciarios-da-previdencia-social-inss-a-partir-de-1994/)
em 14/09/2026 — é uma fonte secundária (compilação privada), não o Diário Oficial. **Antes de usar
o teto de uma competência específica num parecer real, confirme o valor na Portaria Interministerial
ou na Portaria MTP daquele ano** (buscar "Portaria Interministerial MPS/MF" + o ano, ou
gov.br/previdencia → Legislação). O padrão de vigência é sempre no mês de reajuste do salário mínimo
e dos benefícios — normalmente janeiro, com exceções nos anos de plano econômico (1994-2003, meses
variados).

| Vigência a partir de | Teto (R$) |
|---|---|
| 03/1994 | 582,86 |
| 05/1995 | 832,66 |
| 05/1996 | 957,56 |
| 06/1997 | 1.031,87 |
| 06/1998 | 1.081,50 |
| 12/1998 | 1.200,00 |
| 06/1999 | 1.255,32 |
| 06/2000 | 1.328,25 |
| 06/2001 | 1.430,00 |
| 06/2002 | 1.561,56 |
| 06/2003 | 1.869,34 |
| 01/2004 | 2.400,00 |
| 05/2004 | 2.508,72 |
| 05/2005 | 2.668,15 |
| 04/2006 | 2.801,56 |
| 04/2007 | 2.894,28 |
| 03/2008 | 3.038,99 |
| 02/2009 | 3.218,90 |
| 01/2010 | 3.467,40 |
| 01/2011 | 3.691,74 |
| 01/2012 | 3.916,20 |
| 01/2013 | 4.159,00 |
| 01/2014 | 4.390,24 |
| 01/2015 | 4.663,75 |
| 01/2016 | 5.189,82 |
| 01/2017 | 5.531,31 |
| 01/2018 | 5.645,80 |
| 01/2019 | 5.839,45 |
| 01/2020 | 6.101,06 |
| 01/2021 | 6.433,57 |
| 01/2022 | 7.087,22 |
| 01/2023 | 7.507,49 |
| 01/2024 | 7.786,02 |
| 01/2025 | 8.157,41 |
| 01/2026 | 8.475,55 |

## Manutenção

Todo mês de janeiro, quando o novo teto for publicado, adicione uma linha em
`scripts/tetos_historicos.csv` (formato `AAAA-MM,valor`) e nesta tabela. Sem a linha do ano
corrente, o script usa o último teto conhecido — o que é seguro (subestima, nunca superestima o
benefício), mas gera uma competência desatualizada que o `planejamento-previdenciario-coloqueseunomeaqui-revisor` vai pegar
na conferência.
