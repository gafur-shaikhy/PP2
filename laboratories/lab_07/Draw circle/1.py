import pygame
pygame.init()

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Қозғалатын дөңгелек")

WHITE = (255, 255, 255)  
RED = (255, 0, 0)

x, y = 350, 250 #экранның ортасы
radius = 25

running = True
while running:
    screen.fill(WHITE) 

    pygame.draw.circle(screen, RED, (x, y), radius)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
                running = False

        if event.type== pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                y -= 20

            if event.key == pygame.K_DOWN:
                y += 20

            if event.key == pygame.K_RIGHT:
                x += 20

            if event.key == pygame.K_LEFT:
                x -= 20

    pygame.display.flip()

pygame.quit()