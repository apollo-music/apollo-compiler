#library used fot the project - supported on python 2
import midi

# Instantiate a MIDI Pattern (contains a list of tracks)
pattern = midi.Pattern()

# Instantiate a MIDI Track (contains a list of MIDI events)
track = midi.Track()

#The MIDI Pattern class inherits from the standard python list, 
# so it supports all list features such as append(), extend(), slicing, and iteration.
# The same happens for tracks
# Append the track to the pattern
pattern.append(track)

# Instantiate a MIDI note on event, append it to the track
on = midi.NoteOnEvent(tick=0, velocity=20, pitch=midi.G_3)
track.append(on)

# Instantiate a MIDI note off event, append it to the track
off = midi.NoteOffEvent(tick=100, pitch=midi.G_3)
track.append(off)

# Add the end of track event, append it to the track
eot = midi.EndOfTrackEvent(tick=1)
track.append(eot)

# Tick explanation
# You might notice that the EndOfTrackEvent has a tick value of 1. 
# This is because MIDI represents ticks in relative time. 
# The actual tick offset of the MidiTrackEvent is the sum of its tick 
# and all the ticks from previous events. 
# In this example, the EndOfTrackEvent would occur at tick 101 (0 + 100 + 1). 

# what should be the tick value for a specific tempo?
# Under the hood, MIDI represents Tempo in microseconds. 
# In other words, you convert Tempo to Microseconds per Beat

# calculation for X bpm
# Y = 60 * 1000000 / X (the time of one beat in microseconds)

# Z = Y / Resolution
# Resolution only expresses how many ticks there are per beat

# W = Z / 1000000 = 1 tick represents W time

# X = 120, resolution = 100 -> Y = 500,000  -> Z = 5000 -> W = 0.005s
# 500,000 / (0.005 * 1000000) = 100

# Print out the pattern
print pattern

# Save the pattern to disk
midi.write_midifile("example.mid", pattern)