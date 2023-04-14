""" 
************Questão 1****************
Para tentar solucionar o problema, ele ajustou o documento HTML da seguinte forma:

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <title>Encoding</title>
    <meta charset="utf-8">
</head>
<body>
    <p>paralelepípedo</p>
</body>
</html>

Analise as seguintes proposições.

I. O ajuste realizado não garante que o documento HTML tenha sido armazenado utilizando o encoding UTF-8.

II. Caso o navegador seja configurado para abrir o arquivo utilizando o encoding UTF-8, o ajuste resolverá o problema, ou seja, a letra com acento será exibida corretamente.

III. Caso o desenvolvedor especifique o encoding utilizado pelo navegador na metatag, no lugar de UTF-8, ele resolverá o problema, ou seja, a letra com acento será exibida corretamente.

Resposta: I

************Questão 2****************
Considere o seguinte documento HTML:
<!DOCTYPE html>
<meta charset="utf-8">
<html lang="pt-BR">
<head>
    <title>Testing attributes</title>
</head>
<body>
    <p>What is the lang attribute about?</p>
</body>
</html>

Ao utilizar o atributo “lang” do elemento “html”, o desenvolvedor tinha a intenção de fazer algum tipo de manipulação ou especificação envolvendo o idioma da página. Observe um detalhe interessante: o código “pt-BR” se refere ao idioma português do Brasil. Por outro lado, o conteúdo da página está em inglês.

Analise as seguintes proposições:

I. O atributo lang utilizado pelo desenvolvedor tem como finalidade instruir o navegador a traduzir a página, o que quer dizer que ela será apresentada em português para o usuário.
II. O uso do atributo lang está incorreto. Ele deveria ser utilizado como atributo de DOCTYPE.
III. Embora o atributo lang indique o idioma português do Brasil e o conteúdo textual esteja em inglês, o navegador é capaz de abrir a página, ainda que apresente eventuais erros.

Respota: III

************Questão 3****************
Considere o seguinte documento HTML:
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Nomes</title>
</head>
<body>
    <h1>Lista de Nomes</h1>
    <ol>
        <li>Antonio</li>
        <li>Rodrigo</li>
        <li>Jaqueline</li>
        <li>João</li>
    </ol>
</body>
</html>

A missão do desenvolvedor é fazer com que a página exiba uma lista de nomes ordenada alfabeticamente, de cima para baixo. Considere que a página não está sob efeito de nenhum código CSS e que os valores padrão para os atributos relevantes para essa questão são aqueles utilizados pelos navegadores mais comuns, como Chrome, Edge, Firefox, Safari etc.

Analise as seguintes proposições.

I. O desenvolvedor conseguiu cumprir a sua missão.
II. Ainda que “ol” signifique “ordered list”, alterar a ordem dos elementos “li” (de “list item”) filhos de ol pode fazer com que o desenvolvedor falhe no cumprimento de sua missão.
III. A exibição em ordem alfabética é garantida pelo elemento HTML “ol”, que significa “ordered list”. Caso o elemento “ol” seja alterado para “ul”, de “unordered list”, o desenvolvedor terá falhado no cumprimento da missão.

Respostas: I e II

************Questão 4****************
Dois desenvolvedores, Maria e João,  estão envolvidos no desenvolvimento de um portal para fazer a venda de cosméticos. A exibição de um item precisa conter:

- um cabeçalho
- um corpo com dois elementos textuais
- um rodapé

João fez uma primeira proposta, veja:
<div class="item-cosmetico">
    <div class="cabecalho">
        Batom
    </div>
    <div class="corpo">
        <p>Vermelho</p>
        <p>O melhor para voce</p>
    </div>
    <div class="rodape">Batons XYZ</div>
</div>

Maria analisou o código e fez algumas sugestões de alteração. O resultado foi esse:
<article>
    <header>
        <p>Batom</p>
    </header>
    <div>
        <p>Vermelho</p>
        <p>Coleção tons marcantes</p>
    </div>
    <footer>Batons XYZ - A melhor marca</footer>
</article>

Considere que as classes CSS sequer existem. Elas estão sendo utilizadas apenas com o intuito de promover a legibilidade do código.

Diante do cenário descrito, analise as seguintes proposições.

I. O código de João faz uso de elementos HTML semânticos, o que pode ser comprovado pela aplicação das classes CSS, cujos nomes deixam clara a razão de ser de cada elemento HTML.
II. No código de Maria, o uso do elemento “footer” é inapropriado, pois ele é filho de um elemento “article” e sabemos que somente o “body” de um documento HTML pode ter um rodapé.
III. No que diz respeito ao uso de elementos HTML semânticos, o código de Maria é mais condizente com as boas práticas do que o código de João.

Resposta: III

************Questão 5****************
Dois alunos, Daniel e Carlos, conversam sobre o uso do elemento HTML “table”. 

Daniel está preocupado com a disposição visual dos elementos de sua página, ou seja, com o leiaute dela. Ele acredita que utilizar o elemento table pode ser uma boa ideia para organizar os elementos na página. 

Carlos, por sua vez, está inclinado a concordar com Daniel. Ele ainda adicionou à conversa a seguinte consideração: você poderia utilizar o elemento HTML “table” tanto para o leiaute quanto para a exibição de dados tabulares. Entretanto, ele leu algo sobre a metodologia “tableless”. Como foi a primeira vez que estudou sobre isso, os conceitos não ficaram muito claros. 

Após novas discussões e estudos, os dois concluíram que, na verdade, não se deve utilizar elementos HTML “table”.

Analise as seguintes proposições.

I. Daniel estava correto quando acreditava ser apropriado organizar o leiaute de sua página usando um elemento HTML “table”.
II. Ao adicionar a consideração descrita, Carlos estava parcialmente correto. Ele só esqueceu de comentar que o uso do elemento HTML “table” para leiaute e dados tabulares deveria ser mutuamente exclusivo numa página. Ou seja, se uma página o utiliza para organizar seu leiaute, ela não deve utilizá-lo para a exibição de dados tabulares. E vice-versa.
III. A conclusão a que ambos chegaram sobre não utilizar o elemento HTML “table” está parcialmente correta, já que há formas de uso apropriadas e inapropriadas para ele.

Resposta: III

************Questão 6****************
Os alunos de uma instituição têm acesso a um programa de monitoria. Neste programa, alunos veteranos oferecem conteúdo, exercícios e fazem plantões de dúvidas. Um dos exercícios propostos envolve o seguinte código.

/*arquivo q8.css*/
.texto {
    color: red;
}

p{
    color: green;
}

<!-- arquivo q8.html -->
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="q8.css">
    <title>CSS</title>
</head>
<body>
    <p class="texto">Qual cor?</p>
</body>
</html>

Alguns alunos estão discutindo sobre o exercício. Mateus acredita que a cor que prevalece é determinada pelo efeito cascata do CSS. Ana Beatriz acredita que os seletores apresentados têm especificidades diferentes. Cadu acredita que alterar a ordem em que os seletores são apresentados altera o resultado final.

Qual(is) alunos(as) estão correto(as)?

Resposta: Ana Beatriz, apenas.

************Questão 7****************
Considere o seguinte seletor CSS

.principal p#promocao

Qual frase descreve corretamente os elementos HTML afetados por ele?

a. Todo elemento que tenha a classe principal ou todo elemento “p” que tenha o id promocao.

b. Todo elemento “p” que tenha o id promocao que seja descendente de um elemento que tenha a classe     principal.

c. Todo elemento “p” que tenha a classe promocao que seja descendente de um elemento que tenha a classe principal.

d. Todo elemento “p” que tenha o id promocao que seja filho direto de um elemento que tenha a classe principal.

e. Na verdade,este não é um seletor CSS válido.

Rsposta: b

************Questão 8****************
Considere o seguinte trecho de código.
Nota. Para esta questão, lembre-se da aba “computed” do Chrome Dev Tools. Há exemplos nas apostilas.

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <title>Box model e box sizing</title>
    <style>
        p{
            box-sizing: border-box;
            padding: 10px;
            width: 300px;
            background-color: green;
        }
        
        div{
            box-sizing: content-box;
            padding-left: 10px;
            padding-right: 10px;
            width: 300px;
            background-color: green;
        }
    </style>
</head>
<body>
    <p>Parágrafo</p>
    <h1>No meaning at all</h1>
</body>
</html>

Agora analise as seguintes proposições.

I. Na aba computed, as larguras resultantes (soma de width e padding à esquerda e à direita) do elemento “p” e do elemento “div” são iguais.
II. Na aba computed, o valor de “width” do elemento “p” é igual a 290px.
III.Na aba computed, os valores de “width” dos elementos “p” e “div” são diferentes.

Resposta: III

************Questão 9****************
Os atributos “itemscope” e "itemtype” podem ser aplicados a elementos HTML comuns, como um “h1”, um “article” e até um “video”. Além disso, seu uso está relacionado à especificação dos microdados de uma página.

Resposta: Verdadeiro

************Questão 10****************
É correto dizer que todo o CSS utilizado pela página a seguir é do tipo “inline”, ainda que existam regras duplicadas.

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <title>Cursos</title>
</head>
<body>
    <h1 style="color: green">Portal de cursos</h1>
    <p style="color: blue">Temos cursos nas mais diversas áreas</p>
    <p style="color: blue">Venha conversar conosco e conhecer nossas ofertas de <strong>bolsas de estudos<strong>.</p>
</body>
</html>

Resposta: Verdadeiro
"""
