import pygame
import os
pygame.init()
pygame.mixer.init()

path_folder = "C:\\Users\\Lenovo\\Music\\"

song1 = os.path.join(path_folder, "Bakr - Сирень.mp3")
song2 = os.path.join(path_folder, "V $ X V PRiNCE - После Дождя.mp3")
song3 = os.path.join(path_folder, "Ирина Кайратовна - 5000.mp3")

photo1 = "C:\\Users\\Lenovo\\Pictures\\серень.jpg"
photo2 = "C:\\Users\\Lenovo\\Pictures\\дождь.jpg"
photo3 = "C:\\Users\\Lenovo\\Pictures\\ик5000.jpg"


PlayList = [song1, song2, song3]
current = 0

Photos = [photo1, photo2, photo3]



screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Музыкалық плэйер")

pygame.mixer.music.load(PlayList[current])
pygame.mixer.music.play()


def draw_cover():
    cover_path = Photos[current]  # қазіргі обложка
    if os.path.exists(cover_path):  # бар жоғына тексеру
        cover = pygame.image.load(cover_path)  # суретті қабылдаймыз
        cover = pygame.transform.scale(cover, (500, 500))  # өлшемін өзгерту
        screen.blit(cover, (0, 0))  # экран ортасына орналастыру
    else:
        screen.fill((0, 0, 0))

running = True
while running:

    screen.fill((0, 0, 0))  # экранды тазартамыз
    draw_cover()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            if event.key == pygame.K_s:
                pygame.mixer.music.stop()

            if event.key == pygame.K_n:
                current = (current + 1) % 3
                pygame.mixer.music.load(PlayList[current]) 
                pygame.mixer.music.play()

            if event.key == pygame.K_p:
                current = (current - 1)  % 3
                pygame.mixer.music.load(PlayList[current])
                pygame.mixer.music.play()

    pygame.display.flip()                

pygame.quit()