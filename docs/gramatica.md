# Linguagem Apollo - Gramática
## Tocando notas
A função `play` deve ser evocada toda vez que o usuário queira tocar uma nota, com o pitch determinado pelo número entre `[]`:
```
play: [70]
```
## Sequência básica de notas
Uma sequência de notas é determinado pelos números (pitch) entre `[]`, por exemplo:
```
play: [72, 73, 74]
```
Toca a sequência de notas com o pitch determinado.
## Notas simultâneas
Notas que devem ser tocadas ao mesmo tempo são determinadas entre `()`, por exemplo:
```
play: [72, (60, 61, 62), 73]
```
## Configurando `Play`
O volume e duração das notas em um `play` podem ser modificadas alterando os valores globais `AMP` e `DUR`:
```
amp = 10
dur = 2
play: [72, (60, 61, 62), 73]
```
É possível também sobreescrever tais valores em um `play` específico, não alterando os valores globais; por exemplo:
```
amp = 10
dur = 2
play: [72, (60, 61, 62), 73]
play: [72, 73], amp = 8, dur = 2
play: [72, (60, 61, 62), 73]
```
Apenas o segundo `play` irá tocar as duas notas com `amp = 8` e `dur = 2`.

## Adicionando silêncio
Para inserir tempos de silêncio na música, é possível usar a função `sleep`:
```
play: [70, 71]
sleep 10
play: [72, 73]
```

Isso irá criar um tempo de silêncio em *milisegundos* conforme especificado na função.

## Criando repetições
Repetições podem ser criadas usando a função `repeat`, seguida pelo número de vezes que o trecho de código entre `repeat` e `end repeat` irá ser repetido:
```
repeat 10:
play: [70]
end repeat
```
Irá tocar a nota `70` em sequência 10 vezes.

## Criando variáveis
Variáveis podem ser criadas usando o termo `var`, seguido pelo nome da variável e o valor que ela irá receber:
```
var nota: 70
play: [nota,nota+1,nota-1]
```
Pode-se usar variáveis para armazenar uma sequência de notas também:
```
var acorde: (70, 72, 73)
var sequencia: [70, 71, acorde, 70]
play: sequencia
```
Vale notar que variáveis não são passadas por referência às outras; portanto, no exemplo acima, se `acorde` fosse modificado após a variável `sequencia` ter sido declarada, as notas em `sequencia` não seriam modificadas.

## Criando `Sequences`
As sequences serão somente sequências de notas sequenciais. Se seqA é chamada antes de seqB, toca-se seqA e depois seqB.

```
sequence seqA, inst = I, amp = A, dur = D:
end sequence
```

## Criando `Instruments`
Os instruments definem qual o instrumento será utilizado. Por exemplo, após chamarmos

```
instr = ACOUSTICBASS
```

Todos as notas seguintes serão tocadas com o instrumento "baixo". A lista de instrumentos suportados pode ser vista aqui: http://www.pjb.com.au/muscript/gm.html

## Criando `Tracks`
Para paralelizar notas, é necessário o uso de `tracks`; por exemplo:
```
track melody:
play: [70, 72, 74]
end track

track bass:
play: [(60, 62, 63), (60, 62, 63), (60, 62, 63)]
end track
```
Irá tocar as notas em ambos os `plays` ao mesmo tempo. Para todos os efeitos, `tracks` diferentes se comportam como programas em escopos diferentes, portanto apenas variáveis e configurações declaradas no escopo global (fora das tracks) podem ser referenciadas:
```
var sequencia: [70, 71, 72]
amp = 10
dur = 2

track melody_1:
amp = 5
var nova_sequencia: [69, 70, 71]
play: [sequencia, nova_sequencia]
end track

track melody_2:
play: [sequencia, sequencia]
end track
```
As notas em `melody_1` irão tocar com `amp = 5`, ao contrário de `melody_2`.
## Sincronizando `Tracks` através de `Sync`
A sincronização de `tracks` ocorre através do uso de `sync` - uma track é interrompida (`sync`) e só continua tocando quando outra track emite o sinal através de uma `cue`. Por exemplo:
```
var sequencia: [70, 71, 72]

track melody_1:
play: [sequencia]
cue melody_2
play: [sequencia]
endtrack

track melody_2:
play: [sequencia]
sync
play: [70]
endtrack

call melody_1
```

Como é possível observar, o argumento entre `()` de `cue` é o nome do sinal emitido, e o argumento entre `()` de `sync` é o nome do sinal que deve ser recebido para a respectiva `track` continuar sendo tocada.
