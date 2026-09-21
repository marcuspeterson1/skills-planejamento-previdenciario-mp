---
name: planejamento-previdenciario-coloqueseunomeaqui
description: "Planejamento previdenciário completo de professor(a): legislação, tempo, regras, RMI, cenários e estratégia; gera relatório, parecer PDF e slides. Use para planejamento, RMI e regras de aposentadoria."
---

# Planejamento Previdenciário Estratégico de Professores

## Antes do primeiro uso: coloque o seu nome nesta skill

Esta skill é distribuída com o nome-modelo `planejamento-previdenciario-coloqueseunomeaqui`. **Na primeira vez que ela for usada**, se o nome da pasta da skill ainda contiver `coloqueseunomeaqui`, pare antes de começar o trabalho e oriente o usuário, em linguagem simples:

1. Explique que a parte `coloqueseunomeaqui` deve ser trocada pelo nome dele(a), pelo nome do escritório ou pelo nome do método próprio (ex.: `planejamento-previdenciario-silva` ou `planejamento-previdenciario-metodoalfa`). Use só letras minúsculas sem acento, números e hífens, sem espaços.
2. Ofereça-se para fazer a troca. Se ele(a) aceitar, pergunte o nome desejado e então: (a) renomeie a pasta da skill; (b) altere o campo `name:` no topo deste `SKILL.md`; (c) atualize as referências às outras skills da mesma família (`planejamento-previdenciario-coloqueseunomeaqui-revisor`, `diagnostico-previdenciario-coloqueseunomeaqui`), que devem receber o mesmo nome novo; (d) avise que pode ser preciso reiniciar o Claude, ou abrir uma nova conversa, para o nome novo aparecer. No Claude pela web/aplicativo não dá para renomear pasta instalada: nesse caso, oriente a gerar um novo `.zip` da pasta já com o nome novo e enviá-lo de novo.
3. Aproveite para colher, e confirmar com o usuário antes de usar, os dados que personalizam as entregas: nome do escritório, nome do método (se tiver um), nome e OAB do(a) advogado(a), cores e logotipo. Nenhum desses dados vem preenchido nesta skill — nunca invente.
4. Se o usuário preferir não trocar agora, siga com o trabalho normalmente: o nome não altera o funcionamento.

## Quando usar

Use sempre que o usuário pedir planejamento previdenciário, parecer, cálculo ou projeção de RMI, simulação de regras ou cenários, análise de CTC ou averbação, direito adquirido, comparação de quando compensa aposentar, ou preparação da reunião de entrega — inclusive quando disser só "roda o planejamento da professora X" ou "qual a melhor regra para ele". Não é o diagnóstico inicial de CNIS (esse tem skill própria: `diagnostico-previdenciario-coloqueseunomeaqui`); esta é o produto completo, rodado com a documentação do cliente em mãos.

Este é o produto principal do escritório: a auditoria previdenciária estratégica completa de um professor ou professora, entregue como parecer, relatório técnico e
reunião de apresentação. O cliente já pagou por ele e vai tomar decisões de vida a partir dele —
sair ou não do emprego, continuar ou não contribuindo, averbar ou não um período, requerer agora
ou daqui a três anos.

**O que diferencia este trabalho de uma consulta previdenciária comum:** ele não termina em uma
data. Ele responde, para aquele professor específico:

QUANDO se aposentar · POR QUAL REGRA · EM QUAL REGIME · COM QUAL VALOR · QUAL É A BASE LEGAL ·
QUANTO PRECISA INVESTIR ATÉ LÁ · QUAIS PERÍODOS PRECISAM SER CORRIGIDOS OU APROVEITADOS · QUAIS
DOCUMENTOS PRECISAM SER PROVIDENCIADOS · SE EXISTE FORMA DE ANTECIPAR OU AUMENTAR O BENEFÍCIO ·
QUAL É A ESTRATÉGIA FINANCEIRAMENTE MAIS VANTAJOSA.

Um planejamento que só diz "a professora poderá se aposentar em 2031" não foi entregue.

## As 6 regras de ouro (violar qualquer uma invalida o trabalho)

Regras condensadas do que mais custou caro nesta área — na prática previdenciária de servidores (RPPS) e nesta própria skill. Leia antes de abrir o primeiro documento do cliente.

1. **Identifique o REGIME e, se houver RPPS, o ENTE e a lei de reforma DELE antes de qualquer
   cálculo.** Não existe "regra da EC 103" automática para servidor estadual/municipal — cada ente
   com RPPS tem sua própria emenda/lei, e enquanto o ente não reformou, valem as regras anteriores
   (art. 4º, § 9º; art. 10, § 7º; art. 20, § 4º da EC 103). **Presumir a regra federal é o erro
   mais caro e mais comum desta área.** Confirme no CADPREV antes de pesquisar a lei em si —
   `references/pesquisa-legislacao-rpps.md`.
2. **Nunca faça a conta de cabeça.** Tempo, média, coeficiente, teto e descarte são calculados
   pelos scripts (`scripts/tempo.py`, `scripts/rmi.py`, `scripts/cenarios.py`) — nunca
   mentalmente e nunca só pelo número de uma calculadora ou de um software de cálculo.
3. **Nunca presuma tempo de magistério.** Direção, coordenação e assessoramento pedagógico podem
   contar (LDB art. 67, § 2º; ADI 3.772/STF), mas cargo administrativo, readaptação, licença
   prolongada e função gratificada fora do magistério normalmente não contam — e é justamente onde
   o INSS ou o ente glosa. Um único período mal qualificado derruba a regra inteira do professor.
4. **Simule TODAS as regras aplicáveis e compare pelo BENEFÍCIO FINAL, nunca uma única rota.**
   Direito adquirido, cada regra de transição, regra permanente, com e sem CTC, com e sem
   descarte — e, quando houver mais de um regime, a possibilidade de duas aposentadorias
   distintas.
5. **Teste sempre o descarte de contribuições (art. 26, § 6º)**, mas comparando o PROVENTO FINAL,
   nunca só a média — descartar sobe a média e desce o coeficiente ao mesmo tempo, e pode derrubar
   um requisito da regra escolhida.
6. **Cheque concomitância antes de somar tempo ou somar salário.** Art. 96, II da Lei 8.213/91
   veda contar tempo concomitante duas vezes. Atenção especial a vínculos do MESMO empregador
   reportados em CNPJs diferentes ao longo do tempo (comum em RAIS/GFIP/eSocial) — é concomitância
   de REGISTRO, não emprego simultâneo de verdade: some o tempo uma vez só e não duplique o
   salário da competência que aparecer nos dois registros.

## Antes de começar: a regra de bloqueio

**É proibido concluir data de aposentadoria, RMI, direito adquirido ou estratégia antes de
concluir o levantamento legislativo do caso (etapas 1 a 3 abaixo).** Essa não é uma formalidade
de processo. O erro que mais destrói um planejamento de professor é aplicar automaticamente a EC
103/2019 a um servidor municipal cujo município ainda não reformou o próprio regime — o art. 4º,
§ 9º, o art. 10, § 7º e o art. 20, § 4º da própria EC 103 mandam continuar aplicando as normas
anteriores aos Estados e Municípios "enquanto não promovidas alterações na legislação interna
relacionada ao respectivo regime próprio". Aplicar a regra errada muda a data em anos e a RMI em
milhares de reais, e o cliente só descobre no indeferimento.

A ordem é sempre:

**IDENTIFICAR O CASO → LEVANTAR A LEGISLAÇÃO APLICÁVEL → VALIDAR A VIGÊNCIA → ANALISAR OS
DOCUMENTOS → CALCULAR → SIMULAR CENÁRIOS → RECOMENDAR A ESTRATÉGIA.**

Nunca inverta. Se em algum ponto a legislação de um RPPS não puder ser confirmada, marque a
conclusão correspondente como **PENDENTE DE VALIDAÇÃO DA LEGISLAÇÃO LOCAL** e siga com o resto —
não apresente aquele número como definitivo e não o leve para os slides.

## Entrada

A pasta de documentos do cliente, que normalmente traz: CNIS atualizado, CTPS (física e digital),
carnês e comprovantes de recolhimento, fichas funcionais e assentamentos, portarias de nomeação e
exoneração, contratos temporários, contracheques, declarações de tempo de serviço e de exercício
de magistério, CTC, documentos de averbação, PPP, LTCAT, processos administrativos anteriores.

Trabalhe com o que existir. **A ausência de um documento é um achado, não um obstáculo** — ela vai
para o checklist documental e para o plano de ação. Se a análise depender de um documento que não
está na pasta, diga qual conclusão ficou pendente por causa dele, em vez de preencher a lacuna com
suposição.

### Dois modos de entrega: ESBOÇO e DEFINITIVO

Nem todo cliente chega com a pasta completa, e esperar a documentação toda antes de entregar
qualquer coisa deixa o cliente sem retorno por semanas — às vezes o professor nunca consegue reunir
100% do que falta. Por isso o planejamento roda em dois modos possíveis; decida qual se aplica logo
no início, a partir do que a pasta tem:

- **ESBOÇO PRELIMINAR** — use quando faltar documento que pode mudar tempo, regime ou regra
  aplicável (o caso mais comum: falta CTPS/declaração de um vínculo antigo, falta CTC de um RPPS
  anterior, falta PPP quando há indício de tempo especial). Rode o fluxo completo (etapas 1 a 12)
  normalmente, mas **toda conclusão que depende do documento ausente sai com o selo PENDENTE**, com
  a frase exata do que aquele documento mudaria se chegasse ("se a declaração de magistério do
  período X confirmar a função, o tempo de professor sobe para Y e a regra Z passa a estar
  disponível"). As três entregas (relatório, parecer, apresentação) saem normalmente, mas cada uma
  leva, na capa ou no cabeçalho, a marca **"ESBOÇO — sujeito a ajuste conforme documentação
  pendente"** e a lista exata do que falta e o que cada item pode mudar. Isso não é uma versão
  "fraca" do produto — é a entrega certa para quem ainda não tem tudo, e evita o cliente ficar
  semanas sem nenhum retorno.
- **DEFINITIVO** — quando a pasta está completa, ou quando o usuário confirma que um documento
  pendente do esboço não vai ser conseguido (então a conclusão correspondente vira PENDENTE
  definitivo, não mais "esperando chegar"). Roda o mesmo fluxo; a diferença é que não sobra selo
  PENDENTE por documento que ainda estava a caminho.

**Ao evoluir de ESBOÇO para DEFINITIVO, não redija do zero.** Edite as três entregas já existentes:
atualize os pontos que o documento novo resolveu, troque os selos correspondentes, e **confira
cruzado de novo** (todo número que aparece em mais de um lugar muda junto). Registre no relatório
técnico qual documento chegou e o que ele mudou — é auditoria útil para o cliente entender por que
o número final é diferente do esboço que ele recebeu antes.

### Quando o cliente tem tempo em mais de um regime (caso misto)

**Isto não é exceção — é o caso mais comum.** Um professor efetivo de rede com RPPS quase sempre
também tem algum tempo em RGPS (rede privada antes de efetivar, contrato temporário anterior ao
concurso, período como contribuinte individual). Detecte isso já na etapa 1 (ficha do caso: "a que
regime cada vínculo pertence") — não é preciso o cliente ter dois vínculos simultâneos, basta ter
passado por regimes diferentes em períodos diferentes da vida.

Quando identificar caso misto:

- Faça o levantamento normativo **separadamente para cada regime** (etapa 2) e só depois cruze —
  nunca aplique regra de um regime ao tempo do outro.
- Teste explicitamente a possibilidade de **duas aposentadorias distintas** (uma por regime) contra
  a de **uma só com contagem recíproca via CTC** — compare pelo benefício total, e antes de
  recomendar a CTC confirme que ela não inviabiliza o benefício no regime de origem (regra de ouro
  4 e 6, e art. 25, § 3º da EC 103 em `base-normativa-federal.md`, seção 7).
- **Isso é trabalho genuinamente maior** que um caso de regime único — dois levantamentos
  normativos, duas apurações de tempo, e a comparação entre "duas aposentadorias" e "uma
  contagem recíproca" multiplicam os cenários a simular. Registre esse volume de trabalho
  explicitamente no relatório técnico (quantos regimes, quantos cenários testados) — é informação
  que o(a) advogado(a) pode usar para justificar o valor cobrado num caso misto, que tende a custar mais
  que um planejamento de regime único. A decisão de precificar diferente é comercial, do(a) advogado(a);
  esta skill só deixa o volume de trabalho visível e auditável.

Quando o escritório usar um software de gestão/cálculo previdenciário com integração (MCP ou API), use-o para localizar o cliente, ler os arquivos já importados e conferir siglas do CNIS. **Atenção ao que essa integração faz e ao que ela não faz:** em regra ela não executa cálculo previdenciário por API — confirme isso antes de depender dela. Ver etapa 7.

## Fluxo de trabalho

### 1. Identificar o caso

Antes de qualquer pesquisa, monte a ficha do caso: nome, data de nascimento, sexo, todos os
vínculos com órgão/empregador, cargo e natureza (efetivo, temporário, celetista, contribuinte
individual), e a que regime cada um pertence — RGPS, RPPS municipal (qual município), RPPS
estadual (qual estado), RPPS federal, ou regime não identificado.

Essa ficha define o que pesquisar. Um caso 100% RGPS pesquisa uma coisa; uma professora com 12
anos de prefeitura e 18 anos de rede privada pesquisa três (RGPS, RPPS daquele município,
e as regras de contagem recíproca entre eles).

### 2. Levantar a legislação aplicável

Siga `references/pesquisa-legislacao-rpps.md`, que traz o roteiro de busca, as fontes oficiais e
os erros típicos. A base federal já mapeada e conferida está em `references/base-normativa-federal.md`
— leia esse arquivo antes de testar qualquer regra, mas leia-o como **mapa**, não como código:
ele diz qual artigo governa qual pergunta e onde conferir o texto vigente.

**Pesquise na web em toda execução.** Mesmo num caso puramente RGPS, confirme se houve alteração
posterior às normas do mapa. Num caso com RPPS, a pesquisa da lei local é obrigatória e não tem
substituto: descubra se o ente promoveu reforma própria, quando ela entrou em vigor, o que foi
recepcionado, quais regras permanentes e de transição foram criadas, e se há regra específica para
professor. Se o professor tiver vínculo em mais de um ente, faça o levantamento separadamente para
cada um.

Monte a **linha do tempo normativa do cliente**: o que estava em vigor em cada marco relevante da
vida contributiva dele (pré-EC 20/1998, EC 20/1998, EC 41/2003, EC 47/2005, EC 70/2012, EC 88/2015,
EC 103/2019, reforma estadual, reforma municipal, alterações posteriores).

### 3. Validar a vigência e a jurisprudência

Para cada norma que vai sustentar uma conclusão: data de publicação, início de vigência, alterações
posteriores, revogação expressa ou tácita, declaração de inconstitucionalidade, modulação de
efeitos. **Nunca cite uma norma só porque ela aparece em material antigo do escritório.**

Pesquise também o entendimento consolidado sobre os pontos controvertidos do caso — STF, STJ, TNU,
TRFs, tribunais de contas e o próprio INSS —, priorizando repercussão geral, repetitivos, súmulas e
precedentes vinculantes. Decisão isolada pode ser usada, mas nunca como fundamento principal sem
que o risco jurídico esteja escrito ao lado dela.

### 4. Auditar os documentos e reconstruir os vínculos

Liste cronologicamente **todos** os vínculos e cruze as fontes: CNIS × CTPS × ficha funcional ×
contracheques × portarias × CTC × declarações. Para cada vínculo registre: período, empregador,
função, regime, se consta do CNIS, se consta de outra fonte, qual documento comprova, situação e
providência necessária.

Aponte vínculos ausentes, incompletos, com datas divergentes, com remunerações divergentes,
concomitantes, sem contribuição, ainda não averbados e não computados pelo órgão.

**Atenção ao padrão de "mesmo emprego, dois registros"**: quando o mesmo empregador aparece em
vínculos com a mesma data de início e período quase idêntico, mas CNPJ diferente, normalmente é o
mesmo emprego reportado por duas fontes ao longo do tempo (RAIS/GFIP/eSocial), não dois empregos
simultâneos de verdade — confira as competências de cada um antes de somar tempo ou salário; a
regra 6 do topo desta skill existe por causa desse padrão.

Trate **todos** os indicadores do CNIS: sigla, explicação jurídica, tradução em linguagem simples,
impacto, se impede ou não o cômputo automático, como regularizar e quais documentos são
necessários. `references/indicadores-cnis.md` cobre os mais frequentes e traz a URL do Anexo V
oficial para os demais — nunca descreva um indicador de memória.

### 5. Qualificar o tempo de magistério

Esta é a análise que define o produto. Classifique cada período como: **efetivo exercício das
funções de magistério**, **tempo comum**, **potencialmente controvertido**, ou **carente de
comprovação complementar**.

**Nunca presuma que todo vínculo com Secretaria de Educação é tempo qualificado de professor.**
Direção, coordenação e assessoramento pedagógico podem contar, nos termos do art. 67, § 2º da LDB
e do entendimento consolidado (ADI 3.772/STF), mas cargo administrativo, readaptação, licença
prolongada, cessão e função gratificada fora do magistério normalmente não contam — e é justamente
onde o INSS glosa. Para cada período, diga se há possibilidade jurídica de cômputo como magistério
e com qual fundamento; quando o documento que sustentaria isso não estiver na pasta, marque
PENDENTE e leve para o checklist.

Lembre que as regras do professor exigem tempo **exclusivamente** em funções de magistério na
educação infantil, fundamental e médio — um único período mal qualificado derruba a regra inteira,
então o total de magistério precisa ser apurado com o mesmo rigor do tempo total.

### 6. Apurar tempo, carência e requisitos

Use `scripts/tempo.py` em vez de somar períodos à mão — ele faz união com desconto de
concomitância, converte em anos/meses/dias, corta por marco temporal e projeta a data em que cada
requisito é atingido. Somar períodos manualmente é onde aparecem os erros que depois deixam o
parecer, os slides e a planilha divergindo entre si.

Apure separadamente: tempo total no RGPS; tempo em cada RPPS; tempo de magistério; tempo comum;
tempo já averbado; tempo disponível para averbação; tempo até 16/12/1998, até 31/12/2003, até
13/11/2019 e posterior; carência; tempo de serviço público; tempo no cargo; tempo na carreira
quando a lei local exigir. Sempre em **anos, meses e dias**.

Analise também, quando houver indício: **tempo especial** (se houver PPP na pasta, rode a análise
completa — preenchimento, agentes, metodologia, responsável técnico, EPC/EPI, coerência com LTCAT,
possibilidade de enquadramento e de conversão até 13/11/2019, e quais campos precisam de retificação)
e **tempo rural** (local de nascimento, profissão dos pais, idade de início, documentos antigos,
INCRA/ITR/sindicato/notas de produtor; se houver indício razoável, dimensione o período, a
necessidade de indenização, o custo e o impacto).

### 7. Testar todas as regras

Comece pelo **direito adquirido**: verifique, em cada marco normativo, se o cliente já havia
preenchido os requisitos de alguma aposentadoria antes da mudança. Nunca descarte uma regra antiga
sem simular o valor — a EC 103, art. 3º garante a concessão a qualquer tempo pelos critérios da
legislação vigente na data em que os requisitos foram atendidos, e essa é frequentemente a melhor
opção de um professor com vida contributiva longa.

Depois teste **todas** as regras potencialmente aplicáveis do regime dele, não só as mais
conhecidas: pontos, idade progressiva, pedágio de 50%, pedágio de 100%, regras permanentes, regras
do RPPS federal, regras de transição estaduais e municipais, aposentadoria por idade e comum quando
vantajosas. Os requisitos conferidos de cada uma estão em `references/base-normativa-federal.md`.

Para cada regra apresente: requisitos, requisitos já preenchidos, requisitos faltantes, data exata
de implementação, RMI estimada, documentação necessária, riscos, vantagens e desvantagens. Uma
regra que não se aplica também merece uma linha dizendo por quê — é isso que impede o cliente de
voltar em seis meses perguntando "e a regra do pedágio?".

Verifique se há possibilidade de **aposentadorias distintas em regimes diferentes** e, antes de
recomendar qualquer averbação ou CTC, confira se usar aquele tempo num regime não inviabiliza o
benefício no outro. Recomendação de averbação sem esse teste é o erro mais caro que este
planejamento pode conter.

**Software de cálculo do escritório — como encaixar.** Se o escritório usa um motor de cálculo previdenciário como fonte oficial para RMI, atrasados e valor da causa, ele aplica os índices de correção e a legislação vigente e entrega resultado auditável — mas costuma ser executado pelo próprio usuário, não por API. Então a divisão de trabalho é esta:

- **Esta skill faz a leitura jurídica e o cálculo independente**: reconstrução dos vínculos,
  qualificação do magistério, teste de todas as regras, apuração de tempo, RMI própria, cenários e
  estratégia. É o que permite auditar o número que o motor devolver.
- **O motor do software fecha os números oficiais.** Encaminhe o usuário à análise certa, informando que o cliente e o CNIS já estão (ou precisam ser) cadastrados lá.
- **Quando os dois números voltarem, compare-os e registre a divergência expressamente** no
  relatório técnico, em vez de escolher um em silêncio. Divergência não é erro de um dos dois: é o
  ponto que precisa ser investigado antes do requerimento.

O motor do software também resolve, sozinho, a atualização monetária dos salários de contribuição
— que é a pendência mais comum desta skill quando as fontes oficiais de índice não estão acessíveis.
Se a RMI ficou como piso nominal, é ali que ela se fecha — ou use `references/teto-inss-historico.md`
e a tabela oficial de índices do INSS/Dataprev para fechar por conta própria (ver etapa 8).

### 8. Calcular a RMI

Refaça o cálculo de forma independente, com `scripts/rmi.py`. Não se limite ao valor de calculadora
ou de software. A metodologia, o tratamento de salários concomitantes, o teto, e a regra de
descarte estão em `references/calculo-e-cenarios.md`.

**Teto do RGPS: use sempre o histórico por competência, nunca o de hoje.** `scripts/rmi.py` já
aplica por padrão o teto vigente em cada competência (`scripts/tetos_historicos.csv` +
`references/teto-inss-historico.md`) sobre o valor nominal, antes da correção monetária — essa
ordem é a que a lei manda, e capar pelo teto de hoje um salário antigo já corrigido produz um
número errado. Só use `--teto` (valor fixo) com justificativa registrada no relatório.

Três conferências que já custaram caro quando foram puladas: (i) **o 13º salário não integra o
salário de benefício** (Lei 8.213, art. 29, § 3º), e o CNIS frequentemente lança a remuneração de
dezembro já somada ao 13º — uma competência de dezembro muito acima das vizinhas é sinal disso, e
expurgá-la exige a ficha financeira daquele ano; (ii) **some as bases concomitantes** mês a mês
antes de calcular a média, respeitado o teto — mas confira antes se a concomitância é de emprego
de verdade ou de REGISTRO (regra 6 do topo desta skill); somar duas vezes o salário de um único
emprego reportado sob dois CNPJs infla a RMI de forma incorreta; (iii) confira se o segurado tem
**mais de uma inscrição (NIT)** no extrato — vínculos espalhados entre dois NITs travam o
requerimento e podem fazer o sistema deixar de somar parte do tempo.

Teste **sempre** o descarte de contribuições que reduzem a média (EC 103, art. 26, § 6º): informe
quais competências sairiam, o fundamento, o tempo recalculado, a média recalculada, o benefício
recalculado e o ganho mensal, anual e projetado. Não recomende descarte que derrube um requisito da
aposentadoria.

**Atenção ao que o script confere e ao que ele NÃO confere** (achado de um relatório de validação com caso real: das 5 competências que ele mandou descartar, 4 eram de magistério
e a cliente chegava ao pedágio de 100% com folga zero — o descarte "melhorava" a RMI de uma
aposentadoria que deixava de existir). O `rmi.py` confere sozinho o **tempo total** contra
`--tempo-minimo-dias`. Ele só protege o **tempo de magistério** se você passar
`--competencias-magisterio <arquivo>` (lista das competências qualificadas, uma `AAAA-MM` por
linha) e `--folga-magisterio-dias <N>` (quanto tempo de magistério sobra acima do exigido pela
regra escolhida; o default é **0**, ou seja, nenhuma competência de magistério é descartada).
Sem essas flags o script avisa em `stderr` que a conferência do tempo de professor é **manual** —
e é mesmo: confira competência a competência antes de levar o descarte ao parecer.

### 9. Simular os cenários de contribuição futura

Simule, quando aplicáveis, os cenários A a G descritos em `references/calculo-e-cenarios.md`
(permanecer no vínculo; contribuinte individual pelo mínimo; pelo teto; pelo último salário de
contribuição; valor intermediário estratégico; parar de contribuir; outra categoria mais econômica).

**Nunca recomende facultativo para quem exerce atividade remunerada** — é filiação obrigatória, e a
contribuição feita na categoria errada não é aproveitada.

Para cada cenário: contribuição mensal, tempo restante, custo total até a aposentadoria, data da
aposentadoria, RMI projetada, diferença de RMI, prazo para recuperar o investimento e retorno
financeiro estimado. `scripts/cenarios.py` monta a tabela.

### 10. Fazer a análise econômica

Consulte a **tábua de mortalidade do IBGE vigente na data do planejamento** (busque na web; não use
expectativa memorizada) para o sexo e a idade do cliente. Calcule, para cada cenário, o valor total
estimado a receber = benefício mensal projetado × número de pagamentos até a expectativa de vida,
considerando o 13º quando pertinente.

Compare explicitamente **aposentar antes e receber por mais tempo** contra **esperar para ter RMI
maior**, com o ponto de equilíbrio em meses. Não trate o maior benefício mensal como
automaticamente melhor — para um professor de 58 anos, quatro anos a mais de espera custam quatro
anos de benefício que nunca voltam.

**Quando a RMI apurada ficar bem abaixo do salário atual do cliente** (comum em quem teve anos de
salário baixo no início da carreira, mesmo corrigidos), isso não é um defeito do planejamento — é
exatamente o tipo de achado que torna os cenários de contribuição futura (etapa 9) e o custo de
postergar mais relevantes, não menos. Não amenize o número nem o esconda: explique a composição
(quais anos pesam a média para baixo) e mostre o que cada cenário de contribuição futura faz a
esse número. Isso é entrega de valor, não má notícia — o cliente está pagando exatamente para saber
disso antes de decidir, não depois.

Deixe escrito que a expectativa de vida é ferramenta estatística de comparação, não previsão
individual.

### 11. Definir a estratégia

Apresente sempre os quatro recortes — **cenário mais rápido**, **maior benefício**, **menor
investimento**, **melhor custo-benefício** — e então a **estratégia recomendada pelo escritório**,
justificada considerando conjuntamente segurança jurídica, tempo, idade, RMI, custo de contribuição,
possibilidade de aposentadoria em mais de um regime, expectativa de vida, retorno financeiro,
complexidade documental e risco administrativo/judicial.

A recomendação é do(a) advogado(a), e precisa ser defensável perante outro advogado que leia o relatório.

**Averbação: "poder" não é "dever".** Quando o caso permitir averbar um período (CTC de outro
regime), isso é um dos pontos que mais motiva a contratação — mas nunca recomende automaticamente
só porque é juridicamente possível. Poder averbar um tempo não significa que averbar é a melhor
estratégia para aquele cliente: compare o cenário com e sem a averbação pelo benefício final (regra
de ouro 4), verifique se ela não inviabiliza aposentadoria no regime de origem (seção "caso misto",
acima), e só recomende quando o resultado comparado mostrar vantagem real. A estratégia em torno da
averbação — inclusive quando a resposta certa é "não averbar" ou "averbar só parte do tempo" — é
parte do que o cliente está pagando para saber.

### 12. Montar o plano de ação

Organize em **urgente**, **antes do requerimento**, **no momento do requerimento** e **após o
requerimento**. Para cada providência: o que fazer → onde fazer → documento necessário → objetivo →
prioridade.

## Como classificar cada conclusão

Marque toda conclusão relevante com um destes selos, e use-os também nos slides:

- **CONFIRMADO** — documentação e fundamento jurídico suficientes.
- **PROVÁVEL** — fortes elementos, mas depende de confirmação documental ou de posicionamento do órgão.
- **PENDENTE** — documentação ou base jurídica insuficiente; diga o que falta.
- **PENDENTE DE VALIDAÇÃO DA LEGISLAÇÃO LOCAL** — o RPPS envolvido não pôde ser confirmado.
- **NÃO RECOMENDADO** — juridicamente possível, mas com risco jurídico ou financeiro relevante.

Um planejamento honesto tem selos misturados. Um planejamento em que tudo é CONFIRMADO
provavelmente não auditou a própria base.

## Saídas obrigatórias

Três entregas, sempre, geradas **da mesma análise estruturada** — nunca redigidas como três
exercícios independentes, ou elas divergem nos números:

1. **Relatório técnico interno** (para o(a) advogado(a)) — completo, sem simplificação.
2. **Parecer / Planejamento Previdenciário do cliente** (PDF em identidade visual do escritório) —
   linguagem profissional e clara, sem excesso de juridiquês.
3. **Apresentação da reunião** (PPTX montado com a skill `pptx`, na identidade visual do escritório), com o roteiro completo **apenas nas notas do apresentador**, nunca no corpo do slide.

A estrutura detalhada de cada uma, a identidade visual e o roteiro da reunião estão em
`references/entregaveis.md`. Leia esse arquivo antes de gerar qualquer arquivo, e consulte os
skills `pdf` e `pptx` para a mecânica.

**Confira cruzado antes de entregar:** todo número que aparece em mais de um lugar (tempo total,
tempo de magistério, datas, RMI, custo dos cenários) tem que ser idêntico nas três entregas. Se um
mudar numa correção, releia os três documentos inteiros — não só o trecho corrigido.

## Auditoria final e revisão independente

Duas travas, nesta ordem — nenhuma substitui a outra:

1. **Autoconferência**: antes de considerar o trabalho pronto para revisão, responda internamente
   às perguntas de `references/auditoria-final.md`. Se qualquer resposta for NÃO, revise antes de
   prosseguir.
2. **Revisão independente obrigatória**: nenhum planejamento, memória de cálculo ou parecer sai
   para o(a) advogado(a) sem passar pela skill `planejamento-previdenciario-coloqueseunomeaqui-revisor` (agente
   independente que refaz contagens e médias, ataca o enquadramento e devolve veredito
   PRONTO/NÃO PRONTO). Invoque-a como subagente ao final do trabalho. Se o veredito for NÃO
   PRONTO, corrija os defeitos GRAVES e submeta de novo — não entregue "com ressalvas".

## Forma de tratamento

Nos documentos e slides, o cliente é **Professor [Nome]** ou **Professora [Nome]**, tratado por
**senhor/senhora**, sem informalidade e sem travessão no texto corrido. Isso vale para o parecer,
para os slides e para qualquer mensagem que o(a) advogado(a) vá encaminhar ao cliente.

## Padrão de segurança

Nunca: invente períodos ou salários; presuma a existência de um documento; presuma tempo de
magistério; presuma averbação já feita; presuma legislação local; presuma que o cálculo do software
está correto; apresente data ou RMI como definitiva quando ela depende de informação ausente;
aplique regra de RGPS a RPPS sem validação; aplique automaticamente a EC 103/2019 a Estado ou
Município; use legislação revogada; capeie salário pelo teto de hoje em vez do teto histórico da
competência; ou baseie o planejamento apenas em calculadora previdenciária.

Quando faltar informação, o caminho é dizer o que falta e classificar a conclusão — não estimar. Um
número presumido levado a um requerimento se volta contra o segurado, e o cliente não tem como
saber que aquele número nunca foi verificado.
