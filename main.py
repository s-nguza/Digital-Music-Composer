from midiutil import MIDIFile
import random
import pygame
from time import sleep


def user_input():
  print("Welcome to our Digital Music Composer")
  tempo = int(input("What temp do you want(BPM): "))
  mood = input("What mood would you like(sad,happy,love): ").strip().upper()
  key = input("Choose a key (C, D, E, F, G, A, B): ").strip().upper()
  return tempo,mood,key



def compose_music(mood, tempo, key):
    midi = MIDIFile(1)
    midi.addTrackName(0, 0, "Track 1")
    midi.addTempo(0, 0, tempo)

    scale = [60, 62, 64, 65, 67, 69, 71, 72]  # C major scale

    time = 0
    duration = 1
    for _ in range(16):  # A 16-note melody
        note = random.choice(scale)
        midi.addNote(0, 0, note, time, duration, 100)
        time += duration

    with open(f"output_{mood}.mid", "wb") as output_file:
        midi.writeFile(output_file)
    print(f"Random music composed and saved as 'output_{mood}.mid'!")



def play_midi(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        sleep(1)  # Let the music play


   

def main():
  tempo,mood,key = user_input()

  compose_music(mood, tempo, key)
  play_midi(f"output_{mood}.mid")

  



if __name__ == "__main__":
    main()
