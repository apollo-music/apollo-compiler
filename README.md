# Apollo music generator

Este é o repositório para o código da linguagem musical Apollo.

## Como executar
Para execução é desejável o docker instalado. Considerando que ele ja esteja instalado, entre na pasta `src`e executa `docker build -t apollo .`. Com isso, uma imagem com todas as dependencias será criada a estará pronta para o uso.

Digite `docker images` verificar se a imagem foi gerada. Deverá ter um output:
```
```

Com isso, execute `docker run -it --rm --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" -v=$(pwd)/..:$(pwd)/.. -w=$(pwd) apollo bash`. E assim estará dentro de um terminal que poderá executar `./start.py <nome to arquivo>
