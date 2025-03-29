import pygame
import sys
import random

# pygame-ді бастау
pygame.init()

# Терезенің өлшемдері
HEIGHT = 600
WIDTH = 600

# Тор өлшемі
grid_SIZE = 20 
grid_WIDTH = WIDTH // grid_SIZE
grid_HEIGHT = HEIGHT // grid_SIZE

# Бағыттар
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Уақыт және экран
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()

# Тағамның экранда болу ұзақтығы (миллисекунд)
FOOD_TIMEOUT = 5000

# Торды сызып беру функциясы
def drawGrid(surface):
    for y in range(0, grid_HEIGHT):
        for x in range(0, grid_WIDTH): 
            r = pygame.Rect((x * grid_SIZE, y * grid_SIZE), (grid_SIZE, grid_SIZE))
            # Шахмат тәрізді фон
            if (x + y) % 2 == 0:
                pygame.draw.rect(surface, (200, 100, 100), r)
            else:
                pygame.draw.rect(surface, (180, 80, 80), r)

# Жылан классы
class Snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]  # бастапқы позиция
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])  # кездейсоқ бағыт
        self.color = (51, 255, 255)  # түсі

    # Жыланның басының координатасын қайтару
    def get_head_position(self):
        return self.positions[0]

    # Бағытты өзгерту
    def turn(self, point):
        # Артқа бұрылуға тыйым салу
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    # Жыланды қозғалту
    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        # Жаңа позицияны табу, экран шекарасынан шықса, қайта айналып шығады
        new = (((cur[0] + (x * grid_SIZE)) % WIDTH), (cur[1] + (y * grid_SIZE)) % HEIGHT)

        # Егер өзін-өзі соқса — қайтадан басталады
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    # Жыланды қайтадан бастапқы жағдайға келтіру
    def reset(self):
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    # Жыланды экранға салу
    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (grid_SIZE, grid_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (200, 100, 100), r, 1)  # шекарасы

    # Пернетақтаны өңдеу
    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:  
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)

# Тағам классы
class Food(object):
    def __init__(self):
        self.color = (223, 163, 49)
        self.randomize_position()  # алғашқы орнын орнату

    # Тағамның кездейсоқ орны мен салмағын орнату
    def randomize_position(self):
        self.position = (random.randint(0, grid_WIDTH - 1) * grid_SIZE,
                         random.randint(0, grid_HEIGHT - 1) * grid_SIZE)
        self.weight = random.randint(1, 3)  # тағам салмағы
        self.spawn_time = pygame.time.get_ticks()  # пайда болған уақыты

    # Тағамды экранға салу (ішінде салмағы жазылады)
    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (grid_SIZE, grid_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (200, 100, 100), r, 1)  # шекарасы

        # Тағам салмағын көрсету
        font = pygame.font.SysFont("monospace", 16)
        text = font.render(str(self.weight), True, (0, 0, 0))
        text_rect = text.get_rect(center=r.center)
        surface.blit(text, text_rect)

# Объектілерді құру
snake = Snake()
food = Food()
FPS = 5  # бастапқы жылдамдық
score = 0

myfont = pygame.font.SysFont("monospace", 16)

# Негізгі ойын циклі
while True:
    snake.handle_keys()       # пернелерді тексеру
    drawGrid(surface)         # фон торын салу
    snake.move()              # жыланды қозғалту

    # Егер тағам көп уақыттан бері алынбаған болса – жаңадан шығару
    if pygame.time.get_ticks() - food.spawn_time > FOOD_TIMEOUT:
        food.randomize_position()

    # Егер жылан тағамды жесе
    if snake.get_head_position() == food.position:
        snake.length += food.weight    # ұзарады
        score += food.weight           # ұпай қосылады
        FPS += food.weight             # жылдамдығы артады
        food.randomize_position()      # жаңа тағам

    # Объектілерді салу
    snake.draw(surface)
    food.draw(surface)
    
    screen.blit(surface, (0, 0))  # экранға салу
    text = myfont.render("Score: {0}".format(score), 1, (0, 0, 0))
    screen.blit(text, (5, 10))  # ұпайды көрсету
    
    pygame.display.flip()  # экранды жаңарту
    clock.tick(FPS)        # FPS бойынша кадр шектеу
