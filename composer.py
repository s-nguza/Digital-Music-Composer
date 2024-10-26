from MIDIUtil import MIDIFile
import random

class Composer:
    def create_melody(self, mood="neutral", tempo=120):
        midi = MIDIFile(1)  # One track MIDI
        track = 0
        time = 0  # Start at the beginning
        midi.addTempo(track, time, tempo)

        # Generate a simple melody
        for i in range(8):  # 8 notes in this melody
            pitch = random.choice([60, 62, 64, 65, 67, 69, 71])  # Random note
            duration = 1  # One beat duration
            volume = 100  # Standard volume
            midi.addNote(track, 0, pitch, time, duration, volume)
            time += duration  # Move to the next note time

        with open("melody.mid", "wb") as output_file:
            midi.writeFile(output_file)

        return "melody.mid"
