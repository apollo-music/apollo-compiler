import midi

pattern = midi.Pattern(format=1, resolution = 100, tick_relative=1)
track = midi.Track()
pattern.append(track)

# definicao de variaveis
bixo = [65, 66]
amp = 100
dur = 200

# definicao de variavel de tempo da musica
beat = 0

# tocando a primiera nota
note_on = midi.NoteOnEvent(tick=beat, velocity= 100, pitch=72)
track.append(note_on)

# definindo beat para que a nota seja solta no tempo certo
beat = dur

# soltando a primeira nota
note_off = midi.NoteOnEvent(tick=beat, velocity= 0, pitch=72)
track.append(note_off)

# arrumando beat para 0
beat = 0

# tocando o arcorde   
note_on = midi.NoteOnEvent(tick=beat, velocity= 100, pitch=60)
track.append(note_on)
note_on = midi.NoteOnEvent(tick=beat, velocity= 100, pitch=61)  
track.append(note_on)
note_on = midi.NoteOnEvent(tick=beat, velocity= 100, pitch=62)
track.append(note_on)

# definindo o tempo de duracao do acorde
beat = dur

# soltando as notas
note_off = midi.NoteOnEvent(tick=beat, velocity= 0, pitch=60)
track.append(note_off)

# tick eh uma medida relativa, logo deve ser setado para zero
beat = 0

# soltando o resto das notas ao mesmo tempo
note_off = midi.NoteOnEvent(tick=beat, velocity= 0, pitch=61)
track.append(note_off)
note_off = midi.NoteOnEvent(tick=beat, velocity= 0, pitch=62)
track.append(note_off)

# tocando o ultimo acorde
note_on = midi.NoteOnEvent(tick=beat, velocity= 100, pitch=bixo[0])
track.append(note_on)
note_on = midi.NoteOnEvent(tick=beat, velocity= 100, pitch=bixo[1])
track.append(note_on)

# setando a duracao do acrode
beat = dur

# soltando o acorde
note_off = midi.NoteOnEvent(tick=beat, velocity= 0, pitch=bixo[0])
track.append(note_off)

# arrumando beat
beat = 0

# soltando o resto das notas ao mesmo tempo
note_off = midi.NoteOnEvent(tick=beat, velocity= 0, pitch=bixo[1])
track.append(note_off)

# Add the end of track event, append it to the track
eot = midi.EndOfTrackEvent(tick=0)
track.append(eot)

# Print out the pattern
print pattern

# Save the pattern to disk
midi.write_midifile("test1.mid", pattern)

