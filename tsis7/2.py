import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont("Arial", 24)

music_files = ["Lenka - Everything at Once (dizer.net).mp3", "Icon For Hire - Think I'm Sick (dizer.net).mp3", "Beartooth - You Never Know (dizer.net).mp3"]
current_track = 0
pygame.mixer.music.load(music_files[current_track])

play_key = pygame.K_SPACE
stop_key = pygame.K_s
next_key = pygame.K_RIGHT
prev_key = pygame.K_LEFT

pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == play_key:
                pygame.mixer.music.unpause()

            elif event.key == stop_key:
                pygame.mixer.music.pause()

            elif event.key == next_key:
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()

            elif event.key == prev_key:
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()

    screen.fill((255, 255, 255))
    text = font.render("Press Space to play, S to stop, left/right arrow to skip", True, (0, 0, 0))
    screen.blit(text, (20, 20))
    pygame.display.update()
