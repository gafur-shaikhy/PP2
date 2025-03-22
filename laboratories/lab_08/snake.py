import pygame
import sys
import random

pygame.init()

HEIGHT = 600
WIDTH = 600
grid_SIZE = 20 
grid_WIDTH = WIDTH // grid_SIZE
grid_HEIGHT = HEIGHT // grid_SIZE
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()

def drawGrid(surface):
    for y in range(0, grid_HEIGHT):
        for x in range(0, grid_WIDTH): 
            r = pygame.Rect((x * grid_SIZE, y * grid_SIZE), (grid_SIZE, grid_SIZE))
            if (x + y) % 2 == 0:
                pygame.draw.rect(surface, (200, 100, 100), r)  # қанық қызыл
            else:
                pygame.draw.rect(surface, (180, 80, 80), r)  # оданда қанық қызыл

class Snake(object):
    def __init__(self):
        self.length = 4  # жылан ұзындығы
        self.direction = RIGHT  # крч оңға қозғалып бастайды
        # жыланның бірінші позициясы 4 блок
        x, y = WIDTH // 2, HEIGHT // 2
        self.positions = [((x - i * grid_SIZE, y)) for i in range(self.length)]
        self.color = (17, 24, 47)

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * grid_SIZE)) % WIDTH), (cur[1] + (y * grid_SIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            return True  # егер жылан өзіне тисе True
        
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
        return False  # егер тимеген жағдайда False

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (grid_SIZE, grid_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

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

class Food(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_WIDTH - 1) * grid_SIZE,
                         random.randint(0, grid_HEIGHT - 1) * grid_SIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (grid_SIZE, grid_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

snake = Snake()
food = Food()
FPS =  5
score = 0

myfont = pygame.font.SysFont("monospace", 16)
game_over_font = pygame.font.SysFont("monospace", 36)  # кішкентай шрифт

game_over = False

while True:
    if not game_over:
        snake.handle_keys()
        drawGrid(surface)
        game_over = snake.move()  # Проверяем, столкнулась ли змея с собой

        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            FPS += 1
            food.randomize_position()

        snake.draw(surface)
        food.draw(surface)
        
        screen.blit(surface, (0, 0))
        text = myfont.render("Score: {0}".format(score), 1, (0, 0, 0))
        screen.blit(text, (5, 10))
        
        if game_over:
            game_over_text = game_over_font.render("Game Over! Score: {0}".format(score), 1, (0, 0, 0))
            # Центрируем текст на экране
            text_width, text_height = game_over_font.size("Game Over! Score: {0}".format(score))
            screen.blit(game_over_text, (WIDTH // 2 - text_width // 2, HEIGHT // 2 - text_height // 2))
        
        pygame.display.flip()
        clock.tick(FPS)
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()