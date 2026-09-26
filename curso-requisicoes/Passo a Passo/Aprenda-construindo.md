# Aprenda a programar construindo o painel de requisições

Uma aula para escrever o projeto à mão, compreender as decisões e depois criar suas próprias funcionalidades.

**Para quem é:** quem ainda está aprendendo o que significam uma tag, uma variável e uma função. Você não precisa saber Python, instalar banco de dados ou usar um terminal para acompanhar a construção.

**O que construiremos:** a interface do protótipo de requisições: menu, apresentação, cartões de e-mail, pedidos agrupados por setor, busca, filtros, contadores e troca de tema. Os pedidos são inventados. A parte de e-mails é uma representação visual, sem conexão com uma caixa postal. Este curso acompanha o protótipo independente, não a aplicação Flask da BaseV2.

O código mostrado nos blocos de construção vem dos três arquivos do projeto. O CSS ganhou quebras de linha para ficar legível na aula; as regras são as mesmas. Os arquivos do projeto original não foram alterados. Alguns exemplos menores são exercícios de laboratório e estão identificados como tal.

## Aula 0 — Seu primeiro resultado, antes do painel

Crie uma pasta chamada `meu-painel`. Abra essa pasta em um editor de texto para código que você já tenha. Crie `index.html`, `styles.css` e `app.js`. Confira se o Windows não acrescentou `.txt` aos nomes. Os três arquivos ficam lado a lado, na mesma pasta.

Crie também `rascunho.html`. Ele é seu laboratório: exemplos identificados como **laboratório** vão nele, sem se misturar ao painel. Escreva isto à mão:

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8">
    <title>Meu primeiro teste</title>
  </head>
  <body>
    <h1>Eu escrevi esta página</h1>
    <p>Estou aprendendo a construir meu próprio painel.</p>
  </body>
</html>
```

Salve e abra `rascunho.html` no navegador. A frase do `h1` aparece como título grande. A frase do `p` aparece como parágrafo. Troque uma palavra, salve no editor e recarregue a página. Esse ciclo — escrever, salvar, observar — será usado durante todo o curso.

`<p>` abre um elemento; `</p>` fecha esse elemento. O texto entre eles é seu conteúdo. O navegador lê as tags e constrói a página. As tags não aparecem escritas na tela porque são instruções de marcação.

Uma tag pode estar dentro de outra. Chamamos a de fora de **pai** e a de dentro de **filho**. A indentação, os espaços no começo das linhas, ajuda você a enxergar essa relação. Ela não cria a relação: são as tags de abertura e fechamento que a criam.

**Preveja:** se você escrever dois `<p>...</p>` seguidos, verá dois parágrafos. Faça o teste. Depois coloque `<strong>aprendendo</strong>` no meio de um deles. `strong` identifica um trecho importante; o navegador normalmente o mostra em negrito.

### Como estudar este material

1. Leia a explicação anterior ao bloco.
2. Digite o bloco no arquivo indicado. Não digite as três crases que delimitam os exemplos neste material.
3. Explique com suas palavras pelo menos uma linha: “isto procura o campo de busca”, por exemplo.
4. Faça a experiência proposta e compare com a conferência.
5. Antes da próxima experiência, desfaça a alteração experimental para continuar seguindo o código original.

Os blocos de construção estão na ordem exata de cada arquivo. O HTML termina na Aula 1; depois você preenche o CSS na Aula 2 e o JavaScript na Aula 3. Há blocos intermediários com estruturas ainda abertas: complete a aula correspondente antes de avaliar o arquivo inteiro. Nos pontos indicados, você pode testar partes no laboratório.

Não tente decorar todas as propriedades. Aprenda a reconhecer o problema que cada uma resolve. Ao encontrar um erro, leia primeiro a mensagem e confira o último trecho que digitou.

## Aula 1 — HTML: dar significado e estrutura à página

Antes de escrever o painel, diferencie três coisas:

```html
<div class="metric" id="meu-resumo">12 pedidos</div>
```

- `div` é o **nome da tag**. Cria um agrupamento genérico, sem dizer que ele é um menu, título ou parágrafo. Por padrão participa do layout como bloco; o CSS pode mudar isso.
- `class="metric"` é um **atributo**: uma informação adicional. A classe permite agrupar vários elementos para aplicar o mesmo estilo. `metric` é um nome escolhido por quem escreveu o projeto, não uma palavra especial do HTML.
- `id="meu-resumo"` identifica este elemento dentro da página. Use um ID único. Ele pode ser usado por links e pelo JavaScript.
- `12 pedidos` é o conteúdo. A `div` não cria os dados, não calcula o número e não ganha uma borda sozinha.
- `</div>` encerra o agrupamento. Quando há várias divisões dentro de divisões, cada fechamento precisa corresponder à abertura correta.

`span` também agrupa conteúdo, mas normalmente aparece dentro de uma linha de texto. Ele é útil para colorir uma palavra ou um ícone. `section`, `nav`, `header`, `main`, `aside` e `footer` acrescentam significado ao agrupamento. Use uma `div` quando você precisa agrupar elementos e nenhuma dessas funções semânticas descreve bem o grupo.

Classes como `hero__copy` e `metric--accent` são uma convenção de nomes: `__` indica uma parte e `--` uma variação. O navegador não atribui comportamento especial a esses sinais. `class="metric metric--accent"` aplica duas classes ao mesmo elemento.

### 1.1 — O documento e suas informações

Comece o `index.html` vazio. Aqui você informa como o navegador deve ler o documento e onde procurar aparência e comportamento.

**Digite no arquivo `index.html`.** Este trecho corresponde às linhas 1–14 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```html
<!doctype html>
<html lang="pt-BR" data-theme="dark">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="color-scheme" content="dark light">
    <meta name="description" content="Protótipo interativo de acompanhamento de requisições por setor.">
    <title>Requisições por setor · Protótipo Supersonic</title>
    <link rel="stylesheet" href="styles.css">
    <script src="app.js" defer></script>
  </head>
  <body>
    <a class="skip-link" href="#conteudo">Pular para o conteúdo</a>

```

Leia cada linha:

- `<!doctype html>` pede o modo de renderização padrão do HTML moderno. Não é uma tag de conteúdo e não tem fechamento.
- `<html>` envolve todo o documento. `lang="pt-BR"` informa o idioma. `data-theme="dark"` é um atributo criado para este projeto: inicialmente o tema é escuro.
- `<head>` reúne informações sobre a página. Não é a barra superior visível; a barra será um `header` no `body`.
- `charset="utf-8"` orienta a leitura de caracteres como `ç` e `ã`.
- `viewport` pede que a largura de referência acompanhe o dispositivo e que a escala inicial seja 1. Isso ajuda o CSS a responder a telas pequenas.
- `color-scheme` declara que a página aceita aparências escura e clara para recursos nativos. Quem pinta os cartões é o CSS.
- `description` fornece uma descrição do documento, não um parágrafo visível.
- `title` dá nome à aba do navegador. O título principal visível será um `h1`.
- `link` carrega a folha de estilos. `rel="stylesheet"` descreve sua finalidade; `href` aponta para o arquivo.
- `script` carrega `app.js`. `defer` faz esse script externo executar depois que o HTML foi analisado, permitindo encontrar os elementos da página. O arquivo JavaScript ainda vazio não faz nada.
- `</head>` termina as informações; `<body>` começa o conteúdo da página.
- O link `href="#conteudo"` aponta para um elemento com `id="conteudo"`. Mais adiante criaremos esse elemento. Ele permite pular o menu, especialmente ao navegar com o teclado.

`meta` e `link` são elementos vazios: não precisam de `</meta>` ou `</link>`. Uma linha em branco só organiza o código.

**Pare e pense / experimente:** Qual texto muda a aba do navegador e qual mudará o título grande da página?

**Conferência:** A aba usa `title`. O texto grande usa `h1`, que ainda será escrito. São lugares diferentes, mesmo que você escolha o mesmo texto para os dois.

### 1.2 — A moldura do aplicativo e o menu lateral

A tela terá duas grandes regiões: menu à esquerda e conteúdo à direita. A primeira `div` será o agrupamento que permite ao CSS organizar as duas.

**Digite no arquivo `index.html`.** Este trecho corresponde às linhas 15–33 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```html
    <div class="app-shell">
      <!-- A navegação é autônoma para o protótipo; na aplicação será substituída pelo menu compartilhado. -->
      <aside class="sidebar" id="sidebar" aria-label="Navegação do protótipo">
        <a class="brand" href="#inicio" aria-label="Supersonic — início do painel">
          <span class="brand__mark" aria-hidden="true"><span></span></span>
          <span class="brand__text"><strong>SUPERSONIC</strong><small>Compras &amp; manutenção</small></span>
        </a>
        <div class="sidebar__label">ÁREA DE TRABALHO</div>
        <nav class="main-nav" aria-label="Seções do painel">
          <a class="main-nav__link is-active" href="#inicio"><span aria-hidden="true">◫</span> Visão geral</a>
          <a class="main-nav__link" href="#emails"><span aria-hidden="true">✉</span> E-mails recebidos</a>
          <a class="main-nav__link" href="#setores"><span aria-hidden="true">▦</span> Requisições por setor</a>
        </nav>
        <div class="sidebar__note"><span class="live-dot" aria-hidden="true"></span> Protótipo com dados fictícios</div>
        <div class="sidebar__foot">Interface conceitual · sem conexão ao ERP</div>
      </aside>

      <div class="sidebar-backdrop" id="sidebar-backdrop" hidden></div>

```

A `div.app-shell` envolve o aplicativo inteiro. Ela continua aberta depois deste trecho porque ainda receberá o conteúdo principal.

O texto entre `<!--` e `-->` é um comentário. Ele ajuda quem lê o arquivo e não aparece no painel.

`aside.sidebar` contém o menu lateral. `id="sidebar"` será usado para abri-lo e fechá-lo em telas menores. `aria-label` fornece um nome acessível; não desenha um texto na tela nem implementa uma ação.

Dentro do link da marca, `brand__mark` e seu `span` vazio formam o símbolo com CSS. `brand__text` agrupa o nome em `strong` e a descrição em `small`. `&amp;` representa o caractere `&` no HTML. Os fechamentos encerram primeiro o conteúdo interno e depois o link.

Cada divisão tem uma tarefa:

| Elemento | Por que existe |
| --- | --- |
| `div.sidebar__label` | Agrupa o rótulo “ÁREA DE TRABALHO” para posicionar e estilizar esse texto. |
| `nav.main-nav` | Identifica a região com links de navegação. |
| `div.sidebar__note` | Junta o ponto decorativo e o aviso de dados fictícios. |
| `div.sidebar__foot` | Guarda a observação no fim do menu. |
| `div.sidebar-backdrop` | Será a camada escurecida atrás do menu móvel. Começa oculta. |

Os três links levam a `#inicio`, `#emails` e `#setores`, seções da mesma página. `is-active` é uma segunda classe do primeiro link, usada para destacá-lo. Os símbolos decorativos têm `aria-hidden="true"` para não acrescentar ruído na leitura assistiva.

`hidden` é um atributo booleano: sua presença pede para esconder o elemento. Escrever `hidden="false"` ainda coloca o atributo no elemento; não é a forma de mostrá-lo. O JavaScript usará a propriedade `hidden = false` para remover esse estado.

**Pare e pense / experimente:** O nome `sidebar` é uma palavra reservada? E o atributo `aria-label` abre o menu?

**Conferência:** `sidebar` é um nome escolhido pelo autor. `aria-label` só informa o nome acessível; abrir o menu exigirá comportamento em JavaScript e regras de CSS.

### 1.3 — A barra superior

Agora começa a segunda grande região, `app-main`. Dentro dela colocaremos uma barra superior e o conteúdo.

**Digite no arquivo `index.html`.** Este trecho corresponde às linhas 34–46 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```html
      <div class="app-main">
        <header class="topbar" id="inicio">
          <div class="topbar__left">
            <button class="icon-button mobile-menu" id="menu-toggle" type="button" aria-controls="sidebar" aria-expanded="false" aria-label="Abrir menu">☰</button>
            <div class="breadcrumb">Compras <span aria-hidden="true">/</span> <strong>Requisições</strong></div>
          </div>
          <div class="topbar__right">
            <span class="topbar__edition">PRÉVIA INTERATIVA</span>
            <button class="theme-button" id="theme-toggle" type="button" aria-label="Ativar tema claro">☀ <span>Tema claro</span></button>
            <span class="user-avatar" title="Equipe de compras — exemplo" aria-label="Equipe de compras">SC</span>
          </div>
        </header>

```

`div.app-main` agrupa tudo que fica ao lado do menu. `header.topbar` é o cabeçalho visível dessa região. O ID `inicio` recebe os links que apontam para o começo.

`div.topbar__left` agrupa botão de menu e caminho da página. `div.topbar__right` agrupa indicação de prévia, troca de tema e avatar. Essas duas divisões permitem distribuir os grupos pelas extremidades com CSS.

O botão de menu tem duas classes. `type="button"` deixa explícito que é um botão de ação, não de envio de formulário. `aria-controls="sidebar"` indica qual região ele controla; `aria-expanded="false"` informa que ela está recolhida. Esses atributos precisam acompanhar o comportamento real; por si só não abrem ou fecham nada.

`div.breadcrumb` apresenta “Compras / Requisições”. A barra é decorativa e o nome da seção recebe importância com `strong`. Aqui é uma indicação visual, não uma árvore de links navegáveis.

O botão `theme-toggle` contém um símbolo e um `span` com a ação disponível. O `span.user-avatar` mostra iniciais fixas de exemplo. O atributo `title` fornece uma dica que o navegador pode exibir ao passar o mouse; não representa uma conta autenticada. O `</header>` fecha a barra; `app-main` continua aberto.

**Pare e pense / experimente:** Por que o botão de menu e o botão de tema têm IDs diferentes?

**Conferência:** O JavaScript precisa localizar cada um separadamente e associar uma ação diferente a cada botão.

### 1.4 — A apresentação principal

`main` identifica o conteúdo principal. A primeira seção apresenta o propósito do painel e dois atalhos.

**Digite no arquivo `index.html`.** Este trecho corresponde às linhas 47–65 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```html
        <main class="content" id="conteudo">
          <section class="hero" aria-labelledby="page-title">
            <div class="hero__copy">
              <div class="eyebrow"><span class="live-dot" aria-hidden="true"></span> CENTRAL DE ACOMPANHAMENTO</div>
              <h1 id="page-title">Requisições em foco<span>.</span></h1>
              <p>Veja as solicitações por setor, identifique pendências recebidas por e-mail e abra cada cartão para conferir os detalhes.</p>
              <div class="hero__actions">
                <a class="primary-link" href="#setores">Explorar requisições <span aria-hidden="true">↗</span></a>
                <a class="subtle-link" href="#emails">Ver e-mails recebidos <span aria-hidden="true">→</span></a>
              </div>
            </div>
            <div class="hero__visual" aria-hidden="true">
              <div class="visual__top"><span class="window-dots">● ● ●</span><span>REQUISIÇÕES</span><span>↗</span></div>
              <div class="visual__row"><span class="visual__icon">01</span><span><strong>Operações</strong><small>Filiais e solicitações</small></span><span class="visual__count">03</span></div>
              <div class="visual__row"><span class="visual__icon">02</span><span><strong>Manutenção</strong><small>Itens e serviços</small></span><span class="visual__count">03</span></div>
              <div class="visual__row"><span class="visual__icon">03</span><span><strong>Facilities</strong><small>Infraestrutura</small></span><span class="visual__count">02</span></div>
            </div>
          </section>

```

`main.content` tem `id="conteudo"`, destino do link de pular navegação. `section.hero` agrupa uma parte temática. `aria-labelledby="page-title"` usa o texto do elemento com esse ID como nome acessível da seção; diferentemente de `aria-label`, recebe um ID, não uma frase.

Leia as divisões de dentro para fora:

- `hero__copy` guarda toda a parte textual da apresentação.
- `eyebrow` agrupa o pequeno rótulo acima do título e seu ponto decorativo.
- `h1` é o título principal. O ponto final está em um `span` para receber outra cor sem mudar o restante do título.
- `p` explica o objetivo da tela.
- `hero__actions` junta os dois links para que possam ficar lado a lado e quebrar de linha quando necessário.
- `hero__visual` agrupa a ilustração feita com HTML e CSS. Seu conteúdo é decorativo e está oculto da leitura assistiva.
- `visual__top` é a barra da ilustração com bolinhas, título e seta.
- Cada `visual__row` reúne um número, nome, descrição e contagem. O `span` sem classe agrupa `strong` e `small` para ficarem na mesma coluna. `visual__count` separa o número à direita.

As três linhas da ilustração são textos fixos. Elas não são os cartões de pedidos reais do protótipo e não mudam com os filtros. `</div>` depois das linhas fecha a ilustração; `</section>` fecha a apresentação. `main` segue aberto para receber as próximas seções.

**Pare e pense / experimente:** Se filtrar somente Tecnologia no painel pronto, a ilustração de Operações desaparecerá?

**Conferência:** Não. Ela é decorativa e fixa. Mais adiante os filtros agirão sobre os dados usados para construir a lista de requisições.

### 1.5 — Aviso e quatro indicadores

Os indicadores mostram quantidades. Por enquanto, o HTML contém um travessão; os números virão do JavaScript.

**Digite no arquivo `index.html`.** Este trecho corresponde às linhas 66–74 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```html
          <p class="demo-alert"><strong>Dados de demonstração.</strong> Setores, situações e vínculos por e-mail nesta prévia ilustram a interface. A definição de “aberta” e os dados reais dependem do Rodopar.</p>

          <section class="metrics" aria-label="Resumo demonstrativo">
            <div class="metric"><span>Requisições na prévia</span><strong id="metric-total">—</strong><small>Registros fictícios</small></div>
            <div class="metric"><span>Setores apresentados</span><strong id="metric-sectors">—</strong><small>Blocos separados</small></div>
            <div class="metric"><span>Com e-mail associado</span><strong id="metric-email">—</strong><small>Vínculos de exemplo</small></div>
            <div class="metric metric--accent"><span>Situações ilustradas</span><strong id="metric-status">—</strong><small>Cores da legenda enviada</small></div>
          </section>

```

`p.demo-alert` dá contexto aos dados fictícios. O `strong` destaca o início do aviso.

`section.metrics` agrupa quatro cartões. Cada `div.metric` junta três elementos: `span` para o nome, `strong` para o número e `small` para a observação.

Os quatro IDs têm destinos diferentes: `metric-total` recebe a quantidade de pedidos encontrados; `metric-sectors`, a quantidade de setores com resultados; `metric-email`, a quantidade de pedidos encontrados com o indicador de e-mail; `metric-status`, a quantidade de situações distintas nos resultados. São quatro cálculos diferentes.

A última divisão recebe também `metric--accent`, uma variação visual. Todas continuam sendo cartões da classe `metric`. A classe não calcula nada; o ID permite que o JavaScript encontre o número a atualizar.

**Pare e pense / experimente:** Por que usar a mesma classe `metric` quatro vezes e quatro IDs diferentes?

**Conferência:** A classe reaproveita a aparência; os IDs identificam alvos diferentes para atualizar o conteúdo.

### 1.6 — Cartões que abrem sem JavaScript

O navegador já sabe abrir e fechar um elemento `details`. Aprender recursos nativos evita ter que programar tudo do zero.

**Digite no arquivo `index.html`.** Este trecho corresponde às linhas 75–91 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```html
          <section class="section email-section" id="emails" aria-labelledby="email-heading">
            <div class="section__header">
              <div><div class="section__eyebrow">01 / CAIXA DE ENTRADA</div><h2 id="email-heading">Recebidas por e-mail</h2><p>Uma prévia da fila que ficará em destaque no dashboard.</p></div>
              <span class="section__tag">2 mensagens fictícias</span>
            </div>
            <div class="email-grid">
              <details class="email-card">
                <summary><span class="email-card__icon" aria-hidden="true">✉</span><span class="email-card__summary"><strong>Peças para manutenção predial</strong><small>Filial 05 · recebida hoje · vínculo proposto</small></span><span class="email-card__chevron" aria-hidden="true">⌄</span></summary>
                <div class="email-card__body"><p>A mensagem menciona uma solicitação de materiais. Na integração real, o vínculo será conferido com a chave do Rodopar antes de aparecer na ficha.</p><span class="email-tag">Aguardando confirmação</span></div>
              </details>
              <details class="email-card">
                <summary><span class="email-card__icon" aria-hidden="true">✉</span><span class="email-card__summary"><strong>Reposição de insumos para operação</strong><small>Filial 10 · recebida ontem · sem vínculo</small></span><span class="email-card__chevron" aria-hidden="true">⌄</span></summary>
                <div class="email-card__body"><p>Esta mensagem permanece na triagem até que uma requisição existente seja identificada e o vínculo seja confirmado.</p><span class="email-tag email-tag--muted">A identificar</span></div>
              </details>
            </div>
          </section>

```

`section.email-section` é a região dos e-mails fictícios. Ela também recebe `section`, classe que compartilhará espaçamento com outras regiões.

`div.section__header` agrupa o cabeçalho. A `div` interna sem classe mantém juntos o rótulo `section__eyebrow`, o título `h2` e o parágrafo. Assim, o selo `section__tag` pode ficar ao lado desse conjunto.

`div.email-grid` agrupa os dois cartões para distribuí-los em colunas. Cada cartão é um `details`, com um `summary` como cabeçalho acionável. Clique no `summary` e o navegador alterna o atributo `open`. Não precisamos escrever uma função para esse comportamento básico.

No `summary`, três partes têm responsabilidades distintas: `email-card__icon` mostra o ícone; `email-card__summary` agrupa título e descrição; `email-card__chevron` mostra a seta. `div.email-card__body` guarda o parágrafo e o selo que aparecem quando o cartão abre.

O segundo cartão repete a estrutura com outro conteúdo. Seu selo tem a classe extra `email-tag--muted`, uma variante visual. Os `</details>` fecham cada cartão; os dois últimos fechamentos encerram a grade e a seção.

O texto “2 mensagens fictícias” é fixo. Não existe busca de e-mails nem contagem automática dessa caixa de entrada neste código.

**Pare e pense / experimente:** No laboratório, escreva `<details><summary>Ver resposta</summary><p>Você abriu o cartão.</p></details>`. Teste com mouse e com teclado.

**Conferência:** O parágrafo fica recolhido inicialmente. Ao acionar o cabeçalho, aparece. Ao escrever `open` na tag inicial, o cartão passa a iniciar aberto.

### 1.7 — Campos de busca e seleção

O HTML cria os controles. Mais adiante, o JavaScript lerá seus valores e decidirá quais pedidos mostrar.

**Digite no arquivo `index.html`.** Este trecho corresponde às linhas 92–105 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```html
          <section class="section requisitions-section" id="setores" aria-labelledby="sector-heading">
            <div class="section__header">
              <div><div class="section__eyebrow">02 / VISÃO POR SETOR</div><h2 id="sector-heading">Requisições por setor</h2><p>Os cabeçalhos dos cartões seguem a situação ilustrativa de cada requisição.</p></div>
              <span class="section__tag">Clique para expandir</span>
            </div>

            <div class="toolbar" role="search" aria-label="Filtros das requisições">
              <label class="field field--search"><span>Buscar</span><input id="search-input" type="search" placeholder="Código, descrição, setor ou filial…" autocomplete="off"></label>
              <label class="field"><span>Setor</span><select id="sector-filter"><option value="">Todos os setores</option></select></label>
              <label class="field"><span>Situação</span><select id="status-filter"><option value="">Todas as situações</option></select></label>
              <label class="field"><span>E-mail</span><select id="email-filter"><option value="">Todos</option><option value="with">Com e-mail</option><option value="without">Sem e-mail</option></select></label>
              <button class="clear-button" id="clear-filters" type="button">Limpar filtros</button>
            </div>

```

O cabeçalho repete a estrutura já aprendida: seção, agrupamento de título e selo. `id="setores"` é o destino dos links para a lista.

`div.toolbar` reúne todos os filtros. `role="search"` identifica a região como busca. Dentro dela, cada `label` envolve o nome e seu controle, criando a associação entre os dois.

- `input type="search"` cria o campo de texto. `placeholder` é a dica que aparece vazio; o rótulo “Buscar” continua visível. `autocomplete="off"` pede que o navegador não ofereça preenchimento anterior, embora navegadores possam adotar decisões próprias.
- `select` cria uma lista de seleção e `option` representa uma escolha.
- `value=""` é um texto vazio. Aqui significa não restringir por aquele filtro. O texto visível “Todos os setores” é diferente do valor que o JavaScript lê.
- `sector-filter` e `status-filter` começam com uma única opção. As outras serão criadas a partir das listas do JavaScript.
- `email-filter` já tem três opções fixas: vazio, `with` e `without`. Os dois últimos valores significam com e sem e-mail para a regra que escreveremos.
- O botão `clear-filters` existe, mas ainda não sabe limpar nada. O listener de clique será escrito na Aula 3.

`field--search` é a variação de classe que permitirá à busca ocupar mais espaço na grade de filtros.

**Pare e pense / experimente:** Mude só o texto visível “Com e-mail” para “Vinculados”, mantendo `value="with"`. A regra de filtro precisará mudar?

**Conferência:** Não. O JavaScript usa o valor `with`, não o texto apresentado na opção. Separe nomes mostrados ao usuário de valores usados no programa.

### 1.8 — Espaços dinâmicos e fechamento do documento

Terminaremos o arquivo. Algumas divisões ficam vazias de propósito: o JavaScript preencherá essas regiões.

**Digite no arquivo `index.html`.** Este trecho corresponde às linhas 106–118 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```html
            <div class="legend" id="status-legend" aria-label="Legenda de situações ilustrativas"></div>
            <div class="results-bar"><p id="results-count" role="status" aria-live="polite"></p><div class="results-bar__actions"><button id="expand-all" type="button">Expandir todos</button><button id="collapse-all" type="button">Recolher todos</button></div></div>
            <div id="sector-list" class="sector-list"></div>
            <div class="empty-state" id="empty-state" hidden><span aria-hidden="true">⌕</span><h3>Nenhuma requisição encontrada</h3><p>Ajuste a busca ou limpe os filtros para voltar à visão completa.</p><button id="empty-reset" type="button">Limpar filtros</button></div>
          </section>

          <footer class="footer">Protótipo de interface · dados fictícios · situações pendentes de homologação com o Rodopar.</footer>
        </main>
      </div>
    </div>
    <noscript>Ative o JavaScript para usar busca, filtros e cartões interativos desta prévia.</noscript>
  </body>
</html>
```

`div.legend` receberá a legenda de situações. `div.results-bar` junta uma mensagem e um grupo de botões. Sua `div.results-bar__actions` mantém “Expandir todos” e “Recolher todos” lado a lado.

O `p#results-count` começa vazio. `role="status"` e `aria-live="polite"` permitem anunciar suas atualizações em tecnologia assistiva sem exigir uma interrupção imediata. Esses atributos não fazem a contagem.

`div#sector-list` é o recipiente para os setores gerados pelo JavaScript. Não há requisições escritas diretamente aqui no HTML.

`div.empty-state` reúne ícone, título, explicação e botão para o caso em que os filtros não encontrem nada. `hidden` evita que apareça junto da lista inicial. O botão `empty-reset` é outro caminho para limpar filtros.

`</section>` fecha a seção dos setores. `footer` é o rodapé do conteúdo. Depois são fechados, nesta ordem, `main`, `div.app-main` e `div.app-shell`. A ordem importa porque esses elementos foram abertos um dentro do outro.

`noscript` oferece uma mensagem quando a execução de scripts está desativada. Não é uma mensagem automática para erro de JavaScript. `</body>` e `</html>` concluem o documento.

**Ponto de conferência do HTML:** salve e abra `index.html`. Sem CSS, a página deve parecer simples, empilhada e com estilos padrão do navegador. Os e-mails abrem com `details`. Os quatro números ainda são travessões; os filtros ainda não geram a lista. Isso é esperado, porque `app.js` está vazio.

**Pare e pense / experimente:** Desenhe em papel a árvore `app-shell → sidebar + app-main → topbar + main`. Depois localize no arquivo a abertura e o fechamento de cada agrupamento.

**Conferência:** O menu lateral é irmão de `app-main`. A barra superior e o conteúdo principal ficam dentro de `app-main`. Mover um fechamento pode mudar essa organização mesmo quando o navegador tenta corrigir o HTML.

## Aula 2 — CSS: decidir como cada elemento ocupa e pinta a tela

No laboratório, coloque dentro de `head` este exemplo. Ele é apenas uma experiência; no painel as regras ficam em `styles.css`.

```html
<style>
  p {
    color: blue;
    padding: 16px;
    border: 1px solid black;
  }
</style>
```

`p` é o **seletor**: diz quais elementos recebem as regras. `{` abre o bloco e `}` fecha. `color` é uma **propriedade**; `blue` é o valor. Os dois-pontos separam propriedade e valor, e o ponto e vírgula encerra a declaração. A regra pinta o texto do parágrafo de azul, afasta o conteúdo de sua borda e desenha a borda.

Todo elemento ocupa uma caixa. **Conteúdo** é a parte com o texto; **padding** é o espaço entre conteúdo e borda; **border** é a borda; **margin** fica do lado de fora. Experimente trocar `padding: 16px` por `margin: 16px`: o espaço muda de lado da borda. Nem toda caixa precisa de uma `div`; um `p` também tem caixa.

### Como ler seletores do projeto

| Escrita | Leia assim |
| --- | --- |
| `.metric` | Elementos que têm a classe `metric`. O ponto pertence ao seletor, não ao nome da classe no HTML. |
| `#metric-total` | O elemento com esse ID. |
| `h1` | Elementos da tag `h1`. |
| `.hero h1` | Um `h1` em qualquer nível dentro de `.hero`. O espaço indica descendência. |
| `.sector > summary` | Somente o `summary` filho direto do setor, evitando atingir os cabeçalhos dos cartões internos. |
| `.main-nav__link.is-active` | O mesmo elemento precisa ter as duas classes. Não há espaço. |
| `.a, .b` | A mesma regra se aplica a `.a` e a `.b`. |
| `[hidden]` | Qualquer elemento que tenha o atributo `hidden`. |
| `[data-status="pending"]` | Elementos com aquele atributo e valor exatos. |
| `.email-card[open]` | Um cartão de e-mail que está com o atributo `open`. |
| `:hover` | O ponteiro está sobre o elemento. |
| `:focus` / `:focus-visible` | O elemento está focado / o navegador determina que deve mostrar indicação visível de foco, comum ao usar teclado. |
| `::before` | Uma pequena parte visual gerada antes do conteúdo, sem uma tag nova no HTML. |
| `span + span` | Um `span` imediatamente depois de outro `span` irmão. |
| `:not([hidden])` | Um elemento que não possui o atributo `hidden`. |

O navegador combina regras. Algumas propriedades, como cor e fonte, podem ser herdadas do elemento pai. Outras, como margem, não são herdadas normalmente. Entre regras concorrentes entram em jogo importância, especificidade e ordem. Neste projeto, por exemplo, uma classe com `[open]` seleciona um estado mais específico que a classe sozinha. Regras posteriores com a mesma prioridade e especificidade podem substituir as anteriores.

### Unidades e abreviações que você vai digitar

- `px`: pixel de CSS, uma unidade da interface; não é obrigatoriamente um pixel físico da tela.
- `%`: proporção de uma referência que depende da propriedade. `width: 100%` normalmente usa a largura do bloco que contém o elemento; porcentagens em `transform` usam outra referência.
- `vw` e `vh`: porcentagens da largura e altura da janela de visualização. `100vh` corresponde à altura dessa referência, com particularidades das barras móveis dos navegadores.
- `em`: proporção do tamanho de fonte; em `letter-spacing`, `.1em` acompanha a fonte do próprio elemento.
- `fr`: fração do espaço disponível em uma grade. `1fr 1fr` cria duas colunas de mesma participação.
- `s`: segundos. `.2s` é um quinto de segundo.
- `padding: 10px 16px`: 10 em cima/baixo, 16 nos lados. Com três valores: cima, lados, baixo. Com quatro: cima, direita, baixo, esquerda. `margin` usa a mesma ordem.
- `border: 1px solid ...`: espessura, tipo de linha e cor. `border-left` aplica só à esquerda.
- `#81d4f6`: cor hexadecimal; pares representam vermelho, verde e azul. `#fff` abrevia branco. `rgba(0, 0, 0, .18)` é preto com transparência de 18%.

### Duas maneiras de distribuir elementos

**Flexbox** organiza os filhos principalmente em uma direção: uma fila ou coluna. `display: flex` ativa esse modelo. `flex-direction: column` muda para coluna; `gap` separa os filhos; `flex-wrap: wrap` permite criar outra linha. Na direção padrão de fila, `align-items: center` alinha verticalmente e `justify-content: space-between` distribui horizontalmente pelas extremidades. Ao mudar a direção, os eixos também mudam.

**Grid** define colunas e linhas. `display: grid` ativa a grade; `grid-template-columns` define as colunas. `repeat(2, minmax(0, 1fr))` repete duas colunas que podem encolher até zero e dividir o espaço disponível igualmente. `minmax(0, 1fr)` ajuda a impedir que conteúdo largo imponha uma largura mínima excessiva à coluna; ele não garante, sozinho, que todo conteúdo interno deixe de transbordar.

`place-items: center` centraliza os itens nos dois eixos da célula. `align-self` e `justify-self` tratam do item individual. `min-width: 0` permite que itens de flex/grid encolham além de sua largura mínima automática. No projeto, essas escolhas ajudam textos a caberem em áreas pequenas.

Agora preencha o `styles.css` vazio, seguindo os blocos. Você pode salvar e recarregar depois de cada bloco completo para observar o progresso. A lista de pedidos continuará vazia até a Aula 3.

### 2.1 — :root, variáveis e os dois temas

Uma cor aparece em muitos lugares. Dar um nome a ela permite mudar o conjunto sem procurar cada cartão individualmente.

**Digite no arquivo `styles.css`.** Este trecho corresponde às linhas 1–35 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```css
/* A paleta concentra a adaptação futura ao tema da aplicação, sem afetar estilos fora do protótipo. */
:root {
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  color-scheme: dark;
  --page: #0d1115;
  --page-soft: #11171c;
  --panel: #171d22;
  --panel-raised: #1c242a;
  --panel-hover: #212c33;
  --text: #edf4f8;
  --muted: #9ba9b4;
  --line: #2c3942;
  --line-soft: #263139;
  --accent: #81d4f6;
  --accent-strong: #28ace0;
  --accent-faint: rgba(70, 180, 229, .13);
  --shadow: 0 18px 55px rgba(0, 0, 0, .18);
}
html[data-theme="light"] {
  color-scheme: light;
  --page: #f4f8fb;
  --page-soft: #eaf2f7;
  --panel: #ffffff;
  --panel-raised: #f8fbfd;
  --panel-hover: #eef6fa;
  --text: #1c3442;
  --muted: #607788;
  --line: #d8e4eb;
  --line-soft: #e6eef2;
  --accent: #087fad;
  --accent-strong: #078fca;
  --accent-faint: #e3f5fc;
  --shadow: 0 16px 35px rgba(35, 69, 86, .08);
}
```

`/* ... */` é um comentário de CSS. `:root` é uma pseudoclasse que seleciona a raiz do documento; no HTML, essa raiz é o elemento `html`. O sinal `:` faz parte da sintaxe. Não é uma tag que você precise criar.

`font-family` é uma lista de fontes em ordem de preferência. O navegador tenta uma disponível; escrever `Inter` não baixa nem instala essa fonte. As alternativas do sistema permitem funcionar sem rede. `color-scheme: dark` orienta a aparência escura dos controles nativos.

As propriedades iniciadas por `--` são **propriedades personalizadas de CSS**, frequentemente chamadas de variáveis. `--page: #0d1115` guarda um valor com um nome. `background: var(--page)` consulta esse valor. A declaração, sozinha, não pinta toda a página.

Leia os nomes deste conjunto:

| Nome | Intenção visual |
| --- | --- |
| `--page`, `--page-soft` | Fundo principal e uma variação, usada por exemplo no menu. |
| `--panel`, `--panel-raised`, `--panel-hover` | Superfícies de painéis e variações. Um nome declarado só produz efeito onde for usado; `--panel-hover` é uma reserva de paleta neste arquivo. |
| `--text`, `--muted` | Texto principal e texto secundário. |
| `--line`, `--line-soft` | Bordas e divisórias. |
| `--accent`, `--accent-strong`, `--accent-faint` | Destaques e fundos de destaque. |
| `--shadow` | Uma sombra completa, não apenas uma cor. |

Em `0 18px 55px rgba(...)`, os primeiros valores da sombra significam deslocamento horizontal zero, vertical 18 e desfoque 55. Há também formas com espalhamento, vistas adiante.

O segundo seletor, `html[data-theme="light"]`, só corresponde à raiz quando o atributo vale `light`. Ele redefine os mesmos nomes com cores claras. Os elementos que usam `var(...)` passam a consultar os novos valores herdados. Mais adiante o JavaScript trocará exatamente esse atributo.

**Pare e pense / experimente:** Mude temporariamente `data-theme="dark"` para `data-theme="light"` na primeira tag do HTML. Depois de escrever as regras de `body`, observe a mudança. Por que não precisamos trocar classe de cada cartão?

**Conferência:** Os componentes consultam nomes compartilhados. Ao trocar os valores desses nomes na raiz, seus descendentes passam a receber a outra paleta. O JavaScript completo também restaurará o tema salvo, por isso faça esta experiência antes da Aula 3 ou use o botão de tema depois.

### 2.2 — Regras gerais, foco e o link de pular

Este bloco tira algumas diferenças padrão do navegador e prepara a navegação por teclado.

**Digite no arquivo `styles.css`.** Este trecho corresponde às linhas 36–49 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```css
* {
  box-sizing: border-box;
}
html {
  scroll-behavior: smooth;
}
body {
  margin: 0;
  background: var(--page);
  color: var(--text);
  font-size: 14px;
  line-height: 1.5;
}
button, input, select {
  font: inherit;
}
button {
  cursor: pointer;
}
a {
  color: inherit;
}
:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}
[hidden] {
  display: none !important;
}
section[id] {
  scroll-margin-top: 90px;
}
.skip-link {
  position: fixed;
  top: -55px;
  left: 12px;
  z-index: 200;
  padding: 10px 16px;
  background: var(--accent);
  color: #071a24;
  border-radius: 8px;
}
.skip-link:focus {
  top: 10px;
}
```

O seletor `*` alcança todos os elementos. `box-sizing: border-box` faz uma largura declarada incluir padding e borda; a margem continua fora. Isso facilita calcular tamanhos.

`scroll-behavior: smooth` suaviza deslocamentos como os links internos. `body` perde a margem padrão, recebe fundo e texto da paleta, fonte de 14px e `line-height: 1.5`, uma altura de linha de 1,5 vezes o tamanho da fonte. `background` pinta o fundo; `color` pinta o texto.

`font: inherit` faz os controles herdarem a configuração de fonte. `cursor: pointer` usa o cursor de ação sobre botões. `a { color: inherit; }` faz os links herdarem a cor em vez de usarem obrigatoriamente o azul padrão.

`outline` desenha um contorno de foco sem reservar espaço como a borda; `outline-offset` afasta esse contorno. `[hidden] { display: none !important; }` reforça o ocultamento mesmo quando outra regra comum define `display`. O `!important` aumenta a prioridade desta declaração; não é algo para espalhar em toda regra quando um estilo não funciona.

`scroll-margin-top: 90px` reserva uma folga no alinhamento de rolagem das seções com ID, ajudando o cabeçalho fixo a não cobrir o destino.

O link `.skip-link` fica com `position: fixed`, preso à janela. `top: -55px` inicialmente o põe acima da área visível; `left` posiciona pela esquerda; `z-index` controla sua ordem de sobreposição no contexto de empilhamento. `padding` amplia a área clicável e `border-radius` arredonda os cantos. Quando recebe foco, `top: 10px` o traz para dentro da tela.

**Pare e pense / experimente:** No painel, pressione Tab desde o início. O link “Pular para o conteúdo” deve aparecer quando recebe foco. O que aconteceria se ele tivesse `display: none`?

**Conferência:** Ele normalmente deixaria de participar da navegação por foco enquanto estivesse oculto. O deslocamento usado aqui mantém o link disponível para teclado.

### 2.3 — Duas colunas e todos os detalhes do menu

Agora o agrupamento `app-shell`, que você escreveu no HTML, ganha a função visual de organizar menu e conteúdo.

**Digite no arquivo `styles.css`.** Este trecho corresponde às linhas 50–68 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```css
.app-shell {
  display: grid;
  grid-template-columns: 244px minmax(0, 1fr);
  min-height: 100vh;
}
.sidebar {
  position: sticky;
  top: 0;
  align-self: start;
  display: flex;
  flex-direction: column;
  height: 100vh;
  padding: 27px 17px 18px;
  background: var(--page-soft);
  border-right: 1px solid var(--line);
  z-index: 40;
}
.brand {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 9px;
  text-decoration: none;
}
.brand__mark {
  width: 33px;
  height: 33px;
  flex: 0 0 33px;
  display: grid;
  place-items: center;
  border-radius: 9px;
  background: linear-gradient(145deg, #38c3ee 0 45%, #123a4e 46% 65%, #edf6fb 66%);
  box-shadow: 0 0 0 1px rgba(149, 222, 250, .24);
}
.brand__mark span {
  width: 10px;
  height: 10px;
  transform: rotate(45deg);
  background: var(--page-soft);
}
.brand__text {
  display: flex;
  flex-direction: column;
  min-width: 0;
  line-height: 1.15;
}
.brand__text strong {
  font-size: 12px;
  font-weight: 850;
  letter-spacing: .055em;
}
.brand__text small {
  margin-top: 5px;
  font-size: 10px;
  color: var(--muted);
  letter-spacing: .02em;
}
.sidebar__label {
  margin: 52px 12px 14px;
  color: var(--muted);
  font-size: 10px;
  font-weight: 750;
  letter-spacing: .16em;
}
.main-nav {
  display: grid;
  gap: 5px;
}
.main-nav__link {
  display: flex;
  align-items: center;
  gap: 13px;
  min-height: 42px;
  padding: 9px 12px;
  border-radius: 10px;
  color: var(--muted);
  text-decoration: none;
  font-weight: 600;
}
.main-nav__link span {
  display: grid;
  width: 17px;
  place-items: center;
  color: var(--accent);
  font-size: 17px;
}
.main-nav__link:hover, .main-nav__link.is-active {
  color: var(--text);
  background: var(--accent-faint);
}
.main-nav__link.is-active {
  box-shadow: inset 2px 0 0 var(--accent-strong);
}
.sidebar__note {
  display: flex;
  align-items: center;
  gap: 9px;
  margin: auto 9px 16px;
  padding: 11px;
  border: 1px solid var(--line);
  border-radius: 10px;
  color: var(--muted);
  font-size: 11px;
}
.live-dot {
  display: inline-block;
  width: 7px;
  height: 7px;
  flex: 0 0 7px;
  border-radius: 50%;
  background: #5bd4b8;
  box-shadow: 0 0 0 4px rgba(91, 212, 184, .12);
}
.sidebar__foot {
  padding: 0 11px;
  color: var(--muted);
  font-size: 11px;
}
.app-main {
  min-width: 0;
}
```

Leia as regras junto de seus elementos:

- `.app-shell`: Grid com 244px para o menu e o espaço restante para o conteúdo. `min-height: 100vh` pede pelo menos uma altura de tela.
- `.sidebar`: `position: sticky` com `top: 0` mantém o menu junto ao topo durante a rolagem dentro dos limites aplicáveis. `align-self: start` alinha o item ao início da área. Flex em coluna empilha seus conteúdos; a borda direita separa menu e página.
- `.brand`: Flex coloca símbolo e nome lado a lado. `text-decoration: none` retira o sublinhado do link.
- `.brand__mark`: tamanho quadrado e `flex: 0 0 33px` para não crescer nem encolher, com base de 33px. Grid centraliza o desenho interno. O gradiente linear tem ângulo de 145 graus e faixas de cor; `box-shadow` com desfoque zero e espalhamento de 1px cria um contorno visual.
- `.brand__mark span`: o quadrado interno é girado 45 graus. `transform` altera a apresentação, sem recalcular o layout como se o elemento tivesse sido colocado em outra posição.
- `.brand__text`: empilha nome e subtítulo. As duas regras seguintes definem tamanho, peso e espaçamento das letras. `font-weight` pede um peso que a fonte disponível precisa conseguir representar.
- `.sidebar__label`: usa margem maior em cima para separar a legenda da marca. `letter-spacing` afasta as letras; não cria espaços no conteúdo do HTML.
- `.main-nav`: Grid e `gap` separam links. `.main-nav__link` usa Flex, altura mínima, preenchimento, borda arredondada e cor secundária. Seu `span` tem uma área estável para o ícone.
- As regras com `:hover` e `.is-active` alteram cor e fundo. A sombra `inset 2px 0 0` fica para dentro e cria a marca visual do link ativo.
- `.sidebar__note`: `margin-top: auto` consome o espaço disponível acima do aviso no Flex em coluna, empurrando-o para baixo. Borda e padding delimitam a nota.
- `.live-dot`: um pequeno quadrado com `border-radius: 50%` vira círculo. A sombra sem desfoque, com espalhamento de 4px, faz o halo. `inline-block` permite dimensão de caixa mantendo participação na linha.
- `.sidebar__foot`: texto pequeno com afastamento lateral.
- `.app-main`: `min-width: 0` permite ao conteúdo encolher dentro da coluna de Grid.

`z-index: 40` do menu e `z-index: 30` do cabeçalho serão parte da ordem de sobreposição. Números maiores não vencem universalmente todos os contextos de empilhamento; aqui esses valores coordenam os elementos desta interface.

**Pare e pense / experimente:** Troque temporariamente `244px` por `300px` em `.app-shell`. O que muda? E se apagar somente `display: grid`?

**Conferência:** A primeira mudança alarga a coluna do menu. Sem Grid, `grid-template-columns` deixa de organizar as duas regiões e os elementos voltam a seguir outro fluxo de layout.

### 2.4 — Barra superior, botões e largura de leitura

O cabeçalho reúne dois grupos, e o conteúdo precisa de limites para continuar legível em telas largas.

**Digite no arquivo `styles.css`.** Este trecho corresponde às linhas 69–80 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```css
.topbar {
  position: sticky;
  top: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  height: 67px;
  padding: 0 clamp(22px, 3.4vw, 54px);
  border-bottom: 1px solid var(--line-soft);
  background: var(--page);
}
.topbar__left, .topbar__right {
  display: flex;
  align-items: center;
  gap: 16px;
  min-width: 0;
}
.breadcrumb {
  white-space: nowrap;
  color: var(--muted);
  font-size: 12px;
}
.breadcrumb span {
  padding: 0 9px;
  opacity: .55;
}
.breadcrumb strong {
  color: var(--text);
  font-weight: 700;
}
.topbar__edition {
  font-size: 10px;
  color: var(--muted);
  letter-spacing: .12em;
  font-weight: 750;
}
.theme-button, .icon-button {
  min-height: 36px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 7px 11px;
  border: 1px solid var(--line);
  border-radius: 9px;
  background: var(--panel);
  color: var(--text);
}
.theme-button:hover, .icon-button:hover {
  border-color: var(--accent);
}
.user-avatar {
  display: grid;
  place-items: center;
  width: 33px;
  height: 33px;
  border-radius: 50%;
  background: #16a8d9;
  color: #fff;
  font-size: 10px;
  font-weight: 850;
}
.mobile-menu {
  display: none;
}
.content {
  max-width: 1550px;
  margin: 0 auto;
  padding: 28px clamp(22px, 3.4vw, 54px) 32px;
}
```

`.topbar` combina posicionamento sticky com Flex. `justify-content: space-between` afasta os grupos; `align-items: center` os alinha. O padding lateral usa `clamp(22px, 3.4vw, 54px)`: começa com um tamanho proporcional à janela, mas nunca menor que 22 nem maior que 54.

`.topbar__left` e `.topbar__right` também são contêineres Flex, mas organizam os elementos dentro de cada grupo. É possível ter Flex dentro de Flex.

`.breadcrumb` usa `white-space: nowrap` para manter seu texto em uma linha. Sua barra ganha padding e `opacity: .55`, tornando esse elemento inteiro parcialmente transparente. O `strong` recebe destaque. `.topbar__edition` regula a legenda de prévia.

`.theme-button` e `.icon-button` compartilham dimensões, borda e cores. `inline-flex` cria um contêiner Flex com participação externa de elemento em linha. O seletor com vírgula evita repetir as mesmas propriedades. Ao passar o ponteiro, muda só a cor da borda.

`.user-avatar` desenha o círculo de iniciais, com Grid centralizando o texto. `.mobile-menu` começa com `display: none`, pois em telas grandes o menu já fica visível; uma media query fará o botão aparecer.

`.content` tem `max-width: 1550px`, limitando o crescimento. `margin: 0 auto` centraliza quando sobra espaço horizontal. O padding cria espaço interno de leitura. Não é necessário fixar uma largura para cada parágrafo.

**Pare e pense / experimente:** Com uma janela estreita, o padding que usa `clamp` pode virar zero?

**Conferência:** Não. O limite mínimo declarado é 22px para essa regra. Regras posteriores específicas para telas pequenas poderão substituí-lo.

### 2.5 — A apresentação, seus desenhos e suas camadas

Observe como um desenho pode ser composto de elementos simples. O projeto não usa uma imagem externa para a ilustração de setores.

**Digite no arquivo `styles.css`.** Este trecho corresponde às linhas 81–104 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```css
.hero {
  position: relative;
  overflow: hidden;
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(280px, .85fr);
  align-items: center;
  gap: 36px;
  min-height: 270px;
  padding: clamp(25px, 4vw, 48px);
  border: 1px solid var(--line);
  border-radius: 17px;
  background: radial-gradient(circle at 82% 7%, rgba(62, 178, 227, .16), transparent 46%), var(--panel);
  box-shadow: var(--shadow);
}
.hero::before {
  content: "";
  position: absolute;
  inset: 0 auto 0 0;
  width: 3px;
  background: linear-gradient(var(--accent-strong), transparent);
}
.hero__copy, .hero__visual {
  position: relative;
}
.eyebrow, .section__eyebrow {
  display: flex;
  align-items: center;
  gap: 10px;
  color: var(--accent);
  font-size: 10px;
  font-weight: 800;
  letter-spacing: .17em;
}
.hero h1 {
  max-width: 560px;
  margin: 12px 0 11px;
  font-size: clamp(31px, 3.4vw, 47px);
  line-height: 1.11;
  letter-spacing: -.045em;
}
.hero h1 span {
  color: var(--accent-strong);
}
.hero p {
  max-width: 530px;
  margin: 0;
  color: var(--muted);
  font-size: 14px;
  line-height: 1.7;
}
.hero__actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 14px 20px;
  margin-top: 23px;
}
.primary-link {
  display: inline-flex;
  align-items: center;
  gap: 28px;
  padding: 10px 15px;
  border-radius: 8px;
  background: #7dd0f0;
  color: #092231;
  text-decoration: none;
  font-size: 12px;
  font-weight: 800;
}
.primary-link:hover {
  background: #a5e4fb;
}
.subtle-link {
  color: var(--text);
  font-size: 12px;
  font-weight: 700;
  text-decoration: none;
}
.subtle-link:hover {
  color: var(--accent);
}
.subtle-link span {
  margin-left: 7px;
}
.hero__visual {
  max-width: 380px;
  width: 100%;
  justify-self: end;
  overflow: hidden;
  border: 1px solid var(--line);
  border-radius: 13px;
  background: var(--page-soft);
  box-shadow: 0 24px 55px rgba(0,0,0,.16);
  transform: rotate(-2deg);
}
.visual__top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 8px;
  padding: 10px 13px;
  color: var(--muted);
  border-bottom: 1px solid var(--line);
  font-size: 9px;
  font-weight: 750;
  letter-spacing: .08em;
}
.window-dots {
  color: #667985;
  font-size: 8px;
  letter-spacing: 2px;
}
.visual__row {
  display: grid;
  grid-template-columns: 35px 1fr auto;
  gap: 9px;
  align-items: center;
  margin: 8px;
  padding: 9px;
  border: 1px solid var(--line);
  border-radius: 9px;
  background: var(--panel);
}
.visual__icon {
  display: grid;
  place-items: center;
  width: 32px;
  height: 32px;
  border-radius: 7px;
  background: var(--accent-faint);
  color: var(--accent);
  font-size: 10px;
  font-weight: 850;
}
.visual__row strong, .visual__row small {
  display: block;
}
.visual__row strong {
  font-size: 11px;
}
.visual__row small {
  color: var(--muted);
  font-size: 9px;
}
.visual__count {
  color: var(--accent);
  font-size: 12px;
  font-weight: 800;
}
.demo-alert {
  margin: 15px 1px 0;
  padding: 10px 13px;
  border-left: 2px solid var(--accent-strong);
  background: var(--accent-faint);
  color: var(--muted);
  font-size: 11px;
}
.demo-alert strong {
  color: var(--text);
}
```

`.hero` usa uma grade de duas colunas: texto com participação `1.15fr`, ilustração com `.85fr` e mínimo de 280px. `gap` separa as áreas. `overflow: hidden` recorta conteúdo que ultrapasse a caixa, inclusive efeitos. Borda, raio, sombra e gradiente radial criam o painel.

`radial-gradient(circle at 82% 7%, ..., transparent 46%)` cria uma transição de cor circular com centro deslocado. Depois da vírgula externa, `var(--panel)` é a cor de fundo. `transparent` é transparente.

`.hero::before` cria a faixa lateral: `content: ""` faz o pseudo-elemento existir; `position: absolute` o posiciona em relação ao ancestral posicionado, aqui `.hero` com `position: relative`. `inset: 0 auto 0 0` equivale a topo zero, direita automática, base zero e esquerda zero. A largura é 3px. O gradiente linear faz a faixa desaparecer gradualmente.

As regras seguintes correspondem às partes que você já criou:

- `.hero__copy` e `.hero__visual`: estabelecem posicionamento relativo, sem deslocamento declarado.
- `.eyebrow` e `.section__eyebrow`: alinham ponto e texto, ajustando tamanho, peso e espaçamento.
- `.hero h1`: limita largura e dá tamanho responsivo ao título com `clamp`. `letter-spacing` negativo aproxima as letras. O `span` recebe a cor do ponto final.
- `.hero p`: limita a largura de leitura, usa cor secundária e entrelinha maior.
- `.hero__actions`: Flex com quebra de linha. `gap: 14px 20px` separa linhas em 14 e colunas em 20.
- `.primary-link`: aparência de ação destacada, embora continue sendo um link HTML. `:hover` clareia seu fundo.
- `.subtle-link`: ação discreta; no hover sua cor muda, e o `span` da seta tem margem.
- `.hero__visual`: largura máxima de 380px, largura de 100% até esse limite, alinhamento à direita da célula, recorte, sombra e uma rotação de -2 graus.
- `.visual__top`: distribui as três partes da barra; `.window-dots` regula as bolinhas.
- `.visual__row`: três colunas, de 35px, espaço flexível e largura automática. Borda e margem separam cada linha.
- `.visual__icon`: centraliza o número no quadrado arredondado.
- `.visual__row strong` e `small`: `display: block` faz nome e descrição ocuparem linhas próprias. As regras seguintes definem fonte e cor de cada um.
- `.visual__count`: destaca a contagem decorativa.
- `.demo-alert`: cria o aviso abaixo da apresentação com borda à esquerda. Seu `strong` usa a cor principal para diferenciar a parte importante.

Não confunda `position: relative` com “tamanho responsivo”. Ele participa do sistema de posicionamento. Responsividade aqui vem de tamanhos flexíveis, `clamp` e media queries.

**Pare e pense / experimente:** Retire no laboratório a rotação de uma caixa e depois coloque `rotate(10deg)`. O texto e a borda giram juntos?

**Conferência:** Sim. O transform atua sobre a apresentação do elemento e seus conteúdos. Não altera o texto armazenado nem cria outro elemento.

### 2.6 — Indicadores, títulos de seção e cartões de e-mail

Os mesmos fundamentos reaparecem. A repetição é uma oportunidade de ler cada regra sem depender da explicação.

**Digite no arquivo `styles.css`.** Este trecho corresponde às linhas 105–121 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```css
.metrics {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 12px;
  margin-top: 20px;
}
.metric {
  display: flex;
  flex-direction: column;
  min-height: 100px;
  padding: 14px 17px;
  border: 1px solid var(--line);
  border-radius: 11px;
  background: var(--panel);
}
.metric > span {
  color: var(--muted);
  font-size: 11px;
  font-weight: 650;
}
.metric strong {
  margin: 5px 0 0;
  color: var(--text);
  font-size: 26px;
  line-height: 1.1;
}
.metric small {
  margin-top: auto;
  color: var(--muted);
  font-size: 10px;
}
.metric--accent strong {
  color: var(--accent);
}
.section {
  margin-top: 45px;
}
.section__header {
  display: flex;
  justify-content: space-between;
  align-items: end;
  gap: 18px;
  margin-bottom: 17px;
}
.section__header h2 {
  margin: 6px 0 2px;
  font-size: clamp(21px, 2vw, 26px);
  line-height: 1.2;
  letter-spacing: -.025em;
}
.section__header p {
  margin: 0;
  color: var(--muted);
  font-size: 12px;
}
.section__tag {
  flex: 0 0 auto;
  padding: 6px 10px;
  border: 1px solid var(--line);
  border-radius: 99px;
  color: var(--muted);
  font-size: 10px;
  font-weight: 700;
}
.email-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 11px;
}
.email-card {
  min-width: 0;
  overflow: hidden;
  border: 1px solid var(--line);
  border-radius: 11px;
  background: var(--panel);
}
.email-card summary {
  display: flex;
  align-items: center;
  gap: 13px;
  min-height: 73px;
  padding: 12px 15px;
  cursor: pointer;
  list-style: none;
}
.email-card summary::-webkit-details-marker {
  display: none;
}
.email-card:hover {
  border-color: var(--accent-strong);
}
.email-card__icon {
  display: grid;
  flex: 0 0 35px;
  width: 35px;
  height: 35px;
  place-items: center;
  border-radius: 8px;
  background: var(--accent-faint);
  color: var(--accent);
  font-size: 17px;
}
.email-card__summary {
  min-width: 0;
}
.email-card__summary strong, .email-card__summary small {
  display: block;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
.email-card__summary strong {
  font-size: 12px;
}
.email-card__summary small {
  margin-top: 3px;
  color: var(--muted);
  font-size: 10px;
}
.email-card__chevron {
  margin-left: auto;
  color: var(--muted);
  transition: transform .2s;
}
.email-card[open] .email-card__chevron {
  transform: rotate(180deg);
}
.email-card__body {
  padding: 0 16px 15px 63px;
  color: var(--muted);
  font-size: 11px;
}
.email-card__body p {
  margin: 0 0 9px;
}
.email-tag {
  display: inline-block;
  padding: 4px 7px;
  border-radius: 5px;
  background: rgba(255, 192, 133, .13);
  color: #f2ae71;
  font-weight: 700;
}
.email-tag--muted {
  background: var(--accent-faint);
  color: var(--accent);
}
```

`.metrics` cria quatro colunas iguais. `.metric` empilha nome, número e observação em coluna. `.metric > span` trata somente o rótulo filho direto; `strong` destaca o número; `small` usa `margin-top: auto` para aproveitar o espaço acima da observação. `.metric--accent strong` troca a cor do número da variação.

`.section` separa regiões verticalmente. `.section__header` distribui o bloco de textos e o selo, alinhando-os ao final do eixo transversal. Suas regras de `h2` e `p` ajustam a hierarquia. `.section__tag` tem `flex: 0 0 auto`, evitando que cresça ou encolha, e um raio grande para o formato de selo.

`.email-grid` cria duas colunas iguais. `.email-card` define superfície e borda. `.email-card summary` organiza ícone, textos e seta em Flex e remove o marcador padrão com `list-style: none`. `::-webkit-details-marker` é um seletor específico para ocultar o marcador em navegadores que o suportam.

O hover destaca a borda. `.email-card__icon` cria a caixa do ícone com base fixa. `.email-card__summary` pode encolher. Nos seus textos, quatro propriedades trabalham juntas: `display: block`, `overflow: hidden`, `white-space: nowrap` e `text-overflow: ellipsis`. Com uma largura efetivamente limitada, esse conjunto permite mostrar reticências quando falta espaço.

`.email-card__chevron` usa `margin-left: auto` para ir à direita. `transition: transform .2s` suaviza a mudança de rotação. Quando `[open]` está no cartão, a seta gira 180 graus. O CSS está reagindo ao estado do HTML.

`.email-card__body` dá espaçamento ao conteúdo expandido; seu parágrafo ganha margem inferior. `.email-tag` desenha o selo de situação, e `.email-tag--muted` muda seu fundo e cor. “Muted” é um nome visual; não significa que a mensagem foi silenciada em um serviço de e-mail.

**Pare e pense / experimente:** Troque `repeat(4, ...)` de `.metrics` por `repeat(2, ...)`. Quantas linhas serão necessárias para quatro indicadores?

**Conferência:** Duas linhas de duas colunas. Você mudou a distribuição, não precisou escrever novos cartões no HTML.

### 2.7 — Aparência dos filtros, legenda e resultados

Agora os controles formam uma barra organizada. A lista ainda ficará vazia até o JavaScript gerar os elementos.

**Digite no arquivo `styles.css`.** Este trecho corresponde às linhas 122–128 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```css
.toolbar {
  display: grid;
  grid-template-columns: minmax(180px, 2fr) repeat(3, minmax(124px, 1fr)) auto;
  gap: 10px;
  align-items: end;
  padding: 14px;
  border: 1px solid var(--line);
  border-radius: 11px;
  background: var(--panel);
}
.field {
  display: grid;
  gap: 5px;
  min-width: 0;
}
.field span {
  color: var(--muted);
  font-size: 10px;
  font-weight: 750;
}
.field input, .field select {
  width: 100%;
  height: 37px;
  padding: 0 11px;
  border: 1px solid var(--line);
  border-radius: 7px;
  background: var(--page-soft);
  color: var(--text);
  outline: none;
  font-size: 11px;
}
.field input:focus, .field select:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 2px var(--accent-faint);
}
.field input::placeholder {
  color: var(--muted);
  opacity: .75;
}
.clear-button {
  height: 37px;
  padding: 0 12px;
  border: 1px solid var(--line);
  border-radius: 7px;
  background: transparent;
  color: var(--text);
  font-size: 11px;
  font-weight: 650;
}
.clear-button:hover {
  border-color: var(--accent);
}
.legend {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  margin: 15px 0 10px;
}
.legend__item {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  min-height: 24px;
  padding: 3px 7px;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: var(--panel);
  color: var(--muted);
  font-size: 10px;
}
.legend__swatch {
  width: 8px;
  height: 8px;
  border-radius: 2px;
  background: var(--status-accent);
}
.results-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  min-height: 33px;
}
.results-bar p {
  margin: 0;
  color: var(--muted);
  font-size: 11px;
}
.results-bar__actions {
  display: flex;
  gap: 5px;
}
.results-bar__actions button {
  padding: 5px 8px;
  border: none;
  background: none;
  color: var(--accent);
  font-size: 10px;
  font-weight: 700;
}
.results-bar__actions button:hover {
  text-decoration: underline;
}
```

`.toolbar` usa uma coluna de busca com mínimo de 180px e participação `2fr`, três colunas de filtro com mínimo de 124px e `1fr`, e uma coluna automática para o botão. Os mínimos podem não caber em uma tela pequena; as media queries mudarão a grade.

`.field` empilha nome e controle com Grid. Seu `span` recebe fonte de rótulo. As regras de `input` e `select` são compartilhadas: largura total, altura, padding, borda, fundo e fonte. `outline: none` remove o contorno padrão nesses controles, mas a regra de `:focus` logo em seguida fornece borda e sombra visíveis; não remova as duas indicações juntas. `::placeholder` seleciona o texto de dica.

`.clear-button` desenha o botão de limpar; seu hover muda a borda. `.legend` é Flex com quebra para distribuir as situações por mais de uma linha. `.legend__item` agrupa ponto e nome; `.legend__swatch` é o pequeno quadrado que usa `--status-accent`. Essa variável será definida em cada situação.

`.results-bar` separa texto de resultado e grupo de ações. Seu `p` remove margem padrão. `.results-bar__actions` distribui os botões com Flex. A regra dos botões deixa o fundo transparente e tira a borda, conservando o elemento HTML `button` e sua ação pelo teclado. O hover acrescenta sublinhado.

**Pare e pense / experimente:** Por que a lista de seleção precisa de `width: 100%`, se a grade já tem colunas?

**Conferência:** A grade define o espaço disponível. A largura faz o controle ocupar o espaço de seu agrupamento, em vez de depender apenas de uma largura intrínseca do conteúdo.

### 2.8 — Cada parte dos setores e das requisições

Esses seletores ainda não encontrarão cartões no HTML inicial. Eles estilizarão os elementos que `cardHtml` e `sectorHtml` criarão na Aula 3.

**Digite no arquivo `styles.css`.** Este trecho corresponde às linhas 129–146 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```css
.sector-list {
  display: grid;
  gap: 13px;
  margin-top: 5px;
}
.sector {
  overflow: hidden;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--panel);
}
.sector > summary {
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 62px;
  padding: 12px 16px;
  cursor: pointer;
  list-style: none;
  background: var(--panel-raised);
}
.sector > summary::-webkit-details-marker {
  display: none;
}
.sector__icon {
  display: grid;
  flex: 0 0 37px;
  width: 37px;
  height: 37px;
  place-items: center;
  border: 1px solid var(--line);
  border-radius: 8px;
  color: var(--accent);
  background: var(--page-soft);
  font-size: 15px;
}
.sector__heading {
  display: grid;
  min-width: 0;
}
.sector__heading strong {
  font-size: 13px;
}
.sector__heading small {
  color: var(--muted);
  font-size: 10px;
}
.sector__count {
  margin-left: auto;
  padding: 3px 7px;
  border: 1px solid var(--line);
  border-radius: 5px;
  color: var(--muted);
  font-size: 10px;
  font-weight: 750;
}
.sector__chevron {
  color: var(--muted);
  font-size: 20px;
  line-height: 1;
  transition: transform .2s;
}
.sector[open] > summary .sector__chevron {
  transform: rotate(180deg);
}
.sector__body {
  padding: 14px;
  border-top: 1px solid var(--line);
}
.card-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 11px;
}
.request-card {
  min-width: 0;
  overflow: hidden;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: var(--page-soft);
  transition: border-color .15s;
}
.request-card:hover {
  border-color: var(--status-accent);
}
/* O cabeçalho utiliza a cor da situação sem fazer da cor a única identificação: o rótulo textual permanece visível. */
.request-card > summary {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  align-items: start;
  gap: 12px;
  padding: 11px 12px;
  border-left: 3px solid var(--status-accent);
  background: color-mix(in srgb, var(--status-accent) 22%, var(--panel-raised));
  cursor: pointer;
  list-style: none;
}
.request-card > summary::-webkit-details-marker {
  display: none;
}
.request-card__id {
  color: var(--muted);
  font-size: 9px;
  font-weight: 800;
  letter-spacing: .09em;
}
.request-card__title {
  display: block;
  margin: 4px 0 2px;
  overflow: hidden;
  color: var(--text);
  font-size: 12px;
  font-weight: 750;
  line-height: 1.35;
}
.request-card__branch {
  color: var(--muted);
  font-size: 10px;
}
.request-card__right {
  display: grid;
  justify-items: end;
  gap: 7px;
}
.status-pill {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  max-width: 110px;
  padding: 4px 7px;
  border: 1px solid color-mix(in srgb, var(--status-accent) 55%, var(--line));
  border-radius: 5px;
  background: color-mix(in srgb, var(--status-accent) 15%, var(--panel-raised));
  color: var(--text);
  font-size: 9px;
  font-weight: 800;
  white-space: nowrap;
}
.status-pill::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 2px;
  background: var(--status-accent);
}
.request-card__chevron {
  color: var(--muted);
  transition: transform .2s;
}
.request-card[open] .request-card__chevron {
  transform: rotate(180deg);
}
.request-card__preview {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 6px 11px;
  min-height: 35px;
  padding: 7px 12px 7px 15px;
  color: var(--muted);
  font-size: 10px;
}
.request-card__preview span + span::before {
  content: "·";
  margin-right: 11px;
  color: var(--accent);
}
.request-card__detail {
  padding: 12px 13px 13px 15px;
  border-top: 1px solid var(--line);
  background: var(--panel);
}
.request-card__detail > p {
  margin: 0 0 12px;
  color: var(--text);
  font-size: 11px;
  line-height: 1.55;
}
.request-card__detail dl {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 10px;
  margin: 0;
}
.request-card__detail dt {
  color: var(--muted);
  font-size: 9px;
}
.request-card__detail dd {
  margin: 2px 0 0;
  color: var(--text);
  font-size: 11px;
  font-weight: 700;
  overflow-wrap: anywhere;
}
.request-card__detail .detail-note {
  margin: 11px 0 0;
  padding: 7px 8px;
  border-radius: 6px;
  background: var(--accent-faint);
  color: var(--muted);
  font-size: 10px;
}
.empty-state {
  display: grid;
  justify-items: center;
  padding: 38px 18px;
  border: 1px dashed var(--line);
  border-radius: 12px;
  text-align: center;
}
.empty-state > span {
  color: var(--accent);
  font-size: 30px;
}
.empty-state h3 {
  margin: 6px 0 3px;
}
.empty-state p {
  margin: 0 0 16px;
  color: var(--muted);
}
.empty-state button {
  padding: 7px 11px;
  border: 1px solid var(--line);
  border-radius: 7px;
  background: var(--panel);
  color: var(--text);
}
.footer {
  margin-top: 38px;
  padding: 19px 0;
  border-top: 1px solid var(--line);
  color: var(--muted);
  font-size: 10px;
}
```

Leia a sequência como uma montagem:

- `.sector-list`: grade vertical que separa setores.
- `.sector`: moldura, recorte e superfície do grupo.
- `.sector > summary`: só o cabeçalho principal do setor recebe este Flex, preenchimento e fundo. O `>` evita selecionar os `summary` das requisições que estarão dentro dele.
- `.sector__icon`: quadrado do ícone, com base fixa no Flex.
- `.sector__heading`: agrupa nome e subtítulo; seus `strong` e `small` têm tamanhos distintos.
- `.sector__count`: margem automática à esquerda a empurra para a direita; borda e raio formam o selo de quantidade.
- `.sector__chevron`: seta com rotação animada. O seletor de setor aberto exige que a seta esteja no `summary` filho direto.
- `.sector__body`: padding e borda superior delimitam a área expandida. `.card-grid` distribui pedidos em duas colunas.
- `.request-card`: caixa de cada pedido; hover e transition suavizam a mudança da cor de borda.
- `.request-card > summary`: grade com uma coluna flexível para os textos e uma automática para a situação. A borda esquerda usa a cor da situação. `color-mix(in srgb, ... 22%, ...)` mistura 22% da primeira cor com o restante da segunda, no espaço de cor indicado.
- `.request-card__id`, `__title` e `__branch`: hierarquia do código, título e filial. O título é bloco e usa entrelinha própria. Ocultar overflow, sozinho, não significa que sempre haverá reticências.
- `.request-card__right`: agrupa situação e seta, alinhadas ao final com `justify-items: end`.
- `.status-pill`: selo com limite de largura e texto sem quebra. Mistura cores no fundo e na borda. Seu `::before` desenha o quadradinho da situação usando `content: ""`.
- `.request-card__chevron`: gira quando o pedido está aberto.
- `.request-card__preview`: distribui pequenos textos com quebra de linha. `span + span::before` põe “·” antes de cada span precedido imediatamente por outro span; por isso o primeiro não recebe separador.
- `.request-card__detail`: área detalhada. Seu parágrafo filho direto, a grade `dl` e os pares `dt`/`dd` recebem estilos diferentes. `overflow-wrap: anywhere` permite quebrar palavras longas para evitar estouro. `.detail-note` desenha o aviso final dentro dessa área.
- `.empty-state`: usa Grid e alinhamento para a mensagem de nenhum resultado; borda tracejada diferencia o estado. As regras seguintes tratam ícone, título, texto e botão.
- `.footer`: separação superior, padding, cor secundária e fonte pequena.

**Uma observação sobre o nome “preview”:** o nome da classe não define visibilidade. Como essa `div` estará dentro de um `details`, fora do `summary`, o navegador normalmente a oculta quando o cartão fecha, assim como os demais detalhes. Sempre observe a estrutura real, não só o nome escolhido pelo programador.

As regras reaproveitam padding, borda, fonte e layout já estudados. Para ler uma linha longa, separe-a em declarações terminadas por `;` e pergunte qual propriedade trata de caixa, texto, cor ou interação.

**Pare e pense / experimente:** Qual seletor faria uma regra atingir todos os `summary` dentro do setor? Qual atinge só o cabeçalho imediato?

**Conferência:** `.sector summary` alcança descendentes em qualquer nível. `.sector > summary` alcança apenas filhos diretos. Essa diferença importa quando há cartões expansíveis dentro de setores expansíveis.

### 2.9 — Relacionando dados a cores

Aqui existe uma ligação entre os nomes das situações no JavaScript e a aparência dos cartões.

**Digite no arquivo `styles.css`.** Este trecho corresponde às linhas 147–157 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```css
/* As cores reproduzem visualmente a legenda fornecida;
não são um mapeamento de códigos do ERP. */
[data-status="registered"], [data-status-key="registered"] {
  --status-accent: #e1e5ea;
}
[data-status="pending"], [data-status-key="pending"] {
  --status-accent: #a9cfff;
}
[data-status="approved"], [data-status-key="approved"] {
  --status-accent: #9ee8e8;
}
[data-status="partial"], [data-status-key="partial"] {
  --status-accent: #f8f19c;
}
[data-status="rejected"], [data-status-key="rejected"] {
  --status-accent: #f6b2bd;
}
[data-status="canceled"], [data-status-key="canceled"] {
  --status-accent: #afb8c1;
}
[data-status="released"], [data-status-key="released"] {
  --status-accent: #9be5a4;
}
[data-status="quotation"], [data-status-key="quotation"] {
  --status-accent: #f8b884;
}
[data-status="closed"], [data-status-key="closed"] {
  --status-accent: #f48e20;
}
```

Cada regra seleciona dois tipos de elemento: um cartão com `data-status` e uma entrada de legenda com `data-status-key`. Ambos recebem o mesmo valor de `--status-accent`.

A sequência corresponde a Cadastrado, Pendente, Aprovado, Parcial, Reprovado, Cancelado, Liberado, Em cotação e Baixado. As cores são rótulos ilustrativos; não deduzimos regras do ERP a partir delas.

Essa variável definida no cartão é herdada por suas partes internas, como o selo. Ela não precisa estar no `:root`, porque seu valor varia de cartão para cartão.

O CSS não traduz `pending` para “Pendente”. Essa tradução virá do catálogo de JavaScript. Para adicionar uma situação própria depois, você precisará pensar no valor de dados, no nome visível e na regra de cor correspondente.

**Pare e pense / experimente:** Se escrever `data-status="pendente"`, a regra `[data-status="pending"]` será aplicada?

**Conferência:** Não. Os valores precisam corresponder. A linguagem não traduz automaticamente a palavra entre português e inglês.

### 2.10 — Tela pequena e preferência por menos movimento

Uma media query aplica um conjunto de regras quando uma condição sobre o ambiente é atendida. As demais regras do arquivo continuam existindo.

**Digite no arquivo `styles.css`.** Este trecho corresponde às linhas 158–171 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```css
@media (max-width: 1180px) {
  .toolbar {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
  .field--search {
    grid-column: span 2;
  }
  .clear-button {
    justify-self: stretch;
  }
  .hero {
    grid-template-columns: minmax(0, 1fr) 270px;
    gap: 22px;
  }
}
@media (max-width: 920px) {
  .app-shell {
    display: block;
  }
  .sidebar {
    position: fixed;
    left: 0;
    top: 0;
    bottom: 0;
    width: min(265px, 86vw);
    transform: translateX(-102%);
    transition: transform .2s;
    box-shadow: var(--shadow);
  }
  .sidebar.is-open {
    transform: translateX(0);
  }
  .sidebar-backdrop:not([hidden]) {
    position: fixed;
    inset: 0;
    z-index: 35;
    background: rgba(1, 8, 12, .65);
    display: block;
  }
  .mobile-menu {
    display: inline-flex;
  }
  .metrics {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
@media (max-width: 700px) {
  .topbar__edition {
    display: none;
  }
  .hero {
    display: block;
    min-height: auto;
  }
  .hero__visual {
    display: none;
  }
  .email-grid, .card-grid {
    grid-template-columns: 1fr;
  }
  .toolbar {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
  .field--search {
    grid-column: 1 / -1;
  }
  .clear-button {
    grid-column: 1 / -1;
  }
  .section__tag {
    display: none;
  }
}
@media (max-width: 450px) {
  .topbar {
    padding: 0 15px;
  }
  .content {
    padding: 17px 15px 27px;
  }
  .theme-button span {
    display: none;
  }
  .topbar__right {
    gap: 8px;
  }
  .hero {
    padding: 24px 20px;
  }
  .metrics {
    gap: 8px;
  }
  .metric {
    min-height: 89px;
    padding: 11px;
  }
  .metric strong {
    font-size: 22px;
  }
  .section {
    margin-top: 34px;
  }
  .toolbar {
    grid-template-columns: 1fr;
  }
  .field--search, .clear-button {
    grid-column: auto;
  }
  .results-bar {
    align-items: flex-start;
    flex-direction: column;
  }
  .request-card__detail dl {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
@media (prefers-reduced-motion: reduce) {
  html {
    scroll-behavior: auto;
  }
  .sidebar, .sector__chevron, .request-card__chevron, .email-card__chevron {
    transition: none;
  }
}
```

`@media (max-width: 1180px)` significa largura de visualização até 1180px, inclusive. A barra ganha três colunas; a busca ocupa duas com `grid-column: span 2`; o botão se estica na célula. A apresentação reduz a coluna da ilustração para 270px e diminui o espaço entre colunas.

Até 920px, `.app-shell` passa a bloco. O menu torna-se `fixed`, preso ao lado esquerdo, com largura `min(265px, 86vw)`: o menor desses dois valores. `translateX(-102%)` desloca-o para fora da tela usando sua própria largura como referência. A classe `.is-open` zera esse deslocamento. A transição suaviza a mudança.

O backdrop sem `hidden` cobre a janela usando `inset: 0`, com fundo preto transparente e z-index entre conteúdo e menu. O botão móvel aparece e os indicadores passam a duas colunas.

Até 700px, o texto de edição e a ilustração desaparecem; a apresentação fica em bloco; cartões e e-mails usam uma coluna. Os filtros passam a duas colunas e busca/limpar ocupam a largura toda com `grid-column: 1 / -1`. O `-1` indica a última linha da grade explícita, não uma largura negativa. Os selos de seção são ocultados.

Até 450px, padding e espaços diminuem; o texto do botão de tema some, mas seu nome acessível continua disponível. Filtros usam uma coluna. `grid-column: auto` desfaz a ocupação explícita anterior. Os resultados se organizam em coluna. Os detalhes dos pedidos passam de três para duas colunas.

As condições são cumulativas: em 400px, todas as regras de largura anteriores também se aplicam e as declarações posteriores resolvem vários conflitos. Não são quatro páginas diferentes.

`prefers-reduced-motion: reduce` respeita a preferência por menos movimento: retira a rolagem suave e as transições indicadas.

**Ponto de conferência do CSS:** salve e recarregue. A página já deve ter cores, menu, apresentação e e-mails estilizados. Diminua a janela. O botão de menu aparece, mas só passará a abrir o menu quando escrevermos JavaScript. Contadores e requisições ainda dependem da próxima aula.

**Pare e pense / experimente:** Por que esconder o texto “Tema claro” no celular não deixa necessariamente o botão sem nome para um leitor de tela?

**Conferência:** O botão tem `aria-label`, que fornece seu nome acessível. Ao criar seus próprios botões só com ícones, você também precisa dar um nome que descreva a ação.

## Aula 3 — JavaScript: guardar informações, tomar decisões e reagir

Antes de escrever o `app.js`, abra o laboratório no navegador e suas ferramentas de desenvolvedor, na aba Console. Nos exemplos de laboratório, você pode digitar uma linha no Console e executar. As instruções abaixo pertencem ao Console, não ao HTML. Se executar uma declaração com `const` duas vezes no mesmo contexto e aparecer “already been declared”, recarregue o laboratório para começar de novo.

### 3.0 — Entenda os símbolos antes de encontrar as funções

```javascript
const nome = "Ana";
let quantidade = 2;
quantidade = quantidade + 1;
console.log(nome, quantidade);
```

`const` declara um nome que não poderá ser associado a outro valor depois. `let` declara um nome que aceita nova atribuição. `=` atribui o resultado à direita ao nome da esquerda; não significa comparação. Aspas delimitam um texto, chamado **string**. `2` é um número, sem aspas. `;` termina a instrução. `console.log` mostra informações no Console. O resultado é o nome e a quantidade 3.

Agora precisamos representar vários dados de um mesmo pedido:

```javascript
const pedido = {
  titulo: "Troca de teclado",
  quantidade: 2,
  email: false
};
console.log(pedido.titulo);
pedido.quantidade = 3;
```

O conjunto entre `{}` é um **objeto**, com propriedades no formato `nome: valor`. Vírgulas separam propriedades. `pedido.titulo` lê uma propriedade. `false` é um booleano, um valor lógico; seu outro valor é `true`. A string `"false"` não é o booleano `false`.

**Cuidado com uma ideia comum:** `const pedido` impede fazer `pedido = outroObjeto`, mas não impede mudar `pedido.quantidade`. O vínculo do nome é constante; o conteúdo do objeto pode ser mutável. O mesmo vale para um array.

```javascript
const titulos = ["Teclado", "Monitor", "Mouse"];
console.log(titulos[0]);
console.log(titulos.length);
```

Colchetes criam um **array**, uma lista ordenada. As posições começam em zero. `titulos[0]` é “Teclado”; `length` é 3. Um objeto pode estar dentro de um array, e suas propriedades podem conter outros objetos ou listas.

Uma **função** dá nome a uma tarefa:

```javascript
function dobrar(numero) {
  const resultado = numero * 2;
  return resultado;
}
console.log(dobrar(4));
```

`function` declara a função; `dobrar` é o nome escolhido; `numero` é um **parâmetro**, um nome para a entrada. Ao chamar `dobrar(4)`, o argumento 4 ocupa esse parâmetro. O corpo entre chaves é executado; `*` multiplica; `return` devolve 8 e termina essa chamada. Declarar a função não executa seu corpo. `dobrar` é a função; `dobrar(4)` é uma chamada.

O `resultado` criado dentro da função pertence àquele escopo; não se torna automaticamente um nome disponível fora dela. O projeto também terá funções que atualizam a tela, sem um `return` explícito. Elas retornam `undefined` implicitamente, mas seu trabalho importante é o efeito produzido na página.

Outra forma de escrever uma função pequena é a **arrow function**:

```javascript
const dobrarCurto = (numero) => numero * 2;
```

`=>` separa parâmetros e corpo. Quando o corpo é uma expressão sem chaves, seu resultado é retornado implicitamente. Com um bloco `{ ... }`, use `return` quando quiser devolver um resultado. Uma arrow e uma função tradicional têm outras diferenças, como o tratamento de `this`; neste projeto as arrows servem principalmente como pequenas tarefas passadas para métodos.

Vamos conhecer quatro métodos de listas:

```javascript
const numeros = [1, 2, 3];
console.log(numeros.map((n) => n * 2));
console.log(numeros.filter((n) => n > 1));
console.log(numeros.find((n) => n > 1));
numeros.forEach((n) => console.log(n));
```

| Método | Trabalho | Resultado deste exemplo |
| --- | --- | --- |
| `map` | Transforma cada item e cria outra lista. | `[2, 4, 6]` |
| `filter` | Mantém os itens cujo teste é verdadeiro. | `[2, 3]` |
| `find` | Devolve o primeiro item que satisfaz o teste, ou `undefined`. | `2` |
| `forEach` | Executa uma ação para cada item; não constrói uma lista de resultados. | Mostra 1, 2 e 3 no Console. |

A função passada ao método é uma **callback**: o método a chama nos momentos necessários. Os parâmetros como `n`, `request` e `sector` são nomes escolhidos pelo autor. Não precisam ser declarados fora da própria callback.

### Uma ponte entre JavaScript e HTML

O navegador representa a página como uma árvore de objetos chamada **DOM**. `document` dá acesso ao documento. `document.querySelector("h1")` encontra o primeiro elemento que corresponde ao seletor. Para alterar apenas texto, podemos fazer:

```javascript
document.querySelector("h1").textContent = "Eu alterei este título";
```

Experimente no Console do laboratório. A mudança aparece na página, mas não reescreve seu arquivo HTML. Ao recarregar, o arquivo é lido outra vez.

`querySelector` devolve `null` se não encontra o elemento. Tentar acessar `.textContent` ou `.addEventListener` de `null` gera erro. Por isso os IDs do HTML e do JavaScript devem coincidir, e o script precisa executar quando os elementos já existem.

Agora escreva o `app.js` vazio com os blocos a seguir. Durante a digitação, funções ainda não declaradas e chaves ainda abertas podem tornar o arquivo incompleto. A primeira conferência do painel funcionando vem depois de `init();`, ao final da aula. Use os exemplos de laboratório para experimentar conceitos antes disso.

### 3.1 — const, arrays e objetos de situações e setores

Vamos começar pelos vocabulários do painel. Eles dizem quais situações e quais setores existem.

**Digite no arquivo `app.js`.** Este trecho corresponde às linhas 1–21 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```javascript
/* Protótipo sem conexão: os dados e situações abaixo servem apenas para validar a interface. */
const statusCatalog = [
  { key: "registered", label: "Cadastrado" },
  { key: "pending", label: "Pendente" },
  { key: "approved", label: "Aprovado" },
  { key: "partial", label: "Parcial" },
  { key: "rejected", label: "Reprovado" },
  { key: "canceled", label: "Cancelado" },
  { key: "released", label: "Liberado" },
  { key: "quotation", label: "Em cotação" },
  { key: "closed", label: "Baixado" },
];

const sectors = [
  { key: "operations", label: "Operações", subtitle: "Materiais de uso diário", icon: "◫" },
  { key: "maintenance", label: "Manutenção", subtitle: "Peças e serviços", icon: "⚙" },
  { key: "facilities", label: "Facilities", subtitle: "Infraestrutura e apoio", icon: "▤" },
  { key: "technology", label: "Tecnologia", subtitle: "Equipamentos e suporte", icon: "⌘" },
  { key: "supply", label: "Suprimentos", subtitle: "Abastecimento e consumo", icon: "◇" },
];

```

O comentário inicial declara o propósito demonstrativo. `const statusCatalog = [` cria o nome da lista de situações. Cada `{ key: ..., label: ... }` é um objeto. `key` é o valor interno e `label` é o nome mostrado. Não existe tradução automática: cada par foi escrito explicitamente.

As nove entradas seguem a mesma estrutura. A linha final `];` fecha o array e termina a declaração. A vírgula depois do último objeto é permitida em JavaScript e facilita acrescentar itens. Isso não faz do arquivo um documento JSON: ele também contém declarações, funções e comentários, que não fazem parte do formato JSON.

`sectors` é outra lista. Cada setor contém `key`, `label`, `subtitle` e `icon`. O ícone é um caractere de texto. Os cinco valores internos são `operations`, `maintenance`, `facilities`, `technology` e `supply`. Serão usados para relacionar pedidos a setores.

Os nomes `statusCatalog` e `sectors` são escolhas do projeto. O mesmo conceito pode servir a categorias de livros, matérias escolares ou áreas de uma oficina.

**Pare e pense / experimente:** Qual valor deveria aparecer na tela: `quotation` ou “Em cotação”? Qual valor deve permanecer consistente no código?

**Conferência:** “Em cotação” é o rótulo legível. `quotation` é a chave usada para relacionar registros, filtros e regra de cor. Você pode inventar outras chaves, desde que atualize todas as relações correspondentes.

### 3.2 — Os doze pedidos e seus tipos de dados

Cada pedido é um objeto. Para facilitar sua digitação, você pode colocar uma propriedade por linha dentro de cada objeto; preserve aspas, vírgulas, chaves e valores.

**Digite no arquivo `app.js`.** Este trecho corresponde às linhas 22–36 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```javascript
const requests = [
  { id: "20101", sector: "operations", status: "registered", branch: "10", title: "Materiais de embalagem para a operação", description: "Reposição de insumos para a área operacional. Registro demonstrativo sem vínculo com o ERP.", reference: "24/09/2026", deadline: "29/09/2026", item: "Insumos de embalagem", email: false },
  { id: "20102", sector: "operations", status: "pending", branch: "10", title: "Reposição de fitas para expedição", description: "Solicitação fictícia de material de uso recorrente da expedição.", reference: "24/09/2026", deadline: "30/09/2026", item: "Fita adesiva", email: true },
  { id: "20103", sector: "operations", status: "quotation", branch: "05", title: "Equipamentos de apoio à separação", description: "Exemplo de cartão com acompanhamento de cotação, sem preço ou fornecedor real.", reference: "23/09/2026", deadline: "02/10/2026", item: "Equipamento de apoio", email: false },
  { id: "20104", sector: "maintenance", status: "approved", branch: "05", title: "Componentes para manutenção preventiva", description: "Peças e materiais descritos de forma resumida. O detalhamento de itens dependerá do contrato com o Rodopar.", reference: "23/09/2026", deadline: "30/09/2026", item: "Componentes diversos", email: true },
  { id: "20105", sector: "maintenance", status: "partial", branch: "01", title: "Serviços de revisão de equipamentos", description: "O rótulo “Parcial” é visual. Seu significado operacional ainda precisa ser confirmado.", reference: "22/09/2026", deadline: "03/10/2026", item: "Serviço de revisão", email: false },
  { id: "20106", sector: "maintenance", status: "released", branch: "01", title: "Ferramentas para equipe técnica", description: "Exemplo de requisição liberada, sem presumir entrega, pagamento ou baixa.", reference: "22/09/2026", deadline: "01/10/2026", item: "Ferramentas manuais", email: false },
  { id: "20107", sector: "facilities", status: "rejected", branch: "04", title: "Adequações no espaço de apoio", description: "Registro fictício usado para mostrar a cor e a leitura de uma situação reprovada.", reference: "20/09/2026", deadline: "Não informado", item: "Serviço predial", email: false },
  { id: "20108", sector: "facilities", status: "canceled", branch: "04", title: "Materiais para pequena reforma", description: "Exemplo cancelado. Não há motivo ou histórico de cancelamento real nesta prévia.", reference: "20/09/2026", deadline: "Não informado", item: "Materiais prediais", email: false },
  { id: "20109", sector: "technology", status: "closed", branch: "01", title: "Periféricos para estação de trabalho", description: "O estado ilustrativo “Baixado” não indica pagamento nem confirma recebimento.", reference: "19/09/2026", deadline: "Não informado", item: "Periféricos", email: false },
  { id: "20110", sector: "technology", status: "pending", branch: "10", title: "Suporte de rede para unidade", description: "Solicitação demonstrativa de suporte técnico e peças de infraestrutura.", reference: "24/09/2026", deadline: "28/09/2026", item: "Componentes de rede", email: true },
  { id: "20111", sector: "supply", status: "quotation", branch: "16", title: "Materiais de limpeza e consumo", description: "Exemplo de requisição em cotação, com itens resumidos para a primeira visualização.", reference: "24/09/2026", deadline: "05/10/2026", item: "Materiais de consumo", email: false },
  { id: "20112", sector: "supply", status: "approved", branch: "19", title: "Água para área administrativa", description: "Requisição fictícia para validar o agrupamento por setor e as cores de situação.", reference: "21/09/2026", deadline: "30/09/2026", item: "Galões de água", email: false },
];

```

Leia o primeiro objeto como uma ficha:

| Propriedade | Significado nesta interface |
| --- | --- |
| `id` | Código do pedido como texto. Use valores únicos; os conjuntos de cartões abertos usam esse código. |
| `sector` | Chave de um setor existente em `sectors`. |
| `status` | Chave de uma situação existente em `statusCatalog`. |
| `branch` | Código da filial como texto; `"01"` conserva o zero inicial. |
| `title` | Título curto do cartão. |
| `description` | Explicação mostrada ao expandir. |
| `reference` | Data de referência apresentada como texto. |
| `deadline` | Texto do prazo; pode ser “Não informado”. |
| `item` | Resumo do material ou serviço. |
| `email` | Booleano que marca a associação fictícia a e-mail. |

Os outros onze objetos repetem exatamente o formato com conteúdos diferentes. Não são onze regras novas de programação. Operações e Manutenção têm três registros cada; Facilities, Tecnologia e Suprimentos têm dois cada. Três registros têm `email: true`.

Datas estão escritas como strings. Este programa não calcula atraso nem compara datas cronologicamente. O texto “Baixado” também não comprova pagamento. Dados e regras de negócio são decisões que precisam ser definidas, não inferidas da aparência.

Digitar `email: "false"` seria um erro de significado: a string não vazia é tratada como verdadeira em testes booleanos comuns. Digite o booleano sem aspas.

**Pare e pense / experimente:** Por que `branch: "01"` é texto, enquanto `email: true` não está entre aspas?

**Conferência:** A filial é um código que precisa manter sua representação. `email` representa uma condição de sim/não que será usada em decisões. Escolher o tipo certo evita interpretações erradas.

### 3.3 — state: o que a pessoa escolheu agora

As requisições são os dados. O estado guarda as escolhas atuais de visualização. Separar os dois permite filtrar sem apagar pedidos.

**Digite no arquivo `app.js`.** Este trecho corresponde às linhas 37–45 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```javascript
const state = {
  query: "",
  sector: "",
  status: "",
  email: "",
  openSectors: new Set(sectors.map((sector) => sector.key)),
  openCards: new Set(),
};

```

`state` é um objeto. `query`, `sector`, `status` e `email` começam com strings vazias. Neste programa, vazio significa que a pessoa não aplicou aquele filtro.

`Set` é uma coleção de valores únicos. `new Set()` cria uma coleção vazia. `new` constrói uma instância. Para comparar: uma lista pode ter `['a', 'a']`; um conjunto criado a partir dela terá apenas um `'a'`.

Desmonte a linha de `openSectors` em duas etapas mentais:

```javascript
// Laboratório de leitura: esta decomposição explica a linha do bloco original.
const chaves = sectors.map((sector) => sector.key);
const setoresAbertos = new Set(chaves);
```

`map` percorre os objetos e extrai a chave de cada um. O conjunto guarda essas chaves; por isso os setores começam abertos. `openCards` começa vazio; os pedidos individuais começam fechados.

Como `state` foi declarado com `const`, não reatribuímos o objeto inteiro. É permitido mudar `state.query` ou substituir `state.openCards` por outro conjunto. São propriedades internas do objeto.

Este estado está na memória da página. Recarregar recria seus valores iniciais. Ele não é um banco de dados.

**Pare e pense / experimente:** Se usar `new Set()` também em `openSectors`, como começarão os setores?

**Conferência:** Fechados, porque a montagem de cada setor verificará se sua chave pertence ao conjunto. Sem chaves, nenhum receberá o atributo `open` inicialmente.

### 3.4 — Guardar referências aos elementos da página

Precisaremos consultar os campos e preencher a lista muitas vezes. Vamos localizar esses elementos e dar nomes às referências.

**Digite no arquivo `app.js`.** Este trecho corresponde às linhas 46–52 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```javascript
const sectorList = document.querySelector("#sector-list");
const emptyState = document.querySelector("#empty-state");
const searchInput = document.querySelector("#search-input");
const sectorFilter = document.querySelector("#sector-filter");
const statusFilter = document.querySelector("#status-filter");
const emailFilter = document.querySelector("#email-filter");

```

Cada linha declara uma constante que recebe o resultado de `document.querySelector`. O `#` significa ID no seletor.

`sectorList` aponta para o recipiente dos setores; `emptyState`, para o aviso de lista vazia; `searchInput`, para o campo de busca; `sectorFilter`, `statusFilter` e `emailFilter`, para as três seleções.

Esses nomes não contêm uma cópia do HTML em formato de texto. Eles referenciam objetos do DOM. Mudar `searchInput.value` muda o valor do campo correspondente.

`const searchInput` permite manter a mesma referência, mas não impede editar propriedades do elemento. O `defer` escrito no HTML ajuda a garantir que o navegador já tenha analisado esses elementos antes de executar as buscas.

**Pare e pense / experimente:** O que acontece se o HTML tiver `id="search-input"`, mas esta linha procurar `"#searchInput"`?

**Conferência:** A busca não encontra o elemento e retorna `null`. Os nomes precisam ser exatamente os mesmos. Um erro posterior pode aparecer ao tentar usar uma propriedade dessa referência inexistente.

### 3.5 — escapeHtml: mostrar dados como texto

Mais adiante montaremos HTML com textos dos pedidos. Antes disso, precisamos impedir que caracteres desses textos sejam confundidos com marcação.

**Digite no arquivo `app.js`.** Este trecho corresponde às linhas 53–59 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```javascript
function escapeHtml(value) {
  // Valores de integração futura também deverão entrar na interface como texto, nunca como HTML executável.
  return String(value).replace(/[&<>"']/g, (character) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
  })[character]);
}

```

`function escapeHtml(value)` recebe um valor. `String(value)` o converte para texto. O método `.replace(...)` procura partes desse texto e substitui cada correspondência.

`/[&<>"']/g` é uma expressão regular. As barras delimitam o padrão; os colchetes significam “um destes caracteres”; o `g` pede todas as correspondências. O padrão encontra `&`, `<`, `>`, aspas duplas e aspas simples.

A arrow recebe um caractere encontrado. Dentro de `({ ... })` está um objeto usado como mapa de substituição. Os parênteses permitem que as chaves sejam lidas como um objeto devolvido, não como o bloco de comandos da arrow. `[character]` acessa a propriedade cujo nome é o caractere recebido.

O mapa converte `&` em `&amp;`, `<` em `&lt;`, `>` em `&gt;`, aspas duplas em `&quot;` e simples em `&#39;`. O `return` devolve o texto transformado. Exemplo: o texto `<b>oi</b>` é preparado para aparecer literalmente, em vez de criar um elemento `b` quando inserido como HTML.

Essa função foi feita para os contextos de texto e atributos HTML entre aspas usados aqui. Ela não é uma solução universal para inserir dados em JavaScript, CSS ou URLs. Quando se quer mudar somente texto, `textContent` costuma evitar a necessidade de montar HTML.

**Pare e pense / experimente:** No Console do painel depois de completar a aula, execute `escapeHtml("A & B < C")`. Que transformações espera?

**Conferência:** O resultado deve ser `A &amp; B &lt; C`. O primeiro `&` e o sinal `<` precisam ser tratados para preservar sua apresentação como texto.

### 3.6 — searchable: buscar sem diferença de maiúsculas e acentos

Quem busca “operacao” normalmente também espera encontrar texto com acentos. A função prepara uma versão adequada à comparação.

**Digite no arquivo `app.js`.** Este trecho corresponde às linhas 60–63 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```javascript
function searchable(value) {
  return String(value).normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLocaleLowerCase("pt-BR");
}

```

`searchable(value)` converte a entrada para string. `.normalize("NFD")` decompõe caracteres quando existe uma forma canônica apropriada: uma letra acentuada pode ser representada por letra-base e marca de acento.

`.replace(/[̀-ͯ]/g, "")` remove marcas combinantes nessa faixa de códigos Unicode. O hífen dentro dos colchetes indica intervalo. A substituição é o texto vazio. Isso cobre as marcas relevantes aos exemplos comuns de português; não é uma regra universal para todos os sistemas de escrita.

`.toLocaleLowerCase("pt-BR")` passa o texto para minúsculas com a localidade indicada. Os pontos encadeiam operações: o resultado de uma vira entrada da próxima.

`return` entrega a versão preparada, sem modificar o texto original do pedido. A busca pode comparar “manutencao” com “Manutenção”, enquanto o cartão continua exibindo a grafia original.

**Pare e pense / experimente:** Qual deve ser o resultado de `searchable("MANUTENÇÃO")`?

**Conferência:** `manutencao`. O nome mostrado no cartão não precisa perder acentos só porque a busca normaliza a comparação.

### 3.7 — statusLabel: procurar um rótulo e lidar com ausência

Esta função traduz a chave interna para o texto que a pessoa verá.

**Digite no arquivo `app.js`.** Este trecho corresponde às linhas 64–67 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```javascript
function statusLabel(key) {
  return statusCatalog.find((status) => status.key === key)?.label ?? "Não classificado";
}

```

`statusCatalog.find(...)` procura o primeiro objeto que passe no teste da callback. O parâmetro `status` representa um objeto do catálogo a cada tentativa.

`status.key === key` compara a chave do objeto com o parâmetro da função. `===` é igualdade estrita; não confunda com `=`, que atribui um valor.

Quando `find` acha, devolve o objeto. Quando não acha, devolve `undefined`. `?.label` é acesso opcional: se o resultado for `null` ou `undefined`, não tenta ler a propriedade de um objeto ausente. `??` fornece “Não classificado” quando o resultado à esquerda é `null` ou `undefined`.

Não confunda `??` com `||`. O primeiro só usa a alternativa nessas duas ausências; `||` também usa a alternativa diante de valores falsy como string vazia, zero e `false`.

Ao chamar `statusLabel("approved")`, recebemos “Aprovado”. Um valor desconhecido recebe o texto de reserva.

**Pare e pense / experimente:** Por que simplesmente escrever `.find(...).label` pode quebrar?

**Conferência:** Se nenhuma entrada corresponder, `find` devolve `undefined`. Acessar `.label` diretamente nessa ausência lança um erro. O acesso opcional e a alternativa tratam esse caso.

### 3.8 — cardHtml: construir uma requisição com os seus dados

Agora vamos reunir HTML e dados. A função recebe um pedido e devolve o texto HTML do cartão. Ela ainda não coloca esse texto na página.

**Digite no arquivo `app.js`.** Este trecho corresponde às linhas 68–84 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```javascript
function cardHtml(request) {
  const { id, status, branch, title, description, reference, deadline, item, email } = request;
  return `
    <details class="request-card" data-card-id="${escapeHtml(id)}" data-status="${escapeHtml(status)}" ${state.openCards.has(id) ? "open" : ""}>
      <summary aria-label="Requisição ${escapeHtml(id)}: ${escapeHtml(title)}, situação ${escapeHtml(statusLabel(status))}">
        <span><span class="request-card__id">REQ. ${escapeHtml(id)}</span><strong class="request-card__title">${escapeHtml(title)}</strong><span class="request-card__branch">Filial ${escapeHtml(branch)}</span></span>
        <span class="request-card__right"><span class="status-pill">${escapeHtml(statusLabel(status))}</span><span class="request-card__chevron" aria-hidden="true">⌄</span></span>
      </summary>
      <div class="request-card__preview"><span>${escapeHtml(item)}</span><span>Ref. ${escapeHtml(reference)}</span><span>${email ? "E-mail associado" : "Sem e-mail"}</span></div>
      <div class="request-card__detail">
        <p>${escapeHtml(description)}</p>
        <dl><div><dt>Filial</dt><dd>${escapeHtml(branch)}</dd></div><div><dt>Referência</dt><dd>${escapeHtml(reference)}</dd></div><div><dt>Limite</dt><dd>${escapeHtml(deadline)}</dd></div><div><dt>Item resumido</dt><dd>${escapeHtml(item)}</dd></div><div><dt>Situação</dt><dd>${escapeHtml(statusLabel(status))}</dd></div><div><dt>E-mail</dt><dd>${email ? "Sim, ilustrativo" : "Não"}</dd></div></dl>
        <p class="detail-note">Detalhes da primeira etapa. Itens completos, anexos, baixas e cotações dependerão da leitura homologada do Rodopar.</p>
      </div>
    </details>`;
}

```

A primeira linha do corpo usa **desestruturação**: `const { id, status, ... } = request` cria nomes locais com as propriedades de mesmo nome. `id` passa a valer `request.id`, `title` passa a valer `request.title`, e assim por diante. As reticências nesta explicação abreviam a leitura; no código mostrado você digita todos os nomes explicitamente.

Depois de `return`, o caractere usado é a crase simples de JavaScript, que abre uma **template literal**. Ela pode conter várias linhas. `${expressao}` calcula uma expressão e insere seu resultado no texto. Aspas normais não fazem essa interpolação.

Leia o cartão por partes:

1. `details.request-card` envolve o pedido. `data-card-id` guarda seu código no DOM e `data-status` escolhe a regra de cor do CSS.
2. `state.openCards.has(id)` pergunta se o conjunto contém o código. `condicao ? a : b` é um operador ternário: se verdadeiro, usa `a`; caso contrário, `b`. Aqui ele insere `open` ou nada, para reconstruir o estado do cartão.
3. O `summary` recebe um nome acessível com código, título e situação. O primeiro `span` externo agrupa código, título em `strong` e filial.
4. `request-card__right` agrupa selo de situação e seta. `statusLabel(status)` obtém o nome, e `escapeHtml(...)` prepara o resultado para inserção.
5. `div.request-card__preview` agrupa item, data e a indicação de e-mail. O ternário usa o booleano `email` para escolher uma das duas frases.
6. `div.request-card__detail` agrupa descrição e ficha. O `p` contém a descrição preparada.
7. `dl` é uma lista de descrições: cada `dt` é o nome de um campo e cada `dd` é o valor. As seis `div` internas agrupam Filial, Referência, Limite, Item resumido, Situação e E-mail. Cada par pode ocupar uma célula de Grid.
8. O último `p.detail-note` dá contexto sobre funcionalidades futuras. Depois fechamos detalhe, cartão e template literal.

`data-card-id` será acessado em JavaScript como `dataset.cardId`. O hífen vira camelCase no nome da propriedade. Esses atributos carregam strings; não se tornam números ou booleanos automaticamente.

A função gera um cartão para qualquer objeto com o formato esperado. É por isso que não escrevemos doze cartões à mão no HTML principal.

**Pare e pense / experimente:** O que `cardHtml(requests[0])` devolve? Um elemento DOM já inserido ou uma string?

**Conferência:** Uma string com HTML. A função `render`, que ainda vamos escrever, colocará o resultado no recipiente da página. `cardHtml` descreve um cartão; `render` atualiza a tela.

### 3.9 — sectorHtml: um grupo contendo vários cartões

A ideia anterior se repete em outra escala: um setor tem cabeçalho e uma coleção de requisições.

**Digite no arquivo `app.js`.** Este trecho corresponde às linhas 85–97 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```javascript
function sectorHtml(sector, matchingRequests) {
  return `
    <details class="sector" data-sector-id="${escapeHtml(sector.key)}" ${state.openSectors.has(sector.key) ? "open" : ""}>
      <summary aria-label="Setor ${escapeHtml(sector.label)}, ${matchingRequests.length} requisições">
        <span class="sector__icon" aria-hidden="true">${escapeHtml(sector.icon)}</span>
        <span class="sector__heading"><strong>${escapeHtml(sector.label)}</strong><small>${escapeHtml(sector.subtitle)}</small></span>
        <span class="sector__count">${matchingRequests.length} ${matchingRequests.length === 1 ? "requisição" : "requisições"}</span>
        <span class="sector__chevron" aria-hidden="true">⌄</span>
      </summary>
      <div class="sector__body"><div class="card-grid">${matchingRequests.map(cardHtml).join("")}</div></div>
    </details>`;
}

```

A função recebe dois parâmetros: `sector`, o objeto do setor, e `matchingRequests`, a lista de pedidos desse setor que passaram nos filtros.

O `details.sector` tem `data-sector-id` e consulta `state.openSectors.has(sector.key)` para decidir se recebe `open`. O cabeçalho junta ícone, nome, subtítulo, quantidade e seta.

`sector__heading` é um `span` que agrupa `strong` e `small`. `matchingRequests.length` é a quantidade de itens. O ternário compara essa quantidade com 1 para escolher “requisição” no singular ou “requisições” no plural. A linguagem não pluraliza automaticamente.

`div.sector__body` guarda o conteúdo expandido. Dentro dela, `div.card-grid` organiza os cartões. A expressão `matchingRequests.map(cardHtml)` chama a função de cartão para cada pedido. Passamos a função pelo nome, sem chamá-la antes. `map` também oferece índice e array às callbacks; `cardHtml` usa apenas o primeiro parâmetro declarado.

O resultado de `map` é uma lista de strings. `.join("")` junta essas strings sem separador. Sem especificar o separador, `join` usaria vírgulas; não queremos vírgulas extras entre cartões.

O setor devolve outra string HTML. O agrupamento se forma assim: cada pedido vira um cartão; vários cartões viram o corpo de um setor; vários setores formarão a lista.

**Pare e pense / experimente:** Se `matchingRequests` tiver dois pedidos, quantas vezes `cardHtml` será chamada nesta montagem?

**Conferência:** Duas vezes. Haverá duas strings de cartão que serão unidas dentro de `card-grid`. A contagem do setor será 2.

### 3.10 — matches: decidir se um pedido aparece

Aqui estão as regras da busca. A função responde uma pergunta com `true` ou `false`: este pedido atende às escolhas atuais?

**Digite no arquivo `app.js`.** Este trecho corresponde às linhas 98–107 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```javascript
function matches(request) {
  if (state.sector && request.sector !== state.sector) return false;
  if (state.status && request.status !== state.status) return false;
  if (state.email === "with" && !request.email) return false;
  if (state.email === "without" && request.email) return false;
  if (!state.query) return true;
  const sectorName = sectors.find((sector) => sector.key === request.sector)?.label ?? "";
  return searchable([request.id, request.branch, request.title, request.description, request.item, sectorName, statusLabel(request.status)].join(" ")).includes(searchable(state.query));
}

```

`if (condicao)` executa a instrução seguinte quando a condição é verdadeira. Um `return false` encerra imediatamente a chamada atual. Ele não continua testando as linhas seguintes.

Primeira regra: `state.sector && request.sector !== state.sector`. `&&` é o “e” com curto-circuito: só avalia a direita quando a esquerda é truthy. String vazia é falsy. Assim, apenas quando existe um filtro de setor e o pedido tem setor diferente (`!==`) ele é recusado.

A segunda regra repete essa lógica para a situação. A terceira recusa pedidos sem e-mail quando o filtro é `with`; `!request.email` é a negação do booleano. A quarta recusa os que têm e-mail quando o filtro é `without`.

Se não há texto de busca (`!state.query`), o pedido é aceito, porque já sobreviveu aos filtros anteriores. Esse retorno não ignora os filtros; eles foram avaliados antes.

Se existe busca, `find` localiza o nome do setor. Depois a função junta código, filial, título, descrição, item, nome do setor e nome da situação em um único texto, separados por espaços. `searchable` prepara esse texto e a consulta. `.includes(...)` verifica se a consulta aparece como uma sequência dentro do texto preparado.

Exemplo de raciocínio: escolha Manutenção e Pendente. Um pedido de Manutenção com situação Aprovado passa pela primeira condição, falha na segunda e recebe `false`. Os filtros são combinados, não alternativos.

Esta busca é por trecho de texto; não é uma busca inteligente por significado. Um termo desconhecido não recebe sinônimos automaticamente.

**Pare e pense / experimente:** Se o filtro de setor está vazio, `request.sector !== ""` excluirá todos os pedidos?

**Conferência:** Não, porque o lado esquerdo `state.sector` do `&&` é uma string vazia. A condição não passa, e o retorno de exclusão dessa linha não acontece.

### 3.11 — render: transformar o estado atual em tela

“Renderizar”, neste projeto, significa montar a representação visual dos dados atuais e atualizar os elementos correspondentes.

**Digite no arquivo `app.js`.** Este trecho corresponde às linhas 108–120 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```javascript
function render() {
  // Os indicadores contam apenas os registros filtrados. Nenhum estado fictício é classificado aqui como “aberto”.
  const matching = requests.filter(matches);
  const groups = sectors.map((sector) => ({ sector, items: matching.filter((request) => request.sector === sector.key) })).filter(({ items }) => items.length);
  sectorList.innerHTML = groups.map(({ sector, items }) => sectorHtml(sector, items)).join("");
  emptyState.hidden = matching.length !== 0;
  document.querySelector("#metric-total").textContent = String(matching.length);
  document.querySelector("#metric-sectors").textContent = String(groups.length);
  document.querySelector("#metric-email").textContent = String(matching.filter((request) => request.email).length);
  document.querySelector("#metric-status").textContent = String(new Set(matching.map((request) => request.status)).size);
  document.querySelector("#results-count").textContent = `${matching.length} ${matching.length === 1 ? "requisição encontrada" : "requisições encontradas"} em ${groups.length} ${groups.length === 1 ? "setor" : "setores"}`;
}

```

Leia uma instrução de cada vez:

- `requests.filter(matches)` chama o teste para cada pedido e cria `matching`, uma nova lista só com os aceitos. O array original `requests` não é apagado por esse filtro.
- `sectors.map(...)` percorre os setores. Para cada um cria um objeto `{ sector, items: ... }`. A propriedade abreviada `sector` equivale a `sector: sector`.
- O `filter` interno escolhe de `matching` somente os pedidos cuja chave de setor corresponde à chave atual. Cada objeto de grupo guarda o setor e sua lista de itens.
- O `.filter(({ items }) => items.length)` final remove grupos sem itens. A callback desestrutura o objeto recebido para acessar `items`. Zero é falsy; comprimentos positivos são truthy.
- `groups.map(...)` transforma os grupos em strings com `sectorHtml`. A desestruturação fornece `sector` e `items` a essa callback. `join("")` une o resultado.
- `sectorList.innerHTML = ...` interpreta esse texto como HTML e substitui os filhos atuais do recipiente. Agora os cartões aparecem. Por isso os textos variáveis foram preparados com `escapeHtml`.
- `emptyState.hidden = matching.length !== 0`: se há algum resultado, esconde o aviso; se há zero, a comparação dá `false` e o aviso aparece.
- `textContent` atualiza os contadores como texto. `String(...)` torna explícita a conversão do número.
- `matching.length` conta pedidos; `groups.length` conta setores com resultado; outro `filter` conta pedidos com `email` verdadeiro.
- Para situações distintas, `map` extrai as chaves e `new Set(...)` remove duplicações. `.size` conta valores no conjunto. Array usa `length`; Set usa `size`.
- O último texto monta uma frase com números e singular/plural.

**Vamos seguir um caso concreto:** sem filtros, existem 12 pedidos, 5 setores, 3 pedidos com e-mail e 9 situações distintas. Selecionando Manutenção, passam a ser 3 pedidos, 1 setor, 1 pedido com e-mail e 3 situações. A caixa com os dois e-mails fictícios e a ilustração da apresentação continuam fixas.

Cada `render` recria os elementos dos setores. Os conjuntos em `state` guardam quais devem reaparecer abertos. Esse mecanismo é diferente de guardar estado dentro das tags que serão substituídas. Uma aplicação mais complexa também precisaria planejar preservação de foco e outras interações ao reconstruir partes da página.

**Pare e pense / experimente:** Com uma busca que não encontra nada, quais valores aparecem e qual mensagem se torna visível?

**Conferência:** Os quatro indicadores vão para zero, a lista de setores fica vazia e aparece o aviso “Nenhuma requisição encontrada”. Os dados originais continuam no array.

### 3.12 — resetFilters: limpar modelo e controles

O que a pessoa vê nos campos e o que o programa usa para filtrar precisam concordar.

**Digite no arquivo `app.js`.** Este trecho corresponde às linhas 121–133 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```javascript
function resetFilters() {
  state.query = "";
  state.sector = "";
  state.status = "";
  state.email = "";
  searchInput.value = "";
  sectorFilter.value = "";
  statusFilter.value = "";
  emailFilter.value = "";
  render();
  searchInput.focus();
}

```

As quatro primeiras atribuições esvaziam as escolhas guardadas em `state`. As quatro seguintes esvaziam os campos visíveis pelo atributo de objeto `.value`.

Isso é necessário porque o estado e os controles são coisas diferentes. Limpar só `state` pode mostrar uma lista completa enquanto o campo ainda parece filtrado. Limpar só os campos pode deixar `matches` lendo filtros antigos.

`render()` atualiza os resultados com o estado novo. `searchInput.focus()` leva o foco ao campo de busca para a pessoa continuar pelo teclado. A função não retorna uma lista porque seu trabalho é produzir efeitos na interface.

**Pare e pense / experimente:** Por que a função limpa tanto `state.query` quanto `searchInput.value`?

**Conferência:** Um é a escolha que o programa consulta; o outro é o texto do controle na tela. A função sincroniza os dois antes de redesenhar os resultados.

### 3.13 — applyTheme: uma mudança na raiz altera a paleta

Vamos conectar o atributo escrito na primeira tag HTML às variáveis de CSS que você já estudou.

**Digite no arquivo `app.js`.** Este trecho corresponde às linhas 134–140 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```javascript
function applyTheme(theme) {
  document.documentElement.dataset.theme = theme;
  const button = document.querySelector("#theme-toggle");
  button.innerHTML = theme === "dark" ? '☀ <span>Tema claro</span>' : '☾ <span>Tema escuro</span>';
  button.setAttribute("aria-label", theme === "dark" ? "Ativar tema claro" : "Ativar tema escuro");
}

```

`document.documentElement` é o elemento `html`, a raiz. `.dataset.theme = theme` altera seu atributo `data-theme`. Esse é o ponto em que o JavaScript aciona as regras `html[data-theme="light"]` do CSS.

A constante local `button` guarda o botão de tema. Seu `innerHTML` recebe um símbolo e um `span` com texto fixo. Se o tema atual é escuro, a ação oferecida é “Tema claro”; caso contrário, “Tema escuro”. O texto do botão descreve o que acontecerá ao clicar, não apenas o estado atual.

`setAttribute` atualiza `aria-label` para que o nome acessível também descreva essa ação. A função ainda não salva a preferência; veremos o salvamento na inicialização.

Como o HTML inserido nesse botão é composto de literais fixos conhecidos no código, não há texto de pedido entrando nesse `innerHTML`. O contexto é diferente da montagem de cartões com dados variáveis.

**Pare e pense / experimente:** Que três coisas esta função muda?

**Conferência:** O atributo do tema na raiz, o símbolo/texto visível do botão e seu nome acessível. O CSS reage à primeira mudança para recolorir a página.

### 3.14 — setMenuOpen: mostrar menu e acompanhar o estado

A função recebe um booleano: `true` para abrir e `false` para fechar.

**Digite no arquivo `app.js`.** Este trecho corresponde às linhas 141–148 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```javascript
function setMenuOpen(open) {
  document.querySelector("#sidebar").classList.toggle("is-open", open);
  document.querySelector("#sidebar-backdrop").hidden = !open;
  const button = document.querySelector("#menu-toggle");
  button.setAttribute("aria-expanded", String(open));
  button.setAttribute("aria-label", open ? "Fechar menu" : "Abrir menu");
}

```

`classList` permite manipular classes do elemento. `toggle("is-open", open)` usa seu segundo argumento para impor o estado: adiciona a classe se `open` é verdadeiro e remove se é falso. Sem esse segundo argumento, `toggle` simplesmente alternaria.

O backdrop recebe `hidden = !open`. Quando abre, a negação de `true` é `false`, então a camada aparece. Quando fecha, a negação de `false` é `true`, então ela é ocultada.

O botão de menu recebe `aria-expanded` convertido em string e um `aria-label` adequado. Isso mantém a informação acessível de acordo com o que a função acabou de fazer.

O CSS já sabe o que a classe `.is-open` significa em telas pequenas: deslocamento horizontal zero. O JavaScript decide quando aplicar a classe; o CSS decide sua aparência e posição.

**Pare e pense / experimente:** O que resultará de chamar `setMenuOpen(false)` duas vezes?

**Conferência:** O menu permanecerá fechado. O uso do segundo argumento de `toggle` define um estado desejado, em vez de inverter cegamente a cada chamada.

### 3.15 — init: preencher seleções e conectar eventos

Esta função configura a página. Continuaremos seu corpo nos próximos blocos; não escreva uma chave de fechamento extra agora.

**Digite no arquivo `app.js`.** Este trecho corresponde às linhas 149–160 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```javascript
function init() {
  sectorFilter.insertAdjacentHTML("beforeend", sectors.map((sector) => `<option value="${escapeHtml(sector.key)}">${escapeHtml(sector.label)}</option>`).join(""));
  statusFilter.insertAdjacentHTML("beforeend", statusCatalog.map((status) => `<option value="${escapeHtml(status.key)}">${escapeHtml(status.label)}</option>`).join(""));
  document.querySelector("#status-legend").innerHTML = statusCatalog.map((status) => `<span class="legend__item" data-status-key="${escapeHtml(status.key)}"><span class="legend__swatch" aria-hidden="true"></span>${escapeHtml(status.label)}</span>`).join("");

  searchInput.addEventListener("input", () => { state.query = searchInput.value.trim(); render(); });
  sectorFilter.addEventListener("change", () => { state.sector = sectorFilter.value; render(); });
  statusFilter.addEventListener("change", () => { state.status = statusFilter.value; render(); });
  emailFilter.addEventListener("change", () => { state.email = emailFilter.value; render(); });
  document.querySelector("#clear-filters").addEventListener("click", resetFilters);
  document.querySelector("#empty-reset").addEventListener("click", resetFilters);

```

As duas primeiras linhas usam `insertAdjacentHTML("beforeend", ...)` para acrescentar opções dentro do `select`, no final. Assim a opção inicial “Todos” é preservada.

`sectors.map(...)` cria uma opção por setor: `value` recebe a chave e o texto visível recebe o rótulo. O catálogo de situações segue a mesma lógica. `escapeHtml` prepara os valores e `join("")` une as strings.

A terceira linha cria a legenda. Cada item tem `data-status-key` para acionar a regra de cor, um quadradinho decorativo e o rótulo visível. A legenda representa o catálogo completo, mesmo quando os filtros deixam de mostrar algumas situações na lista.

Agora aparecem **eventos**. Um evento é uma ocorrência como digitar, clicar ou mudar uma seleção. `addEventListener(nomeDoEvento, funcao)` registra uma tarefa a executar quando ele acontecer.

No campo de busca, `input` ocorre durante a edição. A callback sem parâmetros, `() => { ... }`, lê o valor, usa `trim()` para retirar espaços no começo e no fim, atualiza `state.query` e chama `render`.

Nos três `select`, `change` lê o valor escolhido, guarda a escolha na propriedade correspondente e redesenha. Aqui o evento não altera a lista de pedidos; só muda a visualização.

Nos botões de limpar, passamos `resetFilters` sem parênteses. Queremos registrar a função para o clique futuro. Escrever `resetFilters()` executaria a função imediatamente e passaria seu resultado, não a tarefa desejada.

Os blocos `{ ... }` das callbacks têm ponto e vírgula entre suas instruções. O `});` fecha o corpo da callback, a chamada do método e a instrução externa.

**Pare e pense / experimente:** Siga a sequência de uma tecla digitada: qual função do programa roda ao final?

**Conferência:** O evento `input` chama a callback, que atualiza `state.query` e chama `render()`. `render` usa `matches` para filtrar e as funções de cartão/setor para montar o resultado.

### 3.16 — Acompanhar quais detalhes estão abertos

Este trecho é mais avançado. Seu objetivo é lembrar quais cartões a pessoa abriu para reconstruí-los de modo consistente depois de filtrar.

**Digite no arquivo `app.js`.** Este trecho corresponde às linhas 161–170 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```javascript
  // O estado de expansão é guardado para que buscar e filtrar não feche os detalhes já abertos.
  sectorList.addEventListener("toggle", (event) => {
    if (!event.isTrusted || !(event.target instanceof HTMLDetailsElement)) return;
    const sectorId = event.target.dataset.sectorId;
    const cardId = event.target.dataset.cardId;
    const targetSet = sectorId ? state.openSectors : state.openCards;
    const identifier = sectorId || cardId;
    if (identifier) event.target.open ? targetSet.add(identifier) : targetSet.delete(identifier);
  }, true);

```

O listener fica no recipiente `sectorList`, que permanece na página. Os cartões dentro dele são recriados por `render`.

`toggle` é o evento associado à mudança de abertura do `details`. A callback recebe `event`, um objeto com informações sobre a ocorrência. `event.target` é o elemento em que o evento se originou, não necessariamente aquele no qual colocamos o listener.

A primeira condição retorna sem fazer nada se o evento não é `isTrusted` ou se seu alvo não é uma instância de `HTMLDetailsElement`. `instanceof` verifica o tipo de objeto; `!` nega; `||` representa “ou” neste teste. Um `return` sem valor apenas encerra a callback.

**Precisão importante:** `isTrusted` indica se o evento foi produzido pelo navegador, em contraste com um evento criado e disparado por script com `dispatchEvent`. Não é prova de ação humana: algumas ações de script também podem resultar em eventos produzidos pelo navegador. Aqui ele participa de uma filtragem de eventos, não de uma autenticação.

`dataset.sectorId` lê `data-sector-id`; `dataset.cardId` lê `data-card-id`. Um setor tem o primeiro; um pedido tem o segundo. O ternário escolhe o conjunto correto, `openSectors` ou `openCards`.

`sectorId || cardId` usa o primeiro valor truthy disponível como identificador. Se ele existe, `.open` consulta o booleano de abertura do `details`: `.add` coloca no conjunto quando aberto e `.delete` remove quando fechado.

O último argumento `true` de `addEventListener` ativa a fase de captura. Ela permite ouvir o evento vindo dos `details` descendentes no caminho de descida pelo DOM; não dependemos de ele propagar por bubbling, porque `toggle` de `details` não borbulha.

Neste mecanismo, o estado é salvo na memória da página. Não passa a sobreviver ao fechamento do navegador. Experimente a sequência abrir, filtrar e limpar para observar como ele se comporta na reconstrução.

**Pare e pense / experimente:** Por que não registrar todos esses listeners diretamente nos cartões uma única vez no começo?

**Conferência:** No começo os cartões ainda não existem, e depois eles serão substituídos por `innerHTML`. O recipiente permanente continua recebendo os eventos por captura dos novos elementos.

### 3.17 — Expandir e recolher em conjunto

Os botões atualizam o estado de abertura e deixam `render` construir a tela de acordo com ele.

**Digite no arquivo `app.js`.** Este trecho corresponde às linhas 171–181 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```javascript
  document.querySelector("#expand-all").addEventListener("click", () => {
    state.openSectors = new Set(sectors.map((sector) => sector.key));
    state.openCards = new Set(requests.map((request) => request.id));
    render();
  });
  document.querySelector("#collapse-all").addEventListener("click", () => {
    state.openSectors.clear();
    state.openCards.clear();
    render();
  });

```

No clique de expandir, `map` extrai todas as chaves dos setores e todos os IDs de pedidos. Cada lista vira um novo `Set`, que substitui a propriedade correspondente de `state`. O objeto `state` continua o mesmo, portanto sua declaração com `const` não é violada.

O `render()` seguinte consulta esses conjuntos e insere `open` nos detalhes. A ação usa todos os registros de `requests`, inclusive os que estejam fora do filtro atual; quando voltarem a ser exibidos, seus IDs estarão no conjunto.

No botão de recolher, `.clear()` esvazia os conjuntos existentes. Outra chamada de `render` monta os detalhes fechados. Observe a diferença entre `.delete(id)`, que remove um valor, e `.clear()`, que remove todos os valores do conjunto.

**Pare e pense / experimente:** Ao recolher todos, os pedidos são apagados?

**Conferência:** Não. Somente as coleções que guardam abertura são esvaziadas. O array `requests` continua com os doze objetos.

### 3.18 — Cliques do menu, links e tecla Escape

Ainda dentro de `init`, conectaremos os controles de navegação às funções já declaradas.

**Digite no arquivo `app.js`.** Este trecho corresponde às linhas 182–196 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```javascript
  const menuButton = document.querySelector("#menu-toggle");
  menuButton.addEventListener("click", () => setMenuOpen(menuButton.getAttribute("aria-expanded") !== "true"));
  document.querySelector("#sidebar-backdrop").addEventListener("click", () => setMenuOpen(false));
  document.querySelectorAll(".main-nav__link").forEach((link) => link.addEventListener("click", () => {
    document.querySelectorAll(".main-nav__link").forEach((item) => item.classList.remove("is-active"));
    link.classList.add("is-active");
    setMenuOpen(false);
  }));
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && menuButton.getAttribute("aria-expanded") === "true") {
      setMenuOpen(false);
      menuButton.focus();
    }
  });

```

A constante `menuButton` localiza o botão. A callback de clique lê `aria-expanded`. `getAttribute` devolve texto ou `null`; por isso a comparação é com a string `"true"`. Se ainda não está expandido, a expressão `!== "true"` passa `true` a `setMenuOpen` e abre. No clique seguinte passa `false`.

O clique no backdrop sempre pede para fechar. `querySelectorAll` encontra todos os links da classe indicada; ao contrário de `querySelector`, retorna uma coleção. `forEach` registra um listener em cada link.

Dentro do clique de um link, outro `forEach` retira `is-active` de todos os links. Depois a classe é adicionada ao link clicado, e o menu é fechado. O link continua com seu comportamento normal de ir à âncora porque não usamos `preventDefault`.

O destaque acompanha o link clicado; este trecho não observa automaticamente a rolagem para descobrir qual seção está na tela. É importante explicar o que o código realmente implementa.

O listener `keydown` no documento examina a tecla. Se é `Escape` e o menu está aberto, fecha o menu e retorna o foco ao botão. O `&&` exige ambas as condições. Isso dá uma maneira de sair do menu usando o teclado.

**Pare e pense / experimente:** Por que comparar `getAttribute("aria-expanded")` com `true` sem aspas não produziria a mesma comparação estrita?

**Conferência:** O atributo é lido como string, enquanto `true` sem aspas é booleano. Em `===` e `!==`, tipos diferentes importam. Já a propriedade `.open` de um elemento details é um booleano.

### 3.19 — Preferência salva e a primeira chamada

Chegamos ao final do arquivo. A última linha é o comando que inicia a configuração da página.

**Digite no arquivo `app.js`.** Este trecho corresponde às linhas 197–209 do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.

```javascript
  let savedTheme = "dark";
  try { savedTheme = localStorage.getItem("requisicoes-preview-theme") || "dark"; } catch { /* A preferência é opcional em ambientes que bloqueiam armazenamento local. */ }
  applyTheme(savedTheme === "light" ? "light" : "dark");
  document.querySelector("#theme-toggle").addEventListener("click", () => {
    const next = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
    applyTheme(next);
    try { localStorage.setItem("requisicoes-preview-theme", next); } catch { /* O tema continua ativo nesta página. */ }
  });

  render();
}

init();
```

`let savedTheme = "dark"` começa com um padrão que poderá ser reatribuído. Usamos `let` porque o valor pode ser substituído pelo que estiver guardado.

`localStorage.getItem(...)` consulta uma string guardada no navegador sob uma chave. `|| "dark"` escolhe o padrão quando a consulta não produz um texto truthy. `try` tenta executar um bloco; `catch` trata uma falha lançada. Alguns ambientes restringem esse armazenamento; a preferência é opcional e o painel deve continuar.

A função seguinte aceita como tema claro apenas o valor `"light"`; qualquer outro valor resulta em escuro. Isso evita usar arbitrariamente um texto salvo como nome de tema.

O listener do botão calcula `next` com um ternário: escuro vira claro, e o restante vira escuro. `const next` não precisa mudar durante essa chamada. `applyTheme(next)` atualiza a tela e `localStorage.setItem(...)` tenta guardar a escolha. Cada clique executa novamente a callback e cria um novo `next` local; `const` não significa que todas as chamadas terão o mesmo valor.

**Limite do armazenamento:** ele guarda a preferência de tema neste projeto, não os pedidos. O comportamento do `localStorage` em páginas abertas por `file:` pode variar entre navegadores. A lógica de tolerância a falhas está prevista por isso. Não trate esse recurso como banco compartilhado entre pessoas.

`render()` faz a primeira montagem dos pedidos. A chave seguinte encerra a declaração de `init`. Finalmente, `init();` chama essa função. Sem essa chamada, você teria descrito as funções, mas não teria conectado os eventos nem feito a primeira renderização.

**Ponto de conferência do projeto:** salve os três arquivos e recarregue. Agora devem aparecer 12 pedidos em 5 setores, 3 com e-mail e 9 situações. Digite “manutencao”, experimente filtros, abra detalhes, limpe os campos e alterne o tema. Em uma janela estreita, abra e feche o menu.

**Pare e pense / experimente:** Se você remover só `init();`, as funções desaparecem? O painel se inicializa?

**Conferência:** As declarações continuam no arquivo, mas essa configuração deixa de ser iniciada por aquela chamada. Ter a receita de uma função é diferente de executá-la.

## Aula 4 — Ver o programa inteiro funcionando na sua cabeça

Vamos simular a execução sem adivinhar:

1. O navegador lê `index.html`, encontra `styles.css` e prepara o carregamento de `app.js` com `defer`.
2. O HTML forma os elementos da página. O CSS determina sua aparência nas condições atuais de tela.
3. O JavaScript cria catálogos, pedidos e estado, encontra elementos e declara as funções.
4. `init()` preenche seleções e legenda, registra eventos, aplica o tema e chama `render()`.
5. `render()` pede a `matches` para escolher os pedidos, agrupa os aceitos por setor, chama as funções que geram HTML e atualiza lista e indicadores.
6. Quando você escolhe Manutenção, a callback de `change` coloca `"maintenance"` em `state.sector` e chama `render()` novamente.
7. Os dados dos outros setores continuam existindo. Ao limpar, `state` volta a não restringir a lista e eles reaparecem.

**Faça um desenho:** escreva quatro caixas: “campo”, “state”, “matches” e “render”. Ligue uma à outra com setas. Embaixo, escreva um exemplo real do que passa por elas: seleção Manutenção → `maintenance` → três pedidos aceitos → três cartões mostrados.

### Prova prática de que você digitou um sistema coerente

Faça estas conferências no painel completo, sem alterar os dados originais:

| Ação | Resultado esperado |
| --- | --- |
| Abrir sem filtros | 12 pedidos, 5 setores, 3 pedidos com e-mail, 9 situações. |
| Filtrar setor Manutenção | 3 pedidos, 1 setor, 1 com e-mail, 3 situações. |
| Limpar e selecionar situação Pendente | 2 pedidos, em Operações e Tecnologia; ambos com e-mail. |
| Limpar e selecionar Com e-mail | 3 pedidos em 3 setores e 2 situações diferentes. |
| Buscar um termo inexistente | Zero resultados e aviso de nenhum pedido encontrado. |
| Limpar os filtros | Os doze pedidos retornam; o campo de busca recebe foco. |
| Expandir todos | Os setores e os pedidos exibidos recebem conteúdo expandido. |
| Recolher todos | Os setores ficam recolhidos; os dados continuam na memória. |
| Alternar o tema | Mudam a paleta e o nome da próxima ação no botão. |
| Estreitar a janela | As grades mudam; o botão de menu aparece; os links continuam disponíveis ao abrir o menu. |

“Com e-mail” aqui usa apenas o booleano fictício do pedido. Não compara o conteúdo dos dois cartões da caixa de entrada nem consulta um serviço externo.

## Aula 5 — Sua primeira ideia: quem é o responsável pelo pedido?

Agora você já tem uma reprodução do projeto. Faça uma cópia da sua pasta digitada antes de experimentar. A atividade abaixo é uma mudança na sua cópia de estudo, não uma instrução para modificar a referência original.

Uma ideia útil precisa virar decisões concretas. “Quero responsável” ainda é vago. Vamos decidir: cada pedido terá um nome de responsável; esse nome aparecerá nos detalhes e poderá ser encontrado na busca; pedidos sem o campo mostrarão “Não informado”.

### Passo 1 — Guardar o dado

No primeiro objeto de `requests`, acrescente uma propriedade antes de `email`, mantendo a vírgula após cada propriedade:

```javascript
responsavel: "Ana",
```

Você acabou de mudar os dados. **Preveja antes de atualizar:** o nome aparecerá sozinho no cartão? Não, porque nenhum trecho da interface lê essa propriedade ainda.

### Passo 2 — Ler o dado na função do cartão

Dentro de `cardHtml`, substitua a linha que desestrutura `request` por este bloco:

```javascript
const {
  id,
  status,
  branch,
  title,
  description,
  reference,
  deadline,
  item,
  email,
  responsavel = "Não informado"
} = request;
```

Todas as propriedades antigas continuam sendo lidas. `responsavel = "Não informado"` define um valor padrão quando essa propriedade for `undefined`, como nos pedidos em que você ainda não escreveu o campo. Um texto vazio existente não é substituído por esse padrão.

### Passo 3 — Mostrar o dado

Ainda em `cardHtml`, encontre o `dl` dentro da template literal. Antes do `</dl>`, acrescente mais um par:

```html
<div>
  <dt>Responsável</dt>
  <dd>${escapeHtml(responsavel)}</dd>
</div>
```

Esse trecho parece HTML, mas deve ser digitado **dentro da string entre crases em `app.js`**, junto aos outros pares. Não o coloque no `index.html`: lá `${...}` seria apenas texto sem o processamento da template literal.

Salve e recarregue. Abra o primeiro pedido. Deve aparecer Ana. Abra um pedido sem a propriedade; deve aparecer “Não informado”. A grade `dl` já sabe distribuir mais um par, pois usa o layout que estudamos.

### Passo 4 — Permitir encontrar pelo nome

Em `matches`, mantenha as condições iniciais e a linha que define `sectorName`. Substitua apenas o último `return searchable(...)` por estas instruções:

```javascript
const textoDoPedido = [
  request.id,
  request.branch,
  request.title,
  request.description,
  request.item,
  request.responsavel || "",
  sectorName,
  statusLabel(request.status)
].join(" ");

return searchable(textoDoPedido).includes(searchable(state.query));
```

Você preservou os campos que já eram pesquisáveis e acrescentou o novo. `request.responsavel || ""` usa texto vazio se o nome não estiver preenchido. `join` produz um texto único, `searchable` normaliza e `includes` procura o trecho digitado.

**Conferência:** limpe os filtros e procure `Ana`. O primeiro pedido deve aparecer. Depois procure `teclado` ou um termo presente nos dados originais para conferir que a busca anterior continua funcionando. Se outros textos também contiverem “ana”, eles podem aparecer porque a regra pesquisa trechos em vários campos; isso é coerente com o que você escreveu.

### Passo 5 — Entender o padrão que você acabou de aprender

Você atravessou três lugares: o objeto que guarda a informação, o HTML que apresenta a informação e a regra que usa a informação para buscar. Esse caminho também serve para uma prioridade ou uma equipe.

Agora tente sozinho: acrescente `prioridade` a dois pedidos, mostre-a nos detalhes e mantenha uma mensagem adequada nos outros. Antes de olhar qualquer solução, escreva no papel quais trechos precisam mudar e por quê.

Depois escolha uma ideia própria: organizar livros, acompanhar tarefas escolares, listar equipamentos ou pedidos de uma oficina. Pergunte: o que cada registro precisa guardar? Quais partes são texto, número ou sim/não? Quais escolhas mudam somente a apresentação? O que precisa continuar salvo depois de fechar a página?

Não acrescente tudo ao mesmo tempo. Termine um comportamento pequeno, verifique-o e só então avance. Você poderá explicar uma mudança que fez sozinho se souber responder: “onde guardei o dado?”, “quem o leu?” e “qual ação fez a tela mudar?”

## Aula 6 — Aprender a encontrar erros

Um erro não significa que você precisa recomeçar o projeto. Significa que o navegador encontrou algo diferente do que esperava. Salve, recarregue e confira o Console; a mensagem costuma indicar arquivo e linha. A origem pode estar antes da linha apontada, como uma aspa ou chave que ficou aberta.

| Sintoma | O que verificar primeiro |
| --- | --- |
| Página sem estilo | Os nomes `styles.css` e `href` coincidem? O arquivo está na mesma pasta? Foi salvo sem `.txt`? |
| Texto com acentos incorretos | Salve os arquivos em UTF-8 e confira o `meta charset`. |
| Travessões e lista vazia mesmo após escrever tudo | O JavaScript carregou? O Console mostra erro? Existe `init();` no fim? |
| `Unexpected token` ou `Unexpected end of input` | Confira aspas, crases, vírgulas, parênteses e chaves no trecho anterior. |
| Erro sobre propriedades de `null` | Compare o seletor com o ID real do HTML e confira o `defer`. |
| `... is not defined` | Procure nome digitado diferente ou variável usada fora do escopo em que foi criada. |
| `Assignment to constant variable` | Você está reatribuindo um nome declarado com `const`? Alterar uma propriedade do objeto é uma operação diferente. |
| Nome da situação aparece “Não classificado” | A chave do pedido existe no catálogo e está escrita exatamente igual? |
| Pedido novo não aparece | A chave de setor existe? Os filtros estão limpos? O objeto entrou dentro do array? |
| Todo pedido parece ter e-mail | Confira se escreveu booleanos `true`/`false`, sem aspas. |
| Bloco parece ficar dentro da região errada | Confira o par de abertura/fechamento das tags e sua árvore de elementos. |
| Uma mudança desaparece depois de recarregar | Você editou só o DOM pelo Console? Para uma mudança permanente no código, salve o arquivo-fonte correspondente. |

**Distinção sobre permanência:** se você editar um objeto no arquivo `app.js` e salvar, ele estará assim na próxima abertura. Se editar apenas o objeto na memória pelo Console, recarregar executa outra vez o arquivo salvo e perde aquela alteração temporária. O mesmo vale para mudanças no HTML feitas pelo inspetor.

### Treine sua investigação

Na sua cópia de exercício, faça intencionalmente um erro de cada vez: troque um ID no JavaScript, remova uma vírgula entre dois objetos e escreva uma situação inexistente. Observe que os três problemas têm sintomas diferentes. Corrija um antes de tentar o próximo.

Use `console.log` temporariamente para observar valores, por exemplo `console.log(state.query)` dentro da callback da busca. A mensagem ajuda a descobrir se o problema está na leitura do campo ou em uma etapa posterior. Depois de entender, retire a mensagem experimental.

## Aula 7 — Perguntas para responder sem olhar a solução

1. Qual é a diferença entre uma `div`, uma classe e um ID?
2. Por que `:root` e `var(--page)` aparecem no CSS?
3. Por que `const state` permite alterar `state.query`?
4. Qual é a diferença entre declarar `function render()` e chamar `render()`?
5. O que muda entre `map`, `filter` e `find`?
6. Por que `resetFilters` limpa estado e campos?
7. Por que `data-card-id` vira `dataset.cardId`?
8. Por que os pedidos não somem para sempre ao filtrar?
9. Qual é a diferença entre `textContent` e `innerHTML`?
10. Você acrescentou um campo ao objeto. Por que ele não apareceu na tela?
11. Onde ficam salvos os pedidos atuais? E a preferência de tema?
12. Em uma largura de 400px, quantas regras `max-width` deste projeto podem estar valendo ao mesmo tempo?

### Respostas comentadas

1. `div` é um tipo de elemento para agrupamento genérico. Classe é um rótulo reutilizável. ID identifica um elemento único no documento. Nenhum deles, sozinho, cria um comportamento de busca.
2. `:root` seleciona a raiz onde declaramos valores compartilhados. `var` consulta uma propriedade personalizada. Alterar os valores da paleta permite recolorir seus usos.
3. `const` impede reatribuir o nome `state` a outro objeto; não congela as propriedades do objeto existente.
4. A declaração descreve uma tarefa. A chamada executa essa tarefa naquele momento, passando argumentos quando existirem.
5. `map` produz uma lista de transformações; `filter`, uma lista de itens aprovados por um teste; `find`, o primeiro item aprovado ou `undefined`.
6. O estado guia a lógica e os campos mostram escolhas para a pessoa. Os dois precisam concordar.
7. A API `dataset` expõe atributos `data-*`, convertendo esse nome com hífen para a forma camelCase correspondente.
8. `filter` cria uma lista nova; não remove os objetos do array original neste código.
9. `textContent` trata o valor como texto. `innerHTML` interpreta marcação e reconstrói conteúdo. Por isso o projeto trata os dados usados na montagem de HTML.
10. Guardar uma propriedade não cria automaticamente um elemento. Uma função de apresentação precisa ler o campo e incluí-lo no conteúdo mostrado.
11. Os exemplos iniciais estão escritos no arquivo `app.js`, e seus objetos ficam na memória quando executados. O tema é a única preferência que este código tenta guardar com `localStorage`.
12. As quatro condições de largura: 1180, 920, 700 e 450. Elas são cumulativas. As regras de preferência de movimento dependem de outra condição, não da largura.

## Para a pessoa que vai acompanhar o aluno

Peça que ele explique uma linha antes de avançar. Se disser “esse comando funciona”, pergunte “qual valor ele recebe?” e “o que muda depois?”. Quando travar, reduza o exemplo para o laboratório. Um `details` com duas linhas ensina abertura melhor do que procurar às cegas em um cartão grande.

Não transforme a aula em uma prova de memória de números de cor. O resultado que importa é ele prever uma mudança, escrevê-la, observar o efeito e justificar o que aconteceu. Deixe que escolha textos, assuntos e pequenas decisões visuais depois que a reprodução inicial funcionar.

O primeiro projeto próprio não precisa ter todos esses recursos. Um título, três registros, uma função que os mostra e um filtro compreendido já dão uma base que ele consegue ampliar por conta própria.

