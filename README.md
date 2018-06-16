[![pipeline status](https://gitlab.ic.unicamp.br/mc911/2018-s1/group-9/badges/development/pipeline.svg)](https://gitlab.ic.unicamp.br/mc911/2018-s1/group-9/commits/development)
[![coverage report](https://gitlab.ic.unicamp.br/mc911/2018-s1/group-9/badges/development/coverage.svg)](https://gitlab.ic.unicamp.br/mc911/2018-s1/group-9/commits/development)
# Apollo music generator

Este é o repositório para o código da linguagem musical Apollo.
## Projeto Escolhido
Nosso group definiu desenvolver uma linguagem de programação que possa ser usada para a criação de música, através da compilação de código e subsequente transformação deste em áudio.

### Objetivos
- Criar uma linguagem de programação de fácil utilização que permita que o usuario possa estudar e compor musica.
- Fazer com que a linguagem seja poderosa o suficiente para emitir sons de diferentes instrumentos, podendo personalizar várias características musicais de acordo com a preferência do programador.
- Aprender sobre a construção de um compilador e colocar em prática conhecimentos obtidos em disciplinas prévias.

### Features
Queremos que, ao final do projeto, tenhamos uma linguagem que possua suporte a:
- Definição de BPM (compasso) da musica e trechos dela (i.e: 60 BPM = 60 batimento por minutos)
- Acordes (i.e: Acorde de sol: G)
- Sintetizar Instrumentos (i.e: Guitarra, Piano, etc)
- Funções (i.e: Refrão em sol: (tocar um conjunto iguais))
- Variáveis (i.e: somar/subtrair notas para ir para a próxima nota na escala)
- Paralelismo (i.e: notas/acordes juntos)
- Duração da Nota (i.e: Uma nota pode durar o batida inteira ou apenas uma porcentagem da batida)
- Loops
- Condicionais (i.e: Caso ja tocou 10 vezes, tocar outro trecho)
- Tom base (clave)

### Resultados Esperados
No fim do projeto teremos uma linguagem de programação simples e bem estruturada que permita ao usuario criar músicas intrumentais.

### Desenvolvimento do projeto
#### Flow do git
git-flow

#### Resources
Iremos colocar resources uteis com todo o grupo na pasta resources no root do diretório. **Essa parte não deverá ser avaliada**.

## Como executar
Para execução é desejável o docker instalado e executando.

Primeiro entre na pasta `src` e execute:

```docker build -t apollo .```

Com isso, uma imagem com todas as dependencias será criada a estará pronta para o uso.

Digite `docker images` verificar se a imagem foi gerada. Deverá ter um output:
```
REPOSITORY                    TAG                 IMAGE ID            CREATED              SIZE
apollo                        latest              a21557abd738        About a minute ago   511MB
```

Com isso, execute `./start_docker.sh`

Se você tiver problemas com permissão, execute `chmod u+x docker_start.sh` e tente novamente.

E assim estará dentro de um terminal em que poderá executar `./run.sh`
