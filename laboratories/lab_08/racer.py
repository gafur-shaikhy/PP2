import pygame
import random

pygame.init()

width, height = 600, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Racer Game")

white = (255, 255, 255)
red = (255, 0, 0)

# Фон
road = pygame.image.load(r"C:\Users\Lenovo\Desktop\PP2\laboratories\lab_08\images\road.jpg")
road = pygame.transform.scale(road, (width, height))

# Машина
car_width, car_height = 80, 80
car = pygame.image.load(r"C:\Users\Lenovo\Desktop\PP2\laboratories\lab_08\images\car.png")
car = pygame.transform.scale(car, (car_width, car_height))
car_x, car_y = width // 2 - car_width // 2, height - 150
car_speed = 5

# Монета
coin_width, coin_height = 40, 40
coin_img = pygame.image.load(r"C:\Users\Lenovo\Desktop\PP2\laboratories\lab_08\images\coin.png")
coin_img = pygame.transform.scale(coin_img, (coin_width, coin_height))
coin_x = random.randint(50, width - 50)
coin_y = -50
coin_speed = 3
coin_collected = 0
coin_exists = True

font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)

clock = pygame.time.Clock()
running = True
game_over = False

while running:
    if not game_over:
        screen.blit(road, (0, 0))

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 0:
            car_x -= car_speed
        if keys[pygame.K_RIGHT] and car_x < width - car_width:
            car_x += car_speed
        if keys[pygame.K_UP] and car_y > 0:
            car_y -= car_speed
        if keys[pygame.K_DOWN] and car_y < height - car_height:
            car_y += car_speed

        # Монета қозғалысы
        if coin_exists:
            coin_y += coin_speed
            screen.blit(coin_img, (coin_x, coin_y))
            if coin_y > height:
                coin_exists = False

        # Монетаны жинау
        if coin_exists and abs(car_x - coin_x) < 40 and abs(car_y - coin_y) < 40:
            coin_collected += 1
            coin_speed += 0.5
            coin_exists = False

        # Жаңа монета жасау
        if not coin_exists:
            coin_x = random.randint(50, width - 50)
            coin_y = -50
            coin_exists = True

        screen.blit(car, (car_x, car_y))

        score_text = font.render(f"Coins: {coin_collected}", True, red)
        screen.blit(score_text, (10, 10))

        if car_x <= 0 or car_x >= width - car_width:
            game_over = True

        pygame.display.flip()
        clock.tick(60)
    else:
        # Game Over экраны
        screen.blit(road, (0, 0))
        game_over_text = game_over_font.render(f"Game Over! Score: {coin_collected}", True, red)
        text_rect = game_over_text.get_rect(center=(width // 2, height // 2))
        screen.blit(game_over_text, text_rect)

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    running = False
                if event.type == pygame.KEYDOWN:
                    waiting = False
            clock.tick(10)

pygame.quit()
