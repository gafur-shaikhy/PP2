import pygame
import sys
import random
import psycopg2

# PostgreSQL-ге қосылу
conn = psycopg2.connect(
    database="snake",
    user="postgres",
    password="admin",
    host="localhost",
    port=5432
)
cur = conn.cursor()

# Қолданушы аты енгізу
username = input("Enter your username: ")

# Қолданушыны тексеру немесе қосу
cur.execute("SELECT id FROM users WHERE username = %s", (username,))
user = cur.fetchone()

if not user:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()
    print("New user created.")
else:
    user_id = user[0]
    print("Welcome back!")

# Алдыңғы деңгей мен ұпай шығару
cur.execute("SELECT MAX(level), MAX(score) FROM user_score WHERE user_id = %s", (user_id,))
level_data = cur.fetchone()
if level_data[0]:
    print(f"Last level: {level_data[0]}, Score: {level_data[1]}")

# Pygame-ді бастау
pygame.init()
HEIGHT, WIDTH = 600, 600
grid_SIZE = 20
grid_WIDTH = WIDTH // grid_SIZE
grid_HEIGHT = HEIGHT // grid_SIZE

UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()
FOOD_TIMEOUT = 5000

def drawGrid(surface):
    for y in range(grid_HEIGHT):
        for x in range(grid_WIDTH):
            r = pygame.Rect((x * grid_SIZE, y * grid_SIZE), (grid_SIZE, grid_SIZE))
            color = (200, 100, 100) if (x + y) % 2 == 0 else (180, 80, 80)
            pygame.draw.rect(surface, color, r)

class Snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (51, 255, 255)

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        self.direction = point

    def move(self):
        global score  # сыртқы score айнымалысын қолдану үшін

        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * grid_SIZE)) % WIDTH), (cur[1] + (y * grid_SIZE)) % HEIGHT)

        # Өз-өзіне соғу => Ойын біту
        if len(self.positions) > 2 and new in self.positions[2:]:
            print("Game Over! Your score:", score)

            # Ұпай мен деңгей сақтау
            cur_db.execute("""
                INSERT INTO user_score (user_id, level, score)
                VALUES (%s, %s, %s)
            """, (user_id, score // 10 + 1, score))
            conn.commit()

            # Экранға шығару
            surface.fill((0, 0, 0))
            gameover_text = myfont.render(f"Game Over! Score: {score}", True, (255, 0, 0))
            screen.blit(gameover_text, (WIDTH // 2 - 100, HEIGHT // 2))
            pygame.display.flip()

            # 3 секунд күту
            pygame.time.wait(3000)

            # Барлығын жабу
            cur_db.close()
            conn.close()
            pygame.quit()
            sys.exit()

        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect(p, (grid_SIZE, grid_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (200, 100, 100), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cur_db.close()
                conn.close()
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
                elif event.key == pygame.K_p:
                    print("Paused. Saving progress...")
                    cur_db.execute("""
                        INSERT INTO user_score (user_id, level, score)
                        VALUES (%s, %s, %s)
                    """, (user_id, score // 10 + 1, score))
                    conn.commit()
                    paused = True
                    while paused:
                        for e in pygame.event.get():
                            if e.type == pygame.KEYDOWN:
                                paused = False
                            elif e.type == pygame.QUIT:
                                cur_db.close()
                                conn.close()
                                pygame.quit()
                                sys.exit()

class Food(object):
    def __init__(self):
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_WIDTH - 1) * grid_SIZE,
                         random.randint(0, grid_HEIGHT - 1) * grid_SIZE)
        self.weight = random.randint(1, 3)
        self.spawn_time = pygame.time.get_ticks()

    def draw(self, surface):
        r = pygame.Rect(self.position, (grid_SIZE, grid_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (200, 100, 100), r, 1)
        font = pygame.font.SysFont("monospace", 16)
        text = font.render(str(self.weight), True, (0, 0, 0))
        surface.blit(text, text.get_rect(center=r.center))

snake = Snake()
food = Food()
FPS = 5
score = 0
myfont = pygame.font.SysFont("monospace", 16)

# DB курсорын snake ішінде де қолдану үшін
cur_db = cur

# Негізгі ойын циклі
while True:
    snake.handle_keys()
    drawGrid(surface)
    snake.move()

    if pygame.time.get_ticks() - food.spawn_time > FOOD_TIMEOUT:
        food.randomize_position()

    if snake.get_head_position() == food.position:
        snake.length += food.weight
        score += food.weight
        FPS += food.weight
        food.randomize_position()

    snake.draw(surface)
    food.draw(surface)
    screen.blit(surface, (0, 0))
    text = myfont.render("Score: {}".format(score), 1, (0, 0, 0))
    screen.blit(text, (5, 10))
    pygame.display.flip()
    clock.tick(FPS)
