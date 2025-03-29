import pygame
import random

pygame.init()

# Терезе өлшемдері
HEIGHT = 800
WIDTH = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Суреттерді жүктеу және өлшемін өзгерту
road = pygame.image.load(r"C:\Users\Lenovo\Desktop\PP2\laboratories\lab_08\images\road.jpg")
road = pygame.transform.scale(road, (WIDTH, HEIGHT))

coin_i = pygame.image.load(r"C:\Users\Lenovo\Desktop\PP2\laboratories\lab_08\images\coin.png")
player_im = pygame.image.load(r"C:\Users\Lenovo\Desktop\PP2\laboratories\lab_08\images\car.png")
enemy_im = pygame.image.load(r"C:\Users\Lenovo\Desktop\PP2\laboratories\lab_09\material\Enemy.png")

# Барлық кейіпкерлердің өлшемдерін біркелкі қыламыз
player_im = pygame.transform.scale(player_im, (100, 100))   # ойыншы - көлік
enemy_im = pygame.transform.scale(enemy_im, (40, 80))       # жау
coin_i = pygame.transform.scale(coin_i, (30, 30))           # монета

# Шрифт және есеп айнымалылары
font = pygame.font.SysFont("Verdana", 30)
count = 0
COIN_THRESHOLD = 5
enemy_upgrade_level = 0

# Ойыншы классы
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_im  # ойыншы суреті
        self.speed = 5          # қозғалыс жылдамдығы
        self.rect = self.image.get_rect()
        # Экранның төменгі жағында орналастыру
        self.rect.midbottom = (WIDTH // 2, HEIGHT - 10)
    
    def move(self):
        # Сол немесе оң жаққа қозғалу
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)

        # Шекарадан шықпауын қадағалаймыз
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

# Монета классы
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.base_image = coin_i  # бастапқы сурет
        self.generate()           # алғашқы генерация
    
    def generate(self):
        # Монетаның салмағы мен өлшемін кездейсоқ анықтау
        self.weight = random.randint(1, 3)
        size = 30 * self.weight
        self.image = pygame.transform.scale(self.base_image, (size, size))
        self.rect = self.image.get_rect()
        self.speed = 5 + self.weight * 2  # салмағына қарай жылдамдығы
        self.rect.left = random.randint(0, WIDTH - self.rect.width)
        self.rect.bottom = 0  # жоғарғы жақтан пайда болады

    def move(self):
        # Төменге қарай қозғалу
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate()  # экраннан шықса, жаңасын генерациялаймыз

# Жау классы
class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed=5):
        super().__init__()
        self.image = enemy_im
        self.speed = speed
        self.rect = self.image.get_rect()
        self.reset_pos()  # бастапқы позицияны орнату
    
    def move(self):
        # Төменге қозғалу
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.reset_pos()  # экраннан шықса, қайтадан үстіне қоямыз

    def reset_pos(self):
        # Жаудың жаңа позициясын экранның үстінде кездейсоқ орнату
        self.rect.left = random.randint(0, WIDTH - self.rect.width)
        self.rect.top = -self.rect.height

# Объектілерді құру
player = Player()
coin = Coin()
enemy = Enemy(speed=5)

# Спрайт топтары
all_sprites = pygame.sprite.Group(player, coin, enemy)
coin_sprites = pygame.sprite.Group(coin)
enemy_sprites = pygame.sprite.Group(enemy)

# Ойын циклын бастау
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        player.move()  # ойыншы қозғалады
        coin.move()    # монета қозғалады
        enemy.move()   # жау қозғалады

        # Егер ойыншы монетаны ұстаса
        if pygame.sprite.spritecollideany(player, coin_sprites):
            count += coin.weight  # ұпай қосылады
            coin.generate()       # жаңа монета пайда болады

            # Белгілі ұпай сайын жау жылдамдайды
            if count // COIN_THRESHOLD > enemy_upgrade_level:
                enemy_upgrade_level = count // COIN_THRESHOLD
                enemy.speed += 1

        # Егер ойыншы жауға соғылса – ойын аяқталады
        if pygame.sprite.spritecollideany(player, enemy_sprites):
            game_over = True

    # Экранға фонды және барлық объектілерді салу
    screen.blit(road, (0, 0))
    all_sprites.draw(screen)

    # Ұпай көрсету
    score_text = font.render(f"Score: {count}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Егер ойын бітсе – Game Over жазуы шығады
    if game_over:
        over_text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(over_text, ((WIDTH - over_text.get_width()) // 2, (HEIGHT - over_text.get_height()) // 2))

    pygame.display.flip()  # экранды жаңарту
    clock.tick(60)         # кадр жылдамдығы – 60 FPS

pygame.quit()
