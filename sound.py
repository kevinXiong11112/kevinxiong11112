import pygame

pygame.mixer.init()
condition = True

if condition:
    for i in range(10):
        pygame.mixer.music.load(r'C:\Users\engik\.vscode\Goat-baa-sound-effect.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
