# Definição da Linguagem de programação *Apollo*
A linguagem de programação *Apollo* é a linguagem de programação para a criação de músicas de maneira intuitiva, voltada aos usuários que queiram explorar possibilidades musicais usando as facilidades de programação para modificar, visualizar e estruturar composições.

## Compilando *Apollo*
Para compilar arquivos utilizando a linguagem Apollo, sugerimos a utilização do [*Docker*](https://www.docker.com/); para mais instruções, leia o arquivo *README* do projeto. 

## Design da Linguagem
A proposta da linguagem é de criar um jeito intuitivo de se criar músicas aproveitando a natureza linear de programação e da leitura do computador; por isso, é priorizado a ordem sequencial das instruções dadas em um script *Apollo* para se tocar a música, intuitivamente como se o código da linguagem fosse a "partitura" lida pelo computador.

### Variáveis
As variáveis da linguagem *Apollo* são fracamente tipadas; isso significa que declaração de tipos não são necessárias. Foi decidido na arquitetura do projeto pela intuitividade ao usuário ao se declarar variáveis, dando mais atenção ao nome da variável e seu significado que a preocupação com seu tipo estático; no geral, as variáveis vão ser declaradas com base de valores musicais numéricos, como por exemplo:

- Volume do áudio.
- Nota / Sequência de notas.
- Duração de notas.

### Paralelismo
Para facilitar o uso de notas paralelas em um mesmo áudio, criou-se o conceito de "tracks" no código; basicamente, duas partes do código irão rodar em paralelo como programas separados a partir do momento que uma "track" é declarada. Isso é similar ao conceito de "faixas musicais" em edição de áudio, e ao mesmo tempo possibilita explorar conceitos de sincronização de código através do uso das keywords estabelecidas na gramática `cue` e `sync`
