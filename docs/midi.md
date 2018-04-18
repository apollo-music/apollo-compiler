# Midi Library
## Funcoes utilizadas


## Note on event
Note on event sera usado sempre que quisermos tocar uma nota
```
midi.NoteOnEvent(tick, velocity, pitch)

tick: when note should be played
velocity: how hard the note should be struck (0-127)
pitch: which note should be played

```

## Note off event
Note on event sera usado sempre que quisermos soltar uma nota
A nota é apertada com note on e solta com note off

```
midi.NoteOffEvent(tick, pitch)

tick: when note should be released
pitch: which note should be released
```

## Program Change Event
Usaremos essa funcao para setar que instrumento sera tocado

```
midi.ProgramChangeEvent(tick, channel, data)

tick: when the instrument sound should start
channel where this sound should be (tip: check the parsed midi file of the midi file created to check the channel being currently used. Usually it is channel 0)
data: instrument according to the list: http://www.pjb.com.au/muscript/gm.html (tip: the data is an array. So, if you want to use instrument 2, use data[2])
```

## End of Track Event
Funcao usada para terminar uma track

```
midi.EndOfTrackEvent(tick)

tick: when track should come to an end
```

## Set Tempo Event
Funcao utilizada para setar o tempo da peça

```
midi.SetTempoEvent(tick=0, data=[])
tick: when the specified tempo should be aplied
tip: leave the data array as shown. Use the set_bpm function of the class to set the bpm. It would be to dificult to set the bpm through the data array.
```



