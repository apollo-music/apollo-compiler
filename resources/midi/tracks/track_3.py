# Estudo sobre uso de tracks para etapas futuras

# Conclusao: duas tracks podem rodar ao mesmo tempo, mas temos que ficar atentos aos ticks
# pois eles funcionarao de maneira separada, como se tivesse tick1 para a track1 e tick2 para a track2

import midi

# Criacao do pattern
pattern = midi.Pattern()

# Criacao da track 1
track1 = midi.Track()
# Criacao da track 2
track2 = midi.Track()

# Colocando as tracks dentro de pattern
pattern.append(track1)
pattern.append(track2)

# Note on na track 1
on = midi.NoteOnEvent(tick=0, velocity= 127, pitch=midi.C_3)
track1.append(on)

# Note on na track 2
on = midi.NoteOnEvent(tick=0, velocity= 127, pitch=midi.D_3)
track2.append(on)

# Note off das notas de ambas as tracks
off = midi.NoteOnEvent(tick=100, velocity= 0, pitch=midi.C_3)
track1.append(off)
off = midi.NoteOnEvent(tick=100, velocity= 0, pitch=midi.D_3)
track2.append(off)

# Finalizacao das tracks
eot = midi.EndOfTrackEvent(tick=0)
track1.append(eot)
track2.append(eot)

# Print out the pattern
print pattern

# Save the pattern to disk
midi.write_midifile("track_3.mid", pattern)