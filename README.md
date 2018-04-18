[![pipeline status](https://gitlab.ic.unicamp.br/mc911/2018-s1/group-9/badges/development/pipeline.svg)](https://gitlab.ic.unicamp.br/mc911/2018-s1/group-9/commits/development)
[![coverage report](https://gitlab.ic.unicamp.br/mc911/2018-s1/group-9/badges/development/coverage.svg)](https://gitlab.ic.unicamp.br/mc911/2018-s1/group-9/commits/development)
# Apollo music generator

Este é o repositório para o código da linguagem musical Apollo.

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
