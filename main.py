from composer import Composer
from audio_player import AudioPlayer

def main():
    # Set up music composer
    composer = Composer()
    audio_player = AudioPlayer()
    
    # Generate and play music
    melody = composer.create_melody(mood="happy", tempo=120)
    audio_player.play(melody)

if __name__ == "__main__":
    main()
