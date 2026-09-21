# Skills de Previdenciário para Professores

Modelo de skills do Claude para planejamento previdenciário de professores (RGPS e RPPS), sem nome de escritório, método ou cliente. **Para baixar tudo:** botão verde **Code → Download ZIP**, no alto desta página, e descompacte.

## O que tem aqui

Este repositório tem **3 skills que trabalham juntas**. Instale as três.

| Skill | Para que serve |
|---|---|
| `diagnostico-previdenciario-coloqueseunomeaqui` | Diagnóstico inicial: lê o CNIS do professor e mostra tempo total, tempo regular, tempo em risco e pendências. Gera relatório, slides, roteiro da reunião e lista de documentos. |
| `planejamento-previdenciario-coloqueseunomeaqui` | Planejamento completo: testa as regras de aposentadoria, calcula a RMI, simula cenários e recomenda a estratégia. |
| `planejamento-previdenciario-coloqueseunomeaqui-revisor` | Revisor independente: tenta derrubar o planejamento antes de ele ser entregue. |

## Instalação rápida (2 minutos)

**Passo 1 — Baixe o repositório.** Abra o **Terminal** (Mac) ou o **PowerShell** (Windows) e cole:

```bash
gh repo clone marcuspeterson1/skills-planejamento-previdenciario-mp
cd skills-planejamento-previdenciario-mp
claude
```

O último comando abre o Claude Code dentro da pasta baixada. Se você usa o aplicativo do Claude em vez do terminal, abra essa pasta (`skills-planejamento-previdenciario-mp`) na aba **Code**.

> **O `gh` pediu login, ou você não o tem?** Troque a primeira linha por:
> `git clone https://github.com/marcuspeterson1/skills-planejamento-previdenciario-mp.git`
> Sem `git` também? Use o botão verde **Code → Download ZIP** desta página, descompacte, e siga a [instalação manual](#instalação-manual-sem-terminal).

**Passo 2 — Cole este prompt no Claude e aperte Enter:**

```text
Instale as 3 skills desta pasta no meu Claude Code, para eu usar em qualquer projeto:

1. Copie as 3 pastas de `skills/` para `~/.claude/skills/` (no Windows: `%USERPROFILE%\.claude\skills`). Crie a pasta `skills` se ela não existir.
2. Se já existir lá uma skill com o mesmo nome, NÃO sobrescreva: me avise e pergunte o que fazer.
3. Confira que cada skill ficou com o `SKILL.md` direto dentro da sua pasta e me mostre a lista final do que foi instalado.
4. Me diga, em português simples, se preciso reiniciar o Claude Code.
5. Depois pergunte qual nome eu quero no lugar de `coloqueseunomeaqui` (meu nome, o do meu escritório ou o do meu método) e faça a troca nas cópias instaladas em `~/.claude/skills/` (não na pasta baixada), nas 3 skills, seguindo a seção "Antes do primeiro uso" de cada uma. Depois me diga o que mais eu preciso preencher.
```

**Passo 3 — Reinicie o Claude Code** (feche e abra de novo). Pronto: digite `/` e procure "previdenciario", ou peça "roda o diagnóstico desse CNIS" enviando o extrato.

---

## Instalação manual (sem terminal)

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
