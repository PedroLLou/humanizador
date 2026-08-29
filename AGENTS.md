# Guia para agentes

Este arquivo explica como mexer no Humanizador sem quebrar o pacote nem o prompt.

## O que tem neste repositório

O Humanizador é uma skill escrita em Markdown. O `SKILL.md` é o prompt que os agentes leem. Não há build.

Mantenha a skill portátil. Não escreva instrução que amarre a skill a uma ferramenta específica.

## Arquivos principais

- `SKILL.md` é a fonte da verdade e o único arquivo de skill do repositório. Contém a metadata YAML, os 42 padrões numerados e os exemplos de cada um.
- `README.md` explica instalação, uso, padrões e histórico de versões.
- `.claude-plugin/plugin.json` descreve o plugin do Claude Code e aponta o carregador de skills para o `SKILL.md` da raiz.
- `.claude-plugin/marketplace.json` permite adicionar este repositório como marketplace do Claude Code.
- `scripts/validate-package.py` confere os arquivos do pacote e os valores compartilhados entre eles.

## Regras de mudança

Mantenha o `SKILL.md` e o `README.md` em sincronia.

- **Padrões:** a skill tem 42 padrões numerados. Se adicionar, remover ou renumerar um padrão, atualize a tabela do README, o título da seção, o validador e toda referência ao número.
- **Versão:** use a mesma versão em `metadata.version` no `SKILL.md`, na primeira entrada de histórico do README e no `.claude-plugin/plugin.json`. Não crie um campo `version` no topo da metadata da skill.
- **Um SKILL.md só:** o arquivo mora na raiz. Não crie cópia em subpasta: o carregador de skills passa a encontrar a mesma skill duas vezes.
- **Compatibilidade:** mantenha instalação e uso neutros entre agentes. Claude Code, Cowork e Codex são exemplos, não limites.
- **Histórico:** anote no README qualquer mudança de comportamento ou correção não óbvia.
- **Checagens:** antes de publicar, rode `python3 scripts/validate-package.py`, `npx skills add . --list` e `claude plugin validate .`.

## Evidência antes de padrão novo

Um padrão só entra se houver evidência de que a IA comete aquilo **em português**. Lista de palavras traduzida do inglês não vale: o vício precisa existir na língua.

- Cite a fonte na seção "Fonte e adaptação" do `SKILL.md`.
- Marque o nível de confiança do padrão: apoio em fonte externa ou heurística de adaptação.
- Se o padrão só existe em inglês, como o excesso de pares com hífen, não traduza. Procure o equivalente funcional em português ou deixe de fora.

## Estilo de escrita

Escreva em português claro no prompt, na documentação, nos comentários de código e nas mensagens de validação.

- Comece pelo ponto principal.
- Use palavras comuns e voz ativa.
- Frases e parágrafos curtos.
- Um termo só para a mesma coisa.
- Use "precisa" para requisito.
- Use título, lista e tabela quando ajudarem quem lê.
- Corte palavra repetida e desnecessária.
- Limite sigla e explique termo técnico.
- Evite dupla negativa.
- Preserve identificador, comando, caminho, campo de schema, citação, expressão vigiada e exemplo que carrega comportamento.
- Preserve o sentido técnico completo.

A skill vale para o próprio repositório: se o texto que você escrever aqui dispara um dos 42 padrões, reescreva.

## Editando a skill

- Mantenha a metadata YAML válida.
- Trate o texto abaixo da metadata como o produto.
- Prefira uma instrução curta e clara a mais uma exceção ou explicação repetida.