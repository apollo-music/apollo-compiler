# Utilizando o git

O gitlab do grupo 9 irá fluir através das seguintes regras e estruturas:

* Ele possuirá Branches fixos e branches temporários, onde cada um deles será definido como se cria, e como gerenciar
* Os branches fixos serão: Master/origin e Develop
* Os branches temporários (ou de suporte) mais básicos poderão ser os seguintes:

  * Features;
  * Releases;
  * Hotfix.

## Branches principais

### Master/origin
Este branch deveria ser familiar para todos os usuários do Git. Paralelo a este branch, existirá um outro branch chamado develop.
Nós consideraremos o origin/master como o principal branch onde os códigos fonte que refletirem o estado de _produção-entrega_ estarão indicados.
É onde os códigos executáveis e desejáveis para apresentações estarão indicados.

Nós consideraremos o origin/develop o branch principal onde o código fonte do HEAD sempre refletirá um estado de última atualização de entrega para eventuais entregas de produção. Ou seja, é  o que podemos chamar de Branch de integração, onde iremos submeter códigos que possua poucos conflitos, e onde as construções do sistema serão feitos.

Quando o código fonte do branch de develop atingir um estado estavel, e estiver pronto para ser entregue, todas as suas mudanças devem ser agrupadas (merged) de volta para o branch Master.

O branch Master deve possuir um indicador numérico para definir em qual versão ele se encontra. Toda vez que uma alteração é feita no branch Master, os testes do software e built-in do proggrama deve ser automaticamente testado.

## Branches de suporte, ou temporários.
A seguir, serão indicados quais são os branches temporários, e de onde eles devem ser criados, e comandos sugeridos para fazer o merge de cada versão de volta para sua respectiva origem.

### Features
* Este branch é criado de: _develop_
* Este branch deve sofrer merge de volta com: _develop_
* Convenção do nome do branch: Qualquer nome, exceto por _master, develop, release-*, ou hotfix-*_

Branches de features (ou as vezes chamados de branches de tópicos) são utilizados para implementar novos features que ainda irão ser utilizados em futuras atualizações/releases. Quando se começa a trabalhar em um feature, não se sabe em qual ponto do projeto exatamente ela vai ser incluida. A essência deste tipo de feature é que, enquanto ele estiver sendo desenvolvido, a branch existe. Uma vez que ele for incorporado no sistema/software

#### Criação do branch:
```
$ git checkout -b myfeature develop
```
_Switched to a new branch "myfeature"_


#### Incorporando um branch feature no develop:

Após terminar de criar os features, eles devem sofrer merged através do branch de develop, para garantir sua release definitiva:
```
$ git checkout develop
Switched to branch 'develop'
$ git merge --no-ff myfeature
Updating ea1b82a..05e9557
(Summary of changes)
$ git branch -d myfeature
Deleted branch myfeature (was 05e9557)
$ git push origin develop

```
A frag --no-gg garante que no merge, sempre seja criado um novo objeto de commit, mesmo que o merge pudesse ser realizado com fast-forwarding. Isto garante evitar perda de recuperação, e manter a informação histórica do branch de feature e de seus grupos conectados no branch de develop. Ou seja, é mais facil recuperar informações de versões antigas desta maneira.

(Nos links ao final do readme, será indicado uma fonte que possui imagens uteis para contextualizar melhor o cenário)

### Releases
* Este branch é criado de: _develop_
* Este branch deve sofrer merge de volta com: _develop e Master_
* Convenção do nome do branch: _release-*_

Branches de release tem o intuito de prepara um novo produto para produção. Neste momento, é possível realizar pequenos reparos de bugs, e preparar todos os registros de meta-data para release.

O momento chave para a criação do branch é quando o branch de delevop está na iminência de estar pronto, e refletir um estado desejado para ser atualizado. É neste estado que é declarado o número da versão.

#### Criação do branch:
Vamos supor que iremos criar uma versão 1.2 do projeto. Para isso, devemos criar um branch da versão correspondente, e nomear ela apropriadamente:
```
$ git checkout -b release-1.2 develop
Switched to a new branch "release-1.2"
$ ./bump-version.sh 1.2
Files modified successfully, version bumped to 1.2.
$ git commit -a -m "Bumped version number to 1.2"
[release-1.2 74d9424] Bumped version number to 1.2
1 files changed, 1 insertions(+), 1 deletions(-)
```

bump-version.sh é uma função ficcional do shell que muda alguns arquivos do working copy para refletir a nova versão. (Isso pode ser feito manualmente através da mudança dos arquivos respectivos)

Este branch irá existir até que a versão seja definitivamente discutida e liberada.

#### Incorporando um branch Release:
Quando concluir todos os ajustes do branch, e ele se tornar uma versão real para ser atualizada, algumas ações devem ser realizadas.

Primeiro, o branch deverá sofrer merge com o Master (isso é pertinente, dado que _por definição_, todo novo release deve ser commitado no master). Depois, esse commit deve ter uma tag, para ser uma referência histórica de versão. Para concluir, as mudanças feitas no master devem sofrer merge de volta para o develop, para que em futuras versões possam também conter correção de bugs .

As primeiras duas etapas no Git:
```
$ git checkout master
Switched to branch 'master'
$ git merge --no-ff release-1.2
Merge made by recursive.
(Summary of changes)
$ git tag -a 1.2


```
Nota: é possivel usar as flags -s ou -u para assinalar a tag criptograficamente.

Para manter as mudanças feitas no branch do release, é necessário fazer um merge de volta para o Develop. No Git:
```
$ git checkout develop
Switched to branch 'develop'
$ git merge --no-ff release-1.2
Merge made by recursive.
(Summary of changes)

```

Depois de todas as mudanças serem realizas, basta deletar o branch, visto que ele não é mais necessário:

```
$ git branch -d release-1.2
Deleted branch release-1.2 (was ff452fe).
```

### Hotfix
* Este branch é criado de: _master_
* Este branch deve sofrer merge de volta com: _master e develop_
* Convenção do nome do branch: _hotfix-*_

Como o nome diz, é o branch responsável para consertar bugs que ocorreram ao longo do lançamento de alguma versão do master. Após a correção do bug, a tag correspondente ao master é atualizada com um numerador a mais, baseado no número de bugs que já foi reparado

(Ou seja, no exemplo acima, caso haja um hotfix da versão 1.2, após seu reparo, ela será atualizada para versão 1.2.1)

#### Criação do branch:

```
$ git checkout -b hotfix-1.2.1 master
Switched to a new branch "hotfix-1.2.1"
$ ./bump-version.sh 1.2.1
Files modified successfully, version bumped to 1.2.1.
$ git commit -a -m "Bumped version number to 1.2.1"
[hotfix-1.2.1 41e61bb] Bumped version number to 1.2.1
1 files changed, 1 insertions(+), 1 deletions(-)

```
Não esquecer de atualizar a versão após extrair o branch! (Bump)

Após reparar o bug, ele deve sofrer commit em uma ou mais commits separados:

```
$ git commit -m "Fixed severe production problem"
[hotfix-1.2.1 abbe5d6] Fixed severe production problem
5 files changed, 32 insertions(+), 17 deletions(-)

```
#### Incorporando um branch hotfix:

Quando concluido, o bugfix deve ser convergido de volta (merged) tanto no master quanto no develop. É muito similar ao método de como os branches de release são concluidos.

Primeiro, será atualizado o master, e sua respectiva tag:
```
$ git checkout master
Switched to branch 'master'
$ git merge --no-ff hotfix-1.2.1
Merge made by recursive.
(Summary of changes)
$ git tag -a 1.2.1
```
Depois, será incluso o bugfix no develop, também:
```
$ git checkout develop
Switched to branch 'develop'
$ git merge --no-ff hotfix-1.2.1
Merge made by recursive.
(Summary of changes)
```
A exceção desta regra é quando um branch de release existe. Neste cenário, o hotfix deverá ser convergido (merged)  no branch de release, ao inves do branch de develop.


Finalmente, remova o branch temporário:
```
$ git branch -d hotfix-1.2.1
Deleted branch hotfix-1.2.1 (was abbe5d6).
```
Links de referência:

[A successful Git branching model](http://nvie.com/posts/a-successful-git-branching-model/ "A successful Git branching model")

[Understanding the GitHub Flow](https://guides.github.com/introduction/flow/)

[Using Git tutorial 1](https://gist.github.com/hofmannsven/6814451)

[git - guia prático](http://rogerdudler.github.io/git-guide/index.pt_BR.html)

[Chapter 3
Ramificação (Branching) no Git](https://git-scm.com/book/pt-br/v1/Ramifica%C3%A7%C3%A3o-Branching-no-Git)
