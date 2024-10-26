import pygame

class AudioPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

    def play(self, file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        
        # Keep the program running while the music plays
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Check every 10 milliseconds
