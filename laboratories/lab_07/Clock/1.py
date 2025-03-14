import pygame
import time
pygame.init()


length, width = 700, 500
screen = pygame.display.set_mode((length, width))


clock_picture = pygame.image.load(r"C:\Users\Lenovo\Downloads\clock.png")
minute_line = pygame.image.load(r"C:\Users\Lenovo\Downloads\min_hand.png")
second_line = pygame.image.load(r"C:\Users\Lenovo\Downloads\sec_hand.png")

clock_picture = pygame.transform.scale(clock_picture, (700, 500))
minute_line = pygame.transform.scale(minute_line, (700, 700))
second_line = pygame.transform.scale(second_line, (700, 700))

clock_center = ((length // 2), (width // 2))

running = True
clock = pygame.time.Clock()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.localtime()
    second = current_time.tm_sec
    minute = current_time.tm_min

    minute_angle = (-6 * minute) -54
    second_angle = (-6 * second) + 48

    rotated_second = pygame.transform.rotate(second_line, second_angle)
    rotated_minute = pygame.transform.rotate(minute_line, minute_angle)

    min_rect = rotated_minute.get_rect(center = clock_center)
    sec_rect = rotated_second.get_rect(center = clock_center)

    screen.fill((0, 0 , 0))
    screen.blit(clock_picture, (0, 0))
    screen.blit(rotated_minute, min_rect)
    screen.blit(rotated_second, sec_rect)

    pygame.display.flip()
    clock.tick(1)
    
pygame.quit()    