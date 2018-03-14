# Etapas
O projeto será realizado em três etapas (*milestones*):

## Etapa 1
Para entrega da primeira etapa faremos um compilador que converterá um código em uma música. A idéia é que ao final da entrega tenhamos uma linguagem que terá duas funções:

Os componentes basicos das nossas "partituras" serao:

  - notas musicais:
    - play (nota) (amp) (dur): essa funcao irá tocar uma nota (*nota*) em uma dada amplitude (*amp*) e por uma dada duracao (*dur*)
      - (nota):definimos a nota a ser tocada e em qual oitava ela se encontrara. exemplo: c3 (do tocado na terceira oitava).
      - (amp): definimos a amplitude da nota, definindo a dinamica da musica.
      - (dur): definimos a duracao da nota dentro da musica em funcao da batida do metronomo.
    - metronomo: definimos o valor de beats per minute (bpm), que sera o valor base da duracao das notas.
    - sleep (dur): essa funcao irá indicar que o programa deve não tocar nenhum som por uma dada duracao (*dur*)

Com esses componentes, será possível já tocar melodias simples que não tenham duas notas tocando ao mesmo tempo.

## Etapa 2
Na segunda etapa do projeto iremos implementar labels, loops e synthesizers.

A ideia de labels é que a linguagem ofereça suporte para que o programador designe um nome para um bloco de código. Assim, se desejarmos repetir uma 
sequência de instruções, é possível executar o bloco especificando somente o nome do bloco e não repetir o código do bloco.

Loops também são estruturas da linguagem que faz muito sentido dado o seu propósito (produzir música). Podemos, por exemplo, designar por um label um refrão, e repetir
dentro do loop o refrão.

Synthesizers podem ser interpretados como os "instrumentos" que irão tocar as notas especificadas pelo programador. Assim é possível, por exemplo, que toquemos
uma música com uma guitarra ou com um berimbau.

## Etapa 3
Essa etapa será a mais desafiadora: aqui objetivamos implementar threads para que vários sons de diversos instrumentos toquem simultaneamente. 

# Distribuição do trabalho
Nesta seção, detalhamos a distribuição do trabalho para cada um dos 6 membros da equipe.

## Membro 1
 - **Nome:** Henrique Lacreta Alves
 - **RA:** 138507
 - **Responsável por:**

## Membro 2
 - **Nome:** Henrique Noronha Facioli
 - **RA:** 157986
 - **Responsável por:**

## Membro 3
 - **Nome:** Jose Renato Vicente
 - **RA:** 155984
 - **Responsável por:**

## Membro 4
 - **Nome:** Matheus Jun Ota
 - **RA:** 138889
 - **Responsável por:**

## Membro 5
 - **Nome:** Matheus Mortatti Diamantino
 - **RA:** 156740
 - **Responsável por:**

## Membro 6
 - **Nome:** Thiago Silva de Farias
 - **RA:** 148077
 - **Responsável por:**