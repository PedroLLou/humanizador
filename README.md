# Humanizador

Skill que reescreve texto com cara de IA para soar como pessoa escrevendo, em português do Brasil, sem mudar o que o texto diz.

Ela conhece 42 vícios que os modelos cometem escrevendo em português: o "crucial" que aparece em todo parágrafo, o travessão cortando a frase no meio, o "Além disso" abrindo cada bloco, a vírgula antes do "e" que veio do inglês, o elogio inflado, a fonte sem nome e o parágrafo final otimista que não diz nada. Para cada um ela sabe o que tirar e o que colocar no lugar.

O que ela não faz é inventar. Nome, número, data, citação e fonte só entram se estiverem no texto original ou se você fornecer. Em texto pessoal ela preserva o seu estilo; em texto técnico e de referência, mantém o tom neutro.

É só Markdown, então funciona em qualquer agente que suporte skills.

## Como funciona

A skill trabalha com 42 padrões. Ela faz uma primeira passada sem tratar a estrutura original como fixa. Depois confere o rascunho contra os padrões e contra as afirmações do texto original, e reescreve o que ainda precisar.

Ela não inventa nada. Nome, número, data, citação ou qualquer detalhe factual precisa vir do texto original ou de você. Em texto pessoal, ela preserva o seu estilo. Em texto técnico e de referência, mantém tom neutro. Se você mandar uma amostra da sua escrita, ela segue a amostra em vez das regras de estilo padrão.

Quando você cola um texto, ela mostra o rascunho, uma crítica curta do que ainda soa artificial e a versão final. Quando você aponta um arquivo, ela mexe só na prosa e deixa código, dados, frontmatter e destino de link intactos.

Ela também vale para escrever do zero. Nesse modo a lista funciona como filtro de saída: escreve direto, varre os padrões antes de entregar e devolve só o texto, sem relatório.

## Exemplo

**Antes**, um "sobre nós" gerado por IA:

> Fundada em 2019, a TechFlow se consolidou como uma referência no cenário de soluções digitais para o varejo. Além disso, a empresa conta com uma equipe robusta de profissionais altamente qualificados, evidenciando seu compromisso com a excelência. Especialistas do setor apontam que a companhia desempenha um papel crucial na transformação digital de pequenos negócios — não apenas oferecendo tecnologia, mas construindo parcerias duradouras. Apesar dos desafios do mercado, o futuro é promissor.

**Depois**:

> A TechFlow foi fundada em 2019 e faz software para o varejo. O trabalho é com pequenos negócios que estão informatizando a operação.

Encolheu porque quase tudo que saiu era elogio, não informação. Nove padrões dispararam nesse parágrafo:

| Trecho | Padrão |
| --- | --- |
| "se consolidou como uma referência no cenário" | 1 (importância inflada), 4 (folheto de turismo), 7 (cenário) |
| "Além disso" | 26 (conectivo empilhado) |
| "equipe robusta de profissionais altamente qualificados" | 4, 7 (robusto), 42 (advérbio sem função) |
| "evidenciando seu compromisso com a excelência" | 3 (gerúndio raso) |
| "Especialistas do setor apontam" | 5 (fonte vaga) |
| "desempenha um papel crucial" | 1, 7 (crucial) |
| "— não apenas oferecendo..., mas construindo..." | 14 (travessão), 9 (não apenas X, mas Y) |
| "Apesar dos desafios... o futuro é promissor" | 6 (desafios e perspectivas), 25 (final otimista) |

Repare que a versão final não ganhou nenhum dado que não estivesse no original. "2019" e "pequenos negócios" estavam lá. Número de funcionários, nome de produto e faturamento não entram, mesmo que deixassem o texto bem mais concreto. Quando falta informação, a skill pergunta em vez de preencher.

## Instalação

### Claude no app, no site e no Cowork

Baixe o `humanizador.zip` na [aba Releases](https://github.com/PedroLLou/humanizador/releases/latest) e suba em **Configurações → Customizar → Skills → botão "+" → "Criar skill"**. Depois deixe o toggle ligado.

Não use o botão verde "Code → Download ZIP" desta página: ele empacota o repositório inteiro, e o Claude espera um ZIP com uma pasta contendo o `SKILL.md` na raiz dela.

### Claude Code

O caminho mais curto é adicionar o repositório como marketplace e instalar o plugin:

```
/plugin marketplace add PedroLLou/humanizador
/plugin install humanizador@humanizador
```

Sem plugin, clonando direto na pasta de skills. Linux e macOS:

```bash
git clone https://github.com/PedroLLou/humanizador.git ~/.claude/skills/humanizador
```

Windows, no PowerShell:

```powershell
git clone https://github.com/PedroLLou/humanizador.git "$env:USERPROFILE\.claude\skills\humanizador"
```

Troque `~/.claude/skills/` por `.claude/skills/` dentro de um projeto para instalar só naquele projeto. Confira com `/skills` na sessão.

### Outros agentes

Qualquer ferramenta que carregue skills em Markdown serve: copie o `SKILL.md` para a pasta de skills dela. Se a ferramenta não tiver esse conceito, cole o conteúdo do arquivo como instrução de sistema.

## Uso

O caso mais comum é colar o texto:

```
Humaniza esse texto:

Fundada em 2019, a TechFlow se consolidou como uma referência...
```

A resposta vem em três partes: o rascunho, uma crítica curta do que ainda soa artificial e a versão final.

### Em cima de um arquivo

```
Humaniza a prosa do docs/post-de-lancamento.md
```

Aqui ela escreve só a versão final no arquivo e mexe apenas na prosa. Bloco de código, frontmatter YAML, dados e destino de link ficam intactos.

### Imitando a sua voz

Cole uma amostra sua antes do texto a reescrever:

```
Aqui vai uma amostra da minha escrita:
[2 ou 3 parágrafos seus]

Agora humaniza esse texto:
[texto com cara de IA]
```

A amostra tem prioridade sobre as regras de estilo, inclusive sobre a regra de travessão: se você usa travessão, ela mantém na mesma frequência.

### Escrevendo do zero

```
Escreve um post de LinkedIn sobre [assunto]
```

Não precisa citar a skill. Ela entra sozinha em pedido de texto que você vai publicar ou assinar: post, artigo, legenda, e-mail, proposta, README, bio. A resposta vem só com o texto, já varrido.

### Só apontando, sem reescrever

```
Passa esse texto pelos padrões do humanizador e só me diz o que dispara, sem reescrever nada.
```

Serve para aprender a enxergar os vícios em vez de terceirizar a correção.

### O que ela não vai fazer

- Inventar dado para o texto ficar mais concreto
- Trocar toda palavra difícil por uma fácil, porque a lista do padrão 7 não é proibição de vocabulário
- Deixar informal um texto que precisa ser formal, como petição, laudo ou ata
- Apagar o seu regionalismo, a sua gíria ou a sua opinião
## Os 42 padrões

### Conteúdo

| # | Padrão | Antes | Depois |
| --- | --- | --- | --- |
| 1 | Importância e legado inflados | "marcando um momento decisivo na evolução de..." | "foi criado em 1989, dentro de uma descentralização mais ampla" |
| 2 | Citar nome famoso para provar importância | "citado na Folha, no G1, no Estadão e na BBC" | Mantém só a citação com contexto útil |
| 3 | Análise rasa com gerúndio | "simbolizando... refletindo... evidenciando..." | Mantém só o que a fonte sustenta |
| 4 | Linguagem de folheto de turismo | "encravada na deslumbrante região serrana" | "é uma cidade na região serrana" |
| 5 | Fontes vagas | "Especialistas acreditam que é crucial" | Nomeia a fonte real ou corta a afirmação |
| 6 | Seção formulaica de desafios e perspectivas | "Apesar dos desafios... segue prosperando" | Mantém os fatos e tira o discurso |

### Linguagem e gramática

| # | Padrão | Antes | Depois |
| --- | --- | --- | --- |
| 7 | Palavras batidas de IA | "crucial... ademais... cenário... testemunho... evidenciando" | "também... precisa... continua comum" |
| 8 | Fugir de "é", "tem" e "fica" | "configura-se como... conta com... ostenta" | "é... tem" |
| 9 | "Não apenas X, mas Y" e final cortado | "Não é só X, é Y", "..., sem achismo" | Diz o ponto direto |
| 10 | Trios forçados | "inovação, inspiração e insights" | Usa o número de itens que o sentido pede |
| 11 | Troca de nome e abertura repetida | "a empresa... a companhia... a marca" | Um nome só, ou junta as frases |
| 12 | Falsa escala "de X a Y" | "do Big Bang à matéria escura" | Lista os temas direto |
| 13 | Voz passiva e sujeito sumido | "Não é necessário arquivo de configuração" | "Você não precisa de arquivo de configuração" |

### Estilo

| # | Padrão | Antes | Depois |
| --- | --- | --- | --- |
| 14 | Travessão e meia-risca | "instituições — não as pessoas — e ainda assim..." | Troca por ponto, vírgula ou parênteses (diálogo fica) |
| 15 | Negrito demais | "**OKRs**, **KPIs**, **BMC**" | "OKRs, KPIs, BMC" |
| 16 | Lista com mini-título em negrito | "**Desempenho:** o desempenho melhorou" | Vira prosa quando a lista não ajuda |
| 17 | Maiúscula em toda palavra do título | "Estratégias De Negociação E Parcerias" | "Estratégias de negociação e parcerias" |
| 18 | Emojis | "🚀 Fase de lançamento: 💡 Insight:" | Tira os emojis |
| 19 | Aspas curvas | `disse “o projeto”` | `disse "o projeto"` |
| 26 | Conectivo empilhado | "Além disso... Ademais... Dessa forma... Por fim" | Junta as frases ou começa pela informação |
| 27 | Fingir revelar uma verdade profunda | "No fundo, o que realmente importa é..." | Diz o ponto direto |
| 28 | Anunciar o que vem a seguir | "Vamos mergulhar", "é o seguinte" | Começa pelo conteúdo |
| 29 | Título repetido na primeira frase | "## Desempenho" + "Velocidade importa." | Deixa o título fazer o trabalho |
| 30 | Escrever sobre a versão antiga | "Esta função foi criada para substituir..." | Descreve o que ela faz agora |
| 31 | Frase de efeito e fragmento dramático | "Sem preferência. Sem viés. Sem nostalgia." | Frases de tamanho natural e afirmação específica |
| 32 | Máxima de camiseta | "Simetria é a linguagem da confiança" | Diz a afirmação específica |
| 33 | Falsa sinceridade na abertura | "Sinceramente? Depende..." | Responde direto |
| 34 | Responder objeção que ninguém fez | "Não se trata principalmente de..." | Tira a defesa sem base |
| 35 | Rejeitar alternativa falsa | "Uma opção tentadora seria..., mas" | Tira a opção falsa e mantém as reais |
| 39 | Simetria excessiva | Todo parágrafo do mesmo tamanho, toda lista com três itens | Quebra o ritmo de propósito |
| 40 | Ausência de cena e baixa materialidade | "cresceu bastante e atende diversos segmentos" | Puxa o dado concreto do original, sem inventar |
| 41 | Fonte inventada | Referência, link ou DOI que não existe | Marca para verificar, não conserta por cima |

### Chatbot

| # | Padrão | Antes | Depois |
| --- | --- | --- | --- |
| 20 | Sobra de chatbot no texto | "Espero ter ajudado! Qualquer dúvida..." | Tira |
| 21 | Aviso de limite de conhecimento e chute | "Embora os detalhes sejam escassos..." | Diz o que se sabe ou corta a afirmação |
| 22 | Tom bajulador | "Ótima pergunta! Você está certíssimo!" | Responde direto |

### Enrolação e ressalvas

| # | Padrão | Antes | Depois |
| --- | --- | --- | --- |
| 23 | Frases de enchimento | "com o intuito de", "devido ao fato de que" | "para", "porque" |
| 24 | Ressalva em cima de ressalva | "talvez possivelmente possa" | "pode" |
| 25 | Final genérico e otimista | "O futuro é promissor" | Termina em um fato ou em um plano real |

### Específicos do português

| # | Padrão | Antes | Depois |
| --- | --- | --- | --- |
| 36 | Cheiro de tradução do inglês | "No final do dia, nós precisamos entregar valor acionável" | "Precisamos entregar algo que o time consiga usar" |
| 37 | Formalidade de ofício e gerundismo | "Venho por meio desta... estaremos verificando o mesmo" | "Recebemos seu chamado. Vamos verificar" |
| 38 | Pontuação importada do inglês | "maçãs, bananas, e laranjas"; "o prazo é curto." | Sem vírgula de série; ponto fora das aspas |
| 42 | Advérbio em -mente sem função | "impactou significativamente" | "melhorou" |

## Confiança e evidência

Os padrões 7, 9, 14, 18, 19, 20, 26, 38 e 41 têm apoio direto em fonte externa em português ou em medição publicada. Os demais vêm da lista original em inglês ou da adaptação, e valem como heurística, não como prova.

Nenhum padrão isolado prova nada. O sinal é o acúmulo. A lista do parágrafo 7 não é uma proibição de palavras: "crucial" existe no português de gente, e uma ocorrência não denuncia nada.

## Histórico de versões

- **1.3.0** — A skill passou a valer também para escrever do zero, não só para reescrever. A descrição ganhou os gatilhos de escrita nova (post, artigo, e-mail, README) e o arquivo ganhou a seção "Escrevendo do zero", com a ordem de escrever direto, passar a lista antes de entregar e nunca dizer que conferiu sem ter conferido.
- **1.2.0** — O texto que chega já com marca forte de gente passa a valer como amostra do estilo do autor, então os padrões 14 e 33 deixam de valer como regra ali. Contração ("pra", "tá", "né") entrou na lista de marcas humanas a preservar em registro informal. O padrão 25 passou a cobrir a conclusão que só repete o texto. Mais conectivos vigiados no padrão 26.

- **1.1.0** — Cinco padrões novos, do 38 ao 42: pontuação importada do inglês, simetria excessiva, ausência de cena, fonte inventada e advérbio em -mente sem função. O padrão 7 ganhou aviso de que a lista não é proibição de vocabulário. A lista de falso positivo ganhou a vírgula correta e o alerta sobre detectores automáticos. Cada padrão passou a declarar se tem apoio em fonte externa ou se é heurística.
- **1.0.0** — Primeira versão em português do Brasil, com 37 padrões. Exceção do travessão de diálogo, regra de título em português, conectivo empilhado no lugar do padrão de hífen do original, e dois padrões próprios da língua: cheiro de tradução do inglês e formalidade de ofício.
## O que mudou em relação ao original em inglês

- Todos os exemplos foram reescritos em português, com as expressões que a IA realmente usa em português, não com tradução das expressões em inglês.
- O parágrafo 14 ganhou a exceção do travessão de diálogo, que é norma da língua.
- O parágrafo 17 passou a explicar a regra de título em português: maiúscula só na primeira palavra e nos nomes próprios.
- O parágrafo 26 do original tratava do excesso de pares com hífen, um vício que só existe em inglês. No lugar entrou o conectivo empilhado no começo de cada parágrafo.
- Entraram dois padrões novos: 36, cheiro de tradução do inglês, e 37, formalidade de ofício e gerundismo.
- A lista de falso positivo ganhou o registro jurídico e acadêmico, o regionalismo, a vírgula correta e o aviso sobre detectores automáticos, para não achatar tudo num português neutro de manual.
- Na revisão 1.1 entraram cinco padrões novos (38 a 42), depois de checar a lista contra fontes em português.

## Fontes

- [blader/humanizer](https://github.com/blader/humanizer), skill original em inglês.
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), origem da lista de padrões.
- [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup), que mantém a página.
- Marcelo Sabbatini, ["Texto chocho: como identificar a escrita da IA?"](https://iaedpraxis101.substack.com/p/texto-chocho-como-identificar-a-escrita).
- Pew Research Center, ["How Much of the Internet Is Written With AI?"](https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/), agosto de 2026 (amostra só em inglês).
- [Inteligência artificial na Wikimedia](https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial_na_Wikimedia), Wikipédia em português.

## Licença

MIT. Veja [LICENSE](LICENSE).
