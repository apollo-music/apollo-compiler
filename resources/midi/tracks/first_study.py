import midi

# Instantiate a MIDI Pattern (contains a list of tracks)
pattern = midi.Pattern(format=1, resolution = 100, tick_relative=1)

# Instantiate a MIDI Track (contains a list of MIDI events)
track = midi.Track()

# Append the track to the pattern
pattern.append(track)

# Set some meta text information of the track
text = midi.TextMetaEvent(text='C Major Scale')
track.append(text)

# Set the name of the track
trackname = midi.TrackNameEvent(text='solo track')
track.append(trackname)

# Set the instrument played
instrument = midi.ProgramChangeEvent(tick=0, channel=0, data=[1])
track.append(instrument)

# Setting the tempo of the song 
a = midi.SetTempoEvent()
a.set_bpm(bpm = 240)
track.append(a)

# Instantiate a MIDI note on event, append it to the track
on = midi.NoteOnEvent(tick=0, velocity=250, pitch=midi.C_3)
track.append(on)
# Instantiate a MIDI note off event, append it to the track
off = midi.NoteOffEvent(tick=100, pitch=midi.C_3)
track.append(off)

# Instantiate a MIDI note on event, append it to the track
on = midi.NoteOnEvent(tick=0, velocity=250, pitch=midi.D_3)
track.append(on)
# Instantiate a MIDI note off event, append it to the track
off = midi.NoteOffEvent(tick=100, pitch=midi.D_3)
track.append(off)

# Instantiate a MIDI note on event, append it to the track
on = midi.NoteOnEvent(tick=0, velocity=250, pitch=midi.E_3)
track.append(on)
# Instantiate a MIDI note off event, append it to the track
off = midi.NoteOffEvent(tick=100, pitch=midi.E_3)
track.append(off)

# Instantiate a MIDI note on event, append it to the track
on = midi.NoteOnEvent(tick=0, velocity=250, pitch=midi.F_3)
track.append(on)
# Instantiate a MIDI note off event, append it to the track
off = midi.NoteOffEvent(tick=100, pitch=midi.F_3)
track.append(off)

# Instantiate a MIDI note on event, append it to the track
on = midi.NoteOnEvent(tick=0, velocity=250, pitch=midi.G_3)
track.append(on)
# Instantiate a MIDI note off event, append it to the track
off = midi.NoteOffEvent(tick=100, pitch=midi.G_3)
track.append(off)

# Instantiate a MIDI note on event, append it to the track
on = midi.NoteOnEvent(tick=0, velocity=250, pitch=midi.A_3)
track.append(on)
# Instantiate a MIDI note off event, append it to the track
off = midi.NoteOffEvent(tick=100, pitch=midi.A_3)
track.append(off)

# Instantiate a MIDI note on event, append it to the track
on = midi.NoteOnEvent(tick=0, velocity=250, pitch=midi.B_3)
track.append(on)
# Instantiate a MIDI note off event, append it to the track
off = midi.NoteOffEvent(tick=100, pitch=midi.B_3)
track.append(off)

# Add the end of track event, append it to the track
eot = midi.EndOfTrackEvent(tick=0)
track.append(eot)

# Print out the pattern
print pattern

# Save the pattern to disk
midi.write_midifile("first_study.mid", pattern)
