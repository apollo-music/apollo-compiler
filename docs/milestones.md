# Etapas
O projeto será realizado em três etapas (*milestones*):

## Etapa 1
Para entrega da primeira etapa faremos um compilador que converterá um código em uma música. A idéia é que ao final da entrega tenhamos uma linguagem que terá duas funções:

Os componentes basicos das nossas "partituras" serao:

  - notas musicais:
    - play (nota): essa funcao irá tocar quantas notas forem fornecidas (*nota*)
      - (nota):definimos a nota a ser tocada e em qual oitava ela se encontrara. exemplo: c3 (do tocado na terceira oitava).
    - AMP (amp): definimos a amplitude das próximas notas que serão tocadas, definindo a dinamica da musica.
    - DUR (dur): definimos a duracao das próximas notas que serão tocadas dentro da musica em funcao da batida do metronomo.
    - metronomo: definimos o valor de beats per minute (bpm), que sera o valor base da duracao das notas.
    - sleep (dur): essa funcao irá indicar que o programa deve não tocar nenhum som por uma dada duracao (*dur*)

Com esses componentes, será possível já tocar melodias simples que não tenham duas notas tocando ao mesmo tempo.

## Etapa 2
Na segunda etapa do projeto iremos implementar labels, loops e synthesizers.

Também iremos extender a função do método play para suportar diferentes notas tocando ao mesmo tempo de um mesmo instrumento (i.e. um acorde)

A ideia de labels é que a linguagem ofereça suporte para que o programador designe um nome para um bloco de código. Assim, se desejarmos repetir uma 
sequência de instruções, é possível executar o bloco especificando somente o nome do bloco e não repetir o código do bloco.

Loops também são estruturas da linguagem que faz muito sentido dado o seu propósito (produzir música). Podemos, por exemplo, designar por um label um refrão, e repetir
dentro do loop o refrão.

Synthesizers podem ser interpretados como os "instrumentos" que irão tocar as notas especificadas pelo programador. Assim é possível, por exemplo, que toquemos
uma música com uma guitarra ou com um berimbau.

## Etapa 3
Essa etapa será a mais desafiadora: aqui objetivamos implementar paralelismo de instrumentos para que vários sons de diversos instrumentos toquem simultaneamente. 

Também implementaremos variáveis, operações entre variáveis e definição de um tom para as operações entre as notas. Por exemplo, se somarmos 1 a uma nota, ao invés do resultado ser a nota seguinte, seria a próxima nota no tom dado.


# Distribuição do trabalho
Nesta seção, detalhamos a distribuição do trabalho para cada um dos 6 membros da equipe. Os números em cada célula indicam em qual etapa aquele membro trabalhará naquela parte do projeto.

![Divisão de Trabalho](img/division.png)
