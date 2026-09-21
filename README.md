# Skills de Previdenciário para Professores

Modelo de skills do Claude para planejamento previdenciário de professores (RGPS e RPPS), sem nome de escritório, método ou cliente. **Para baixar tudo:** botão verde **Code → Download ZIP**, no alto desta página, e descompacte.

## Como instalar

Este repositório tem **3 skills que trabalham juntas**. Instale as três.

| Skill | Para que serve |
|---|---|
| `diagnostico-previdenciario-coloqueseunomeaqui` | Diagnóstico inicial: lê o CNIS do professor e mostra tempo total, tempo regular, tempo em risco e pendências. Gera relatório, slides, roteiro da reunião e lista de documentos. |
| `planejamento-previdenciario-coloqueseunomeaqui` | Planejamento completo: testa as regras de aposentadoria, calcula a RMI, simula cenários e recomenda a estratégia. |
| `planejamento-previdenciario-coloqueseunomeaqui-revisor` | Revisor independente: tenta derrubar o planejamento antes de ele ser entregue. |

O repositório tem duas formas: a pasta `skills/` (para o Claude Code) e a pasta `para-enviar-ao-claude-web/` (para o Claude pelo site ou aplicativo). Escolha **um** dos caminhos abaixo.

---

## Caminho A — Claude Code (recomendado)

É o caminho em que as três skills se enxergam melhor.

**No Mac**
1. Dê dois cliques no `.zip` baixado para descompactar.
2. Abra o **Finder**, aperte `Cmd + Shift + G`, cole `~/.claude/skills` e aperte Enter.
   - Se der erro dizendo que a pasta não existe: abra o **Terminal**, cole `mkdir -p ~/.claude/skills`, aperte Enter e repita o passo 2.
3. Copie as **3 pastas** que estão dentro de `skills/` (as que começam com `diagnostico-` e `planejamento-`) para dentro da pasta que abriu.
4. Feche o Claude Code e abra de novo.

**No Windows**
1. Clique com o botão direito no `.zip` baixado e escolha **Extrair tudo**.
2. Abra o **Explorador de Arquivos**, clique na barra de endereço, cole `%USERPROFILE%\.claude\skills` e aperte Enter. (Se a pasta não existir, crie primeiro uma pasta `.claude` e, dentro dela, uma pasta `skills`.)
3. Copie as **3 pastas** de dentro de `skills/` para dentro dessa pasta.
4. Feche o Claude Code e abra de novo.

**Como saber se deu certo:** o caminho de cada arquivo deve ficar assim (exemplo no Mac):
`~/.claude/skills/diagnostico-previdenciario-coloqueseunomeaqui/SKILL.md`
Se o `SKILL.md` estiver uma pasta mais para dentro (pasta dentro de pasta), a skill não aparece — suba o conteúdo um nível.
Depois, numa conversa nova, digite `/` e procure "previdenciario", ou pergunte: "quais skills de previdenciário você tem?".

---

## Caminho B — Claude pelo site ou aplicativo (claude.ai)

Exige que a opção de **execução de código e criação de arquivos** esteja ligada nas configurações da sua conta.

1. Abra o Claude e vá em **Personalizar (Customize) → Skills**. (Em algumas versões: **Configurações → Capacidades → Skills**.)
2. Clique em **Adicionar / +** e escolha o primeiro `.zip` da pasta `para-enviar-ao-claude-web/`.
3. Repita com os outros dois `.zip`. **Um arquivo por vez**, as três.
4. Confira se as três aparecem na lista com a chavinha **ligada**.

Cada `.zip` já tem a pasta da skill na raiz, que é o formato que o Claude exige.

---

## Passo obrigatório depois de instalar: coloque o SEU nome

Os nomes vêm com `coloqueseunomeaqui` de propósito. Na primeira vez que você usar qualquer uma das três, o Claude vai parar e oferecer a troca. Ele explica o que fazer e pergunta o nome que você quer (o seu, o do escritório ou o do seu método).

Se ele não oferecer sozinho, escreva na conversa:

> Quero personalizar as skills de previdenciário com o meu nome. Troque `coloqueseunomeaqui` por `[SEU NOME OU MÉTODO]` nas três skills e me diga o que mais eu preciso preencher.

Regras do nome: só letras minúsculas sem acento, números e hífens, sem espaços. Exemplo: `planejamento-previdenciario-silva`.
No Claude Code o Claude faz a troca por você. No Claude pelo site, a troca exige gerar um `.zip` novo da pasta com o nome novo e enviar de novo.

---

## O que você ainda precisa preencher (nada vem pronto)

Estas skills **não trazem** dados de nenhum escritório. Antes de usar com cliente real, tenha à mão e informe ao Claude:
- nome do escritório, seu nome e OAB, logotipo e cores;
- o nome do seu método, se tiver um;
- os **pacotes, valores e condições de pagamento** (usados pelo diagnóstico);
- depoimentos **autorizados** pelos clientes, se quiser usar prova social.

O pacote **não inclui apresentação de slides pronta**: o Claude monta os slides do zero, na identidade visual que você informar.

## Bom saber
- Os cálculos usam scripts em Python (só o que já vem com o Python 3, nada para instalar à parte). No Claude pelo site o Python já vem no ambiente de execução; no computador, o Python 3 precisa estar instalado.
- As skills pedem ao Claude para gerar PDF e apresentação. Se ele avisar que não consegue criar o arquivo, confira se a criação de arquivos está ligada (Caminho B) ou peça a ele que ative a capacidade de documentos.
- O resultado é uma **minuta de trabalho** para o advogado revisar: o julgamento jurídico e a decisão final continuam sendo seus.
- A legislação previdenciária muda. As skills mandam pesquisar a norma vigente em cada caso; confirme sempre a fonte.

## Se algo der errado
| Problema | O que fazer |
|---|---|
| A skill não aparece | Confira se a pasta está em `~/.claude/skills/` (não uma pasta acima nem abaixo) e reinicie o Claude Code. |
| O site recusa o `.zip` | Use os `.zip` da pasta `para-enviar-ao-claude-web/`, sem descompactar nem renomear o arquivo. |
| A revisora diz que não achou a skill de planejamento | Instale as três juntas. |
| Depois de renomear, a skill sumiu | Reinicie o Claude ou abra uma conversa nova. |
