import mido
from mido import Message, MidiFile, MidiTrack

# Create a new MIDI file
mid = MidiFile()

# Create a new MIDI track
track = MidiTrack()
mid.tracks.append(track)

# Add some notes to the track based on input music
input_notes = [60, 62, 64, 65, 67, 69, 71, 72]
for note in input_notes:
    track.append(Message('note_on', note=note, velocity=64, time=0))
    track.append(Message('note_off', note=note, velocity=64, time=48))

# Save the MIDI file
mid.save('output.mid')