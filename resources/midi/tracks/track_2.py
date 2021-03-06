import midi

# Instantiate a MIDI Pattern (contains a list of tracks)
pattern = midi.Pattern(format=1, resolution = 100, tick_relative=1)

# Instantiate a MIDI Track (contains a list of MIDI events)
track = midi.Track()

# Append the track to the pattern
pattern.append(track)

# Set the instrument played
instrument = midi.ProgramChangeEvent(tick=0, channel=0, data=[1])
track.append(instrument)

# Setting the tempo os the track
self = midi.SetTempoEvent(data = [15, 66, 64])
tempo = midi.SetTempoEvent.set_bpm(self, bpm = 120)
track.append(self)

# Instantiate a MIDI note on event, append it to the track and then a pseudo "note off event"
on = midi.NoteOnEvent(tick=0, velocity= 127, pitch=midi.C_3)
track.append(on)
on = midi.NoteOnEvent(tick=100, velocity= 127, pitch=midi.E_3)
track.append(on)
on = midi.NoteOnEvent(tick=100, velocity= 127, pitch=midi.G_3)
track.append(on)
on = midi.NoteOnEvent(tick=100, velocity= 127, pitch=midi.B_3)
track.append(on)

off = midi.NoteOnEvent(tick=100, velocity= 0, pitch=midi.C_3)
track.append(off)
off = midi.NoteOnEvent(tick=200, velocity= 0, pitch=midi.E_3)
track.append(off)
off = midi.NoteOnEvent(tick=300, velocity= 0, pitch=midi.G_3)
track.append(off)
off = midi.NoteOnEvent(tick=400, velocity= 0, pitch=midi.B_3)
track.append(off)


# Add the end of track event, append it to the track
eot = midi.EndOfTrackEvent(tick=0)
track.append(eot)

# Print out the pattern
print pattern

# Save the pattern to disk
midi.write_midifile("track_2.mid", pattern)