# Cálculo da RMI, descarte, cenários de contribuição e análise econômica

## 1. Cálculo próprio da RMI

Refaça o cálculo, mesmo tendo o número de uma calculadora ou de um software de cálculo. O objetivo
não é desconfiar do software: é que o parecer precisa poder ser auditado por outro advogado, e para
isso cada elemento tem que estar explícito.

Elementos a explicitar sempre:

1. **Período básico de cálculo** — 07/1994 em diante (ou início da contribuição, se posterior),
   conforme o art. 26 da EC 103.
2. **Salários de contribuição** competência a competência, com a origem de cada um (CNIS,
   contracheque, carnê, CTC).
3. **Atualização monetária** — informe qual tabela de índices foi usada e a data-base. Não use
   fatores de memória: puxe a tabela vigente (INSS/Dataprev ou a publicada mensalmente) e registre a
   referência no relatório técnico.
4. **Média** aritmética simples de 100% do período.
5. **Coeficiente** conforme a regra aplicada (ver `base-normativa-federal.md`, seção 5) — e, no
   caso do art. 17, fator previdenciário em vez de coeficiente.
6. **Teto** do RGPS na data e, se houver, teto/limitação do RPPS.
7. **Salários concomitantes** — no RGPS pós-Lei 9.876/1999 somam-se as bases do mesmo mês,
   respeitado o teto; em CTC de RPPS, a remuneração da certidão entra pelo valor certificado.

Registre a RMI **na data de implementação de cada regra**, não só a de hoje: a comparação entre
regras só faz sentido com cada uma no seu momento.

`scripts/rmi.py` faz a média, o coeficiente e o teste de descarte a partir de um CSV de salários de
contribuição. Ele não inventa índices: se a tabela de atualização não for fornecida, ele calcula
sobre valores nominais e **marca o resultado como não atualizado** — nesse caso o número não vai
para o parecer.

## 2. Descarte de contribuições (EC 103, art. 26, § 6º)

Teste sempre. O descarte é um dos poucos lugares onde o planejamento gera ganho puro, e é
invisível para o cliente que faz o pedido sozinho.

Para cada estratégia de descarte apresente: quais competências saem, o fundamento, o tempo de
contribuição recalculado, a média recalculada, o coeficiente recalculado, o benefício recalculado,
o ganho mensal, o ganho anual e o ganho projetado até a expectativa de vida.

Duas travas obrigatórias, que o script confere mas você precisa reler:

- O descarte **não pode** derrubar o tempo mínimo, a carência, a pontuação ou a idade exigidos pela
  regra escolhida. Descartar 18 meses que reduziam a média mas que eram os meses que fechavam os 25
  anos de magistério é um erro que só aparece no indeferimento.
- Descartar competências reduz o tempo, e portanto pode reduzir o **coeficiente** (2% por ano). O
  ganho na média precisa superar a perda no coeficiente — o teste é do valor final, nunca da média
  isolada.

## 3. Cenários de contribuição futura

Simule os que forem juridicamente possíveis para aquele cliente. Nem todos são:

| Cenário | Descrição | Quando faz sentido |
|---|---|---|
| **A** | Permanecer no vínculo atual, contribuindo normalmente | referência de comparação; sempre calcule |
| **B** | Sair do vínculo e contribuir como contribuinte individual pelo salário mínimo | quando falta pouco tempo e a média já está formada |
| **C** | Sair do vínculo e contribuir como contribuinte individual pelo teto | quando falta tempo e a média é baixa |
| **D** | Contribuir pelo valor equivalente ao último salário de contribuição | manutenção da média |
| **E** | Valor intermediário definido estrategicamente | o mais comum na prática; teste 2 ou 3 patamares |
| **F** | Parar de contribuir | quando o requisito já está cumprido ou a espera é só de idade |
| **G** | Outra categoria de segurado cabível e mais econômica | verificar enquadramento antes |

**Trava jurídica:** nunca recomende **facultativo** para quem exerce atividade remunerada. A
filiação nesse caso é obrigatória, e a contribuição na categoria errada não é aproveitada — o
cliente paga e perde.

Para cada cenário calcule: contribuição mensal, tempo restante, custo total até a aposentadoria,
data da aposentadoria, RMI projetada, diferença de RMI em relação ao cenário A, prazo (em meses)
para recuperar o investimento adicional e retorno financeiro estimado.

Atenção às alíquotas e ao efeito da EC 103 sobre contribuições abaixo do mínimo: competências com
recolhimento inferior ao salário mínimo, a partir de 11/2019, exigem complementação, agrupamento ou
uso de excedente para serem computadas. Antes de recomendar complementar, **calcule se compensa**:
compare o custo da complementação com o ganho de tempo e de RMI que ela produz. Muitas vezes não
compensa, e dizer isso é parte do serviço.

## 4. Expectativa de vida e valor total do benefício

Consulte a **tábua completa de mortalidade do IBGE vigente na data do planejamento** — busque na web
(https://www.ibge.gov.br, "Tábuas Completas de Mortalidade"), pelo sexo e pela idade do cliente.
Não use número memorizado: a tábua é atualizada anualmente e é a mesma base que o INSS usa para o
fator previdenciário.

Cálculo:

```
pagamentos estimados = (expectativa de sobrevida em anos na idade da aposentadoria) × 13
valor total estimado = RMI projetada × pagamentos estimados
```

Use 13 pagamentos por ano quando o benefício tiver 13º (regra do RGPS e da maioria dos RPPS);
registre a premissa.

Escreva sempre, no parecer e nos slides, que a expectativa de vida é **ferramenta estatística de
comparação, não previsão individual**. O cliente precisa entender que o número serve para escolher
entre cenários, não para saber quanto tempo vai viver.

## 5. Tabela comparativa obrigatória

Toda entrega traz esta tabela, com uma linha por cenário relevante:

| Cenário | Data da aposentadoria | Idade | RMI | Investimento adicional até aposentar | Valor projetado até a expectativa de vida |
|---|---|---|---|---|---|

E, abaixo dela, os números que transformam a tabela em decisão:

- diferença de investimento entre cenários;
- diferença mensal e anual de benefício;
- meses necessários para recuperar o investimento adicional (ponto de equilíbrio);
- retorno acumulado;
- **custo de postergar** — quanto o cliente deixa de receber, em reais, por cada ano que espera.

**Nunca conclua que o maior benefício mensal é a melhor opção sem fazer essa conta.** Uma professora
de 55 anos que espera quatro anos por uma RMI 12% maior costuma levar mais de vinte anos para
recuperar os quatro anos de benefício que não recebeu — e isso muda a recomendação.

`scripts/cenarios.py` monta a tabela e calcula ponto de equilíbrio, custo de postergação e a idade
em que a espera passa a compensar.

**Meça sempre num horizonte comum.** Se cada cenário for medido a partir da sua própria data de
aposentadoria, os anos em que o cliente ainda não recebe nada somem da conta e o cenário mais
tardio parece melhor por construção. O script resolve isso levando todos os cenários até a mesma
data final; a pergunta que fecha a comparação é **"com que idade a espera passa a compensar?"**.
Quando essa idade fica próxima ou acima da expectativa de sobrevida do cliente, esperar é uma
aposta, não uma estratégia — e o parecer deve dizer isso com essas palavras.

**Quando o cliente não desembolsa nada, o custo do cenário não é dinheiro, é tempo de trabalho.**
Empregado e servidor têm a contribuição descontada em folha: nesses casos a coluna de investimento
fica zerada em todos os cenários e a comparação inteira se desloca para o custo de postergar. Diga
isso explicitamente, ou a tabela dá a impressão falsa de que esperar é de graça.

**Verifique se o cliente pode aposentar e continuar trabalhando.** No RGPS não há
incompatibilidade entre a aposentadoria por tempo de contribuição e a continuidade do vínculo, o
que muitas vezes torna a data mais cedo dominante — o cliente soma benefício e salário. O
contraponto obrigatório, que precisa aparecer no mesmo parágrafo: o STF vedou a desaposentação e a
reaposentação (Tema 503), de modo que as contribuições posteriores não aumentam o benefício. Em
RPPS a regra é outra e depende do ente — confira antes de afirmar.

## 6. Os quatro recortes finais

Feche a análise econômica nomeando explicitamente:

- **CENÁRIO MAIS RÁPIDO** — primeira data juridicamente segura.
- **MAIOR BENEFÍCIO** — maior RMI.
- **MENOR INVESTIMENTO** — menor desembolso até lá.
- **MELHOR CUSTO-BENEFÍCIO** — melhor relação entre investimento e retorno.

E então a **ESTRATÉGIA RECOMENDADA PELO ESCRITÓRIO**, que pode ou não coincidir com qualquer um
dos quatro, justificada por segurança jurídica, tempo, idade, RMI, custo, possibilidade de
aposentadoria em mais de um regime, expectativa de vida, retorno, complexidade documental e risco.
