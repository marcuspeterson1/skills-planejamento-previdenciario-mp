# Indicadores do CNIS — referência oficial

Fonte primária e autoritativa: **Anexo V da Portaria DIRBEN/INSS nº 990/2022** (alterada pela
Portaria DIRBEN/INSS nº 1.316/2025), "Relação dos Indicadores Disponibilizados no CNIS":
`https://portalin.inss.gov.br/assets/anexos/pt990/AnexoV.pdf`

Este arquivo cobre os indicadores mais comuns em CNIS de professores/servidores municipais
(o público principal desta skill). **Ele não é exaustivo** — existem mais de 100
indicadores no Anexo V oficial. Se um indicador aparecer no CNIS de um cliente e não estiver
listado aqui, **busque-o (web_fetch) na URL acima antes de descrevê-lo no relatório**. Nunca
descreva um indicador de memória sem checagem, e nunca invente o significado de um indicador
desconhecido — se o fetch falhar ou o indicador realmente não constar do Anexo V, registre
expressamente que ele exige análise documental/humana complementar.

O Anexo V tem duas categorias:
- **CsPendencia (Indicadores de Pendência)** — sinalizam algo que pode impedir o cômputo do
  vínculo/remuneração até ser tratado. É aqui que está a maior parte do "tempo em risco".
  Nem toda pendência é grave: os esclarecimentos de cada indicador dizem se "há impacto no
  reconhecimento de direitos" ou não.
- **CsIndicador (Indicadores de Alerta)** — em geral informativos, não bloqueiam o vínculo,
  mas registram uma situação que vale a pena checar (ex.: ajuste automático de valor mínimo).

## Indicadores mais frequentes

### PEXT — Vínculo com informação extemporânea, passível de comprovação
**Grupo:** Vínculos e Remunerações · **Tipo:** Pendência (impacta o reconhecimento de direitos)
O vínculo (ou parte dele) foi inserido fora do prazo legal (art. 19, §3º do RPS/Decreto 3.048/99).
Se a regularidade não for comprovada, o período informado extemporaneamente não conta para
tempo de contribuição nem para o cálculo da renda mensal inicial.
**Documentos:** CTPS, contrato de trabalho, contracheques/holerites, termo de rescisão, extrato
FGTS, declaração do empregador.
**Providência:** requerimento de vínculo extemporâneo no Portal CNIS/Meu INSS.

### PADM-EMPR — Data de admissão anterior ao início/posterior ao encerramento da atividade do empregador
**Grupo:** Vínculos e Remunerações · **Tipo:** Pendência
A data de admissão do vínculo é anterior à data de constituição da empresa no CNPJ (ou
posterior ao seu encerramento). Segundo o próprio Anexo V, **não há impacto automático no
reconhecimento de direitos** — desde que o vínculo seja comprovado e validado.
**Documentos:** CTPS, contrato de trabalho, termo de rescisão ou outro documento trabalhista
com as datas corretas.
**Providência:** Requerimento de Vínculo (ação "Alterar") no módulo VRE do Portal CNIS.

### PRPPS — Vínculo de empregado com informações de Regime Próprio (Servidor Público)
**Grupo:** Vínculos e Remunerações · **Tipo:** Pendência
Sinaliza que parte ou todo o vínculo esteve sob Regime Próprio de Previdência Social (RPPS) —
comum em professores efetivos de rede municipal/estadual. **Muito relevante para o público desta skill.** O período em RPPS não é automaticamente contado pelo INSS (RGPS); é
necessário avaliar se o vínculo teve trechos em RGPS (ex.: contratado antes de efetivar) e, para
o trecho RPPS, obter a CTC (Certidão de Tempo de Contribuição) do ente público para eventual
averbação — o CNIS sozinho não basta.
**Documentos:** CTC do RPPS, declarações do órgão público sobre o regime em cada período.
**Providência:** solicitar CTC ao ente federativo; ajuste dos períodos de regime no vínculo via
Portal CNIS quando a fonte (RAIS/GFIP) não refletir a realidade.
**Antes de recomendar CTC:** confirme por busca ao vivo (ver passo 3.5 do SKILL.md) se o ente
público realmente tem RPPS instituído para a categoria do cargo naquele período — o indicador
PRPPS pode aparecer por classificação incorreta da fonte (RAIS/GFIP) mesmo quando o servidor
sempre esteve, de fato, no RGPS (ex.: cargo comissionado/contratado em município sem regime
próprio, ou fora da categoria abrangida pelo RPPS local).

### PREM-BLOQ-EC103 — Pendência de bloqueio de remuneração/contribuição para ajuste entre competências
**Grupo:** Ajustes EC103 · **Tipo:** Pendência (impacta o reconhecimento de direitos)
Só aparece em competências a partir de 11/2019 (Emenda Constitucional 103/2019). Bloqueia a
remuneração daquela competência para fins de agrupamento/complementação/utilização entre
competências — ou seja, o INSS pode desconsiderar aquele mês no cálculo. É sempre
**consequência de outro indicador** (ex.: PEXT, PEMP-CAD, contribuição pelo Plano Simplificado
concomitante com vínculo de empregado, inconsistência cadastral da empresa) — a pendência real
está no indicador que o acompanha na mesma competência.
**Providência:** identificar e tratar a pendência de origem; solicitar "Ajustes para Alcance do
Salário Mínimo – EC 103/2019" pelo Meu INSS ou telefone 135.

### PSC-MEN-SM-EC103 — Salário de contribuição menor que o mínimo (a partir de 11/2019)
**Grupo:** Ajustes EC103 · **Tipo:** Pendência
Sucessora do antigo PREC-MENOR-MIN para competências a partir de 11/2019. A competência é
passível de complementação, utilização ou agrupamento (art. 29 da EC 103/2019). É mutuamente
exclusiva com PREM-BLOQ-EC103 (se este existir, aquele não é verificado).
**Providência:** ajuste via Meu INSS (canal remoto), ou complementação de contribuição.

### PSE-POS / PSE-PEN / PSE-NEG — Período de Segurado Especial (Positivo/Pendente/Negativo)
**Grupo:** Segurado Especial · **Tipo:** Pendência
Período migrado das bases CAFIR/RGP de segurado especial (trabalhador rural em regime de
economia familiar), ainda não ratificado no CNIS — mesmo o "Positivo" é tecnicamente uma
pendência porque precisa de ratificação ou exclusão pelo próprio segurado no Portal CNIS.
**Providência:** ratificação ou exclusão do período pelo segurado no Portal CNIS.

### IREM-INDPEND — Remunerações com indicadores/pendências
**Grupo:** genérico · **Tipo:** Alerta/guarda-chuva
Indicador genérico que sinaliza que existe algum outro indicador mais específico associado
àquela remuneração. **Nunca trate como pendência isolada** — procure, na mesma competência, o
indicador específico que o acompanha (é ele que define a causa e a providência real).

### ISE-CVU — Segurado especial concomitante com período urbano
**Grupo:** Segurado Especial · **Tipo:** Alerta relevante
Indica sobreposição entre um período de segurado especial (rural) e outro vínculo/atividade
urbana. Essa concomitância pode descaracterizar a condição de segurado especial para aquele
trecho — exige análise individualizada, não deve ser tratado como "regular" nem como
"definitivamente inválido" sem mais informação.

### IVIN-JORN-DIFERENCIADA — Vínculo com regime de jornada diferenciada
**Grupo:** informativo · **Tipo:** Alerta
Apenas informa que a jornada do vínculo foge do padrão (ex.: cargo comissionado, gerência).
Em geral não exige ação, salvo se as datas/remunerações no CNIS parecerem incorretas.

## Indicadores "positivos" comuns (não são pendência)
- **AEXT-VT** — acerto de vínculo extemporâneo já validado pelo INSS. Informativo, positivo.
- **AVRC-DEF** — acerto de vínculo extemporâneo deferido. Informativo, positivo.

## Como classificar risco (para a linguagem do relatório e dos slides)
Usar três níveis, alinhados à paleta visual do escritório:
- **Verde (regular / resolvido)** — competência sem indicador de pendência, ou pendência já
  tratada (indicador de acerto presente).
- **Âmbar (pendência de baixo custo/simples)** — ex.: complementação de valor mínimo
  (PSC-MEN-SM-EC103), indicador informativo que só precisa checagem.
- **Vermelho (pendência relevante / risco de não reconhecimento)** — ex.: PEXT sem
  documentação disponível, PRPPS sem CTC, PREM-BLOQ-EC103 não tratado, vínculo em aberto sem
  data de encerramento, vínculo duplicado.

A classificação exata depende sempre da documentação disponível — nunca apresente uma
competência com pendência como "perdida" antes de esgotar a possibilidade de comprovação
documental, nem apresente uma pendência como resolvida sem confirmação.
