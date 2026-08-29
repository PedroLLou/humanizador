---
name: humanizador
description: |
  Escreve e reescreve texto em português do Brasil sem os vícios de IA. Use ao
  reescrever, sempre que o usuário pedir para "humanizar", "tirar a cara de IA",
  "deixar mais natural" ou revisar algo que soe artificial. Use também ao
  ESCREVER DO ZERO qualquer texto em português que uma pessoa vai publicar ou
  assinar como dela: post de rede social, artigo, legenda, e-mail, proposta,
  release, README, documentação, roteiro, bio, descrição de produto. Cobre 42
  padrões, entre eles travessão de aparte, "não é X, é Y", conectivo empilhado,
  elogio inflado, fonte vaga, gerúndio raso, trio forçado, palavra batida de IA,
  enrolação e sobra de chatbot. Preserva todas as afirmações do texto original e
  não inventa detalhe.
license: MIT
metadata:
  version: "1.3.0"
  base: blader/humanizer 2.11.2
---

# Humanizador: tirar os padrões de escrita de IA

Reescreva o texto para soar como quem escreveu, não como um chatbot. Não mude o que o texto diz nem invente detalhe.

São 42 padrões, agrupados por tipo. Nenhum deles prova nada sozinho: o sinal é o acúmulo, não a ocorrência isolada. Os créditos das fontes estão no fim do arquivo.

## O que fazer

Quando receber um texto para humanizar:

1. **Ache os padrões de IA.** Passe o texto pela lista abaixo.
2. **Preserve todas as afirmações.** Você pode encurtar o que é chato, ampliar o que é útil, juntar ou separar parágrafos. A informação tem que continuar lá mesmo quando a estrutura mudar.
3. **Não invente fato.** Não acrescente fato, nome, número, data, citação ou fonte que não venha do texto original ou do usuário. Se faltar um detalhe para a frase funcionar, pergunte ou escreva uma frase mais simples. Você pode acrescentar opinião ou reação quando a voz do autor pedir, mas nunca uma afirmação factual. Ficção é exceção, porque inventar faz parte do trabalho.
4. **Acerte o tom.** Use o registro certo: formal, informal ou técnico. Só coloque personalidade quando o texto e o autor pedirem.

O tipo de entrada define o que você devolve. Veja [Como devolver o resultado](#como-devolver-o-resultado). O processo de reescrita é o mesmo em todos os modos.

## Escrevendo do zero

Quando o texto ainda não existe, a lista vale como filtro de saída, não como conserto.

1. **Escreva direto**, com a informação que você tem. Não fique tentando desviar dos 42 padrões enquanto escreve. Isso trava a frase e produz texto sem graça, que é o problema que a skill existe para resolver.
2. **Passe a lista antes de entregar.** Cinco padrões respondem pela maioria dos escorregões em texto novo: travessão de aparte (§14), "não é X, é Y" (§9), conectivo abrindo parágrafo (§26), trio forçado (§10) e final otimista (§25). Comece por esses cinco e depois varra o resto.
3. **Entregue só o texto.** No modo de escrita não mostre rascunho nem lista de padrões: o usuário pediu um texto, não um relatório de revisão.

A regra de não inventar continua valendo e aqui pesa mais. Escrevendo do zero é fácil tapar buraco com número plausível, data aproximada ou fonte que soa certa. Use só o que o usuário deu ou o que você verificou de fato. Se faltar dado para a frase funcionar, escreva a frase mais simples e diga ao usuário o que falta.

Não anuncie que passou pela lista. E nunca afirme que conferiu um texto sem ter conferido: dizer "passei pelos padrões" sem ter passado é pior que o vício que ficou.

## Imitar a voz de quem escreve

Se o usuário mandar uma amostra da escrita dele, analise antes de reescrever:

1. Leia a amostra primeiro. Repare no tamanho das frases, na escolha de palavras, em como os parágrafos começam, na pontuação, nas frases repetidas e nas transições.
2. Copie esses hábitos. Não troque palavra informal por formal nem apague manias propositais.
3. Sem amostra, siga as regras de estilo deste documento.

A amostra manda mais que as regras daqui. Se a amostra usa travessão, mantenha na mesma frequência. Não aplique o §14 como proibição.

**O próprio texto pode ser a amostra.** Quando o texto que chegou já traz marca forte de gente (regionalismo, opinião assumida, primeira pessoa, detalhe concreto que só quem viveu sabe, humor, autocorreção), ele não é saída de chatbot: é escrita de alguém que quer uma revisão. Trate esse texto como a amostra de estilo do autor. Nesse caso o §14 e o §33 não valem como regra: o travessão de aparte e um "olha" no começo do parágrafo fazem parte da voz dele. Aponte o que achar e deixe a escolha com o autor, em vez de corrigir por conta.

## Personalidade só quando cabe

Tirar os padrões de IA é metade do trabalho. O resultado ainda precisa soar como gente.

Use personalidade em post de blog, ensaio, opinião e texto pessoal, quando combinar com o autor. Mantenha neutro o texto de referência, técnico, jurídico e factual. Não coloque opinião nem primeira pessoa onde não cabe.

Quando personalidade couber, preserve as opiniões, as dúvidas, os sentimentos mistos, o humor, os comentários de canto de boca e o ritmo irregular do autor. Nunca invente fato para o texto parecer mais pessoal.

## Padrões de conteúdo

### 1. Importância e legado inflados

**Palavras de alerta:** marca um momento decisivo, é um verdadeiro testemunho de, desempenha um papel crucial/fundamental/central, consolida-se como, reforça sua importância, reflete uma tendência mais ampla, simbolizando seu legado duradouro, deixou uma marca indelével, preparou o terreno para, ponto de virada, cenário em constante evolução, raízes profundas, divisor de águas
**Problema:** o texto de IA transforma detalhe comum em marco histórico, prova de legado ou reflexo de uma grande tendência.
**Antes:**
> O Instituto de Estatística da Catalunha foi oficialmente criado em 1989, marcando um momento decisivo na evolução da estatística regional na Espanha. A iniciativa fez parte de um movimento mais amplo de descentralização administrativa e fortalecimento da governança regional.
**Depois:**
> O Instituto de Estatística da Catalunha foi criado em 1989, dentro de um processo mais amplo de descentralização administrativa na Espanha.

### 2. Citar nome famoso para provar importância

**Palavras de alerta:** ampla cobertura na mídia, veículos de imprensa nacionais, referência no setor, presença ativa nas redes sociais, escrito por um dos maiores especialistas
**Problema:** o texto lista veículos conhecidos ou número de seguidores para provar que a pessoa importa. A lista quase nunca dá contexto útil.
**Antes:**
> Suas análises já foram citadas na Folha, no G1, no Estadão e na BBC. Ela mantém uma presença ativa nas redes sociais, com mais de 500 mil seguidores.
**Depois:**
> Suas análises já foram citadas na Folha e na BBC.

Se a fonte explica o que a pessoa disse e onde, mantenha essa citação. Não invente contexto para encurtar.

### 3. Análise rasa com gerúndio

**Palavras de alerta:** destacando, evidenciando, ressaltando, reforçando, garantindo, refletindo, simbolizando, promovendo, contribuindo para, consolidando, proporcionando, abrangendo
**Problema:** o texto gruda um gerúndio no fim da frase para um fato simples parecer profundo.
**Antes:**
> A paleta de azul, verde e dourado do templo dialoga com a beleza natural da região, simbolizando o cerrado e o rio, refletindo a profunda conexão da comunidade com a terra.
**Depois:**
> O templo é pintado de azul, verde e dourado, cores escolhidas para lembrar o cerrado e o rio.

### 4. Linguagem de folheto de turismo

**Palavras de alerta:** conta com, vibrante, rica história, encravada, aninhada, no coração de, às margens de, imperdível, deslumbrante, de tirar o fôlego, beleza natural exuberante, compromisso com a excelência, referência absoluta, revolucionário (figurado), renomado
**Problema:** o texto vira anúncio, principalmente ao descrever lugar, cultura, produto ou empresa.
**Antes:**
> Encravada na deslumbrante região serrana do estado, Nova Aurora se destaca como uma cidade vibrante, de rica herança cultural e beleza natural de tirar o fôlego.
**Depois:**
> Nova Aurora é uma cidade na região serrana do estado.

### 5. Fontes vagas

**Palavras de alerta:** especialistas afirmam, estudos apontam, pesquisas indicam, relatórios do setor mostram, analistas destacam, observadores apontam, muitos críticos argumentam, diversas publicações
**Problema:** o texto atribui a afirmação a especialistas, críticos, estudos ou relatórios sem nome.
**Antes:**
> Por suas características únicas, o rio Haolai desperta o interesse de pesquisadores e ambientalistas. Especialistas acreditam que ele desempenha um papel crucial no ecossistema regional.
**Depois:**
> Pesquisadores e ambientalistas estudam o rio Haolai por suas características incomuns.

Cite a fonte real quando o texto original tiver uma. Se não tiver, corte a afirmação. Nunca invente fonte.

### 6. Seção formulaica de "desafios e perspectivas"

**Palavras de alerta:** apesar dos desafios, enfrenta desafios típicos, Desafios e perspectivas, O futuro reserva, segue crescendo, continua prosperando
**Problema:** artigos de IA colam no fim uma seção sobre desafios, futuro ou crescimento contínuo. Essa seção costuma repetir vaguidão em vez de trazer fato.
**Antes:**
> Apesar da prosperidade industrial, Korattur enfrenta desafios típicos das áreas urbanas, como congestionamento e falta de água. Apesar desses desafios, com sua localização estratégica e as iniciativas em andamento, Korattur segue prosperando como parte integrante do crescimento de Chennai.
**Depois:**
> Korattur tem congestionamento recorrente e falta de água.

Só acrescente data ou ação concreta se vier do texto original ou do usuário.

## Padrões de linguagem e gramática

### 7. Palavras que a IA usa demais em português

**Alta frequência:** crucial, fundamental, essencial, imprescindível, primordial, robusto, vibrante, cenário, panorama, paisagem (abstrato), tapeçaria, testemunho, ressaltar, destacar, evidenciar, sublinhar, aprimorar, fomentar, alavancar, potencializar, impulsionar, sinergia, holístico, mergulhar, intrincado, nuances, jornada, entrelaçar, ademais, outrossim, notadamente, "vale ressaltar", "é importante notar", "em resumo", "não à toa", "de forma eficaz", "ganhar destaque"
**Adjetivos genéricos:** dinâmico, inovador, eficiente, transformador, envolvente, fascinante, disruptivo, poderoso, meticuloso, moderno, completo, único
**Problema:** essas palavras aparecem em texto de IA muito mais do que na escrita de gente, principalmente em blocos. "Crucial" e "mergulhar" são os dois casos mais citados em português. "Mergulhar" é a tradução direta de *delve*, o marcador clássico do inglês.

**Cuidado:** esta lista não é uma proibição. Todas essas palavras existem no português de gente. O sinal é o acúmulo, não a ocorrência. Um "crucial" em três mil palavras não é nada; três "crucial", dois "cenário" e um "testemunho" no mesmo texto já são. Troque só o que não está sustentando peso.
**Antes:**
> Além disso, um traço marcante da culinária somali é a incorporação da carne de camelo. Um verdadeiro testemunho da influência colonial italiana é a ampla adoção da massa no cenário gastronômico local, evidenciando como esses pratos se integraram à dieta tradicional.
**Depois:**
> A culinária somali também usa carne de camelo. A massa, trazida pela colonização italiana, continua comum, principalmente no sul.

### 8. Fugir de "é", "tem" e "fica"

**Palavras de alerta:** configura-se como, apresenta-se como, consolida-se como, figura como, atua como, se destaca como, conta com, dispõe de, possui, ostenta, abriga
**Problema:** o texto troca verbos simples por perífrase comprida.
**Antes:**
> A Galeria 825 configura-se como o espaço expositivo da LAAA para arte contemporânea. O local conta com quatro ambientes e ostenta mais de 280 metros quadrados.
**Depois:**
> A Galeria 825 é o espaço de exposições da LAAA para arte contemporânea. Tem quatro salas, somando 280 metros quadrados.

### 9. "Não apenas X, mas Y" e final cortado

**Problema:** o texto abusa de "não apenas... mas também", "não é só X, é Y" e "mais do que X, é Y". Também corta o fim da frase em vez de escrever a oração inteira.
**Antes:**
> Não é apenas a batida que sustenta o vocal; é parte da agressividade e da atmosfera. Não se trata só de uma música, trata-se de um manifesto.
**Depois:**
> A batida pesada reforça o tom agressivo da música.
**Antes (final cortado):**
> As opções vêm do item selecionado, sem achismo.
**Depois:**
> As opções vêm do item selecionado, então o usuário não precisa adivinhar.

### 10. Trios forçados

**Problema:** o texto força as ideias em grupos de três para soar completo.
**Antes:**
> O evento conta com palestras, painéis e oportunidades de networking. Os participantes podem esperar inovação, inspiração e insights do setor.
**Depois:**
> O evento tem palestras e painéis. Também sobra tempo para conversar entre uma sessão e outra.

### 11. Trocar o nome do mesmo sujeito e repetir o começo da frase

**Problema:** o texto resolve repetição por regra, não de ouvido. Ele fica rebatizando a mesma coisa ("a empresa", "a companhia", "a organização", "a marca") ou começa várias frases seguidas com o mesmo sujeito.

Use um nome só para o mesmo sujeito. Para aberturas repetidas, junte as frases, mude o sujeito ou comece pela ação.
**Antes (troca de sinônimos):**
> A empresa cresceu 30% no ano. A companhia abriu duas filiais. A organização hoje emprega 400 pessoas. A marca planeja entrar no Nordeste.
**Depois:**
> A empresa cresceu 30% no ano, abriu duas filiais e hoje emprega 400 pessoas. O próximo passo é entrar no Nordeste.
**Antes (aberturas repetidas):**
> Ela reparou na porta. Ela reparou na fechadura. Ela guardou os dois detalhes.
**Depois:**
> Ela reparou na porta e na fechadura, e guardou os dois detalhes.

**Antes (mesma ideia com sinônimos):**
> A IA transforma empresas, altera negócios e modifica processos.
**Depois:**
> A IA muda a dinâmica do mercado ao transformar as empresas.

Não proíba a palavra repetida. Conserte o padrão de frase. A frase que sobrar ainda pode começar com "Ela".

### 12. Falsa escala "de X a Y"

**Problema:** o texto usa "de X a Y" ou "desde X até Y" quando X e Y não formam escala nenhuma.
**Antes:**
> Nossa jornada pelo universo nos levou da singularidade do Big Bang à grande teia cósmica, do nascimento das estrelas à dança enigmática da matéria escura.
**Depois:**
> O livro trata do Big Bang, da formação das estrelas e das teorias atuais sobre matéria escura.

### 13. Voz passiva e sujeito sumido

**Palavras de alerta:** foi realizado, é possível observar, pode-se afirmar, observa-se que, faz-se necessário, não é necessário
**Problema:** o texto esconde quem age ou apaga o sujeito. Use voz ativa quando isso deixar claro quem faz o quê.
**Antes:**
> Não é necessário arquivo de configuração. Os resultados são preservados automaticamente.
**Depois:**
> Você não precisa de arquivo de configuração. O sistema guarda os resultados sozinho.

## Padrões de estilo

### 14. Travessão e meia-risca

**Regra:** a versão final não pode ter travessão (—) nem meia-risca (–) como aparte no meio da frase, a menos que a amostra do autor use. Troque por ponto, vírgula, dois-pontos ou parênteses, ou reescreva a frase. Cheque também travessão com espaço (` — `) e hífen duplo (` -- `) usado como travessão.

**Exceção do português:** travessão de fala em diálogo de ficção fica. Isso é norma da língua, não vício de IA.

**Antes:**
> O termo é promovido principalmente por instituições holandesas — não pelas próprias pessoas. Ninguém escreve "Holanda, Europa" como endereço — e ainda assim o erro continua — até em documentos oficiais.
**Depois:**
> O termo é promovido principalmente por instituições holandesas, não pelas próprias pessoas. Ninguém escreve "Holanda, Europa" como endereço, e ainda assim o erro continua, até em documentos oficiais.

Antes de devolver a reescrita, procure por `—` e `–`. Tire cada um, menos os de diálogo e menos se a amostra do autor usar. Nesse caso, mantenha a mesma frequência da amostra.

### 15. Negrito demais

**Problema:** o chatbot põe negrito em palavra e expressão sem motivo claro.
**Antes:**
> Ele combina **OKRs (Objectives and Key Results)**, **KPIs (indicadores-chave de desempenho)** e ferramentas visuais como o **Business Model Canvas (BMC)** e o **Balanced Scorecard (BSC)**.
**Depois:**
> Ele combina OKRs, KPIs e ferramentas visuais como o Business Model Canvas e o Balanced Scorecard.

### 16. Lista com mini-título em negrito

**Problema:** o texto vira lista vertical em que todo item começa com rótulo em negrito e dois-pontos.
**Antes:**
> - **Experiência do usuário:** a experiência do usuário melhorou muito com a nova interface.
> - **Desempenho:** o desempenho foi aprimorado com algoritmos otimizados.
> - **Segurança:** a segurança foi reforçada com criptografia ponta a ponta.
**Depois:**
> A atualização melhora a interface, acelera o carregamento com algoritmos otimizados e adiciona criptografia ponta a ponta.

### 17. Maiúscula em toda palavra do título

**Problema:** o chatbot importa o título em caixa-alta do inglês. Em português, título leva maiúscula só na primeira palavra e nos nomes próprios.
**Antes:**
> ## Estratégias De Negociação E Parcerias Globais
**Depois:**
> ## Estratégias de negociação e parcerias globais

O mesmo vale dentro da frase: substantivo comum não leva maiúscula em português. "A Inteligência Artificial no Marketing Digital transformou o Setor" vira "a inteligência artificial no marketing digital transformou o setor".

### 18. Emojis

**Problema:** o chatbot enfeita título e item de lista com emoji.
**Antes:**
> 🚀 **Fase de lançamento:** o produto entra no ar no terceiro trimestre
> 💡 **Insight principal:** o usuário prefere simplicidade
> ✅ **Próximos passos:** marcar reunião de acompanhamento
**Depois:**
> O produto entra no ar no terceiro trimestre. A pesquisa mostrou que o usuário prefere simplicidade. Próximo passo: marcar a reunião de acompanhamento.

### 19. Aspas curvas

**Problema:** o texto de IA usa aspas curvas (“...”) onde o autor ou o formato de destino usa aspas retas ("...").
**Antes:**
> Ele disse que “o projeto está no prazo”, mas outros discordaram.
**Depois:**
> Ele disse que "o projeto está no prazo", mas outros discordaram.

## Padrões de chatbot

### 20. Sobra de chatbot no texto

**Palavras de alerta:** Claro!, Com certeza!, Espero ter ajudado!, Fico à disposição, Qualquer dúvida é só chamar, Segue abaixo, Você está absolutamente certo!, Quer que eu detalhe?, Quer que eu continue?, Posso trazer exemplos?
**Problema:** a saudação, a oferta ou a despedida do chatbot fica dentro de um texto que deveria andar sozinho.
**Antes:**
> Claro! Segue abaixo um panorama da Revolução Francesa. Espero ter ajudado! Qualquer dúvida, é só chamar.
**Depois:**
> A Revolução Francesa começou em 1789, quando a crise financeira e a falta de alimentos levaram a uma revolta generalizada.

### 21. Aviso de limite de conhecimento e chute

**Palavras de alerta:** até a minha última atualização, com base nas informações disponíveis, embora os detalhes sejam escassos, não há informações públicas, mantém uma vida discreta, prefere não se expor, provavelmente estudou/nasceu/começou, acredita-se que
**Problema:** o modelo avisa que não achou fonte e depois preenche o buraco com um chute plausível. Diga o que a fonte não mostra ou corte a frase. Nunca apresente chute como fato.
**Antes (aviso de corte):**
> Embora os detalhes sobre a fundação da empresa não estejam amplamente documentados nas fontes disponíveis, ela parece ter sido criada em algum momento dos anos 1990.
**Depois:**
> A data de fundação da empresa não aparece nas fontes disponíveis. (Ou corte a frase. Só escreva uma data se alguma fonte trouxer.)
**Antes (chute para tapar buraco):**
> Não há informações públicas sobre sua infância, o que sugere que ela mantém uma vida discreta. Provavelmente cresceu em uma família de classe média, o que moldou seu interesse por educação.
**Depois:**
> A infância dela não aparece nas fontes disponíveis. (Ou corte a seção.)

### 22. Tom bajulador

**Problema:** o assistente elogia o usuário ou concorda antes de responder.
**Antes:**
> Ótima pergunta! Você está absolutamente certo, esse é um tema complexo. Excelente ponto sobre os fatores econômicos.
**Depois:**
> Os fatores econômicos que você citou pesam aqui.

## Enrolação e ressalvas

### 23. Frases de enchimento

**Antes → Depois:**
- "com o intuito de alcançar esse objetivo" → "para alcançar isso"
- "devido ao fato de que estava chovendo" → "porque estava chovendo"
- "no presente momento" → "agora"
- "na eventualidade de você precisar de ajuda" → "se você precisar de ajuda"
- "o sistema tem a capacidade de processar" → "o sistema processa"
- "é importante ressaltar que os dados mostram" → "os dados mostram"
- "faz-se necessário revisar" → "é preciso revisar"
- "no que diz respeito ao prazo" → "sobre o prazo"
- "em virtude da chuva" → "por causa da chuva"

### 24. Ressalva em cima de ressalva

**Palavras de alerta:** é possível que, pode ser que, talvez, eventualmente, em alguns casos, de certa forma, ao menos em tese, para ser justo
**Problema:** revisão em cima de revisão empilha ressalva até toda afirmação virar dúvida. Guarde a ressalva só quando a fonte sustentar e o sentido precisar. Tire a ressalva que só conserta um exagero anterior.
**Antes:**
> Pode-se argumentar que a política talvez tenha, em alguns casos, algum possível efeito sobre os resultados.
**Depois:**
> A política pode afetar os resultados.

### 25. Final genérico e otimista

**Problema:** o texto termina em otimismo vago em vez do último fato útil.
**Antes:**
> O futuro é promissor para a empresa. Tempos empolgantes estão por vir nessa jornada rumo à excelência. Este é um passo importante na direção certa.
**Depois:**
> (Corte o parágrafo. Termine no último dado concreto. Se a fonte trouxer planos reais, use os planos.)

O outro fecho formulaico é a conclusão que só repete o que o texto já disse, com "concluindo", "em suma" ou "diante do exposto" na frente. Corte também. Uma conclusão vale quando tira do texto algo que ainda não estava dito.
**Antes:**
> Concluindo, vimos que a política afeta os resultados, que o custo caiu e que a equipe ganhou previsibilidade.
**Depois:**
> (Corte. Quem leu o texto acabou de ler isso.)

### 26. Conectivo empilhado no começo de cada parágrafo

**Palavras de alerta:** Além disso, Ademais, Outrossim, Dessa forma, Nesse sentido, Diante disso, Diante do exposto, À luz do exposto, Por conseguinte, Cabe destacar, Por fim, Em suma, Portanto, Vale lembrar
**Problema:** o texto de IA em português abre quase todo parágrafo e quase toda frase com conectivo. Isso cria um ritmo de redação de vestibular. Um conectivo aqui e ali é normal; três ou quatro seguidos denunciam a máquina. Junte as frases ou comece pela informação.
**Antes:**
> Além disso, a equipe reduziu o tempo de resposta. Ademais, o custo caiu 12%. Dessa forma, o time ganhou previsibilidade. Por fim, vale ressaltar que o churn diminuiu.
**Depois:**
> A equipe reduziu o tempo de resposta e o custo caiu 12%. O time ganhou previsibilidade e o churn diminuiu.

### 27. Fingir revelar uma verdade profunda

**Palavras de alerta:** a verdadeira questão é, no fundo, na real, em sua essência, o que realmente importa, fundamentalmente, o cerne da questão
**Problema:** essas expressões fazem um ponto comum parecer uma revelação.
**Antes:**
> A verdadeira questão é se os times conseguem se adaptar. No fundo, o que realmente importa é a maturidade da organização.
**Depois:**
> A questão é se os times conseguem se adaptar. Isso depende de a empresa estar disposta a mudar seus hábitos.

### 28. Anunciar o que vem a seguir

**Palavras de alerta:** vamos mergulhar, bora entender, vamos por partes, é o seguinte, sem mais delongas, antes de mais nada, aqui está o que você precisa saber, um aviso rápido, só pra constar
**Problema:** o texto anuncia o próximo ponto em vez de dizer o ponto. Uma frase informal como "uma coisa que me pegou de jeito" tem o mesmo problema. Tire o anúncio, não só o tom formal dele.
**Antes:**
> Vamos mergulhar em como funciona o cache no Next.js. É o seguinte:
**Depois:**
> O Next.js faz cache em várias camadas: memoização de requisição, cache de dados e cache de rotas.
**Antes (registro informal):**
> Uma coisa que me pegou de jeito, e presta atenção nessa parte: o servidor de desenvolvimento do webpack não manda o cabeçalho de CORS por padrão.
**Depois:**
> O servidor de desenvolvimento do webpack não manda o cabeçalho de CORS por padrão.

### 29. Título repetido na primeira frase

**Sinal:** um título seguido de um parágrafo de uma linha que só repete o título antes do conteúdo começar.
**Problema:** o texto de IA repete o título logo abaixo dele. Corte a frase repetida.
**Antes:**
> ## Desempenho
>
> Velocidade importa.
>
> Quando a página demora, o usuário sai.
**Depois:**
> ## Desempenho
>
> Quando a página demora, o usuário sai.

### 30. Escrever sobre a versão antiga

**Problema:** documentação e comentário devem descrever o comportamento atual. Só fale da versão anterior em changelog, nota de versão, guia de migração e outros documentos sobre mudança.
**Antes:**
> Esta função foi criada para substituir a abordagem anterior, que percorria todos os itens e custava O(n²).
**Depois:**
> Esta função usa um hash map para busca em O(1).

### 31. Frase de efeito e fragmento dramático

**Problema:** o texto de IA transforma cada frase em fecho de comercial. Uma frase curta dá ênfase. Uma sequência de fragmentos soa forçada.
**Antes:**
> Aí o AlphaEvolve chegou. Sem preferência por simetria. Sem viés estético. Sem nostalgia. As regras antigas acabaram.
**Depois:**
> O AlphaEvolve mudou a busca porque não favorece simetria nem soluções com cara humana. Isso tornou parte das premissas antigas menos útil.

### 32. Máxima de camiseta

**Palavras de alerta:** X é o Y de Z, X vira uma armadilha, X não é ferramenta, é espelho, a linguagem da, a moeda da, a arquitetura da
**Problema:** o texto vira uma afirmação comum em frase de efeito que parece profunda e não acrescenta detalhe. Troque a frase de efeito pela afirmação específica.
**Antes:**
> Simetria é a linguagem da confiança. Eficiência vira armadilha quando o time esquece a camada humana.
**Depois:**
> Layout simétrico costuma parecer mais previsível para o usuário. Times podem otimizar demais o fluxo e perder de vista como as pessoas usam o produto.

### 33. Falsa sinceridade na abertura

**Expressões de alerta:** Sinceramente?, Olha, É o seguinte, Vou ser bem honesto, A real é que, Verdade seja dita, Cá entre nós, usadas como gancho solto ou pausa antes de um ponto banal.
**Problema:** o texto encena uma pausa ou declara honestidade antes de dizer algo trivial. Diga o ponto direto.
**Antes:**
> Vale o preço? Sinceramente? Depende de quanto você vai usar.
**Depois:**
> Vale o preço se você for usar com frequência.

### 34. Responder objeção que ninguém fez

**Expressões de alerta:** não se trata (principalmente) de, não estou dizendo que, só para deixar claro, não me entenda mal, isso não quer dizer que, alguém pode argumentar que... mas, dá para enquadrar de outro jeito, mas
**Problema:** o texto responde a uma objeção que não existe no texto. Desconfie de uma frase sem dono explicando o que o autor não quis dizer, principalmente quando o assunto não aparece em nenhum outro lugar. Uma afirmação direta como "a API não é thread-safe" não é esse padrão.
**Antes:**
> Não se trata principalmente do tamanho do prompt, e não estou dizendo que documentação não importa. Dá para enquadrar o problema de outro jeito, mas a questão é se o agente consegue usar a instrução na hora de agir.
**Depois:**
> A questão é se o agente consegue usar a instrução na hora de agir.

Tire só a defesa sem base. Se houver uma afirmação real dentro dela, diga essa afirmação direto. Mantenha a objeção quando o texto nomear quem a fez ou responder por inteiro.

### 35. Rejeitar alternativa falsa

**Expressões de alerta:** uma opção tentadora seria, poderíamos pensar em, uma abordagem óbvia seria, você pode achar que... mas, seria fácil apenas, alguns sugeririam
**Problema:** o texto apresenta uma opção que ninguém consideraria, rejeita em meia frase e nunca mais toca no assunto. Em geral é resto de rascunho. Tire a opção falsa e diga a restrição real.
**Antes:**
> Os tokens de sessão são rotacionados a cada 24 horas. Uma opção tentadora seria rotacionar reiniciando o serviço de autenticação por cron, mas isso derrubaria todas as sessões ativas. A rotação acontece em memória e os clientes renovam sozinhos.
**Depois:**
> Os tokens de sessão são rotacionados a cada 24 horas, em memória, e os clientes renovam sozinhos.

Uma alternativa rejeitada pode ser legítima. Várias rejeições curtas e desconexas são sinal mais forte. Pergunte que informação nova cada frase traz. Se ela só registra uma edição antiga, reescreva o parágrafo em volta do ponto principal.

## Padrões específicos do português

### 36. Cheiro de tradução do inglês

**Sinais:** pronome sujeito repetido onde o português dispensa ("eu acho que eu vou"), possessivo desnecessário ("lave as suas mãos"), "nós" explícito em todo parágrafo, expressões traduzidas ao pé da letra: no final do dia, entregar valor, acionável, mudança de jogo, deixe-me explicar, vamos destrinchar isso, isso faz sentido (em excesso), no longo prazo, dar um passo atrás, "espero que esta mensagem o encontre bem"
**Problema:** o modelo pensa em inglês e traduz. A gramática fica certa e o texto soa estrangeiro. Corte pronome que o português esconde no verbo e troque a expressão traduzida pela equivalente de verdade.
**Antes:**
> No final do dia, nós precisamos entregar valor acionável. Deixe-me explicar por que isso é uma mudança de jogo para o seu negócio.
**Depois:**
> Precisamos entregar algo que o time consiga usar. Explico por que isso muda a operação.

### 37. Formalidade de ofício e gerundismo

**Expressões de alerta:** venho por meio desta, prezado(a) usuário(a), conforme supracitado, o mesmo / a mesma como pronome, no aguardo de vosso retorno, vou estar enviando, estaremos verificando, iremos estar analisando
**Problema:** o texto de IA em português cai no registro de circular de repartição. O gerundismo aparece menos, mas quando aparece é pelo mesmo motivo: o modelo copia o registro de atendimento formal. Nenhum dos dois é como as pessoas escrevem quando querem ser entendidas.
**Antes:**
> Prezado cliente, venho por meio desta informar que o seu chamado foi recebido. Estaremos verificando o mesmo e retornaremos o mais breve possível.
**Depois:**
> Recebemos seu chamado. Vamos verificar e te responder.

### 38. Pontuação importada do inglês

**Problema:** o modelo aplica convenções da pontuação inglesa a um texto em português. Três casos concretos:

- **Vírgula antes do "e" na enumeração.** "Comprei maçãs, bananas, e laranjas." Isso é a *Oxford comma*, que não existe na norma do português. Tire a vírgula: "maçãs, bananas e laranjas".
- **Ponto final dentro das aspas.** "Ele disse que o prazo é curto." vira "Ele disse que o prazo é curto". Em português o ponto fica fora quando a citação não é uma frase inteira e independente.
- **Ponto e vírgula demais.** O modelo usa ponto e vírgula para colar frases que pediam ponto final, principalmente em texto técnico.

**Antes:**
> Os resultados são animadores; a IA oferece oportunidades; as empresas aproveitam o potencial.
**Depois:**
> Os resultados animam. A IA abre oportunidades e as empresas aproveitam.

### 39. Simetria excessiva

**Problema:** todo parágrafo tem o mesmo tamanho, toda lista tem três itens, toda frase tem a mesma estrutura. Escrita de gente é irregular: um parágrafo de duas linhas ao lado de um de oito, uma lista de dois itens ao lado de uma de cinco. Quando o texto fica métrico demais, quebre o ritmo de propósito.

**Antes:**
> A ferramenta reduz custos, acelera entregas e melhora a qualidade. A equipe ganha tempo, foco e previsibilidade. O cliente recebe respostas rápidas, claras e confiáveis.
**Depois:**
> A ferramenta corta custo e acelera a entrega. A equipe ganha previsibilidade, que era o que faltava. E o cliente para de esperar dois dias por uma resposta.

### 40. Ausência de cena e baixa materialidade

**Problema:** o texto fala em abstrato do começo ao fim. Sem nome, sem número, sem data, sem lugar, sem exemplo. Cada afirmação poderia estar em qualquer texto sobre qualquer empresa.

Este é o único padrão que se conserta acrescentando, e por isso ele depende de você ter o material. Puxe o detalhe concreto do texto original ou pergunte ao usuário. Nunca invente número, data ou nome para "dar materialidade".

**Antes:**
> A empresa cresceu bastante nos últimos anos e hoje atende clientes de diversos segmentos em todo o país.
**Depois (com dado do original):**
> A empresa cresceu de 4 para 40 clientes entre 2023 e 2026, quase todos de logística.
**Depois (sem dado nenhum):**
> A empresa cresceu nos últimos anos. (E pergunte quanto, em que período, atendendo quem.)

### 41. Fonte inventada

**Problema:** diferente do parágrafo 5, que trata de fonte vaga, aqui a fonte é específica e não existe. Referência com autor e ano que não bate, link quebrado, DOI que não resolve, ISBN inválido, número de página inventado, citação atribuída a quem nunca disse. É o sinal que a própria Wikipédia usa para eliminação rápida de artigo gerado por IA.

**O que fazer:** não conserte, não reescreva a citação com outro nome, não "melhore" a referência. Marque para o usuário verificar e tire a afirmação do texto se ela depender só daquela fonte. Se você não pode checar, diga que não pode checar.

### 42. Advérbio em -mente sem função

**Problema:** o texto enche a frase de advérbio que não muda o sentido: significativamente, extremamente, altamente, notavelmente, consideravelmente, efetivamente, essencialmente, basicamente, simplesmente, verdadeiramente.

**Antes:**
> A mudança impactou significativamente o resultado e foi extremamente bem recebida pela equipe.
**Depois:**
> A mudança melhorou o resultado e a equipe gostou.

Advérbio com função fica: "caiu 12% em março, principalmente no Sul" carrega informação.

## Cuidado com falso positivo

### O que não marcar

Gente também usa alguns desses padrões. Nenhum item abaixo é prova sozinho:

- **Gramática impecável e estilo constante.** Muita gente escreve bem ou passou por edição. Texto polido não é texto de IA.
- **Mistura de registro formal e informal.** Isso pode ser da área, da idade ou do jeito da pessoa.
- **Texto "sem graça" ou "robótico".** Texto de IA tem marcas *específicas*. Secura sem essas marcas é só escrita seca.
- **Palavra formal ou acadêmica.** O §7 lista palavras que a IA usa demais. Não simplifique toda palavra difícil.
- **Registro jurídico, acadêmico ou de norma técnica.** Impessoalidade e voz passiva são exigência do gênero. Não converta petição, laudo ou ata em post de blog.
- **Travessão de diálogo.** Em ficção é a norma da língua. O §14 vale para o travessão de aparte, não para a fala.
- **Conectivo isolado.** *Além disso*, *portanto*, *no entanto* só denunciam quando empilhados. Um "no entanto" não é nada.
- **Aspas curvas sozinhas.** Word, Google Docs e a maioria dos editores curvam por padrão. Só contam junto com outras marcas.
- **Vírgula usada corretamente.** Virou meme dizer que vírgula no vocativo ("Oi, João") é coisa de IA. É norma da língua. Pontuação correta não é sinal de nada.
- **Detector automático.** Ferramenta de detecção de IA erra muito e erra torto: penaliza mais quem é neurodivergente e quem não é falante nativo. Não use pontuação de detector como prova, nem para decidir o que reescrever aqui.
- **Uma frase curta para dar ênfase.** Só marque fragmento dramático quando vierem vários seguidos.
- **Repetição proposital de abertura.** "Cheguei. Vi. Venci." é ritmo. Só mexa quando a repetição não acrescenta nada.
- **"Olha" ou "sinceramente" no meio da frase.** São normais na fala e no texto informal. O vício é a abertura teatral solta.
- **Ressalva útil.** Mantenha delimitação de escopo, aviso legal ou de segurança, correção real, objeção com autor nomeado, resposta e item de FAQ.
- **Alternativa real.** Mantenha as opções que o leitor consideraria em documento de arquitetura, tutorial ou argumentação. Tire só a opção improvável que o texto descarta e nunca mais usa.
- **Afirmação sem fonte.** Boa parte da internet não cita fonte. Falta de citação não prova nada.
- **Formatação complexa e correta.** Editor visual e template produzem saída limpa sem IA nenhuma.
- **Texto de segunda mão.** Não reescreva expressão de alerta que aparece dentro de citação, título, nome próprio ou exemplo em que a expressão está sendo discutida, não usada.

Na dúvida, procure vários padrões juntos. Um travessão não prova nada. Vários vícios no mesmo parágrafo já são indício forte.

### Marcas humanas para preservar

Esses detalhes costumam carregar a voz de quem escreve. Preserve, a menos que atrapalhem o sentido:

- **Detalhe específico e estranho.** Um endereço real, uma citação torta, uma frase como "o advogado que trabalhava em cima do meu dentista".
- **Sentimento misto e tensão sem resolução.** "Acho que no geral é bom, mas me incomoda, e não sei explicar direito por quê."
- **Gíria e referência datada.** Meme, gíria e piada interna presas a um ano e a um grupo. Modelo atrasa um ano ou mais nisso.
- **Contração e fala escrita.** "pra", "tá", "cê", "né", "tô", "pro". Texto de IA quase nunca escreve assim, e por isso a tentação é "consertar" para "para", "está", "você". Em registro informal, não expanda: a forma contraída é a escolha do autor. Em texto formal, aí sim a forma plena é a certa.
- **Regionalismo.** "uai", "oxe", "tchê", "massa", "mano". Não padronize para um português neutro de manual.
- **Escolha consciente em primeira pessoa.** Mantenha o corte ou a palavra que o autor sabe justificar.
- **Variação no tamanho das frases.** Escrita de gente alterna curto e longo. Texto de IA tende a um comprimento médio constante.
- **Aparte, parêntese e autocorreção.** "(Fico querendo escrever 'quase' aqui, mas foi certeza mesmo.)" Modelo raramente se interrompe assim.
- **Texto anterior a 30 de novembro de 2022.** Lançamento público do ChatGPT. O que é mais antigo que isso quase nunca é de IA.

---

## Como devolver o resultado

**Texto colado (padrão).** Devolva o rascunho, uma lista curta dos padrões que ainda sobraram e a versão final.

**Modo arquivo.** Quando o usuário indicar um arquivo, faça o processo inteiro mas escreva só o texto final no arquivo. Mexa apenas na prosa. Não toque em bloco de código, metadados YAML, dados e destino de link. Depois entregue um resumo curto ao usuário.

**Modo embutido.** Quando outra tarefa usar esta skill para um pull request, mensagem de commit ou documento, devolva só o texto final.

## Processo de reescrita

1. Leia o original e marque cada padrão de IA.
2. Escreva um rascunho. Leia em voz alta. Confira o ritmo, os detalhes, os verbos simples como *é* e *tem*, e o nível de formalidade.
3. Faça duas perguntas:
   - **"O que ainda soa como IA?"**
   - **"A reescrita adicionou ou perdeu algum fato, nome, número, data, citação, fonte, classificação ou afirmação?"**
   Trate qualquer acréscimo sem base ou afirmação perdida como erro.
4. Escreva a versão final. Diga cada ponto de forma natural, em vez de remendar uma expressão marcada por vez. Se uma frase continuar torta, reescreva o parágrafo em volta do ponto principal. Aplique a regra de travessão do §14.

Devolva o resultado no formato descrito em [Como devolver o resultado](#como-devolver-o-resultado).

## Fonte e adaptação

Esta skill é a versão em português do Brasil de [blader/humanizer](https://github.com/blader/humanizer) (licença MIT), que por sua vez se baseia em [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), mantido pelo WikiProject AI Cleanup.

O ponto central da Wikipédia: modelos de linguagem usam estatística para adivinhar o que vem depois, então o resultado tende ao mais provável para o maior número de casos.

Fontes usadas na adaptação para o português, além das acima:

- Marcelo Sabbatini, ["Texto chocho: como identificar a escrita da IA?"](https://iaedpraxis101.substack.com/p/texto-chocho-como-identificar-a-escrita), IAEdPraxis. Origem de "crucial" e "mergulhar" como marcadores em português, dos adjetivos genéricos, da vírgula de série e do ponto dentro das aspas.
- Pew Research Center, ["How Much of the Internet Is Written With AI?"](https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/), agosto de 2026. Mede o crescimento do travessão, da vírgula de série, do vocabulário de IA e do paralelismo negativo. **A amostra é só de páginas em inglês**, então serve como evidência do mecanismo, não do português.
- [Inteligência artificial na Wikimedia](https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial_na_Wikimedia), Wikipédia em português. Excesso de travessão, excesso de "além disso", material promocional, aspas curvas e referência inexistente.
- Marina Semensato, ["Como saber se um texto foi feito por inteligência artificial?"](https://exame.com/tecnologia/examelab/como-saber-se-um-texto-foi-feito-por-inteligencia-artificial/), Exame, julho de 2026. Excesso de conectivo, conclusão que repete o texto, tom sem opinião, trios e o "não é X, é Y".

Nível de confiança: os parágrafos 7, 9, 14, 18, 19, 20, 26, 38 e 41 têm apoio direto em fonte externa em português ou em medição publicada. Os demais vêm da lista original em inglês ou da adaptação, e valem como heurística, não como prova.

O que mudou em relação ao original em inglês:

- Todos os exemplos foram reescritos em português, com as expressões que a IA realmente usa em português, não com tradução das expressões em inglês.
- O §14 ganhou a exceção do travessão de diálogo, que é norma da língua.
- O §17 passou a explicar a regra de título em português: maiúscula só na primeira palavra e nos nomes próprios.
- O §26 do original tratava do excesso de pares com hífen, um vício que só existe em inglês. No lugar entrou o conectivo empilhado no começo de cada parágrafo, que é o vício equivalente em português.
- Entraram dois padrões novos: §36, cheiro de tradução do inglês, e §37, formalidade de ofício e gerundismo.
- A lista de falso positivo ganhou o registro jurídico e acadêmico, o regionalismo, a vírgula correta e o aviso sobre detectores automáticos.
- Na revisão 1.1 entraram cinco padrões novos, do §38 ao §42: pontuação importada do inglês, simetria excessiva, ausência de cena, fonte inventada e advérbio em -mente sem função.
