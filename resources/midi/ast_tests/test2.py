import midi

pattern  = midi.Pattern(tracks = [[
    midi.NoteOnEvent(tick=0, velocity= 100, pitch=72),
    midi.NoteOnEvent(tick=200, velocity= 0, pitch=72),
    midi.NoteOnEvent(tick=0, velocity= 100, pitch=60),
    midi.NoteOnEvent(tick=0, velocity= 100, pitch=61),
    midi.NoteOnEvent(tick=0, velocity= 100, pitch=62),
    midi.NoteOnEvent(tick=200, velocity= 0, pitch=60),
    midi.NoteOnEvent(tick=0, velocity= 0, pitch=61),
    midi.NoteOnEvent(tick=0, velocity= 0, pitch=62),
    midi.NoteOnEvent(tick=0, velocity= 100, pitch=65),
    midi.NoteOnEvent(tick=0, velocity= 100, pitch=66),
    midi.NoteOnEvent(tick=200, velocity= 0, pitch=65),
    midi.NoteOnEvent(tick=0, velocity= 0, pitch=66),
    midi.EndOfTrackEvent(tick=0, data=[])
    ]])
print pattern
midi.write_midifile("test2.mid", pattern)    