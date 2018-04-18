import midi

# check events.py in python-midi repository for code
# check containers.py in python-midi repository for code
# good documentation website https://github.com/colxi/midi-parser-js/wiki/MIDI-File-Format-Specifications

# List of all midi events supported by the library
# events marked with ++ are the ones that will be used

# NoteEvent(Event) 

### NoteOnEvent(NoteEvent) ++
### Instantiate a MIDI note on event, append it to the track
### tick: when note should be played
### velocity: how hard the note should be struck (0-127)
### pitch: which note should be played (check esquematico.gif)
midi.NoteOnEvent(tick=0, velocity=20, pitch=midi.G_3)

### NoteOffEvent(NoteEvent) ++
### Instantiate a MIDI note off event, append it to the track
### tick: when note should be released
### pitch: which note should be released (check esquematico.gif)
midi.NoteOffEvent(tick=100, pitch=midi.G_3)

# AfterTouchEvent(Event)

# ProgramChangeEvent(Event)

### ProgramChangeEvent(Event) ++
### Choose the instrument
### tick: when the instrument sound should start
### channel where this sound should be
### data: instrument according to the list
### list: http://www.pjb.com.au/muscript/gm.html
midi.ProgramChangeEvent(tick=0, channel=0, data=[2])

# ChannelAfterTouchEvent(Event)

### ControlChangeEvent(Event)++
### tick: when the control change should start
### channel where this change should be
### data: Control change number and value
### example: CC 64 is the dumper pedal. 0-63 means pedal up and 64-127 pedal down
midi.ControlChangeEvent(tick=0, channel=0, data=[91, 58])

# PitchWheelEvent(Event)

# SysexEvent(Event)

# SequenceNumberMetaEvent(MetaEvent)

# MetaEventWithText(MetaEvent)

### TextMetaEvent(MetaEventWithText) ++
### used to write meta data in the midi file
midi.TextMetaEvent(tick=0, text='creator: ', data=[99, 114, 101, 97, 116, 111, 114, 58, 32])

# CopyrightMetaEvent(MetaEventWithText)

### TrackNameEvent(MetaEventWithText) ++
### same usage as in the TextMetaEvent but for track name
midi.TrackNameEvent(tick=0, text='control track', data=[99, 111, 110, 116, 114, 111, 108, 32, 116, 114, 97, 99, 107])

# InstrumentNameEvent(MetaEventWithText)

# LyricsEvent(MetaEventWithText)

# MarkerEvent(MetaEventWithText)

# CuePointEvent(MetaEventWithText)

# ProgramNameEvent(MetaEventWithText)

#  UnknownMetaEvent(MetaEvent)

# ChannelPrefixEvent(MetaEvent)

# PortEvent(MetaEvent)

# TrackLoopEvent(MetaEvent):

### EndOfTrackEvent(MetaEvent) ++
### Add the end of track event, append it to the track
### tick: when track should come to an end
midi.EndOfTrackEvent(tick=1)

### SetTempoEvent(MetaEvent) ++
### Sets the tempo os the track
### tip: use the methods within the class, like set_bpm
midi.SetTempoEvent(tick=0, data=[12, 53, 0])

# SmpteOffsetEvent(MetaEvent)

### TimeSignatureEvent(MetaEvent) ++
### arg0 numerator
### arg1 denumerator
### arg2 metronome pulse
### arg3 number of 32nd notes per MIDI quarter-note
### The numerator is specified as a literal value, but the denominator is specified as
### the value to which the power of 2 must be raised to equal the number of subdivisions per
### whole note. For example, a value of 0 means a whole note because 2 to the power of 0 is 1 (whole note)
midi.TimeSignatureEvent(tick=0, data=[4, 2, 24, 8])

### KeySignatureEvent(MetaEvent) ++
### A positive value for the key specifies 
### the number of sharps and a negative value specifies the number of flats
### A value of 0 for the scale specifies a major key and a value of 1 specifies a minor key. 
midi.KeySignatureEvent(tick=0, data=[0, 0])

# SequencerSpecificEvent(MetaEvent)










