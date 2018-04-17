# Apollo music generator

Este é o repositório para o código da linguagem musical Apollo.

## Como executar
Para execução é desejável o docker instalado.

Primeiro inicie o docker executando:

```systemctl start docker```

Após isso entre na pasta `src` e execute:

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
