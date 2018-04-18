## Análise Semântica

A análise semântica, nesta etapa do projeto, verifica as seguintes condições:

1. Variáveis usadas mas não definidas
2. Variáveis do tipo Expression sendo usadas dentro de um acorde


Foi definida uma estrutura de passeio pela AST que depende do tipo do nó onde se encontra. Por exemplo, se o passeio se encontra e mum nó de SeqNotas, as ações referentes a este nó serão diferentes
de se estivesse em um nó Expression.

Também foi definida a estrutura da Symbol Table. Ela tem uma estrutura de árvore onde cada nó é um escopo e, dentro de cada nó, existe uma lista de todos os simbolos definidos dentro do escopo.

