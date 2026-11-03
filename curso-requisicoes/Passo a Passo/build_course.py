"""Monta uma aula independente a partir de trechos conferidos do protótipo."""
from pathlib import Path
import hashlib
import html
import json
import re

HERE = Path(__file__).resolve().parent
SOURCE = Path('C:/Users/PC/OneDrive - Educacional/Documentos/GitHub/Painel_Requisicao-REQ_NEW/Painel_Requisicao-REQ_NEW/REQUISICAO/prototipo-requisicoes')
sources = {name: (SOURCE / name).read_text(encoding='utf-8') for name in ('index.html', 'styles.css', 'app.js')}
coverage = {name: [] for name in sources}
parts = []

def prose(text):
    parts.append(text.strip() + '\n\n')

def css_for_reading(source):
    # Apenas a apresentação da aula ganha quebras; o arquivo do projeto não é escrito.
    result, indent = [], 0
    for item in re.split(r'([{};])', source):
        if item == '{':
            result[-1] += ' {'
            indent += 1
        elif item == '}':
            indent -= 1
            result.append('  ' * indent + '}')
        elif item == ';':
            result[-1] += ';'
        elif item.strip():
            result.append('  ' * indent + item.strip())
    return '\n'.join(result)

def block(title, name, start, end, before, explanation, experiment, answer):
    prose('### ' + title)
    prose(before)
    prose(f'**Digite no arquivo `{name}`.** Este trecho corresponde às linhas {start}–{end} do projeto estudado. Acrescente depois do trecho anterior desse mesmo arquivo; não repita trechos já digitados.')
    raw = '\n'.join(sources[name].splitlines()[start-1:end])
    code = css_for_reading(raw) if name == 'styles.css' else raw
    lang = {'index.html':'html', 'styles.css':'css', 'app.js':'javascript'}[name]
    prose(f'```{lang}\n{code}\n```')
    coverage[name].extend(range(start, end+1))
    prose(explanation)
    prose('**Pare e pense / experimente:** ' + experiment)
    prose('**Conferência:** ' + answer)

prose(r'''
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
''')

block('1.1 — O documento e suas informações', 'index.html', 1, 14,
'''Comece o `index.html` vazio. Aqui você informa como o navegador deve ler o documento e onde procurar aparência e comportamento.''',
'''Leia cada linha:

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

`meta` e `link` são elementos vazios: não precisam de `</meta>` ou `</link>`. Uma linha em branco só organiza o código.''',
'Qual texto muda a aba do navegador e qual mudará o título grande da página?',
'A aba usa `title`. O texto grande usa `h1`, que ainda será escrito. São lugares diferentes, mesmo que você escolha o mesmo texto para os dois.')

block('1.2 — A moldura do aplicativo e o menu lateral', 'index.html', 15, 33,
'''A tela terá duas grandes regiões: menu à esquerda e conteúdo à direita. A primeira `div` será o agrupamento que permite ao CSS organizar as duas.''',
'''A `div.app-shell` envolve o aplicativo inteiro. Ela continua aberta depois deste trecho porque ainda receberá o conteúdo principal.

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

`hidden` é um atributo booleano: sua presença pede para esconder o elemento. Escrever `hidden="false"` ainda coloca o atributo no elemento; não é a forma de mostrá-lo. O JavaScript usará a propriedade `hidden = false` para remover esse estado.''',
'O nome `sidebar` é uma palavra reservada? E o atributo `aria-label` abre o menu?',
'`sidebar` é um nome escolhido pelo autor. `aria-label` só informa o nome acessível; abrir o menu exigirá comportamento em JavaScript e regras de CSS.')

block('1.3 — A barra superior', 'index.html', 34, 46,
'''Agora começa a segunda grande região, `app-main`. Dentro dela colocaremos uma barra superior e o conteúdo.''',
'''`div.app-main` agrupa tudo que fica ao lado do menu. `header.topbar` é o cabeçalho visível dessa região. O ID `inicio` recebe os links que apontam para o começo.

`div.topbar__left` agrupa botão de menu e caminho da página. `div.topbar__right` agrupa indicação de prévia, troca de tema e avatar. Essas duas divisões permitem distribuir os grupos pelas extremidades com CSS.

O botão de menu tem duas classes. `type="button"` deixa explícito que é um botão de ação, não de envio de formulário. `aria-controls="sidebar"` indica qual região ele controla; `aria-expanded="false"` informa que ela está recolhida. Esses atributos precisam acompanhar o comportamento real; por si só não abrem ou fecham nada.

`div.breadcrumb` apresenta “Compras / Requisições”. A barra é decorativa e o nome da seção recebe importância com `strong`. Aqui é uma indicação visual, não uma árvore de links navegáveis.

O botão `theme-toggle` contém um símbolo e um `span` com a ação disponível. O `span.user-avatar` mostra iniciais fixas de exemplo. O atributo `title` fornece uma dica que o navegador pode exibir ao passar o mouse; não representa uma conta autenticada. O `</header>` fecha a barra; `app-main` continua aberto.''',
'Por que o botão de menu e o botão de tema têm IDs diferentes?',
'O JavaScript precisa localizar cada um separadamente e associar uma ação diferente a cada botão.')

block('1.4 — A apresentação principal', 'index.html', 47, 65,
'''`main` identifica o conteúdo principal. A primeira seção apresenta o propósito do painel e dois atalhos.''',
'''`main.content` tem `id="conteudo"`, destino do link de pular navegação. `section.hero` agrupa uma parte temática. `aria-labelledby="page-title"` usa o texto do elemento com esse ID como nome acessível da seção; diferentemente de `aria-label`, recebe um ID, não uma frase.

Leia as divisões de dentro para fora:

- `hero__copy` guarda toda a parte textual da apresentação.
- `eyebrow` agrupa o pequeno rótulo acima do título e seu ponto decorativo.
- `h1` é o título principal. O ponto final está em um `span` para receber outra cor sem mudar o restante do título.
- `p` explica o objetivo da tela.
- `hero__actions` junta os dois links para que possam ficar lado a lado e quebrar de linha quando necessário.
- `hero__visual` agrupa a ilustração feita com HTML e CSS. Seu conteúdo é decorativo e está oculto da leitura assistiva.
- `visual__top` é a barra da ilustração com bolinhas, título e seta.
- Cada `visual__row` reúne um número, nome, descrição e contagem. O `span` sem classe agrupa `strong` e `small` para ficarem na mesma coluna. `visual__count` separa o número à direita.

As três linhas da ilustração são textos fixos. Elas não são os cartões de pedidos reais do protótipo e não mudam com os filtros. `</div>` depois das linhas fecha a ilustração; `</section>` fecha a apresentação. `main` segue aberto para receber as próximas seções.''',
'Se filtrar somente Tecnologia no painel pronto, a ilustração de Operações desaparecerá?',
'Não. Ela é decorativa e fixa. Mais adiante os filtros agirão sobre os dados usados para construir a lista de requisições.')

block('1.5 — Aviso e quatro indicadores', 'index.html', 66, 74,
'''Os indicadores mostram quantidades. Por enquanto, o HTML contém um travessão; os números virão do JavaScript.''',
'''`p.demo-alert` dá contexto aos dados fictícios. O `strong` destaca o início do aviso.

`section.metrics` agrupa quatro cartões. Cada `div.metric` junta três elementos: `span` para o nome, `strong` para o número e `small` para a observação.

Os quatro IDs têm destinos diferentes: `metric-total` recebe a quantidade de pedidos encontrados; `metric-sectors`, a quantidade de setores com resultados; `metric-email`, a quantidade de pedidos encontrados com o indicador de e-mail; `metric-status`, a quantidade de situações distintas nos resultados. São quatro cálculos diferentes.

A última divisão recebe também `metric--accent`, uma variação visual. Todas continuam sendo cartões da classe `metric`. A classe não calcula nada; o ID permite que o JavaScript encontre o número a atualizar.''',
'Por que usar a mesma classe `metric` quatro vezes e quatro IDs diferentes?',
'A classe reaproveita a aparência; os IDs identificam alvos diferentes para atualizar o conteúdo.')

block('1.6 — Cartões que abrem sem JavaScript', 'index.html', 75, 91,
'''O navegador já sabe abrir e fechar um elemento `details`. Aprender recursos nativos evita ter que programar tudo do zero.''',
'''`section.email-section` é a região dos e-mails fictícios. Ela também recebe `section`, classe que compartilhará espaçamento com outras regiões.

`div.section__header` agrupa o cabeçalho. A `div` interna sem classe mantém juntos o rótulo `section__eyebrow`, o título `h2` e o parágrafo. Assim, o selo `section__tag` pode ficar ao lado desse conjunto.

`div.email-grid` agrupa os dois cartões para distribuí-los em colunas. Cada cartão é um `details`, com um `summary` como cabeçalho acionável. Clique no `summary` e o navegador alterna o atributo `open`. Não precisamos escrever uma função para esse comportamento básico.

No `summary`, três partes têm responsabilidades distintas: `email-card__icon` mostra o ícone; `email-card__summary` agrupa título e descrição; `email-card__chevron` mostra a seta. `div.email-card__body` guarda o parágrafo e o selo que aparecem quando o cartão abre.

O segundo cartão repete a estrutura com outro conteúdo. Seu selo tem a classe extra `email-tag--muted`, uma variante visual. Os `</details>` fecham cada cartão; os dois últimos fechamentos encerram a grade e a seção.

O texto “2 mensagens fictícias” é fixo. Não existe busca de e-mails nem contagem automática dessa caixa de entrada neste código.''',
'No laboratório, escreva `<details><summary>Ver resposta</summary><p>Você abriu o cartão.</p></details>`. Teste com mouse e com teclado.',
'O parágrafo fica recolhido inicialmente. Ao acionar o cabeçalho, aparece. Ao escrever `open` na tag inicial, o cartão passa a iniciar aberto.')

block('1.7 — Campos de busca e seleção', 'index.html', 92, 105,
'''O HTML cria os controles. Mais adiante, o JavaScript lerá seus valores e decidirá quais pedidos mostrar.''',
'''O cabeçalho repete a estrutura já aprendida: seção, agrupamento de título e selo. `id="setores"` é o destino dos links para a lista.

`div.toolbar` reúne todos os filtros. `role="search"` identifica a região como busca. Dentro dela, cada `label` envolve o nome e seu controle, criando a associação entre os dois.

- `input type="search"` cria o campo de texto. `placeholder` é a dica que aparece vazio; o rótulo “Buscar” continua visível. `autocomplete="off"` pede que o navegador não ofereça preenchimento anterior, embora navegadores possam adotar decisões próprias.
- `select` cria uma lista de seleção e `option` representa uma escolha.
- `value=""` é um texto vazio. Aqui significa não restringir por aquele filtro. O texto visível “Todos os setores” é diferente do valor que o JavaScript lê.
- `sector-filter` e `status-filter` começam com uma única opção. As outras serão criadas a partir das listas do JavaScript.
- `email-filter` já tem três opções fixas: vazio, `with` e `without`. Os dois últimos valores significam com e sem e-mail para a regra que escreveremos.
- O botão `clear-filters` existe, mas ainda não sabe limpar nada. O listener de clique será escrito na Aula 3.

`field--search` é a variação de classe que permitirá à busca ocupar mais espaço na grade de filtros.''',
'Mude só o texto visível “Com e-mail” para “Vinculados”, mantendo `value="with"`. A regra de filtro precisará mudar?',
'Não. O JavaScript usa o valor `with`, não o texto apresentado na opção. Separe nomes mostrados ao usuário de valores usados no programa.')

block('1.8 — Espaços dinâmicos e fechamento do documento', 'index.html', 106, 118,
'''Terminaremos o arquivo. Algumas divisões ficam vazias de propósito: o JavaScript preencherá essas regiões.''',
'''`div.legend` receberá a legenda de situações. `div.results-bar` junta uma mensagem e um grupo de botões. Sua `div.results-bar__actions` mantém “Expandir todos” e “Recolher todos” lado a lado.

O `p#results-count` começa vazio. `role="status"` e `aria-live="polite"` permitem anunciar suas atualizações em tecnologia assistiva sem exigir uma interrupção imediata. Esses atributos não fazem a contagem.

`div#sector-list` é o recipiente para os setores gerados pelo JavaScript. Não há requisições escritas diretamente aqui no HTML.

`div.empty-state` reúne ícone, título, explicação e botão para o caso em que os filtros não encontrem nada. `hidden` evita que apareça junto da lista inicial. O botão `empty-reset` é outro caminho para limpar filtros.

`</section>` fecha a seção dos setores. `footer` é o rodapé do conteúdo. Depois são fechados, nesta ordem, `main`, `div.app-main` e `div.app-shell`. A ordem importa porque esses elementos foram abertos um dentro do outro.

`noscript` oferece uma mensagem quando a execução de scripts está desativada. Não é uma mensagem automática para erro de JavaScript. `</body>` e `</html>` concluem o documento.

**Ponto de conferência do HTML:** salve e abra `index.html`. Sem CSS, a página deve parecer simples, empilhada e com estilos padrão do navegador. Os e-mails abrem com `details`. Os quatro números ainda são travessões; os filtros ainda não geram a lista. Isso é esperado, porque `app.js` está vazio.''',
'Desenhe em papel a árvore `app-shell → sidebar + app-main → topbar + main`. Depois localize no arquivo a abertura e o fechamento de cada agrupamento.',
'O menu lateral é irmão de `app-main`. A barra superior e o conteúdo principal ficam dentro de `app-main`. Mover um fechamento pode mudar essa organização mesmo quando o navegador tenta corrigir o HTML.')

prose(r'''
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
''')

block('2.1 — :root, variáveis e os dois temas', 'styles.css', 1, 35,
'''Uma cor aparece em muitos lugares. Dar um nome a ela permite mudar o conjunto sem procurar cada cartão individualmente.''',
'''`/* ... */` é um comentário de CSS. `:root` é uma pseudoclasse que seleciona a raiz do documento; no HTML, essa raiz é o elemento `html`. O sinal `:` faz parte da sintaxe. Não é uma tag que você precise criar.

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

O segundo seletor, `html[data-theme="light"]`, só corresponde à raiz quando o atributo vale `light`. Ele redefine os mesmos nomes com cores claras. Os elementos que usam `var(...)` passam a consultar os novos valores herdados. Mais adiante o JavaScript trocará exatamente esse atributo.''',
'Mude temporariamente `data-theme="dark"` para `data-theme="light"` na primeira tag do HTML. Depois de escrever as regras de `body`, observe a mudança. Por que não precisamos trocar classe de cada cartão?',
'Os componentes consultam nomes compartilhados. Ao trocar os valores desses nomes na raiz, seus descendentes passam a receber a outra paleta. O JavaScript completo também restaurará o tema salvo, por isso faça esta experiência antes da Aula 3 ou use o botão de tema depois.')

block('2.2 — Regras gerais, foco e o link de pular', 'styles.css', 36, 49,
'''Este bloco tira algumas diferenças padrão do navegador e prepara a navegação por teclado.''',
'''O seletor `*` alcança todos os elementos. `box-sizing: border-box` faz uma largura declarada incluir padding e borda; a margem continua fora. Isso facilita calcular tamanhos.

`scroll-behavior: smooth` suaviza deslocamentos como os links internos. `body` perde a margem padrão, recebe fundo e texto da paleta, fonte de 14px e `line-height: 1.5`, uma altura de linha de 1,5 vezes o tamanho da fonte. `background` pinta o fundo; `color` pinta o texto.

`font: inherit` faz os controles herdarem a configuração de fonte. `cursor: pointer` usa o cursor de ação sobre botões. `a { color: inherit; }` faz os links herdarem a cor em vez de usarem obrigatoriamente o azul padrão.

`outline` desenha um contorno de foco sem reservar espaço como a borda; `outline-offset` afasta esse contorno. `[hidden] { display: none !important; }` reforça o ocultamento mesmo quando outra regra comum define `display`. O `!important` aumenta a prioridade desta declaração; não é algo para espalhar em toda regra quando um estilo não funciona.

`scroll-margin-top: 90px` reserva uma folga no alinhamento de rolagem das seções com ID, ajudando o cabeçalho fixo a não cobrir o destino.

O link `.skip-link` fica com `position: fixed`, preso à janela. `top: -55px` inicialmente o põe acima da área visível; `left` posiciona pela esquerda; `z-index` controla sua ordem de sobreposição no contexto de empilhamento. `padding` amplia a área clicável e `border-radius` arredonda os cantos. Quando recebe foco, `top: 10px` o traz para dentro da tela.''',
'No painel, pressione Tab desde o início. O link “Pular para o conteúdo” deve aparecer quando recebe foco. O que aconteceria se ele tivesse `display: none`?',
'Ele normalmente deixaria de participar da navegação por foco enquanto estivesse oculto. O deslocamento usado aqui mantém o link disponível para teclado.')

block('2.3 — Duas colunas e todos os detalhes do menu', 'styles.css', 50, 68,
'''Agora o agrupamento `app-shell`, que você escreveu no HTML, ganha a função visual de organizar menu e conteúdo.''',
'''Leia as regras junto de seus elementos:

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

`z-index: 40` do menu e `z-index: 30` do cabeçalho serão parte da ordem de sobreposição. Números maiores não vencem universalmente todos os contextos de empilhamento; aqui esses valores coordenam os elementos desta interface.''',
'Troque temporariamente `244px` por `300px` em `.app-shell`. O que muda? E se apagar somente `display: grid`?',
'A primeira mudança alarga a coluna do menu. Sem Grid, `grid-template-columns` deixa de organizar as duas regiões e os elementos voltam a seguir outro fluxo de layout.')

block('2.4 — Barra superior, botões e largura de leitura', 'styles.css', 69, 80,
'''O cabeçalho reúne dois grupos, e o conteúdo precisa de limites para continuar legível em telas largas.''',
'''`.topbar` combina posicionamento sticky com Flex. `justify-content: space-between` afasta os grupos; `align-items: center` os alinha. O padding lateral usa `clamp(22px, 3.4vw, 54px)`: começa com um tamanho proporcional à janela, mas nunca menor que 22 nem maior que 54.

`.topbar__left` e `.topbar__right` também são contêineres Flex, mas organizam os elementos dentro de cada grupo. É possível ter Flex dentro de Flex.

`.breadcrumb` usa `white-space: nowrap` para manter seu texto em uma linha. Sua barra ganha padding e `opacity: .55`, tornando esse elemento inteiro parcialmente transparente. O `strong` recebe destaque. `.topbar__edition` regula a legenda de prévia.

`.theme-button` e `.icon-button` compartilham dimensões, borda e cores. `inline-flex` cria um contêiner Flex com participação externa de elemento em linha. O seletor com vírgula evita repetir as mesmas propriedades. Ao passar o ponteiro, muda só a cor da borda.

`.user-avatar` desenha o círculo de iniciais, com Grid centralizando o texto. `.mobile-menu` começa com `display: none`, pois em telas grandes o menu já fica visível; uma media query fará o botão aparecer.

`.content` tem `max-width: 1550px`, limitando o crescimento. `margin: 0 auto` centraliza quando sobra espaço horizontal. O padding cria espaço interno de leitura. Não é necessário fixar uma largura para cada parágrafo.''',
'Com uma janela estreita, o padding que usa `clamp` pode virar zero?',
'Não. O limite mínimo declarado é 22px para essa regra. Regras posteriores específicas para telas pequenas poderão substituí-lo.')

block('2.5 — A apresentação, seus desenhos e suas camadas', 'styles.css', 81, 104,
'''Observe como um desenho pode ser composto de elementos simples. O projeto não usa uma imagem externa para a ilustração de setores.''',
'''`.hero` usa uma grade de duas colunas: texto com participação `1.15fr`, ilustração com `.85fr` e mínimo de 280px. `gap` separa as áreas. `overflow: hidden` recorta conteúdo que ultrapasse a caixa, inclusive efeitos. Borda, raio, sombra e gradiente radial criam o painel.

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

Não confunda `position: relative` com “tamanho responsivo”. Ele participa do sistema de posicionamento. Responsividade aqui vem de tamanhos flexíveis, `clamp` e media queries.''',
'Retire no laboratório a rotação de uma caixa e depois coloque `rotate(10deg)`. O texto e a borda giram juntos?',
'Sim. O transform atua sobre a apresentação do elemento e seus conteúdos. Não altera o texto armazenado nem cria outro elemento.')

block('2.6 — Indicadores, títulos de seção e cartões de e-mail', 'styles.css', 105, 121,
'''Os mesmos fundamentos reaparecem. A repetição é uma oportunidade de ler cada regra sem depender da explicação.''',
'''`.metrics` cria quatro colunas iguais. `.metric` empilha nome, número e observação em coluna. `.metric > span` trata somente o rótulo filho direto; `strong` destaca o número; `small` usa `margin-top: auto` para aproveitar o espaço acima da observação. `.metric--accent strong` troca a cor do número da variação.

`.section` separa regiões verticalmente. `.section__header` distribui o bloco de textos e o selo, alinhando-os ao final do eixo transversal. Suas regras de `h2` e `p` ajustam a hierarquia. `.section__tag` tem `flex: 0 0 auto`, evitando que cresça ou encolha, e um raio grande para o formato de selo.

`.email-grid` cria duas colunas iguais. `.email-card` define superfície e borda. `.email-card summary` organiza ícone, textos e seta em Flex e remove o marcador padrão com `list-style: none`. `::-webkit-details-marker` é um seletor específico para ocultar o marcador em navegadores que o suportam.

O hover destaca a borda. `.email-card__icon` cria a caixa do ícone com base fixa. `.email-card__summary` pode encolher. Nos seus textos, quatro propriedades trabalham juntas: `display: block`, `overflow: hidden`, `white-space: nowrap` e `text-overflow: ellipsis`. Com uma largura efetivamente limitada, esse conjunto permite mostrar reticências quando falta espaço.

`.email-card__chevron` usa `margin-left: auto` para ir à direita. `transition: transform .2s` suaviza a mudança de rotação. Quando `[open]` está no cartão, a seta gira 180 graus. O CSS está reagindo ao estado do HTML.

`.email-card__body` dá espaçamento ao conteúdo expandido; seu parágrafo ganha margem inferior. `.email-tag` desenha o selo de situação, e `.email-tag--muted` muda seu fundo e cor. “Muted” é um nome visual; não significa que a mensagem foi silenciada em um serviço de e-mail.''',
'Troque `repeat(4, ...)` de `.metrics` por `repeat(2, ...)`. Quantas linhas serão necessárias para quatro indicadores?',
'Duas linhas de duas colunas. Você mudou a distribuição, não precisou escrever novos cartões no HTML.')

block('2.7 — Aparência dos filtros, legenda e resultados', 'styles.css', 122, 128,
'''Agora os controles formam uma barra organizada. A lista ainda ficará vazia até o JavaScript gerar os elementos.''',
'''`.toolbar` usa uma coluna de busca com mínimo de 180px e participação `2fr`, três colunas de filtro com mínimo de 124px e `1fr`, e uma coluna automática para o botão. Os mínimos podem não caber em uma tela pequena; as media queries mudarão a grade.

`.field` empilha nome e controle com Grid. Seu `span` recebe fonte de rótulo. As regras de `input` e `select` são compartilhadas: largura total, altura, padding, borda, fundo e fonte. `outline: none` remove o contorno padrão nesses controles, mas a regra de `:focus` logo em seguida fornece borda e sombra visíveis; não remova as duas indicações juntas. `::placeholder` seleciona o texto de dica.

`.clear-button` desenha o botão de limpar; seu hover muda a borda. `.legend` é Flex com quebra para distribuir as situações por mais de uma linha. `.legend__item` agrupa ponto e nome; `.legend__swatch` é o pequeno quadrado que usa `--status-accent`. Essa variável será definida em cada situação.

`.results-bar` separa texto de resultado e grupo de ações. Seu `p` remove margem padrão. `.results-bar__actions` distribui os botões com Flex. A regra dos botões deixa o fundo transparente e tira a borda, conservando o elemento HTML `button` e sua ação pelo teclado. O hover acrescenta sublinhado.''',
'Por que a lista de seleção precisa de `width: 100%`, se a grade já tem colunas?',
'A grade define o espaço disponível. A largura faz o controle ocupar o espaço de seu agrupamento, em vez de depender apenas de uma largura intrínseca do conteúdo.')

block('2.8 — Cada parte dos setores e das requisições', 'styles.css', 129, 146,
'''Esses seletores ainda não encontrarão cartões no HTML inicial. Eles estilizarão os elementos que `cardHtml` e `sectorHtml` criarão na Aula 3.''',
'''Leia a sequência como uma montagem:

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

As regras reaproveitam padding, borda, fonte e layout já estudados. Para ler uma linha longa, separe-a em declarações terminadas por `;` e pergunte qual propriedade trata de caixa, texto, cor ou interação.''',
'Qual seletor faria uma regra atingir todos os `summary` dentro do setor? Qual atinge só o cabeçalho imediato?',
'`.sector summary` alcança descendentes em qualquer nível. `.sector > summary` alcança apenas filhos diretos. Essa diferença importa quando há cartões expansíveis dentro de setores expansíveis.')

block('2.9 — Relacionando dados a cores', 'styles.css', 147, 157,
'''Aqui existe uma ligação entre os nomes das situações no JavaScript e a aparência dos cartões.''',
'''Cada regra seleciona dois tipos de elemento: um cartão com `data-status` e uma entrada de legenda com `data-status-key`. Ambos recebem o mesmo valor de `--status-accent`.

A sequência corresponde a Cadastrado, Pendente, Aprovado, Parcial, Reprovado, Cancelado, Liberado, Em cotação e Baixado. As cores são rótulos ilustrativos; não deduzimos regras do ERP a partir delas.

Essa variável definida no cartão é herdada por suas partes internas, como o selo. Ela não precisa estar no `:root`, porque seu valor varia de cartão para cartão.

O CSS não traduz `pending` para “Pendente”. Essa tradução virá do catálogo de JavaScript. Para adicionar uma situação própria depois, você precisará pensar no valor de dados, no nome visível e na regra de cor correspondente.''',
'Se escrever `data-status="pendente"`, a regra `[data-status="pending"]` será aplicada?',
'Não. Os valores precisam corresponder. A linguagem não traduz automaticamente a palavra entre português e inglês.')

block('2.10 — Tela pequena e preferência por menos movimento', 'styles.css', 158, 171,
'''Uma media query aplica um conjunto de regras quando uma condição sobre o ambiente é atendida. As demais regras do arquivo continuam existindo.''',
'''`@media (max-width: 1180px)` significa largura de visualização até 1180px, inclusive. A barra ganha três colunas; a busca ocupa duas com `grid-column: span 2`; o botão se estica na célula. A apresentação reduz a coluna da ilustração para 270px e diminui o espaço entre colunas.

Até 920px, `.app-shell` passa a bloco. O menu torna-se `fixed`, preso ao lado esquerdo, com largura `min(265px, 86vw)`: o menor desses dois valores. `translateX(-102%)` desloca-o para fora da tela usando sua própria largura como referência. A classe `.is-open` zera esse deslocamento. A transição suaviza a mudança.

O backdrop sem `hidden` cobre a janela usando `inset: 0`, com fundo preto transparente e z-index entre conteúdo e menu. O botão móvel aparece e os indicadores passam a duas colunas.

Até 700px, o texto de edição e a ilustração desaparecem; a apresentação fica em bloco; cartões e e-mails usam uma coluna. Os filtros passam a duas colunas e busca/limpar ocupam a largura toda com `grid-column: 1 / -1`. O `-1` indica a última linha da grade explícita, não uma largura negativa. Os selos de seção são ocultados.

Até 450px, padding e espaços diminuem; o texto do botão de tema some, mas seu nome acessível continua disponível. Filtros usam uma coluna. `grid-column: auto` desfaz a ocupação explícita anterior. Os resultados se organizam em coluna. Os detalhes dos pedidos passam de três para duas colunas.

As condições são cumulativas: em 400px, todas as regras de largura anteriores também se aplicam e as declarações posteriores resolvem vários conflitos. Não são quatro páginas diferentes.

`prefers-reduced-motion: reduce` respeita a preferência por menos movimento: retira a rolagem suave e as transições indicadas.

**Ponto de conferência do CSS:** salve e recarregue. A página já deve ter cores, menu, apresentação e e-mails estilizados. Diminua a janela. O botão de menu aparece, mas só passará a abrir o menu quando escrevermos JavaScript. Contadores e requisições ainda dependem da próxima aula.''',
'Por que esconder o texto “Tema claro” no celular não deixa necessariamente o botão sem nome para um leitor de tela?',
'O botão tem `aria-label`, que fornece seu nome acessível. Ao criar seus próprios botões só com ícones, você também precisa dar um nome que descreva a ação.')

prose(r'''
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
''')

block('3.1 — const, arrays e objetos de situações e setores', 'app.js', 1, 21,
'''Vamos começar pelos vocabulários do painel. Eles dizem quais situações e quais setores existem.''',
'''O comentário inicial declara o propósito demonstrativo. `const statusCatalog = [` cria o nome da lista de situações. Cada `{ key: ..., label: ... }` é um objeto. `key` é o valor interno e `label` é o nome mostrado. Não existe tradução automática: cada par foi escrito explicitamente.

As nove entradas seguem a mesma estrutura. A linha final `];` fecha o array e termina a declaração. A vírgula depois do último objeto é permitida em JavaScript e facilita acrescentar itens. Isso não faz do arquivo um documento JSON: ele também contém declarações, funções e comentários, que não fazem parte do formato JSON.

`sectors` é outra lista. Cada setor contém `key`, `label`, `subtitle` e `icon`. O ícone é um caractere de texto. Os cinco valores internos são `operations`, `maintenance`, `facilities`, `technology` e `supply`. Serão usados para relacionar pedidos a setores.

Os nomes `statusCatalog` e `sectors` são escolhas do projeto. O mesmo conceito pode servir a categorias de livros, matérias escolares ou áreas de uma oficina.''',
'Qual valor deveria aparecer na tela: `quotation` ou “Em cotação”? Qual valor deve permanecer consistente no código?',
'“Em cotação” é o rótulo legível. `quotation` é a chave usada para relacionar registros, filtros e regra de cor. Você pode inventar outras chaves, desde que atualize todas as relações correspondentes.')

block('3.2 — Os doze pedidos e seus tipos de dados', 'app.js', 22, 36,
'''Cada pedido é um objeto. Para facilitar sua digitação, você pode colocar uma propriedade por linha dentro de cada objeto; preserve aspas, vírgulas, chaves e valores.''',
'''Leia o primeiro objeto como uma ficha:

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

Digitar `email: "false"` seria um erro de significado: a string não vazia é tratada como verdadeira em testes booleanos comuns. Digite o booleano sem aspas.''',
'Por que `branch: "01"` é texto, enquanto `email: true` não está entre aspas?',
'A filial é um código que precisa manter sua representação. `email` representa uma condição de sim/não que será usada em decisões. Escolher o tipo certo evita interpretações erradas.')

block('3.3 — state: o que a pessoa escolheu agora', 'app.js', 37, 45,
'''As requisições são os dados. O estado guarda as escolhas atuais de visualização. Separar os dois permite filtrar sem apagar pedidos.''',
'''`state` é um objeto. `query`, `sector`, `status` e `email` começam com strings vazias. Neste programa, vazio significa que a pessoa não aplicou aquele filtro.

`Set` é uma coleção de valores únicos. `new Set()` cria uma coleção vazia. `new` constrói uma instância. Para comparar: uma lista pode ter `['a', 'a']`; um conjunto criado a partir dela terá apenas um `'a'`.

Desmonte a linha de `openSectors` em duas etapas mentais:

```javascript
// Laboratório de leitura: esta decomposição explica a linha do bloco original.
const chaves = sectors.map((sector) => sector.key);
const setoresAbertos = new Set(chaves);
```

`map` percorre os objetos e extrai a chave de cada um. O conjunto guarda essas chaves; por isso os setores começam abertos. `openCards` começa vazio; os pedidos individuais começam fechados.

Como `state` foi declarado com `const`, não reatribuímos o objeto inteiro. É permitido mudar `state.query` ou substituir `state.openCards` por outro conjunto. São propriedades internas do objeto.

Este estado está na memória da página. Recarregar recria seus valores iniciais. Ele não é um banco de dados.''',
'Se usar `new Set()` também em `openSectors`, como começarão os setores?',
'Fechados, porque a montagem de cada setor verificará se sua chave pertence ao conjunto. Sem chaves, nenhum receberá o atributo `open` inicialmente.')

block('3.4 — Guardar referências aos elementos da página', 'app.js', 46, 52,
'''Precisaremos consultar os campos e preencher a lista muitas vezes. Vamos localizar esses elementos e dar nomes às referências.''',
'''Cada linha declara uma constante que recebe o resultado de `document.querySelector`. O `#` significa ID no seletor.

`sectorList` aponta para o recipiente dos setores; `emptyState`, para o aviso de lista vazia; `searchInput`, para o campo de busca; `sectorFilter`, `statusFilter` e `emailFilter`, para as três seleções.

Esses nomes não contêm uma cópia do HTML em formato de texto. Eles referenciam objetos do DOM. Mudar `searchInput.value` muda o valor do campo correspondente.

`const searchInput` permite manter a mesma referência, mas não impede editar propriedades do elemento. O `defer` escrito no HTML ajuda a garantir que o navegador já tenha analisado esses elementos antes de executar as buscas.''',
'O que acontece se o HTML tiver `id="search-input"`, mas esta linha procurar `"#searchInput"`?',
'A busca não encontra o elemento e retorna `null`. Os nomes precisam ser exatamente os mesmos. Um erro posterior pode aparecer ao tentar usar uma propriedade dessa referência inexistente.')

block('3.5 — escapeHtml: mostrar dados como texto', 'app.js', 53, 59,
'''Mais adiante montaremos HTML com textos dos pedidos. Antes disso, precisamos impedir que caracteres desses textos sejam confundidos com marcação.''',
'''`function escapeHtml(value)` recebe um valor. `String(value)` o converte para texto. O método `.replace(...)` procura partes desse texto e substitui cada correspondência.

`/[&<>"']/g` é uma expressão regular. As barras delimitam o padrão; os colchetes significam “um destes caracteres”; o `g` pede todas as correspondências. O padrão encontra `&`, `<`, `>`, aspas duplas e aspas simples.

A arrow recebe um caractere encontrado. Dentro de `({ ... })` está um objeto usado como mapa de substituição. Os parênteses permitem que as chaves sejam lidas como um objeto devolvido, não como o bloco de comandos da arrow. `[character]` acessa a propriedade cujo nome é o caractere recebido.

O mapa converte `&` em `&amp;`, `<` em `&lt;`, `>` em `&gt;`, aspas duplas em `&quot;` e simples em `&#39;`. O `return` devolve o texto transformado. Exemplo: o texto `<b>oi</b>` é preparado para aparecer literalmente, em vez de criar um elemento `b` quando inserido como HTML.

Essa função foi feita para os contextos de texto e atributos HTML entre aspas usados aqui. Ela não é uma solução universal para inserir dados em JavaScript, CSS ou URLs. Quando se quer mudar somente texto, `textContent` costuma evitar a necessidade de montar HTML.''',
'No Console do painel depois de completar a aula, execute `escapeHtml("A & B < C")`. Que transformações espera?',
'O resultado deve ser `A &amp; B &lt; C`. O primeiro `&` e o sinal `<` precisam ser tratados para preservar sua apresentação como texto.')

block('3.6 — searchable: buscar sem diferença de maiúsculas e acentos', 'app.js', 60, 63,
'''Quem busca “operacao” normalmente também espera encontrar texto com acentos. A função prepara uma versão adequada à comparação.''',
'''`searchable(value)` converte a entrada para string. `.normalize("NFD")` decompõe caracteres quando existe uma forma canônica apropriada: uma letra acentuada pode ser representada por letra-base e marca de acento.

`.replace(/[\u0300-\u036f]/g, "")` remove marcas combinantes nessa faixa de códigos Unicode. O hífen dentro dos colchetes indica intervalo. A substituição é o texto vazio. Isso cobre as marcas relevantes aos exemplos comuns de português; não é uma regra universal para todos os sistemas de escrita.

`.toLocaleLowerCase("pt-BR")` passa o texto para minúsculas com a localidade indicada. Os pontos encadeiam operações: o resultado de uma vira entrada da próxima.

`return` entrega a versão preparada, sem modificar o texto original do pedido. A busca pode comparar “manutencao” com “Manutenção”, enquanto o cartão continua exibindo a grafia original.''',
'Qual deve ser o resultado de `searchable("MANUTENÇÃO")`?',
'`manutencao`. O nome mostrado no cartão não precisa perder acentos só porque a busca normaliza a comparação.')

block('3.7 — statusLabel: procurar um rótulo e lidar com ausência', 'app.js', 64, 67,
'''Esta função traduz a chave interna para o texto que a pessoa verá.''',
'''`statusCatalog.find(...)` procura o primeiro objeto que passe no teste da callback. O parâmetro `status` representa um objeto do catálogo a cada tentativa.

`status.key === key` compara a chave do objeto com o parâmetro da função. `===` é igualdade estrita; não confunda com `=`, que atribui um valor.

Quando `find` acha, devolve o objeto. Quando não acha, devolve `undefined`. `?.label` é acesso opcional: se o resultado for `null` ou `undefined`, não tenta ler a propriedade de um objeto ausente. `??` fornece “Não classificado” quando o resultado à esquerda é `null` ou `undefined`.

Não confunda `??` com `||`. O primeiro só usa a alternativa nessas duas ausências; `||` também usa a alternativa diante de valores falsy como string vazia, zero e `false`.

Ao chamar `statusLabel("approved")`, recebemos “Aprovado”. Um valor desconhecido recebe o texto de reserva.''',
'Por que simplesmente escrever `.find(...).label` pode quebrar?',
'Se nenhuma entrada corresponder, `find` devolve `undefined`. Acessar `.label` diretamente nessa ausência lança um erro. O acesso opcional e a alternativa tratam esse caso.')

block('3.8 — cardHtml: construir uma requisição com os seus dados', 'app.js', 68, 84,
'''Agora vamos reunir HTML e dados. A função recebe um pedido e devolve o texto HTML do cartão. Ela ainda não coloca esse texto na página.''',
'''A primeira linha do corpo usa **desestruturação**: `const { id, status, ... } = request` cria nomes locais com as propriedades de mesmo nome. `id` passa a valer `request.id`, `title` passa a valer `request.title`, e assim por diante. As reticências nesta explicação abreviam a leitura; no código mostrado você digita todos os nomes explicitamente.

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

A função gera um cartão para qualquer objeto com o formato esperado. É por isso que não escrevemos doze cartões à mão no HTML principal.''',
'O que `cardHtml(requests[0])` devolve? Um elemento DOM já inserido ou uma string?',
'Uma string com HTML. A função `render`, que ainda vamos escrever, colocará o resultado no recipiente da página. `cardHtml` descreve um cartão; `render` atualiza a tela.')

block('3.9 — sectorHtml: um grupo contendo vários cartões', 'app.js', 85, 97,
'''A ideia anterior se repete em outra escala: um setor tem cabeçalho e uma coleção de requisições.''',
'''A função recebe dois parâmetros: `sector`, o objeto do setor, e `matchingRequests`, a lista de pedidos desse setor que passaram nos filtros.

O `details.sector` tem `data-sector-id` e consulta `state.openSectors.has(sector.key)` para decidir se recebe `open`. O cabeçalho junta ícone, nome, subtítulo, quantidade e seta.

`sector__heading` é um `span` que agrupa `strong` e `small`. `matchingRequests.length` é a quantidade de itens. O ternário compara essa quantidade com 1 para escolher “requisição” no singular ou “requisições” no plural. A linguagem não pluraliza automaticamente.

`div.sector__body` guarda o conteúdo expandido. Dentro dela, `div.card-grid` organiza os cartões. A expressão `matchingRequests.map(cardHtml)` chama a função de cartão para cada pedido. Passamos a função pelo nome, sem chamá-la antes. `map` também oferece índice e array às callbacks; `cardHtml` usa apenas o primeiro parâmetro declarado.

O resultado de `map` é uma lista de strings. `.join("")` junta essas strings sem separador. Sem especificar o separador, `join` usaria vírgulas; não queremos vírgulas extras entre cartões.

O setor devolve outra string HTML. O agrupamento se forma assim: cada pedido vira um cartão; vários cartões viram o corpo de um setor; vários setores formarão a lista.''',
'Se `matchingRequests` tiver dois pedidos, quantas vezes `cardHtml` será chamada nesta montagem?',
'Duas vezes. Haverá duas strings de cartão que serão unidas dentro de `card-grid`. A contagem do setor será 2.')

block('3.10 — matches: decidir se um pedido aparece', 'app.js', 98, 107,
'''Aqui estão as regras da busca. A função responde uma pergunta com `true` ou `false`: este pedido atende às escolhas atuais?''',
'''`if (condicao)` executa a instrução seguinte quando a condição é verdadeira. Um `return false` encerra imediatamente a chamada atual. Ele não continua testando as linhas seguintes.

Primeira regra: `state.sector && request.sector !== state.sector`. `&&` é o “e” com curto-circuito: só avalia a direita quando a esquerda é truthy. String vazia é falsy. Assim, apenas quando existe um filtro de setor e o pedido tem setor diferente (`!==`) ele é recusado.

A segunda regra repete essa lógica para a situação. A terceira recusa pedidos sem e-mail quando o filtro é `with`; `!request.email` é a negação do booleano. A quarta recusa os que têm e-mail quando o filtro é `without`.

Se não há texto de busca (`!state.query`), o pedido é aceito, porque já sobreviveu aos filtros anteriores. Esse retorno não ignora os filtros; eles foram avaliados antes.

Se existe busca, `find` localiza o nome do setor. Depois a função junta código, filial, título, descrição, item, nome do setor e nome da situação em um único texto, separados por espaços. `searchable` prepara esse texto e a consulta. `.includes(...)` verifica se a consulta aparece como uma sequência dentro do texto preparado.

Exemplo de raciocínio: escolha Manutenção e Pendente. Um pedido de Manutenção com situação Aprovado passa pela primeira condição, falha na segunda e recebe `false`. Os filtros são combinados, não alternativos.

Esta busca é por trecho de texto; não é uma busca inteligente por significado. Um termo desconhecido não recebe sinônimos automaticamente.''',
'Se o filtro de setor está vazio, `request.sector !== ""` excluirá todos os pedidos?',
'Não, porque o lado esquerdo `state.sector` do `&&` é uma string vazia. A condição não passa, e o retorno de exclusão dessa linha não acontece.')

block('3.11 — render: transformar o estado atual em tela', 'app.js', 108, 120,
'''“Renderizar”, neste projeto, significa montar a representação visual dos dados atuais e atualizar os elementos correspondentes.''',
'''Leia uma instrução de cada vez:

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

Cada `render` recria os elementos dos setores. Os conjuntos em `state` guardam quais devem reaparecer abertos. Esse mecanismo é diferente de guardar estado dentro das tags que serão substituídas. Uma aplicação mais complexa também precisaria planejar preservação de foco e outras interações ao reconstruir partes da página.''',
'Com uma busca que não encontra nada, quais valores aparecem e qual mensagem se torna visível?',
'Os quatro indicadores vão para zero, a lista de setores fica vazia e aparece o aviso “Nenhuma requisição encontrada”. Os dados originais continuam no array.')

block('3.12 — resetFilters: limpar modelo e controles', 'app.js', 121, 133,
'''O que a pessoa vê nos campos e o que o programa usa para filtrar precisam concordar.''',
'''As quatro primeiras atribuições esvaziam as escolhas guardadas em `state`. As quatro seguintes esvaziam os campos visíveis pelo atributo de objeto `.value`.

Isso é necessário porque o estado e os controles são coisas diferentes. Limpar só `state` pode mostrar uma lista completa enquanto o campo ainda parece filtrado. Limpar só os campos pode deixar `matches` lendo filtros antigos.

`render()` atualiza os resultados com o estado novo. `searchInput.focus()` leva o foco ao campo de busca para a pessoa continuar pelo teclado. A função não retorna uma lista porque seu trabalho é produzir efeitos na interface.''',
'Por que a função limpa tanto `state.query` quanto `searchInput.value`?',
'Um é a escolha que o programa consulta; o outro é o texto do controle na tela. A função sincroniza os dois antes de redesenhar os resultados.')

block('3.13 — applyTheme: uma mudança na raiz altera a paleta', 'app.js', 134, 140,
'''Vamos conectar o atributo escrito na primeira tag HTML às variáveis de CSS que você já estudou.''',
'''`document.documentElement` é o elemento `html`, a raiz. `.dataset.theme = theme` altera seu atributo `data-theme`. Esse é o ponto em que o JavaScript aciona as regras `html[data-theme="light"]` do CSS.

A constante local `button` guarda o botão de tema. Seu `innerHTML` recebe um símbolo e um `span` com texto fixo. Se o tema atual é escuro, a ação oferecida é “Tema claro”; caso contrário, “Tema escuro”. O texto do botão descreve o que acontecerá ao clicar, não apenas o estado atual.

`setAttribute` atualiza `aria-label` para que o nome acessível também descreva essa ação. A função ainda não salva a preferência; veremos o salvamento na inicialização.

Como o HTML inserido nesse botão é composto de literais fixos conhecidos no código, não há texto de pedido entrando nesse `innerHTML`. O contexto é diferente da montagem de cartões com dados variáveis.''',
'Que três coisas esta função muda?',
'O atributo do tema na raiz, o símbolo/texto visível do botão e seu nome acessível. O CSS reage à primeira mudança para recolorir a página.')

block('3.14 — setMenuOpen: mostrar menu e acompanhar o estado', 'app.js', 141, 148,
'''A função recebe um booleano: `true` para abrir e `false` para fechar.''',
'''`classList` permite manipular classes do elemento. `toggle("is-open", open)` usa seu segundo argumento para impor o estado: adiciona a classe se `open` é verdadeiro e remove se é falso. Sem esse segundo argumento, `toggle` simplesmente alternaria.

O backdrop recebe `hidden = !open`. Quando abre, a negação de `true` é `false`, então a camada aparece. Quando fecha, a negação de `false` é `true`, então ela é ocultada.

O botão de menu recebe `aria-expanded` convertido em string e um `aria-label` adequado. Isso mantém a informação acessível de acordo com o que a função acabou de fazer.

O CSS já sabe o que a classe `.is-open` significa em telas pequenas: deslocamento horizontal zero. O JavaScript decide quando aplicar a classe; o CSS decide sua aparência e posição.''',
'O que resultará de chamar `setMenuOpen(false)` duas vezes?',
'O menu permanecerá fechado. O uso do segundo argumento de `toggle` define um estado desejado, em vez de inverter cegamente a cada chamada.')

block('3.15 — init: preencher seleções e conectar eventos', 'app.js', 149, 160,
'''Esta função configura a página. Continuaremos seu corpo nos próximos blocos; não escreva uma chave de fechamento extra agora.''',
'''As duas primeiras linhas usam `insertAdjacentHTML("beforeend", ...)` para acrescentar opções dentro do `select`, no final. Assim a opção inicial “Todos” é preservada.

`sectors.map(...)` cria uma opção por setor: `value` recebe a chave e o texto visível recebe o rótulo. O catálogo de situações segue a mesma lógica. `escapeHtml` prepara os valores e `join("")` une as strings.

A terceira linha cria a legenda. Cada item tem `data-status-key` para acionar a regra de cor, um quadradinho decorativo e o rótulo visível. A legenda representa o catálogo completo, mesmo quando os filtros deixam de mostrar algumas situações na lista.

Agora aparecem **eventos**. Um evento é uma ocorrência como digitar, clicar ou mudar uma seleção. `addEventListener(nomeDoEvento, funcao)` registra uma tarefa a executar quando ele acontecer.

No campo de busca, `input` ocorre durante a edição. A callback sem parâmetros, `() => { ... }`, lê o valor, usa `trim()` para retirar espaços no começo e no fim, atualiza `state.query` e chama `render`.

Nos três `select`, `change` lê o valor escolhido, guarda a escolha na propriedade correspondente e redesenha. Aqui o evento não altera a lista de pedidos; só muda a visualização.

Nos botões de limpar, passamos `resetFilters` sem parênteses. Queremos registrar a função para o clique futuro. Escrever `resetFilters()` executaria a função imediatamente e passaria seu resultado, não a tarefa desejada.

Os blocos `{ ... }` das callbacks têm ponto e vírgula entre suas instruções. O `});` fecha o corpo da callback, a chamada do método e a instrução externa.''',
'Siga a sequência de uma tecla digitada: qual função do programa roda ao final?',
'O evento `input` chama a callback, que atualiza `state.query` e chama `render()`. `render` usa `matches` para filtrar e as funções de cartão/setor para montar o resultado.')

block('3.16 — Acompanhar quais detalhes estão abertos', 'app.js', 161, 170,
'''Este trecho é mais avançado. Seu objetivo é lembrar quais cartões a pessoa abriu para reconstruí-los de modo consistente depois de filtrar.''',
'''O listener fica no recipiente `sectorList`, que permanece na página. Os cartões dentro dele são recriados por `render`.

`toggle` é o evento associado à mudança de abertura do `details`. A callback recebe `event`, um objeto com informações sobre a ocorrência. `event.target` é o elemento em que o evento se originou, não necessariamente aquele no qual colocamos o listener.

A primeira condição retorna sem fazer nada se o evento não é `isTrusted` ou se seu alvo não é uma instância de `HTMLDetailsElement`. `instanceof` verifica o tipo de objeto; `!` nega; `||` representa “ou” neste teste. Um `return` sem valor apenas encerra a callback.

**Precisão importante:** `isTrusted` indica se o evento foi produzido pelo navegador, em contraste com um evento criado e disparado por script com `dispatchEvent`. Não é prova de ação humana: algumas ações de script também podem resultar em eventos produzidos pelo navegador. Aqui ele participa de uma filtragem de eventos, não de uma autenticação.

`dataset.sectorId` lê `data-sector-id`; `dataset.cardId` lê `data-card-id`. Um setor tem o primeiro; um pedido tem o segundo. O ternário escolhe o conjunto correto, `openSectors` ou `openCards`.

`sectorId || cardId` usa o primeiro valor truthy disponível como identificador. Se ele existe, `.open` consulta o booleano de abertura do `details`: `.add` coloca no conjunto quando aberto e `.delete` remove quando fechado.

O último argumento `true` de `addEventListener` ativa a fase de captura. Ela permite ouvir o evento vindo dos `details` descendentes no caminho de descida pelo DOM; não dependemos de ele propagar por bubbling, porque `toggle` de `details` não borbulha.

Neste mecanismo, o estado é salvo na memória da página. Não passa a sobreviver ao fechamento do navegador. Experimente a sequência abrir, filtrar e limpar para observar como ele se comporta na reconstrução.''',
'Por que não registrar todos esses listeners diretamente nos cartões uma única vez no começo?',
'No começo os cartões ainda não existem, e depois eles serão substituídos por `innerHTML`. O recipiente permanente continua recebendo os eventos por captura dos novos elementos.')

block('3.17 — Expandir e recolher em conjunto', 'app.js', 171, 181,
'''Os botões atualizam o estado de abertura e deixam `render` construir a tela de acordo com ele.''',
'''No clique de expandir, `map` extrai todas as chaves dos setores e todos os IDs de pedidos. Cada lista vira um novo `Set`, que substitui a propriedade correspondente de `state`. O objeto `state` continua o mesmo, portanto sua declaração com `const` não é violada.

O `render()` seguinte consulta esses conjuntos e insere `open` nos detalhes. A ação usa todos os registros de `requests`, inclusive os que estejam fora do filtro atual; quando voltarem a ser exibidos, seus IDs estarão no conjunto.

No botão de recolher, `.clear()` esvazia os conjuntos existentes. Outra chamada de `render` monta os detalhes fechados. Observe a diferença entre `.delete(id)`, que remove um valor, e `.clear()`, que remove todos os valores do conjunto.''',
'Ao recolher todos, os pedidos são apagados?',
'Não. Somente as coleções que guardam abertura são esvaziadas. O array `requests` continua com os doze objetos.')

block('3.18 — Cliques do menu, links e tecla Escape', 'app.js', 182, 196,
'''Ainda dentro de `init`, conectaremos os controles de navegação às funções já declaradas.''',
'''A constante `menuButton` localiza o botão. A callback de clique lê `aria-expanded`. `getAttribute` devolve texto ou `null`; por isso a comparação é com a string `"true"`. Se ainda não está expandido, a expressão `!== "true"` passa `true` a `setMenuOpen` e abre. No clique seguinte passa `false`.

O clique no backdrop sempre pede para fechar. `querySelectorAll` encontra todos os links da classe indicada; ao contrário de `querySelector`, retorna uma coleção. `forEach` registra um listener em cada link.

Dentro do clique de um link, outro `forEach` retira `is-active` de todos os links. Depois a classe é adicionada ao link clicado, e o menu é fechado. O link continua com seu comportamento normal de ir à âncora porque não usamos `preventDefault`.

O destaque acompanha o link clicado; este trecho não observa automaticamente a rolagem para descobrir qual seção está na tela. É importante explicar o que o código realmente implementa.

O listener `keydown` no documento examina a tecla. Se é `Escape` e o menu está aberto, fecha o menu e retorna o foco ao botão. O `&&` exige ambas as condições. Isso dá uma maneira de sair do menu usando o teclado.''',
'Por que comparar `getAttribute("aria-expanded")` com `true` sem aspas não produziria a mesma comparação estrita?',
'O atributo é lido como string, enquanto `true` sem aspas é booleano. Em `===` e `!==`, tipos diferentes importam. Já a propriedade `.open` de um elemento details é um booleano.')

block('3.19 — Preferência salva e a primeira chamada', 'app.js', 197, 209,
'''Chegamos ao final do arquivo. A última linha é o comando que inicia a configuração da página.''',
'''`let savedTheme = "dark"` começa com um padrão que poderá ser reatribuído. Usamos `let` porque o valor pode ser substituído pelo que estiver guardado.

`localStorage.getItem(...)` consulta uma string guardada no navegador sob uma chave. `|| "dark"` escolhe o padrão quando a consulta não produz um texto truthy. `try` tenta executar um bloco; `catch` trata uma falha lançada. Alguns ambientes restringem esse armazenamento; a preferência é opcional e o painel deve continuar.

A função seguinte aceita como tema claro apenas o valor `"light"`; qualquer outro valor resulta em escuro. Isso evita usar arbitrariamente um texto salvo como nome de tema.

O listener do botão calcula `next` com um ternário: escuro vira claro, e o restante vira escuro. `const next` não precisa mudar durante essa chamada. `applyTheme(next)` atualiza a tela e `localStorage.setItem(...)` tenta guardar a escolha. Cada clique executa novamente a callback e cria um novo `next` local; `const` não significa que todas as chamadas terão o mesmo valor.

**Limite do armazenamento:** ele guarda a preferência de tema neste projeto, não os pedidos. O comportamento do `localStorage` em páginas abertas por `file:` pode variar entre navegadores. A lógica de tolerância a falhas está prevista por isso. Não trate esse recurso como banco compartilhado entre pessoas.

`render()` faz a primeira montagem dos pedidos. A chave seguinte encerra a declaração de `init`. Finalmente, `init();` chama essa função. Sem essa chamada, você teria descrito as funções, mas não teria conectado os eventos nem feito a primeira renderização.

**Ponto de conferência do projeto:** salve os três arquivos e recarregue. Agora devem aparecer 12 pedidos em 5 setores, 3 com e-mail e 9 situações. Digite “manutencao”, experimente filtros, abra detalhes, limpe os campos e alterne o tema. Em uma janela estreita, abra e feche o menu.''',
'Se você remover só `init();`, as funções desaparecem? O painel se inicializa?',
'As declarações continuam no arquivo, mas essa configuração deixa de ser iniciada por aquela chamada. Ter a receita de uma função é diferente de executá-la.')

prose(r'''
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
''')

def inline(value):
    # Protege conteúdo de código antes da formatação de ênfase.
    protected = []
    def code(match):
        protected.append('<code>' + html.escape(match.group(1)) + '</code>')
        return f'@@CODE{len(protected)-1}@@'
    value = re.sub(r'`([^`]+)`', code, value)
    value = html.escape(value)
    value = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', value)
    for index, item in enumerate(protected):
        value = value.replace(f'@@CODE{index}@@', item)
    return value

def to_html(markdown):
    lines = markdown.splitlines()
    output, headings = [], []
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue
        if line.startswith('```'):
            language, content = line[3:], []
            index += 1
            while index < len(lines) and not lines[index].startswith('```'):
                content.append(lines[index])
                index += 1
            output.append('<div class="code-label">' + html.escape(language) + '</div><pre><code>' + html.escape('\n'.join(content)) + '</code></pre>')
            index += 1
            continue
        heading = re.match(r'^(#{1,3}) (.*)', line)
        if heading:
            level, title = len(heading[1]), heading[2]
            anchor = 'parte-' + str(len(headings))
            headings.append((level, title, anchor))
            output.append(f'<h{level} id="{anchor}">' + inline(title) + f'</h{level}>')
            index += 1
            continue
        if line.startswith('|'):
            rows = []
            while index < len(lines) and lines[index].startswith('|'):
                cells = [x.strip() for x in lines[index].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', x) for x in cells):
                    tag = 'th' if not rows else 'td'
                    rows.append('<tr>' + ''.join(f'<{tag}>' + inline(x) + f'</{tag}>' for x in cells) + '</tr>')
                index += 1
            output.append('<div class="table-wrap"><table>' + ''.join(rows) + '</table></div>')
            continue
        list_match = re.match(r'^(- |\d+\. )(.*)', line)
        if list_match:
            ordered = list_match[1] != '- '
            tag, entries = ('ol' if ordered else 'ul'), []
            pattern = r'^\d+\. (.*)' if ordered else r'^- (.*)'
            while index < len(lines):
                match = re.match(pattern, lines[index])
                if not match:
                    break
                entries.append('<li>' + inline(match[1]) + '</li>')
                index += 1
            output.append(f'<{tag}>' + ''.join(entries) + f'</{tag}>')
            continue
        paragraph = [line]
        index += 1
        while index < len(lines) and lines[index].strip() and not re.match(r'^(#|```|\||- |\d+\. )', lines[index]):
            paragraph.append(lines[index])
            index += 1
        content = ' '.join(paragraph)
        special = ' class="checkpoint"' if content.startswith(('**Pare e pense', '**Conferência:', '**Ponto de conferência')) else ''
        output.append(f'<p{special}>' + inline(content) + '</p>')
    toc = '<nav aria-label="Aulas"><strong>Estude por etapas</strong><ol>' + ''.join(f'<li><a href="#{anchor}">{html.escape(title)}</a></li>' for level, title, anchor in headings if level == 2) + '</ol></nav>'
    return '''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Aprenda construindo — Painel de requisições</title>
<style>
:root{color-scheme:light;font-family:system-ui,-apple-system,"Segoe UI",sans-serif;color:#223345;background:#f6f4ef;line-height:1.75}*{box-sizing:border-box}body{margin:0}.book{max-width:1060px;margin:auto;padding:36px 42px 90px;background:#fff}h1{font-size:clamp(30px,4vw,48px);line-height:1.15;letter-spacing:-.04em;color:#103d4c}h2{margin-top:64px;padding-top:24px;border-top:3px solid #228c91;font-size:28px;line-height:1.3}h3{margin-top:44px;font-size:22px;line-height:1.4;color:#14535c}p{margin:17px 0}li{margin:9px 0}a{color:#086d76;text-underline-offset:3px}nav{background:#eaf5f4;padding:22px 28px;border-radius:12px;margin:28px 0}nav ol{margin-bottom:0}code{font-family:Consolas,"Courier New",monospace;font-size:.9em;background:#eef3f4;padding:2px 5px;border-radius:4px;overflow-wrap:anywhere}pre{margin:0 0 24px;padding:22px;background:#142832;color:#ecf6f7;border-radius:0 0 10px 10px;white-space:pre-wrap;overflow-wrap:anywhere;font-size:14px;line-height:1.65}pre code{background:none;padding:0;color:inherit;font-size:inherit}.code-label{padding:7px 16px;background:#203e4a;color:#acdfe0;border-radius:10px 10px 0 0;font-size:12px;font-weight:700;letter-spacing:.05em}.table-wrap{overflow:auto}table{border-collapse:collapse;width:100%;margin:20px 0;font-size:14px}th,td{border:1px solid #d7e2e5;padding:11px 13px;text-align:left;vertical-align:top}th{background:#eef5f5}td code{white-space:normal}.checkpoint{padding:14px 18px;border-left:4px solid #278c8f;background:#eef8f6}h2,h3{scroll-margin-top:18px}.intro{font-size:12px;letter-spacing:.15em;color:#527780;text-transform:uppercase}.endnote{margin-top:50px;padding-top:18px;border-top:1px solid #ddd;font-size:13px;color:#526474}@media(max-width:650px){.book{padding:20px 18px 60px}pre{padding:14px;font-size:12px}h2{font-size:24px}h3{font-size:20px}nav{padding:16px}}@media print{body,.book{background:white}.book{max-width:none;padding:0}nav{break-after:page}h2{break-before:page}h2,h3,.code-label{break-after:avoid}pre{color:#111;background:#f4f4f4;font-size:10px;white-space:pre-wrap}.code-label{color:#222;background:#e9e9e9}a{color:inherit}table{font-size:11px}}
</style></head><body><main class="book"><div class="intro">Caderno de estudo • do primeiro elemento à primeira ideia própria</div>''' + toc + ''.join(output) + '<p class="endnote">Material elaborado a partir dos arquivos locais do protótipo em 26/09/2026. Trechos conferidos com a versão lida; projetos podem mudar depois. Este caderno é independente e funciona sem rede.</p></main></body></html>'

def main():
    for name, lines in coverage.items():
        expected = list(range(1, len(sources[name].splitlines()) + 1))
        assert lines == expected, f'Cobertura incompleta ou fora de ordem: {name}'
    markdown = ''.join(parts)
    (HERE / 'Aprenda-construindo.md').write_text(markdown, encoding='utf-8')
    (HERE / 'Aprenda-construindo.html').write_text(to_html(markdown), encoding='utf-8')
    manifest = {
        'source': str(SOURCE),
        'files': {name: {'lines':len(content.splitlines()), 'sha256':hashlib.sha256((SOURCE/name).read_bytes()).hexdigest()} for name, content in sources.items()},
        'coverage': 'Todos os trechos, em ordem, sem omitir linhas dos arquivos lidos.',
        'source_edits': False,
    }
    (HERE / 'verificacao.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'markdown_characters':len(markdown), 'source_lines':{name:len(lines) for name,lines in coverage.items()}, 'lessons':sum(1 for line in markdown.splitlines() if line.startswith('### ')), 'output':str(HERE)},ensure_ascii=False))

if __name__ == '__main__':
    main()
