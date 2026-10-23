# Checa pra mim

Uma skill de checagem de fatos para assistentes de IA. Você cola uma afirmação, uma manchete, um boato ou um card e a IA busca evidências, pesa as fontes por critérios objetivos e responde com um veredito:

**Verdadeiro** · **Falso** · **Não é bem assim** · **Sem evidência suficiente**

## Baixar

[**Baixar checapramim.zip**](https://github.com/cauemadeira/checapramim/releases/latest/download/checapramim.zip)

Se a sua plataforma aceitar apenas um arquivo, use a [versão em arquivo único](https://github.com/cauemadeira/checapramim/releases/latest/download/checapramim-arquivo-unico.zip).

## Como instalar

O mesmo arquivo `.zip` serve, em princípio, para todas as plataformas. Os caminhos de menu abaixo vêm de documentação e guias públicos e mudam entre versões. Confirme na tela.

| Plataforma | Como enviar | Como usar |
|---|---|---|
| **Claude** (claude.ai, aplicativo desktop e Cowork) | Customize (ou Settings) > Skills > "+" > Enviar skill, e escolha o `.zip`. Exige plano pago com execução de código habilitada | `/checapramim` seguido da afirmação |
| **Gemini** (app e web) | Settings > Skills > criar ou enviar o `.zip` | Peça a checagem citando a skill `checapramim` |
| **ChatGPT** | Plugins > Skills > Create > "Upload from your computer", com o `.zip`. Pode depender do plano | `@checapramim` seguido da afirmação |
| **Claude Code** | Copie a pasta `checapramim/` (de dentro do `.zip`) para `~/.claude/skills/` | `/checapramim` |
| **Gemini CLI** | `gemini skills install ./checapramim.zip` ou copie a pasta para `~/.gemini/skills/` | Peça a checagem; confirme a ativação |
| **Codex CLI e IDE** | Copie a pasta para `~/.agents/skills/` e reinicie | `$checapramim` |

**Requisito importante:** o assistente precisa ter **busca na web** habilitada. Sem ela, a skill se recusa a emitir veredito.

## Como usar

```
/checapramim "O Brasil tem o maior número de homicídios do mundo."
```

Também funciona colando um boato de WhatsApp, o texto de um card, um link ou uma imagem. Frases como "isso é verdade?" ou "é fake news?" costumam acionar a skill sem o comando.

## Como ela decide

A skill não usa uma lista fixa de veículos "bons" e "ruins". Cada fonte recebe uma nota por critérios verificáveis, e a mesma régua vale para um grande jornal, um blog de nicho de qualquer lado do espectro político e um perfil anônimo.

- **Proximidade da evidência:** a fonte é a origem do dado ou está distante dela?
- **Transparência:** autoria, propriedade e financiamento são identificáveis?
- **Correções e histórico:** a fonte corrige publicamente quando erra?
- **Leitura lateral:** o que fontes independentes dizem sobre ela? (método do [Stanford History Education Group](https://ed.stanford.edu/news/it-doesn-t-take-long-learn-how-spot-misinformation-online-stanford-study-finds))
- **Competência no tema** e **aderência** ao que está sendo checado.

O resultado é um nível de A (alta) a D (fraca). Confiabilidade e viés ideológico são tratados como eixos separados. O viés não rebaixa a fonte, mas aumenta a exigência de corroboração independente. Republicações e agregadores contam como uma só fonte. Fonte de nível D não sustenta veredito.

Detalhes em `skill/checapramim/SKILL.md` e `skill/checapramim/references/`.

## Limites

- **Não substitui checadores profissionais.** É um apoio. Para temas sensíveis, consulte também os checadores signatários do [Código de Princípios da IFCN](https://ifcncodeofprinciples.poynter.org/).
- **Depende de busca na web e do que a IA consegue abrir.** Páginas oficiais restritas, como algumas do gov.br, podem não ser lidas, e a skill declara isso nos "Limites desta checagem".
- **Imagens:** a IA não prova sozinha que uma imagem é falsa ou gerada por IA apenas olhando. O veredito se apoia na origem rastreada.
- **Pode errar.** Confira os links citados antes de repassar um veredito.

## Estado dos testes

| Plataforma | Estado |
|---|---|
| Claude | Testada em 4 casos com avaliação registrada (ver [`evals/RESULTADOS-iteracao-1.md`](evals/RESULTADOS-iteracao-1.md)) |
| Claude Cowork, ChatGPT, Gemini | Instalada e testada manualmente pelo autor em outubro de 2026; funcionou nas três. Sem avaliação estruturada |

Os 4 casos avaliados são pequenos e os critérios foram escritos pelo próprio autor, então os resultados indicam direção, não garantia. Os testes manuais em Cowork, ChatGPT e Gemini foram informais e não geraram registro de casos. Se algo se comportar de forma diferente na sua conta ou no seu plano, abra uma issue contando a plataforma e o que aconteceu.

## Para quem mantém o repositório

```
skill/checapramim/   fonte única da skill (SKILL.md + references/)
scripts/build.py     gera dist/ (zip completo, zip de arquivo único e SKILL.md único)
evals/               casos de teste e resultados
docs/                textos de divulgação
.github/workflows/   cria a Release ao publicar uma tag vX.Y.Z
```

Para gerar os pacotes localmente: `python3 scripts/build.py`.
Para publicar uma versão: atualize o `CHANGELOG.md`, então no GitHub vá em Releases > Draft a new release, crie a tag (ex.: `v0.1.0`) e clique em Publish. A automação gera os pacotes e os anexa à Release.

Edite sempre a pasta `skill/checapramim/`. A versão em arquivo único é gerada a partir dela.

## Licença

[Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.pt-br). Texto completo em `LICENSE`.

Você pode copiar, adaptar e redistribuir, inclusive para fins comerciais, desde que dê o crédito:

> Checa pra mim, de Cauê Madeira / Haikai AI Office. https://github.com/cauemadeira/checapramim
