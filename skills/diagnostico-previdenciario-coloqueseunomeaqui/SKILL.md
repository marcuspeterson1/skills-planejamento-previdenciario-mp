---
name: diagnostico-previdenciario-coloqueseunomeaqui
description: "Diagnóstico inicial a partir do CNIS de professor(a): tempo total, regular e em risco, pendências e indicadores; gera relatório PDF, slides, roteiro e lista de documentos. Use ao receber um CNIS."
---

# Diagnóstico Previdenciário de Professores

## Antes do primeiro uso: coloque o seu nome nesta skill

Esta skill é distribuída com o nome-modelo `diagnostico-previdenciario-coloqueseunomeaqui`. **Na primeira vez que ela for usada**, se o nome da pasta da skill ainda contiver `coloqueseunomeaqui`, pare antes de começar o trabalho e oriente o usuário, em linguagem simples:

1. Explique que a parte `coloqueseunomeaqui` deve ser trocada pelo nome dele(a), pelo nome do escritório ou pelo nome do método próprio (ex.: `diagnostico-previdenciario-silva` ou `diagnostico-previdenciario-metodoalfa`). Use só letras minúsculas sem acento, números e hífens, sem espaços.
2. Ofereça-se para fazer a troca. Se ele(a) aceitar, pergunte o nome desejado e então: (a) renomeie a pasta da skill; (b) altere o campo `name:` no topo deste `SKILL.md`; (c) atualize as referências às outras skills da mesma família (`planejamento-previdenciario-coloqueseunomeaqui`, `planejamento-previdenciario-coloqueseunomeaqui-revisor`), que devem receber o mesmo nome novo; (d) avise que pode ser preciso reiniciar o Claude, ou abrir uma nova conversa, para o nome novo aparecer. No Claude pela web/aplicativo não dá para renomear pasta instalada: nesse caso, oriente a gerar um novo `.zip` da pasta já com o nome novo e enviá-lo de novo.
3. Aproveite para colher, e confirmar com o usuário antes de usar, os dados que personalizam as entregas: nome do escritório, nome do método (se tiver um), nome e OAB do(a) advogado(a), cores e logotipo, **nomes, escopo e valores dos pacotes, e condições de pagamento** (as seções B e C dependem deles). Nenhum desses dados vem preenchido nesta skill — nunca invente.
4. Se o usuário preferir não trocar agora, siga com o trabalho normalmente: o nome não altera o funcionamento.

## Quando usar

Use sempre que o usuário enviar um CNIS (ou "extrato previdenciário", "extrato do INSS") pedindo diagnóstico, análise, parecer, avaliação de pendências, estimativa de tempo de contribuição, ou preparação para a reunião de diagnóstico/venda — mesmo que diga só "roda o diagnóstico desse CNIS" ou "prepara a reunião da/do [nome do cliente]". **Não** é para calcular o valor exato do benefício nem para produzir o Planejamento Previdenciário Estratégico completo (produto mais aprofundado, com skill própria: `planejamento-previdenciario-coloqueseunomeaqui`) — esta skill é o diagnóstico inicial, gratuito para o cliente.

Gera o "Diagnóstico Previdenciário Estratégico": a primeira etapa do funil comercial do escritório. O cliente (normalmente um professor ou professora vinculado ao INSS, muitas vezes com trechos de Regime Próprio) manda o CNIS; o(a) advogado(a) usa o diagnóstico gerado por esta skill na reunião gratuita de 30 minutos (ajuste ao formato do escritório) para mostrar o que está errado no CNIS e conduzir à venda de um dos pacotes do escritório (ver "Pacotes de referência", seção B).

**Por que isso importa:** o diagnóstico é a peça central da conversão comercial do escritório — é ele que mostra ao cliente, de forma concreta, quanto tempo de contribuição está em risco e por quê. Um diagnóstico impreciso ou genérico demais não vende; um diagnóstico que inventa pendências que não existem é um risco ético e reputacional para o(a) advogado(a). As duas coisas importam igualmente: precisão técnica E poder de persuasão visual.

## Entrada

Dois elementos, não um só:

1. O extrato **CNIS em PDF** (baixado do Meu INSS) — continua sendo a fonte técnica, obrigatória.
2. **As respostas do formulário de captação daquele cliente** — regime previdenciário declarado
   (RGPS/RPPS/"não sei informar"), tipo de vínculo (efetivo/contratado/rede privada), tempo de
   atuação como professor(a), cidade/estado, e a situação específica que a pessoa descreveu em
   texto livre. Se a automação estiver rodando via Dossiê do cliente (Google Doc único, seção 1),
   leia as respostas ali; se vier avulso, peça-as.

**Nunca rode o diagnóstico só com o CNIS quando o formulário estiver disponível.** Cruzar as duas
fontes é o que permite: (a) confirmar ou contestar o regime que a pessoa declarou (achado real —
ver passo 3.5); (b) checar se o tipo de vínculo declarado é compatível com os indicadores do CNIS
(ex.: "efetivo" declarado num período em que o CNIS mostra Contribuinte Individual é
inconsistência a registrar, não a ignorar); (c) usar o tempo de magistério que a pessoa informou
como ponto de partida da triagem interna do passo 7, sabendo que pode estar impreciso — a pessoa
pode não saber responder direito, por isso o CNIS sempre tem a palavra final sobre o que entra na
conta, mas o declarado orienta onde procurar.

Não espere outros documentos do cliente (CTPS, RG, laudos) além desses dois — eles só entram nas
etapas pagas (acerto de CNIS/planejamento). Se o PDF do CNIS vier ilegível, corrompido, ou com
páginas faltando, **diga isso explicitamente** no diagnóstico em vez de preencher lacunas por
conta própria. Se as respostas do formulário não estiverem disponíveis por algum motivo, rode
mesmo assim só com o CNIS, mas registre no relatório que o cruzamento não foi possível — não é
motivo para recusar o diagnóstico, é uma ressalva a declarar.

## Fluxo de trabalho

### 1. Ler e estruturar o CNIS

Extraia do PDF, vínculo por vínculo: **o número de sequência (Seq.) exatamente como aparece no
CNIS**, origem (empregador), tipo de filiado (empregado, contribuinte individual, facultativo,
segurado especial), data de início, data de fim (ou "em aberto"), indicadores do vínculo, e cada
competência com sua remuneração e indicadores associados. Monte uma tabela estruturada (ex.:
JSON ou DataFrame) antes de qualquer análise — isso evita erros de transcrição e facilita gerar
tanto o PDF quanto os slides a partir da mesma fonte de dados. **Guarde o número Seq. de cada
vínculo junto com seus dados** — ele é obrigatório mais adiante, tanto para a apuração do tempo
quanto para o quadro de pendências (passo 4 e seção "Saídas").

Extraia também, dos dados cadastrais do segurado no cabeçalho do CNIS: **data de nascimento** e,
se constar, **sexo**. Esses dois dados não entram em nenhuma análise de vínculos, mas são a base
da triagem previdenciária interna do passo 7 — se a data de nascimento não constar do PDF, deixe
isso registrado e trate a idade como informação indisponível na triagem (não estime nem presuma).

### 2. Apurar o tempo total, o tempo regular e o tempo em risco

**O tempo total estimado NÃO se limita às competências com remuneração registrada.** Ele
considera os **períodos dos vínculos previdenciários constantes do CNIS** (início ao fim de cada
vínculo empregatício/contributivo, Seq. por Seq.), **descontadas as concomitâncias entre eles** —
inclusive os períodos que apresentem pendências e que, por isso, ainda dependam de
regularização, validação ou comprovação documental para seu efetivo reconhecimento pelo INSS.
Não exclua um período do tempo total só porque ele tem uma pendência: pendência é motivo para
classificar o período como **em risco**, não para tirá-lo da conta.

**Período de vínculo registrado sem contribuição correspondente é SEMPRE tempo em risco.** Vale
tanto para a lacuna de remuneração **dentro** de um vínculo quanto para o caso extremo do vínculo
declarado no CNIS **sem nenhuma competência de remuneração lançada**. O raciocínio é o mesmo nos
dois: o vínculo existe no extrato, e é isso que sustenta a contagem; o que falta é a contribuição,
e é isso que caracteriza o risco. Nunca trate um período assim como "tempo que não dá para
contar" — é frequentemente onde está a maior oportunidade de recuperação de tempo do cliente, e
escondê-lo mascara o tamanho real do problema.

**Mas NUNCA presuma uma data que o CNIS não informa.** Se o vínculo registrado sem contribuição
não tiver Data Fim **e** não tiver campo de última remuneração, o extrato não oferece nenhum
elemento para medir a sua extensão. Nesse caso, registre-o como **"tempo em risco — extensão a
apurar"**, informe a Data Início que consta, deixe-o **fora** do tempo total estimado por
impossibilidade de delimitação, e diga expressamente no relatório e nos slides que o tempo total é
**um piso e não um teto**. Está proibido, sem exceção, adotar como fim a véspera do vínculo
seguinte, a data de emissão do CNIS, o início da lacuna posterior ou qualquer outra data de
conveniência: número presumido levado a um requerimento previdenciário se volta contra o segurado,
e o cliente não pode receber como estimativa um período que ninguém verificou.

Ficam de fora do tempo total, portanto: o período de segurado especial quando concomitante com
atividade urbana e ainda não ratificado (trate-o como achado à parte); os **intervalos de
calendário em que nenhum vínculo sequer está declarado** no CNIS, que são **lacunas** e devem ser
nomeadas assim (não confundir com uma lacuna de remuneração **dentro** de um vínculo já declarado,
que integra o total — ver abaixo); e o vínculo registrado sem contribuição **cuja extensão o CNIS
não permite delimitar**, pelo motivo do parágrafo anterior.

**Não misture essas duas coisas num número só.** Um intervalo de calendário pode conter, ao mesmo
tempo, um trecho sem nenhum vínculo declarado (lacuna) e um trecho com vínculo declarado e vazio
(tempo em risco a apurar). São situações juridicamente distintas, com providências distintas, e
devem ser apuradas e apresentadas **separadamente**, cada uma com o seu período e o seu rótulo.
Somá-las num único bloco de "tanto tempo sem contribuição" confunde o cliente e a própria
advogado(a), e foi erro identificado em uso real desta skill.

**Passo a passo:**

1. **Delimite o período de cada vínculo.** Use a Data Início e a Data Fim do CNIS. Quando a Data
   Fim estiver em branco (comum), use como fim estimado a competência da última remuneração
   registrada (campo "Últ. Remun." do CNIS) — deixe anotado, no relatório, que a data de
   encerramento formal ainda depende de regularização junto ao Portal CNIS. Um vínculo sem
   nenhuma remuneração e sem Data Fim (não confundir com o vínculo ativo atual) não tem fim
   determinável a partir do extrato: **não invente uma data para ele**. Trate-o como **tempo em
   risco de extensão a apurar** (ver a regra acima), com a Data Início que consta, fora do tempo
   total, e apresente-o com destaque próprio no relatório e nos slides — ele não é um detalhe de
   rodapé, costuma ser o achado mais valioso do caso.
2. **Uma o período de todos os vínculos, descontando concomitâncias.** Quando dois ou mais
   vínculos cobrem o mesmo intervalo de calendário (mesmo cargo relatado por fontes diferentes
   ao longo do tempo — ver alerta de concomitância abaixo), esse intervalo entra **uma única
   vez** no tempo total, não uma vez por vínculo.
3. **Dentro dessa união, classifique cada competência/trecho em regular ou em risco** (critério
   completo na próxima subseção). Tempo aparentemente regular + tempo em risco deve ser
   exatamente igual ao tempo total estimado — confira essa soma sempre que recalcular.
4. **Não faça dupla contagem dentro do tempo em risco.** Se a mesma competência for atingida
   simultaneamente por mais de uma pendência (ex.: um mês com PEXT e PRPPS ao mesmo tempo, ou um
   mês dentro do bloqueio EC103 que também está sob PRPPS), ela entra **uma única vez** no total
   de tempo em risco — nunca some os meses de cada indicador separadamente sem checar
   sobreposição.

**O que integra o tempo em risco** — qualquer período com uma circunstância capaz de comprometer
seu reconhecimento pelo INSS ou que exija comprovação/regularização, incluindo pelo menos:
- **períodos de vínculo registrado no CNIS sem nenhuma contribuição correspondente** — sempre, e
  pelo período inteiro do vínculo. Quando o período for delimitável pelo extrato (Data Início com
  Data Fim, ou Data Início com competência de última remuneração), ele entra no tempo total com
  número. Quando não for delimitável, entra como **extensão a apurar**, sem número e fora do
  total, conforme a regra acima — mas continua sendo tempo em risco, e deve ser dito ao cliente
  com essas palavras;
- lacunas de remuneração **dentro** de um vínculo já registrado no CNIS (não exclua esses meses
  do tempo total — eles integram o total, mas como tempo em risco; troque a lógica de "esse
  período não entra na contagem" pela lógica de "esse período integra o tempo total estimado,
  mas está em risco e depende de comprovação documental para seu efetivo reconhecimento pelo
  INSS");
- competências sob o indicador **PEXT**;
- competências sob o indicador **PRPPS**;
- competências sob **PREM-BLOQ-EC103**;
- qualquer outro indicador de pendência do Anexo V que, segundo `references/indicadores-cnis.md`
  (ou a checagem no Anexo V oficial), tenha impacto no reconhecimento de direitos daquele
  período.

**Nem todo indicador vira tempo em risco.** Indicadores classificados como puramente
informativos/de alerta e que a fonte oficial diz não terem impacto automático no reconhecimento
(ex.: PADM-EMPR, IVIN-JORN-DIFERENCIADA, ou o indicador-guarda-chuva IREM-INDPEND, que só aponta
para outro indicador já contado) **não** devem ser somados ao tempo em risco — mantenha-os no
quadro de pendências como achados de baixo impacto (cor verde), mas sem tirar tempo do bucket
"regular". Achados estruturais que são mais sobre o **processamento do requerimento** do que
sobre o **reconhecimento do tempo em si** (vínculos concomitantes/duplicados, vínculo sem Data Fim
que tem remunerações lançadas, divergência cadastral de NIT/nome/CPF) também ficam de fora da
conta de tempo em risco — eles continuam no quadro de pendências como achados estruturais, mas não
mudam os três números da seção de tempo. **Atenção:** um vínculo sem nenhuma remuneração **não** é
um desses casos — ele é tempo em risco pela regra acima, mesmo quando a sua extensão for
indeterminável.

**A única exceção à regra do vínculo registrado sem contribuição é a concomitância.** Se o período
desse vínculo estiver **integralmente coberto** por outro vínculo que tem remunerações lançadas
nas mesmas competências, o intervalo de calendário já entra uma única vez no total e já está
classificado como regular por força do outro vínculo — não o reclassifique como em risco, sob pena
de dupla contagem. Nesse caso o vínculo sem remuneração continua no quadro de pendências (afeta
salário de contribuição, RMI e o processamento do requerimento), mas não acrescenta tempo em
risco; diga isso expressamente no relatório, para o cliente entender por que aquela pendência não
aparece na conta de tempo. Se a cobertura for apenas parcial, some ao tempo em risco somente o
trecho descoberto.

**Cuidado com vínculos concomitantes/duplicados ao calcular lacunas sem contribuição.** Quando o
mesmo empregador aparece em vários vínculos com datas de início quase idênticas (comum quando
RAIS/GFIP/eSocial reportam o mesmo cargo por fontes diferentes ao longo do tempo), um vínculo
pode não ter remuneração registrada num trecho que **outro vínculo concomitante já cobre**. Antes
de contar um período como "sem nenhuma contribuição", confira as competências de **todos** os
vínculos concomitantes daquele empregador nesse período — não apenas de um vínculo isolado — ou
o tempo em risco sai superestimado (e os números do PDF e dos slides ficam inconsistentes entre
si, porque nem todo lugar do documento vai repetir o mesmo erro do mesmo jeito).

Expresse tudo em anos/meses/dias sempre que possível. **Deixe explícito que é uma estimativa
inicial**, sujeita a confirmação após análise documental.

### 3. Analisar cada vínculo individualmente

Para cada vínculo (identificado sempre pelo seu número Seq.): compare a data de início/fim com
as competências efetivamente presentes; aponte meses sem registro dentro do intervalo do
vínculo; sinalize vínculos em aberto, duplicados ou concomitantes; sinalize remunerações fora do
período do vínculo (antes do início ou depois do fim).

**Checklist mínimo de varredura** — confirme explicitamente, para cada CNIS, se cada um destes
elementos está presente e, quando estiver, trate-o com o mesmo rigor dos demais achados (registre
no quadro de pendências, com o Seq. correspondente, ainda que a conclusão seja "sem impacto
identificado neste diagnóstico"): vínculos e remunerações declarados; períodos ausentes/lacunas;
vínculos sem data de encerramento; vínculos sem nenhuma remuneração (sempre tempo em risco — com
número quando delimitáveis, como "extensão a apurar" quando não; salvo concomitância integral —
ver passo 2); contribuições abaixo do
mínimo mensal exigido (risco para a carência, não só para o tempo); vínculos/contribuições
concomitantes; indicadores do CNIS (passo 4); pendências cadastrais (nome, CPF, NIT divergentes
entre fontes); vínculos com RPPS (passo 3.5); períodos de serviço público (efetivo, comissionado,
temporário); períodos que possam depender de CTC (Certidão de Tempo de Contribuição) de outro
regime; indícios de atividade especial (insalubridade/periculosidade, quando o CNIS ou o cargo
informado sugerir); indícios de atividade de professor/magistério (relevante para as regras
específicas de aposentadoria do professor); indícios de atividade rural; períodos de segurado
especial; contribuições como facultativo ou contribuinte individual (atenção à carência e à
qualidade de segurado); períodos que possam exigir comprovação documental adicional; divergências
entre fontes de informação dentro do próprio CNIS (ex.: RAIS/GFIP/eSocial reportando o mesmo
vínculo de forma diferente); efeitos da EC 103/2019 sobre o vínculo ou o indicador (ex.:
PREM-BLOQ-EC103); e, de forma residual, qualquer outro elemento identificável no CNIS capaz de
afetar tempo de contribuição, carência, qualidade de segurado, regra aplicável ou valor do
benefício. **Não se limite a citar o código do indicador ou o nome da categoria** — explique o que
ele significa naquele caso concreto, qual período é afetado (com o Seq.), qual o risco e qual
providência pode ser necessária (sujeito às restrições da seção "Saídas → A" sobre o que não entra
no PDF).

### 3.5. Verificar se o empregador público tem Regime Próprio de Previdência Social (RPPS)

Sempre que o indicador **PRPPS** aparecer em um vínculo cujo empregador seja um ente público
(prefeitura, secretaria municipal, fundo/instituto municipal de educação, governo estadual etc.
— identificável pelo nome do "Origem do Vínculo" no CNIS), siga este procedimento padrão, tanto
para este diagnóstico quanto para os próximos:

1. **Identifique o indicador PRPPS** no CNIS e o(s) vínculo(s) (Seq.) em que aparece.
2. **Confirme primeiro se o TIPO DE VÍNCULO declarado no formulário (entrada, ver seção acima)
   sustenta sequer a pergunta.** Contratado(a) temporário(a) ou celetista, mesmo trabalhando num
   ente que tem RPPS instituído, continua sendo segurado(a) do RGPS — o RPPS só alcança quem está
   em cargo efetivo. Se o formulário já diz "contratado", o indicador PRPPS naquele vínculo é
   quase sempre inconsistência de fonte (RAIS/GFIP/eSocial classificou errado), não um sinal de
   CTC pendente — registre isso como achado sem precisar de mais pesquisa.
3. **Se o vínculo for (ou puder ser) efetivo, consulte primeiro o CADPREV** — Cadastro Nacional de
   Regimes Próprios de Previdência Social, mantido pela Previc/Ministério da Previdência
   (`https://cadprev.previdencia.gov.br`). É a fonte estruturada e oficial única sobre "esse ente
   tem RPPS instituído", muito mais confiável que busca livre na internet: traz a situação do
   RPPS, o CRP (Certificado de Regularidade Previdenciária) e a legislação que o ente enviou.
   Buscar direto lá, antes de qualquer outra pesquisa, é o que resolve a maioria dos casos numa
   única consulta.
4. **Só recorra à busca livre na internet quando o CADPREV não resolver** (ente não encontrado no
   cadastro, cadastro desatualizado, dúvida sobre a categoria abrangida) — aí sim, site oficial da
   prefeitura/instituto de previdência, portal de transparência, lei orgânica do município.
5. **Registre no diagnóstico o resultado encontrado** — o que a consulta localizou (ou não
   localizou), a fonte exata (CADPREV, com a data da consulta, ou o site alternativo), e se veio do
   CADPREV ou de busca livre (o CADPREV pesa mais na conclusão).
6. **Aponte a hipótese mais provável**, quando houver elementos suficientes para isso (ex.: "não
   foi localizado RPPS instituído no CADPREV; a hipótese mais provável é classificação incorreta da
   fonte RAIS/GFIP/eSocial"). Isso é determinante para orientar corretamente o segurado: só quem
   tem tempo em RPPS instituído e regularmente vinculado pode (e deve) buscar a CTC daquele regime;
   quem trabalhou num município sem RPPS (ou fora do cargo efetivo que o RPPS abrange) já está
   correto no INSS, e o indicador PRPPS pode ser uma inconsistência a corrigir, não um sinal de
   que falta uma CTC.
7. **Deixe expressamente indicada a necessidade de confirmação/validação** antes da conclusão
   definitiva e antes do requerimento previdenciário — junto ao cliente e, quando necessário,
   diretamente com o Município/ente público.

**A pesquisa preliminar nunca deve ser tratada como confirmação definitiva.** O diagnóstico pode
e deve apresentar o resultado da pesquisa e indicar o cenário mais provável, mas a existência ou
inexistência de RPPS **permanece pendente de validação** enquanto não houver confirmação direta
com o ente público ou o cliente — mesmo quando a pesquisa não for conclusiva, registre isso como
ponto a confirmar em vez de presumir uma resposta. Trate o tempo correspondente como **em risco**
(passo 2) até essa validação, independentemente de qual cenário pareça mais provável.

### 4. Identificar indicadores e pendências

Para cada indicador presente no CNIS, use `references/indicadores-cnis.md` como primeira
referência. Se o indicador não estiver lá, **busque-o no Anexo V oficial do INSS antes de
descrevê-lo** (a URL está no topo daquele arquivo) — nunca descreva um indicador de memória sem
checar a fonte, e nunca invente significado, documento ou providência para um indicador que
você não conseguiu confirmar. Para cada indicador relevante, registre: código e nome, número(s)
de vínculo (Seq.) e/ou competência(s) onde aparece, significado, se há impacto no reconhecimento
de direitos (segundo a fonte oficial — isso também determina se ele entra no tempo em risco, ver
passo 2), documentos tipicamente necessários, providência recomendada, e impacto estimado no
tempo de contribuição.

Quando a informação disponível não for suficiente para uma conclusão segura, registre
expressamente que é necessária análise documental complementar — não force uma conclusão.
(A lista de documentos necessários por pendência é para uso interno/da reunião — não entra no
PDF entregue ao cliente; ver restrição na seção "Saídas → A. Relatório em PDF".)

### 5. Diagnosticar necessidade de acerto de CNIS e de planejamento previdenciário

Siga a lógica do funil comercial do escritório: praticamente todo CNIS com pendências reais
justifica recomendar o **Acerto de CNIS**, e a ausência de um cálculo de regra/RMI já justifica
recomendar o **Planejamento Previdenciário** — mas a recomendação deve decorrer dos achados
reais do CNIS analisado, não ser copiada de um template genérico. Aponte os prejuízos concretos
de não regularizar (redução do tempo, atraso na concessão, indeferimento, regra menos
vantajosa, RMI menor) **ligados aos achados específicos daquele CNIS**, não a uma lista
genérica de riscos abstratos.

**Regra fundamental: Diagnóstico não é Planejamento.** O Diagnóstico Previdenciário é gratuito e
tem finalidade de identificação de problemas, riscos, pendências e oportunidades de atuação
jurídica — ele não entrega gratuitamente o que pertence ao Planejamento Previdenciário Estratégico
(produto pago, mais aprofundado). Isso vale tanto para o relatório em PDF quanto para a
apresentação e o roteiro (seção "Saídas"):

**O diagnóstico PODE:**
- apontar erros, pendências, indicadores e riscos;
- explicar as consequências desses problemas;
- apresentar uma **estimativa geral e aproximada** da situação previdenciária quando tecnicamente
  possível a partir dos elementos do CNIS (ex.: tempo total estimado, se esse tempo já se aproxima
  do patamar de alguma regra, se a cliente parece estar próxima ou não de reunir os requisitos —
  sempre em linguagem de indício/estimativa, nunca de conclusão fechada; ver também o passo 7,
  que é o mecanismo interno que decide quando e como essa estimativa aparece na apresentação);
- demonstrar que determinado período ou vínculo precisa ser analisado, comprovado ou regularizado;
- indicar quais providências jurídicas são recomendadas.

**O diagnóstico NÃO PODE:**
- entregar cálculo previdenciário completo;
- definir com precisão a melhor regra de aposentadoria (a "regra vencedora");
- apresentar gratuitamente todas as simulações possíveis;
- definir estratégia contributiva completa;
- entregar projeção detalhada de RMI;
- substituir o Planejamento Previdenciário Estratégico.

Em outras palavras: **não conclua neste diagnóstico se a cliente já pode se aposentar nem qual
regra é a mais vantajosa** — uma estimativa aproximada de proximidade é permitida (e, no perfil
certo, recomendada como gancho comercial — ver passo 7 e "Saídas → B"), mas a conclusão fechada
sobre direito adquirido, regra aplicável, data exata ou RMI é sempre objeto do Planejamento
Previdenciário Estratégico, um produto à parte, mais aprofundado. Quando alguma resposta depender
de análise aprofundada, cálculos, simulações ou comparação entre regras, deixe isso expressamente
reservado ao Planejamento Previdenciário — tanto no relatório quanto na fala da reunião.

### 6. Classificar a situação e concluir

Classifique objetivamente (ex.: "CNIS com pendências relevantes", "CNIS que exige
regularização imediata" — ver `references/indicadores-cnis.md` para os níveis de risco).
Resuma: tempo total estimado, tempo regular, tempo em risco (com a fórmula **tempo total =
tempo aparentemente regular + tempo em risco**, sem dupla contagem), principais pendências
(sempre com o número do vínculo/Seq. correspondente), prejuízos possíveis, serviços
recomendados, próximos passos.

### 7. Triagem previdenciária básica e interna (uso exclusivo da equipe)

Depois de concluído o passo 6, faça **sempre**, para todo CNIS, uma triagem previdenciária básica
e interna — **exclusivamente para orientar a construção da apresentação e a oferta comercial**
(passo "Saídas", seções B e C). Essa triagem:

- **não é um Planejamento Previdenciário completo** e não define com precisão a regra mais
  vantajosa, a data exata da aposentadoria ou a RMI — isso continua sendo objeto exclusivo do
  Planejamento Previdenciário Estratégico (produto pago, mais aprofundado);
- **não entra no relatório em PDF entregue ao cliente** (mantém a regra do passo 5 e das "Regras
  de segurança": este diagnóstico não conclui se a cliente já pode se aposentar nem qual regra é
  mais vantajosa) — o resultado desta triagem só influencia a apresentação em slides e o roteiro
  da reunião, nunca o documento técnico entregue;
- **não é detalhada ao cliente** em nenhum momento — nem na reunião nem no material entregue. O
  máximo que chega ao cliente é a informação comercial cautelosa descrita mais abaixo (seção
  "Saídas → B"), nunca os critérios ou o raciocínio da triagem em si.

**O que verificar** (com base apenas no que já foi apurado nos passos 1-6 e nos dados cadastrais
do passo 1 — data de nascimento e, se houver, sexo):

1. **Tempo de contribuição já próximo ou acima de ~25 anos** — use o tempo total estimado (passo
   2) como referência aproximada. Não é necessário decidir se esse tempo já basta para uma regra
   específica; o gatilho é só a proximidade/superação desse patamar.
2. **Idade compatível com alguma regra de transição ou regra permanente.** Trate isso de forma
   aproximada, sem calcular a regra vencedora: considere as faixas etárias mínimas das regras
   pós-EC 103/2019 (regra por pontos, pedágio de 50%, pedágio de 100%, idade mínima progressiva,
   regra permanente por idade) e, **por este ser um cliente tipicamente vinculado ao magistério**,
   considere também os parâmetros normalmente mais baixos das regras específicas de professor(a)
   (tempo e idade mínima reduzidos em relação à regra geral, tanto nas regras de transição quanto
   na regra permanente do professor) sempre que houver indicação, no CNIS ou no que a cliente já
   informou, de que a atividade é efetivamente de magistério.
3. **Indícios de que os requisitos de algum benefício já foram preenchidos**, mesmo que
   parcialmente contraditórios ou pendentes de confirmação documental (ex.: tempo total já bate
   com o mínimo de alguma regra e a idade também bate, ainda que a pendência de algum vínculo
   torne isso incerto — nesse caso, registre como indício, não como certeza).
4. **Perspectiva de atingir os requisitos nos próximos ~2 anos**, projetando de forma simples a
   partir do ritmo atual (ex.: faltam poucos meses/anos de tempo de contribuição e a idade também
   se aproxima do mínimo da regra dentro dessa janela).

**Não é necessário, nesta etapa:** apurar com precisão qual regra é a mais vantajosa, calcular a
RMI, ou fixar uma data exata de aposentadoria. A única finalidade é identificar internamente se
este é um caso de **aposentadoria já alcançada ou iminente** (dentro de uma janela de referência
de até aproximadamente 2 anos).

**Resultado da triagem:** registre internamente (não no PDF do cliente) um sinalizador simples —
por exemplo, "Triagem interna: indícios de aposentadoria já alcançada/iminente (≤ ~2 anos) — SIM"
ou "— NÃO" — acompanhado de uma frase curta com a razão (ex.: "tempo total estimado ~26 anos,
idade 54, regra de pontos pode estar próxima; pendências no CNIS ainda exigem confirmação"). Esse
sinalizador é o que decide, na seção "Saídas": (a) se a apresentação inclui o aviso comercial de proximidade da aposentadoria e o **Pacote 4** (acompanhamento completo), ou (b) se a apresentação segue
sem esse pacote, oferecendo só os serviços compatíveis com os problemas identificados no
diagnóstico. Trate sempre como **indício**, nunca como conclusão — mesmo quando o sinalizador for
"SIM", a apresentação deve deixar claro que a confirmação depende de análise previdenciária
completa (ver "Saídas → B").

## Força do diagnóstico: nem alarmista, nem suave demais

O diagnóstico deve deixar claro que existe uma parcela relevante do tempo da cliente em risco de
não ser reconhecida pelo INSS caso as pendências não sejam previamente regularizadas — sem
suavizar excessivamente a linguagem. Prefira expressões como "tempo em risco", "risco de
desconsideração pelo INSS", "pode comprometer o reconhecimento do tempo de contribuição", "pode
atrasar ou impedir a concessão do benefício", "exige regularização antes do requerimento".

Cuide da proporção entre os números apresentados. Se o achado mais grave do CNIS ficar fora do
bucket "tempo em risco" por uma tecnicalidade de metodologia, o diagnóstico transmite ao cliente
uma sensação de segurança que os fatos não sustentam. Sempre que houver algo fora do tempo total —
lacuna sem vínculo declarado, ou vínculo em risco de extensão a apurar — apresente cada item com
destaque visual próprio, ao lado dos três números principais, e diga com todas as letras que **o
tempo total estimado é um piso e não um teto**. O que não pode acontecer é o cliente sair da
reunião achando que o problema dele cabe no número pequeno.

Ao mesmo tempo, **nunca afirme que um período está definitivamente perdido** quando ainda existe
possibilidade de comprovação ou regularização, nem que um período está definitivamente
garantido havendo pendência não tratada. O tempo em risco é tempo que **integra o total
estimado** mas cujo reconhecimento depende de ação — não é tempo descartado.

## Saídas

Gere sempre os cinco elementos (PDF, slides, roteiro nas notas do apresentador, lista de
documentos e os requerimentos por órgão) a partir da mesma análise estruturada (passos 1-6) —
nunca escreva o PDF, os slides, o roteiro, a lista e os requerimentos como exercícios de redação
separados, ou eles vão divergir nos números e nas pendências listadas. O resultado da triagem
interna do passo 7 **não afeta o PDF** (seção A, abaixo, permanece igual em todos os casos) — ele
afeta apenas a apresentação em slides e o roteiro (seções B e C), conforme detalhado em cada uma.
A lista de documentos (seção D) e os requerimentos (seção E) não dependem do resultado da
triagem — são gerados sempre, a partir do quadro de pendências, mas só ENVIADOS ao cliente depois
do contrato assinado (ver regra de envio em cada seção).
**Antes de entregar, confira cruzado:** todo número que aparece em mais de um lugar (tempo
total, tempo regular, tempo em risco, datas de um mesmo achado) deve ser idêntico no PDF e nos
slides — se um mudar numa correção, mude nos dois; toda pendência do quadro precisa ter o bloco
correspondente na lista de documentos (seção D), nem a mais nem a menos; e cada documento pedido
na lista precisa aparecer no requerimento do órgão certo (seção E) — nenhum documento "órfão" sem
requerimento que o peça formalmente. Depois de qualquer alteração na apuração do tempo ou no
quadro de pendências, **releia o documento inteiro** (resumo executivo,
seção de tempo, quadro, necessidade de acerto/planejamento, prejuízos, conclusão, recomendações)
para garantir que nenhuma seção ficou com números ou linguagem da versão anterior.

### A. Relatório em PDF (para o cliente)

Consulte o skill `pdf` (e, se preferir montar o layout em HTML antes de converter, o skill
`docx`/`pptx` como referência de padrões de design) antes de gerar o arquivo. Estrutura:

capa → identificação do segurado → resumo executivo → estimativa do tempo total, do tempo
aparentemente regular e do tempo em risco (com o quadro comparativo regular vs. risco e a
composição do tempo em risco por causa — lacunas, PEXT/PRPPS, EC103 etc.) → **quadro geral das
pendências identificadas no CNIS** → necessidade de acerto de CNIS → necessidade de planejamento
previdenciário → prejuízos da não regularização → conclusão → recomendações e próximos passos →
ressalvas técnicas (ver seção "Regras de segurança" abaixo — inclua-as sempre, de forma
resumida, no rodapé ou na última página).

**Não repita, em texto corrido depois do quadro, uma explicação longa indicador por indicador.**
O quadro de pendências é a única apresentação dos indicadores no PDF — não há uma seção
narrativa adicional reexplicando cada um; isso deixaria o documento repetitivo. O texto corrido
do relatório (resumo executivo, necessidade de acerto/planejamento, conclusão) deve remeter aos
achados do quadro em prosa, sem duplicar indicador por indicador.

**O quadro geral de pendências substitui um quadro de vínculos genérico** — a cliente não quer
uma lista de vínculos, quer uma lista das pendências em si, organizada para ela conseguir achar
cada uma rapidamente no próprio extrato do CNIS. Use exatamente estas quatro colunas:

1. **Indicador** — o código tal como aparece no CNIS (ex.: PEXT, PRPPS, PREM-BLOQ-EC103). Se o
   achado não tiver um código de indicador (ex.: vínculos duplicados/concomitantes, um vínculo
   sem data de encerramento), deixe explícito que é um achado estrutural, não um indicador do
   CNIS. Para um vínculo registrado sem nenhuma contribuição, a coluna de impacto deve dizer
   expressamente que se trata de **tempo em risco** e, quando a extensão não for delimitável,
   que o período **não pôde ser medido e não foi presumido** — nunca escreva que ele "não conta"
   nem atribua a ele um número estimado. **Não deixe de fora os achados estruturais** — em
   especial vínculo(s) sem data de
   encerramento (exceto o vínculo ativo atual, que normalmente é aberto mesmo) e vínculos
   duplicados/concomitantes: os dois costumam travar o processamento do requerimento tanto
   quanto um indicador de pendência propriamente dito, e por não terem código são fáceis de
   esquecer no quadro.
2. **Onde** — **identifique sempre, de forma expressa, o número do vínculo (Seq.) correspondente
   no CNIS** — não basta informar apenas o nome do empregador ou o período. Use o padrão "Vínculo
   nº X — [Empregador] — [período]"; quando o mesmo indicador atingir mais de um vínculo,
   informe todos ("Vínculos nº 2, nº 4 e nº 5 — [Empregadores]"). Aplique esse padrão a **todas**
   as linhas da tabela, inclusive aos achados estruturais, sempre que for possível vinculá-los a
   uma sequência específica do CNIS — é o que permite à cliente e ao(à) advogado(a) localizar
   imediatamente no CNIS qual vínculo está sendo analisado.
3. **O que significa / origem** — o significado do indicador e por que ele apareceu ali,
   segundo `references/indicadores-cnis.md` (ou o Anexo V oficial, se não estiver na
   referência).
4. **Impacto na aposentadoria** — a consequência concreta para o tempo de contribuição, para o
   reconhecimento do período ou para o valor do benefício. Deixe claro que o período **integra o
   tempo total estimado**, mas está em risco e depende de comprovação/regularização — não escreva
   como se o período estivesse simplesmente fora da conta.

Uma pendência recorrente em várias competências do mesmo vínculo (ex.: PREM-BLOQ-EC103 repetido
mês a mês por anos) deve virar **uma linha só**, cobrindo o intervalo de competências, não uma
linha por mês.

**Ordene as linhas por gravidade** (maior impacto no tempo de contribuição/no requerimento
primeiro), não pela ordem em que a pendência foi encontrada na leitura do CNIS — é assim que a
cliente vai processar a tabela visualmente. Marque a gravidade com uma **faixa de cor na lateral
esquerda de cada linha** (vermelho = risco relevante, âmbar = risco moderado/a confirmar, verde
= informativo/baixo impacto — mesma paleta do resto do relatório), em vez de criar uma quinta
coluna para isso.

**Não liste, no PDF, quais documentos são necessários para resolver cada pendência.** Descreva
o achado, o indicador, o impacto e a recomendação (ex.: "acerto de CNIS necessário"), mas
**omita a lista de documentos a apresentar** — isso só é informado ao cliente em caso de
contratação. Essa restrição vale só para o PDF entregue ao cliente; a análise interna de quais
documentos seriam necessários pode continuar orientando a recomendação de acerto/planejamento,
só não deve aparecer escrita no relatório.

Linguagem: compreensível para o cliente leigo, sem perder precisão técnica — é um documento que
o professor vai ler sozinho em casa, não só na reunião. Identidade visual: use a identidade visual do escritório (cores, tipografia, logotipo) para títulos e callouts, e a codificação de risco verde/âmbar/vermelho conforme `references/indicadores-cnis.md`.

### B. Apresentação em slides (para a reunião)

**Monte a apresentação com o skill `pptx`**, na identidade visual do próprio escritório — ou parta do modelo de apresentação que o escritório já usa, mapeando cada bloco abaixo para o slide equivalente. Esta skill **não traz um `.pptx` pronto**: visual, fotos, depoimentos e valores pertencem ao escritório que a utiliza.

**Modelo-base de estrutura e profundidade do roteiro: `references/roteiro-modelo.md`.** Toda apresentação e todo roteiro gerados por esta skill devem ter a mesma estrutura, profundidade e qualidade de condução desse roteiro-modelo (escrito com campos entre colchetes). **Nunca copie o texto literalmente para outro cliente** — os achados, números, indicadores, objeções antecipadas e a modalidade recomendada são específicos de cada caso e precisam ser reconstruídos a partir do CNIS e do diagnóstico de cada cliente (ver "ADAPTAÇÃO OBRIGATÓRIA" na seção C, abaixo). Use esse arquivo como referência de: quanto detalhe cada fala deve ter, onde entram as pausas e as perguntas de envolvimento, como a recomendação profissional e o isolamento de objeção são conduzidos **antes** de o preço aparecer na tela, e como é o roteiro de fechamento, pagamento e formalização. Releia esse arquivo sempre que for montar o roteiro de um novo cliente — não confie na memória do padrão.

A reunião conduzida a partir desta apresentação deve levar a cliente a compreender, nesta ordem: (1) qual é a situação previdenciária dela hoje; (2) quais erros, pendências, inconsistências, indicadores ou riscos foram encontrados; (3) quais consequências esses problemas podem gerar; (4) o que precisa ser feito para corrigir ou prevenir esses problemas; (5) por que não é recomendável simplesmente aguardar a aposentadoria ou protocolar um requerimento sem preparação; (6) quais serviços jurídicos são adequados para o caso; (7) qual solução o(a) advogado(a) recomenda; e (8) qual é o próximo passo para contratação. Essa sequência corresponde, na apresentação concreta, a: abertura → fotografia previdenciária (raio-x + linha do tempo) → achados do diagnóstico → problemas prioritários e consequências → transição para a solução → o que precisa ser feito (método) → limite do diagnóstico e solução jurídica (modalidades) → recomendação → isolamento de objeções → investimento → fechamento → pagamento → formalização → próximos passos — ver o mapa de slides e o roteiro detalhados abaixo. Ao final da reunião, a cliente deve chegar à conclusão, por conta própria, de que precisa de atuação profissional para resolver o que foi identificado — a venda decorre do diagnóstico, não de pressão comercial avulsa.

**Pacotes de referência e oferta condicional.** A estrutura comercial de referência tem 4 pacotes — ajuste nomes, escopo e valores aos do escritório (o usuário informa; nada disso vem preenchido aqui e nunca se inventa valor):

- **Pacote 1 — Acerto de CNIS:** tratamento das pendências identificadas.
- **Pacote 2 — Planejamento Previdenciário:** cálculos, análise das regras, melhor momento e estratégia.
- **Pacote 3 — Combo:** Pacote 1 + Pacote 2.
- **Pacote 4 — Acompanhamento completo:** o Combo mais a condução posterior da aposentadoria, dentro do escopo contratado (parte fixa e, se o escritório assim definir, honorários de êxito).

**O Pacote 4 não é oferta padrão de todos os diagnósticos** — só aparece quando a triagem interna do passo 7 sinalizar aposentadoria já alcançada ou iminente (≤ ~2 anos). Decida isso logo no início da montagem dos slides de pacotes:

- **Sinalizador = SIM:** mostre os 4 pacotes; o Pacote 4 é a recomendação central para este cliente.
- **Sinalizador = NÃO:** mostre só os 3 primeiros; não apresente nem recomende o Pacote 4, e o roteiro não pode mencioná-lo.

**Sequência de slides** (mantenha esta ordem; adapte o visual ao escritório):

1. **Capa.**
2. **Quem sou eu** — autoridade rápida, **só com dados reais** do(a) advogado(a): anos de atuação, especialização, quantidade aproximada de professores atendidos, e um link de perfil público de atuação, se houver. Nunca invente número de clientes nem credencial.
3. **Prova social** — depoimentos **reais e autorizados** pelos clientes, identificando cada pessoa apenas por **primeiro nome + sigla do estado (UF)**, nunca nome completo nem cidade. Se o estado de algum depoimento não estiver registrado, **pergunte ao usuário** em vez de presumir. Se não houver depoimentos autorizados, omita o slide.
4. **"O que está errado"** — tabela "O quê / Onde / Quanto vale" com as pendências reais deste CNIS, priorizando as 4-5 mais relevantes/graves (não todas as possíveis) — é o slide que mais pesa na conversão comercial, tem que ser específico do cliente, nunca genérico. Na coluna "Onde", identifique sempre o número do vínculo (ex.: "Vínc. nº 5, 11/2019–05/2026"), no mesmo padrão do quadro do PDF, adaptado ao espaço da célula. **Use a mesma ordenação por gravidade do quadro do PDF** (não a ordem de descoberta) — como só cabem poucas linhas, achados estruturais graves sem código de indicador (vínculo sem data de encerramento, vínculos duplicados) competem por espaço com os indicadores e frequentemente devem entrar no lugar de um achado de baixa gravidade. A cor de cada linha deve refletir a gravidade real do achado. Se o CNIS tiver mais achados do que cabem, adicione slide(s) extra logo depois, no mesmo estilo (verde/âmbar/vermelho, número do vínculo sempre presente).
5. **Como funciona o método** — as etapas do fluxo do escritório: diagnóstico → coleta e análise documental → elaboração da estratégia → cálculos e projeções → execução e acompanhamento, conforme o pacote.
6. **Como podemos te ajudar (comparativo de pacotes, SEM preço)** — este é o slide "sem preço": é nas Notas do Apresentador dele (não do slide 7) que entram a recomendação profissional, a primeira validação e a pergunta de isolamento de objeção (ver seção C, item 9). O preço não pode estar visível na tela enquanto essa conversa acontece.
7. **Escolha a solução ideal / Investimento** — já mostra o investimento; só avance para ele depois que as objeções não financeiras já tiverem sido isoladas na conversa do slide 6; nunca antes.
8. **Fechando hoje** — só se o escritório tiver uma condição especial realmente definida; não invente condição.
9. **Por que agir agora.**

Além disso, insira **entre o slide 3 (prova social) e o slide 4** um pequeno bloco de slides com o resumo quantitativo do diagnóstico — o que dá à reunião a sensação de "auditoria feita na sua frente" antes de entrar no "o que está errado":
- um slide com o tempo total estimado x tempo aparentemente regular x tempo em risco (visual comparativo — barra, anel ou blocos, com as cores verde/âmbar/vermelho, e um resumo do que compõe o tempo em risco por causa — lacunas, PEXT/PRPPS, EC103 etc. — para bater com o callout equivalente do PDF);
- um slide (se fizer sentido pelo volume de vínculos) com a linha do tempo dos vínculos, destacando visualmente onde estão as lacunas/pendências — inclua no vermelho tanto as lacunas de remuneração quanto os trechos "regulares em remuneração" mas atingidos por PEXT/PRPPS/EC103, para refletir a mesma metodologia do quadro de tempo;
- **se o sinalizador do passo 7 for SIM**, inclua também, neste mesmo bloco, um callout curto em **linguagem comercial e cautelosa** avisando que há fortes indícios de que a cliente já esteja próxima da aposentadoria — algo como "Pelos números levantados, você pode já estar próxima (ou já ter direito) de se aposentar" — **seguido sempre**, no mesmo callout ou no slide, de uma ressalva clara de que a confirmação da data, da regra aplicável e da estratégia mais vantajosa depende de uma análise previdenciária completa (o Planejamento Previdenciário Estratégico). Nunca afirme a data, a regra ou o valor do benefício aqui — o callout é um gancho comercial, não uma conclusão técnica. **Se o sinalizador for NÃO, não inclua esse callout.**

Mantenha o mesmo estilo visual em todos os slides, sem misturar paletas. Consulte a seção "Design Ideas" e a checklist de QA do skill `pptx` antes de considerar os slides prontos; rode a conversão para imagem e inspecione visualmente cada slide novo/alterado.

**Regras de recomendação por perfil (slides 6, 7 e roteiro):**

- **Sinalizador do passo 7 = SIM (aposentável ou a ≤ ~2 anos):** a recomendação profissional (nas notas do slide "Como podemos te ajudar" — não no slide de Investimento, que só é revelado depois de isoladas as objeções; ver roteiro, seção C) deve ter o **Pacote 4** como opção central, adaptando a argumentação para mostrar que, por estar muito próxima da aposentadoria, é especialmente importante organizar as pendências, fazer o planejamento adequado e preparar o futuro requerimento — não ofereça o Pacote 4 como mais uma opção genérica entre quatro, ofereça-o como a solução que faz sentido *por causa* da proximidade identificada.
- **Sinalizador = NÃO:** não apresente nem recomende o Pacote 4 (ele não aparece nos slides de pacotes). Recomende apenas entre os serviços efetivamente compatíveis com os problemas e necessidades identificados no diagnóstico daquele CNIS (tipicamente Acerto de CNIS quando há pendências reais, e/ou Planejamento Previdenciário quando ainda falta tempo relevante até a aposentadoria) — nunca copie a recomendação de um cliente anterior sem checar se ela reflete os achados deste CNIS.

**Cuidado ao gerar imagens de conferência (QA) do PPTX.** Ao converter o `.pptx` para PDF só para inspecionar visualmente os slides (`soffice --convert-to pdf`), **nunca use o mesmo nome de arquivo do relatório em PDF entregue ao cliente** — o comando sobrescreve qualquer arquivo existente com esse nome. Gere o PDF de conferência em um diretório separado (ex.: `pptxqa/nome.pdf`) ou com um nome claramente distinto (ex.: `nome_slides_preview.pdf`).

### C. Roteiro de condução da reunião (Anotações do Apresentador)

**Todo `.pptx` entregue para a reunião de diagnóstico deve sair com o roteiro completo de
condução da reunião nas Anotações do Apresentador (Presenter Notes) de cada slide — nunca no
conteúdo visual.** Isso é padrão obrigatório a partir de agora para todo cliente, não um extra
opcional. O objetivo é o(a) advogado(a) conseguir conduzir a reunião inteira em Modo de Apresentador,
sem precisar de nenhum outro documento aberto.

**Modelo-base: `references/roteiro-modelo.md`.** Antes de escrever o roteiro de um
novo cliente, releia esse arquivo — é o padrão obrigatório de estrutura e de profundidade (ver
também a seção B, "Modelo-base obrigatório de estrutura e profundidade"). O roteiro que você
produzir deve ter falas tão completas, perguntas tão bem construídas, transições tão cuidadas e
tratamento de objeção tão detalhado quanto aquele modelo — nunca mais raso.

**ADAPTAÇÃO OBRIGATÓRIA — o roteiro NUNCA é copiado mecanicamente de um cliente para o outro.** A
sequência de condução comercial abaixo (o "Mapa de correspondência roteiro → slide") é o **padrão
fixo**, na mesma lógica do roteiro-modelo. O que muda, cliente a cliente, é **todo o
conteúdo** dentro dessa sequência: achados, perguntas, exemplos, riscos, documentos, serviços,
solução recomendada, objeções prováveis, argumentos e fechamento — nome do cliente, tempo
total/regular/em risco daquele CNIS, vínculos e competências problemáticas específicas, os
indicadores realmente encontrados (não uma lista genérica), lacunas de remuneração daquele caso,
inconsistências cadastrais daquele CNIS, a modalidade mais coerente para aquele perfil (ver
"Regras de recomendação por perfil", seção B), e as objeções previsíveis para aquele caso. Se um
achado existir num cliente mas não no próximo, omita-o; se uma etapa técnica do modelo não se
aplicar ao cliente (ex.: não há RPPS, não há atividade rural), **não invente o achado equivalente
só para preencher o padrão** — adapte a fala ou suprima a etapa, mantendo a estrutura geral. Se um
cliente futuro tiver uma particularidade que não apareceu em nenhum caso anterior, redija a fala
correspondente no mesmo tom e posicione-a no slide certo — nunca deixe o roteiro "genérico" por
falta de um caso de referência exato.

**Objetivo comercial da reunião:** ao final, a cliente deve chegar sozinha à conclusão de "agora
eu sei onde estão os problemas, quais riscos eles representam e por que preciso agir — para
resolver isso corretamente e definir minha estratégia previdenciária, preciso de uma atuação
profissional." A venda decorre do diagnóstico bem conduzido, não de pressão comercial avulsa — o
roteiro constrói essa percepção passo a passo, nunca por atalho.

**Mapa de correspondência roteiro → slide** (a ordem de exibição do `.pptx`, não necessariamente
a ordem física dos arquivos `slideN.xml` — confira sempre `ppt/presentation.xml` →
`p:sldIdLst`/`presentation.xml.rels` para saber qual arquivo cai em qual posição visível, porque
slides extras inseridos com `add_slide.py` recebem números de arquivo altos mas podem ocupar
posições no meio da sequência):

1. **Capa** — abertura da reunião (antes de compartilhar a tela). Siga o padrão do modelo: uma
   fala curta de **preview da agenda** (o que a cliente vai ver primeiro, o que vem depois, e que
   "se fizer sentido, já dá pra deixar encaminhado hoje"), fechada com uma pergunta de
   confirmação simples ("Tudo bem?") e a instrução de aguardar a resposta antes de prosseguir; só
   depois, a introdução do que é o Diagnóstico Previdenciário Estratégico e do método do escritório (a ideia de que a análise vai além da simulação do Meu INSS).
2. **Quem sou eu** — autoridade rápida: anos de atuação, atuação previdenciária direcionada ao magistério, quantidade aproximada de professores atendidos (só números reais), a relação pessoal com o magistério (quando aplicável) e, se houver, a menção a um perfil público de atuação verificável (ver seção B, item 2).
3. **Prova social / depoimentos** — dois ou três depoimentos mais fortes, sem ler tudo, com uma
   frase de conexão (ex.: "muitos chegaram até nós com dúvidas semelhantes").
4. **Raio-x da contribuição** (bloco de resumo quantitativo) — siga o padrão de revelação em
   camadas do modelo: primeiro o tempo total estimado, com pausa; depois a frase de transição
   sinalizando que **o número que mais chama atenção não é esse**; só então o tempo em risco,
   com pausa para a cliente observar o slide, seguido de uma frase de dimensionamento do impacto
   (ex.: proporção do tempo em risco sobre o total) e da reafirmação de que tempo em risco **não é
   tempo perdido**, é tempo que depende de validação/comprovação/regularização. Feche com a
   pergunta de envolvimento ("Você imaginava que tinha tanta coisa assim pendente no seu CNIS?")
   e prepare as duas ramificações de resposta (cliente não imaginava / cliente já desconfiava,
   mas não da extensão) — adapte os números e o tom ao caso, nunca copie os números do modelo.
5. **Linha do tempo dos vínculos** (mesmo bloco) — leitura guiada da linha do tempo, sinalizando
   que os problemas vêm de períodos diferentes da carreira (início, vínculos intermediários) e
   dando destaque específico ao **trecho mais recente/mais grave** daquele CNIS, com o tamanho
   exato desse trecho (ex.: "X anos e Y meses do seu vínculo atual").
6. **"O que está errado" (achados principais)** — abra com a mesma lógica do modelo ("não vou
   transformar isso numa aula sobre siglas do INSS... o importante é você entender o impacto"),
   depois percorra os achados na mesma ordem de gravidade da tabela do PDF, traduzindo cada
   indicador para linguagem de impacto (não de código técnico) — ex.: para um bloqueio de
   remuneração recente, explicar que há remunerações informadas mas atingidas por bloqueio no
   sistema; para PRPPS, que é preciso confirmar o enquadramento junto ao regime; para PEXT, que é
   uma informação extemporânea que o próprio CNIS já sinaliza como pendente de comprovação; para
   lacunas de remuneração, deixar claro que o tempo não foi retirado da conta, mas também não pode
   ser tratado como seguro sem validação. Feche com a "frase-chave" do diagnóstico (ver "Força do
   diagnóstico" acima), seguida de pausa.
7. **"O que está errado" (continuação, se houver)** — os achados estruturais restantes (vínculos
   duplicados, sem data de encerramento, sem remuneração, concomitâncias, achados de baixo
   impacto); **quando o roteiro-base do cliente não tiver falas prontas para esses achados
   secundários** (caso comum — o roteiro de referência normalmente detalha só os achados
   principais do slide anterior), redija conectivos no mesmo tom cauteloso e não-definitivo do
   restante do documento, citando sempre o número do vínculo (Seq.). Feche este bloco com a
   **transição diagnóstico → solução**, no mesmo padrão do modelo: contraste explícito ("se eu
   tivesse encontrado uma vida contributiva completamente limpa, eu diria: ótimo, vamos só
   calcular a regra... mas não foi isso que encontramos") seguido da razão pela qual existe uma
   etapa de organização/proteção antes de qualquer requerimento.
8. **Método do escritório** — a lógica problema → solução, sem ensinar execução, fechada com a
   síntese de três partes do modelo: "primeiro identificamos o problema; depois organizamos e
   protegemos a vida contributiva; e então definimos quando, por qual regra e com qual estratégia
   a cliente deve se aposentar."
9. **Como podemos te ajudar (comparativo de pacotes, sem preço)** — **este slide concentra toda a
   negociação que precisa acontecer antes de o preço aparecer na tela** (ver "PONTO CRÍTICO PARA
   AS NOTAS DO POWERPOINT" no arquivo de referência — não existe um "slide-ponte" separado; tudo
   isso vai nas notas deste slide):
   - apresentação objetiva de cada modalidade disponível — os 4 pacotes (incluindo o Pacote 4)
     se o sinalizador do passo 7 for SIM; só os 3 primeiros se for NÃO (o roteiro não deve mencionar um 4º pacote que não está na tela);
   - a **recomendação profissional**, construída a partir dos achados reais do diagnóstico (nunca
     copiada de um cliente anterior), seguindo as "Regras de recomendação por perfil" (seção B):
     - **sinalizador SIM:** o Pacote 4 é a recomendação central, com a fala mostrando
       por que a proximidade da aposentadoria torna especialmente importante organizar as
       pendências, planejar corretamente e já preparar o futuro requerimento — nunca a apresente
       como "mais uma opção entre três ou quatro";
     - **sinalizador NÃO:** recomende normalmente 2 das 3 modalidades restantes (nunca deixar a
       cliente escolhendo sozinha entre elas), explicando por que as demais isoladamente não
       resolvem o caso (ex.: só Planejamento sem tratar as pendências, ou só Acerto sem depois
       saber a regra/momento) — no mesmo espírito do modelo, sem copiar a lógica literal se não
       fizer sentido para o caso;
   - a **primeira validação**: "Até aqui, essa solução faz sentido para você?" — aguardar resposta;
   - a **pergunta de isolamento de objeção**, sempre adaptada ao caso mas preservando o núcleo:
     "Antes de eu te mostrar o investimento, eu quero só entender uma coisa: existe algum motivo
     que te impediria de seguir comigo hoje, além da questão do valor?" — com a instrução expressa
     de não avançar o slide, aguardar a resposta e não preencher o silêncio;
   - os desdobramentos dessa pergunta (cliente diz que só depende do valor / diz que precisa
     conversar com alguém / diz que precisa pensar / diz que não sabe se precisa agora) — use os
     scripts do arquivo de referência como padrão de profundidade, adaptando à objeção real que
     fizer sentido para aquele caso; só depois de essas objeções estarem isoladas o roteiro deve
     instruir avançar para o próximo slide.
10. **Escolha a solução ideal para você / Investimento** — **só é avançado depois que as objeções
    não financeiras já foram isoladas no slide anterior.** Apresente os valores de todas as
    modalidades de forma objetiva, depois concentre a fala nas duas recomendadas (ou na única
    recomendada, no perfil SIM), explicando com clareza a composição do investimento (parte fixa e
    honorários de êxito, quando for o caso do Pacote 4). Sem pedir desculpas pelo
    preço, sem dizer "eu sei que é caro", sem oferecer desconto espontaneamente.
11. **Condição / formas de pagamento e fechamento** — formas de pagamento (à vista ou parcelado,
    sem juros até o limite praticado pelo escritório); desconto no Pix **somente se a cliente
    perguntar**, aplicando só a condição já definida pelo escritório (nunca inventada na hora). A
    pergunta de fechamento deve ser sempre uma escolha entre as opções recomendadas (ex.: "Entre
    [opção A] e [opção B], qual faz mais sentido para você?"), **nunca** substituída por "Você quer
    contratar?", "O que você achou?" ou "Quer pensar?". Inclua os scripts de objeção financeira
    ("está caro", "preciso pensar", "não tenho esse dinheiro agora") retomando sempre o que já foi
    validado antes do preço (ver arquivo de referência para o padrão de profundidade de cada
    objeção) — nunca ofereça desconto como primeira resposta a "está caro", trabalhe primeiro o
    parcelamento. Inclua também a condução do pagamento ao vivo (não encerrar a chamada, enviar o
    link no WhatsApp, aguardar confirmação) e do envio/assinatura do contrato ainda durante a
    reunião, seguida da fala de pós-contratação (início oficial do atendimento, canais de dúvida).
12. **Por que agir agora / encerramento** — o roteiro de não-fechamento, para quando a cliente não
    contrata na reunião: encerramento profissional, sem insistência, com o aviso de que o
    Diagnóstico Previdenciário será enviado por WhatsApp com o resumo da situação (tempo total,
    tempo em risco, principais pendências) — sem preço nem tratamento de objeções nesse envio (o
    PDF continua sendo só o documento técnico, ver seção A).

**Regras de formatação das Anotações do Apresentador:**
- **Escreva todas as falas na primeira pessoa do singular ("eu", "meu", "comigo"), nunca no
  plural ("nós", "nosso", "conosco", "a gente" no sentido de "nós").** Quem conduz a reunião e
  executa o trabalho é o(a) próprio(a) advogado(a), sozinha — não há equipe apresentando junto. Isso vale
  inclusive para frases fixas do roteiro-base, como a pergunta de isolamento de objeção ("existe
  algum motivo que te impediria de seguir **comigo** hoje...", nunca "conosco"). Ao adaptar o
  roteiro para um novo cliente, confira este ponto explicitamente antes de entregar — é um erro
  fácil de reintroduzir sem perceber, porque frases comerciais em português tendem a soar
  naturais no plural mesmo quando só uma pessoa está de fato falando.
- Preserve o roteiro **por extenso** — nunca resuma em bullets nem condense falas em uma frase
  genérica. o(a) advogado(a) precisa conseguir ler a fala literal durante a ligação.
- **Marque cada trecho das notas com uma etiqueta entre colchetes**, no início da linha, indicando
  o tipo de conteúdo — esse é o padrão obrigatório a partir de agora (substitui qualquer convenção
  anterior de prefixos como ⏸/▶):
  - `[FALA]` — o que o(a) advogado(a) deve dizer à cliente, texto corrido, por extenso.
  - `[PERGUNTA]` — pergunta que o(a) advogado(a) deve fazer à cliente.
  - `[PAUSA]` — momento para aguardar reação/resposta antes de continuar.
  - `[TRANSIÇÃO]` — conexão com o próximo assunto/slide.
  - `[ATENÇÃO]` — orientação de condução da reunião (ex.: não avançar o slide, não preencher o
    silêncio, não oferecer desconto espontaneamente).
  - `[OBJEÇÃO]` — resposta preparada para uma possível resistência da cliente, com a objeção
    identificada no início (ex.: `[OBJEÇÃO — "está caro"]`).
  - `[FECHAMENTO]` — pergunta ou comando de avanço para a próxima etapa da negociação.
  Isso permite ao(à) advogado(a), num relance durante a reunião em Modo de Apresentador, achar rápido se
  aquela linha é para falar, para perguntar, para aguardar, ou para executar.
- Nunca insira o roteiro no corpo visível do slide — só na área de notas (`ppt/notesSlides/`,
  vinculada ao slide correspondente via relacionamento `notesSlide` no `slideN.xml.rels`).
- Slides construídos do zero para este cliente (ex.: os slides extras do "raio-x"/linha do tempo
  criados com `add_slide.py`) **não herdam a relação de notas do slide de origem** —
  `add_slide.py` remove essa referência ao duplicar. É preciso criar manualmente a parte
  `notesSlideN.xml`, o seu `_rels`, o relacionamento em `slideN.xml.rels` e o registro em
  `[Content_Types].xml` para cada slide novo (use um `notesSlideN.xml` existente do próprio
  pacote como modelo de estrutura).

**REGRA FINAL — QA final obrigatório antes de entregar.** Antes de considerar qualquer nova
apresentação finalizada, faça uma conferência comparativa com o padrão de
`references/roteiro-modelo.md` e confirme, slide a slide:
- o roteiro está tão completo quanto o modelo (falas por extenso, não resumidas)?
- existem falas prontas para todos os momentos importantes, não só para os achados principais?
- há perguntas suficientes para envolver a cliente ao longo da reunião, não só no fechamento?
- os riscos foram **explicados** (impacto, consequência), e não apenas listados?
- existe uma transição clara entre o diagnóstico e a solução (o bloco de contraste "se estivesse
  tudo limpo... mas não foi isso que encontramos")?
- ficou clara, na fala, a diferença entre o diagnóstico gratuito e o Planejamento Previdenciário
  completo (ver "Regra fundamental: Diagnóstico não é Planejamento", passo 5)?
- a solução foi recomendada de forma individualizada, a partir dos achados deste CNIS — não
  copiada de um cliente anterior?
- as objeções não financeiras foram isoladas nas notas do slide "Como podemos te ajudar" (item 9
  deste mapa), **antes** de avançar para o slide de Investimento (item 10)?
- há roteiro completo para a apresentação do investimento?
- há tratamento das objeções financeiras pertinentes ao caso ("está caro", "preciso pensar", "não
  tenho esse dinheiro agora")?
- existe uma pergunta de fechamento clara, no formato de escolha entre as opções recomendadas?
- há orientação para o pagamento ao vivo e para a formalização do contrato durante a reunião, e
  também para o encerramento sem contratação (envio do PDF, sem preço nem objeções)?
- nenhum nome, número ou achado de um cliente anterior sobrou nas notas;
- os números citados nas notas (tempo total/regular/risco, vínculos, valores) batem com os do
  diagnóstico e do PDF entregues para este cliente;
- o roteiro completo está disponível em Modo de Apresentador e nada dele aparece no conteúdo
  visual do slide (renderize o `.pptx` para PDF/imagem e confirme visualmente que os slides não
  mudaram);
- rode a validação estrutural do pacote (`pptx/scripts/office/validate.py --original` contra a última versão sem notas) para confirmar que só as partes de notas
  mudaram.

Se alguma dessas etapas estiver superficial ou ausente, complete o roteiro antes de considerar a
apresentação finalizada — não entregue um roteiro "razoável"; o padrão de referência é o roteiro-modelo, não a média dos roteiros já feitos.

### D. Checklist de documentos pós-contrato (uso interno, só depois do "sim")

**Nova saída obrigatória, gerada sempre junto com as três anteriores, mas nunca entregue ao
cliente na reunião de diagnóstico.** É a lista de documentos necessários para resolver cada
pendência do quadro (seção A) — o mesmo conteúdo que a seção A proíbe explicitamente de aparecer
no PDF do cliente (ver "Não liste, no PDF, quais documentos são necessários...", acima) agora vira
um documento próprio, entregue ao cliente **só depois de fechado o contrato**, no formato "Lista de Documentos para Regularização do CNIS".

**Gere sempre, independentemente de o cliente fechar ou não.** Não é retrabalho: a análise de
"que documento resolve essa pendência" já foi feita para escrever a coluna "Impacto na
aposentadoria" do quadro — este documento só reorganiza o que já existe, por bloco, num formato
que o próprio cliente consegue seguir sozinho. Guardar pronto custa nada; ter que refazer na hora
do fechamento, sob pressa, custa erro.

**Diferente do quadro de pendências da seção A, este documento é dirigido ao cliente — mas só
depois que ele contratou.** Linguagem de "a senhora"/"o senhor", sem juridiquês, explicando o
"porquê" de cada bloco.

**Não há PDF-modelo anexado a esta skill.** Siga a estrutura abaixo, com o mesmo nível de detalhe por bloco e o mesmo tom; nunca reaproveite achados, vínculos ou números de outro cliente.

Estrutura (siga esta ordem; é a que já roda em produção):

1. **Capa** — "Lista de Documentos para Regularização do seu CNIS", nome do cliente, CPF, data de
   elaboração, referência ao Diagnóstico Previdenciário que originou a lista, identidade visual do escritório e rodapé institucional (nome do escritório, advogado(a), OAB).
2. **Como usar esta lista** — 3 orientações fixas: (a) não precisa reunir tudo de uma vez, comece
   pelos blocos de prioridade alta; (b) foto legível pelo celular ou PDF já serve, não precisa
   cópia autenticada; (c) se o órgão não localizar um documento, uma declaração escrita da
   ausência também tem valor. Nesta seção, defina a legenda de emissores usada em toda a lista:
   **CLIENTE** (já em posse do cliente, em casa) · **MUNICÍPIO/ENTE** (órgão público de origem do
   vínculo, nomeado especificamente — "Prefeitura de X", "Secretaria de Educação de Y") ·
   **EMPREGADOR** (quando privado) · **ESCRITÓRIO** (providência interna, cliente não precisa
   fazer nada).
3. **Bloco 0 — documentos de abertura** — RG/CNH, CPF, comprovante de residência, certidão de
   casamento, CTPS completa, PIS/PASEP, senha do Meu INSS: os documentos pessoais que abrem
   qualquer pedido, independente da pendência específica. Marque o extrato CNIS já usado no
   diagnóstico como "já em nosso poder".
4. **Um bloco por achado do quadro de pendências (seção A)** — não por indicador isolado: agrupe
   pendências do mesmo vínculo/período no mesmo bloco quando fizer sentido para o cliente separar
   por órgão a que vai pedir, não pelo código técnico. Cada bloco traz:
   - **Rótulo do bloco em linguagem de impacto**, não o código do indicador (ex.: "Seu tempo atual
     com a Prefeitura precisa ser comprovado", não "PEXT").
   - **Onde** — vínculo (Seq.) e período, no mesmo padrão da seção A.
   - **Selo de prioridade** — ALTA (maior tempo de trabalho envolvido) · MÉDIA · MENOR — mesma
     lógica de gravidade da seção A, adaptada para "quanto esforço isso exige do cliente agora".
   - **Lista de documentos**, cada um com o emissor entre colchetes/etiqueta.
   - **Procedimento** — uma frase curta dizendo o que o escritório faz assim que os documentos
     chegarem (ex.: "protocolamos o pedido de acerto no Meu INSS"), para o cliente entender que
     entregar documento não é o fim, é o meio.
5. **Checklist consolidado, por quem emite** — a mesma lista inteira, reagrupada por origem
   (uma seção por Município/Secretaria/Empregador citado nos blocos, mais uma seção "Separar em
   casa" para os itens CLIENTE e uma "Por conta do escritório" para os ESCRITÓRIO), sem
   duplicidade dentro de cada grupo — é o que permite ao cliente ir a um único órgão e pedir tudo
   de uma vez, em vez de voltar bloco por bloco.
6. **Sequência recomendada** — tabela ETAPA / O QUE FAZER / QUEM FAZ / DEPENDE DE, ordenando as
   providências por dependência real (ex.: protocolar na Prefeitura antes de pedir unificação de
   cadastro, que por sua vez precede os pedidos de correção). Última etapa é sempre "conferir o
   extrato corrigido e avançar para o Planejamento Previdenciário" quando aplicável — é o gancho
   para a venda do próximo produto.
7. **Observações finais** — bloco fixo, sempre presente: nenhum documento da lista serve para
   provar que o cliente já pode se aposentar (reforça o limite do diagnóstico, seção "Regra
   fundamental"); declaração de órgão que não localizou documento tem valor; levar sempre 2 vias
   de requerimento e guardar a via protocolada; documentos podem ser enviados aos poucos; na
   dúvida, "é melhor sobrar do que faltar".
8. **Rodapé de encerramento** — nome do escritório, advogado(a) responsável, OAB, cidade e data.

### E. Requerimentos de documentos (um por órgão, para o cliente imprimir e protocolar)

**Nova saída obrigatória, junto com o checklist da seção D — mesma regra de envio (só depois do
contrato assinado).** O checklist diz *o quê* pedir; o requerimento é o documento formal que o
cliente efetivamente entrega no balcão do órgão para pedir. Sem ele, o cliente muitas vezes não
sabe como formalizar o pedido, e o escritório perde tempo tentando descobrir depois por que o
órgão "não recebeu nada". Padrão validado em produção.

**Gere um requerimento por órgão distinto** que aparece na seção D (um para cada Município,
Secretaria ou empregador citado) — nunca um requerimento genérico cobrindo todos os órgãos de
uma vez, porque cada um recebe só o que é da própria competência.

Estrutura de cada requerimento (redigido em primeira pessoa, na voz do cliente — é ele quem
assina e entrega, não o escritório):

1. **Título** — "REQUERIMENTO DE DOCUMENTOS".
2. **Destinatário** — nome completo e correto do órgão (ex.: "À Prefeitura Municipal de X /
   Secretaria Municipal de Educação"), cidade/estado.
3. **Qualificação do requerente** — "Eu, NOME EM MAIXÚSCULA, nacionalidade, estado civil,
   profissão (professor/professora), RG, CPF, endereço completo com CEP — venho requerer a
   expedição das seguintes cópias e declarações referentes ao(s) meu(s) vínculo(s) de trabalho
   com este órgão, necessárias à regularização do meu cadastro junto ao INSS:".
4. **Lista numerada dos documentos** — só os que aquele órgão específico emite (subconjunto do
   checklist consolidado, seção D, para aquele emissor), redigidos como pedido formal em vez de
   rótulo de checklist (ex.: não "Ficha financeira 2010-2026", mas "Ficha financeira completa,
   mês a mês, do período de maio de 2010 até a presente data"). Inclua sempre, quando o achado
   envolver dúvida sobre o regime, um item pedindo declaração expressa sobre RGPS × regime
   próprio, com cópia da lei que o instituiu, se existir; e quando houver indício de duplicidade
   de vínculo/matrícula, um item pedindo esclarecimento por escrito sobre se são vínculos
   distintos ou lançamento repetido.
5. **Cláusula de documento não localizado** — parágrafo fixo: solicitar que, se algum documento
   não for localizado, seja emitida declaração por escrito, assinada e carimbada, informando a
   impossibilidade e o motivo — essa declaração tem valor probatório equivalente para o
   diagnóstico/planejamento.
6. **Fecho** — "Nestes termos, peço deferimento.", local e data (com espaço em branco para
   preencher na hora da assinatura), nome completo e CPF do requerente, espaço para assinatura.
7. **Recibo de protocolo (via do requerente)** — bloco separado, na mesma página ou na seguinte:
   campos para "Recebido em", "Nome de quem recebeu", "Cargo/setor", "Nº do protocolo" e
   "Assinatura e carimbo" — é a prova de que o pedido foi entregue, essencial se o órgão demorar
   ou não responder.
8. **Instrução de uso**, ao final do documento: "Imprima duas vias de cada requerimento, assine
   as duas, entregue uma no protocolo do órgão e guarde a outra com a data e o carimbo de
   recebimento."

**Não há PDF-modelo anexado:** reproduza a estrutura acima; nunca copie nome, vínculos ou datas de outro cliente.

**Nunca junte, no mesmo requerimento, pedidos de dois órgãos diferentes** — mesmo que o cliente
tenha vínculos com ambos. **Nunca presuma o nome exato do setor/secretaria responsável** quando o
CNIS ou o formulário não deixarem claro — nesse caso, use o nome do ente (Município/Estado) sem
inventar o nome do departamento, e sinalize internamente que o(a) advogado(a) deve confirmar o setor
antes de entregar ao cliente.

**Regra de envio (igual à seção D): só sai do escritório depois da confirmação de contrato
assinado.** Antes disso, checklist e requerimentos ficam salvos internamente (na pasta/Dossiê do
cliente, se a automação estiver rodando por lá) — nunca anexados a mensagem para quem ainda não
fechou, mesmo que a pergunta pareça inofensiva ("me manda a lista do que eu preciso"). Se o
cliente perguntar antes de contratar, a resposta é sobre o serviço que resolve a pendência, não a
lista de documentos ou os requerimentos em si (ver roteiro de vendas, seção C).

## Regras de segurança e confiabilidade

Estas regras valem tanto para o PDF quanto para os slides, e devem aparecer resumidas nas
ressalvas técnicas do relatório:

- Não presuma nem invente vínculos, contribuições, remunerações, datas, indicadores ou
  documentos que não estejam no CNIS enviado.
- Diferencie sempre fatos identificados de hipóteses que dependem de confirmação documental ou
  institucional — no relatório, marque claramente o que é "achado" vs. "hipótese a confirmar"
  (a pesquisa preliminar de RPPS, passo 3.5, é sempre hipótese a confirmar, nunca conclusão
  definitiva).
- Nunca apresente como definitivamente perdido um período que ainda possa ser comprovado
  documentalmente, nem como definitivamente válido um período com pendência não tratada. Um
  período com pendência **integra o tempo total estimado** e é classificado como **em risco** —
  não é excluído da conta. Isso inclui o **período de vínculo registrado sem contribuição
  correspondente**, que é sempre tempo em risco (salvo concomitância integral com vínculo que
  tenha remunerações — ver passo 2).
- **Não presuma datas.** Use apenas o que está no extrato. Quando o CNIS não informa Data Fim mas
  informa a competência da última remuneração, essa competência é o fim do período — e isso deve
  ser dito como tal. Quando o CNIS não informa nem Data Fim nem remuneração alguma, **nenhuma data
  pode ser adotada**: nem a véspera do vínculo seguinte, nem a data de emissão do extrato, nem
  qualquer outra. O período vira "extensão a apurar" e fica fora do total, e o relatório explica
  por quê. Fechar a conta com uma data inventada é erro grave: o cliente leva para o INSS um
  número que ninguém verificou.
- Não junte num único número situações juridicamente distintas. Lacuna sem vínculo declarado e
  vínculo declarado sem contribuição são coisas diferentes, com providências diferentes, e devem
  aparecer separadas em todos os lugares — resumo executivo, seção de tempo, quadro de pendências,
  slides e roteiro.
- Se a qualidade do PDF do CNIS impedir leitura segura de alguma parte, diga isso
  explicitamente em vez de estimar ou arredondar.
- Este diagnóstico é uma estimativa inicial e não substitui o Planejamento Previdenciário
  Estratégico completo nem a análise documental individualizada — deixe isso escrito no
  relatório. Não conclua neste diagnóstico se a cliente já pode se aposentar nem qual regra é
  mais vantajosa.
- A triagem previdenciária básica e interna do passo 7 é uma checagem aproximada, de uso exclusivo
  da equipe, para orientar a apresentação e a oferta comercial — **nunca** é uma conclusão sobre
  direito adquirido, regra aplicável, data de aposentadoria ou RMI, e **nunca** substitui o
  Planejamento Previdenciário Estratégico. Não a inclua, em nenhuma versão, no relatório em PDF
  entregue ao cliente, nem detalhe seus critérios na reunião — o único reflexo permitido dela na
  apresentação é o aviso comercial cauteloso e a oferta condicional do Pacote 4,
  descritos na seção "Saídas → B".
- Dados pessoais do segurado (CPF, NIT, nome, remunerações) são sensíveis — trate os arquivos
  de trabalho normalmente, mas não os inclua em nenhum lugar fora do relatório/apresentação
  solicitados.
