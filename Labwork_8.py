'''
import pygame
import random
import time
import sys

pygame.init()
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, (0, 0, 0))

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill((255, 255, 255))
pygame.display.set_caption("Car Game")

road_x = 200
road_y = 0
road_width = 600
road_height = 700
border_width = 15


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("002-transport.png")
        self.image = pygame.transform.scale(self.image, (90, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(road_x + 40, road_x + road_width - 40), 0)
        self.platform = pygame.Rect(
        self.rect.left, self.rect.bottom, self.rect.width, 1
    )

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)


        self.platform.x = self.rect.x
        self.platform.y = self.rect.bottom

        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(road_x + 40, road_x + road_width - 40), 0)
            self.platform.x = self.rect.x
            self.platform.y = self.rect.bottom




class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("001-car.png")
        self.image = pygame.transform.scale(self.image, (90, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (road_x + road_width // 2, SCREEN_HEIGHT - 100)
        self.speed = 5

        self.platform = pygame.Rect(
            self.rect.left, self.rect.bottom, self.rect.width, 1
        )

    def move(self):
        pressed = pygame.key.get_pressed()
        inner_road_left = road_x + border_width + 20
        inner_road_right = road_x + road_width - border_width - 20

        if pressed[pygame.K_LEFT] and self.rect.left > inner_road_left:
            self.rect.move_ip(-self.speed, 0)
        if pressed[pygame.K_RIGHT] and self.rect.right < inner_road_right:
            self.rect.move_ip(self.speed, 0)

        self.platform.x = self.rect.x
        self.platform.y = self.rect.bottom


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = 15
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 0), (self.radius, self.radius), self.radius)
        pygame.draw.circle(self.image, (255, 215, 0), (self.radius, self.radius), self.radius - 5)
        self.rect = self.image.get_rect()
        self.respawn()
        self.speed = random.uniform(3, 6)

    def respawn(self):
        self.rect.center = (random.randint(road_x + self.radius, road_x + road_width - self.radius), 0)
        self.speed = random.uniform(3, 6)

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()


P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill((128, 128, 128))

    pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (road_x, road_y, road_width, road_height))
    pygame.draw.rect(DISPLAYSURF, (91, 91, 91), (road_x, road_y, road_width, road_height), border_width)

    for i in range(20, SCREEN_HEIGHT, 100):
        pygame.draw.rect(DISPLAYSURF, (224, 224, 224), (road_x + road_width // 3 - 10, i, 20, 50))
        pygame.draw.rect(DISPLAYSURF, (224, 224, 224), (road_x + 2 * road_width // 3 - 10, i, 20, 50))

    pygame.draw.rect(DISPLAYSURF, (168, 168, 168), (6, 5, 190, 90), border_radius=7)

    scores = font_small.render(f"Score: {SCORE}", True, (0, 0, 0))
    coins_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, (0, 0, 0))
    speed_text = font_small.render(f"Speed: {SPEED:.1f}", True, (0, 0, 0))
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins_text, (10, 40))
    DISPLAYSURF.blit(speed_text, (10, 70))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        if isinstance(entity, (Player, Enemy, Coin)):
            entity.move()

    if pygame.sprite.spritecollideany(P1, coins):
        COINS_COLLECTED += 1
        C1.respawn()


    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        DISPLAYSURF.fill((255, 0, 0))
        DISPLAYSURF.blit(game_over, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 30))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(60)
'''
'''
import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'
    lines = []
    current_line = []
    drawing = False

    red_but = (20, 20)
    green_but = (55, 20)
    blue_but = (90, 20)
    eraser_but = (120, 20)
    palette_area = pygame.Rect(0, 0, 140, 40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_w:
                    mode = 'eraser'

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if ((pos[0] - red_but[0]) ** 2 + (pos[1] - red_but[1]) ** 2) <= radius ** 2:
                    mode = 'red'
                elif ((pos[0] - green_but[0]) ** 2 + (pos[1] - green_but[1]) ** 2) <= radius ** 2:
                    mode = 'green'
                elif ((pos[0] - blue_but[0]) ** 2 + (pos[1] - blue_but[1]) ** 2) <= radius ** 2:
                    mode = 'blue'
                elif ((pos[0] - eraser_but[0]) ** 2 + (pos[1] - eraser_but[1]) ** 2) <= radius ** 2:
                    mode = 'eraser'
                else:
                    if event.button == 1:
                        drawing = True
                        current_line = []


            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    drawing = False
                    if current_line and mode != 'eraser':
                        lines.append((current_line[:], mode, radius))
                    current_line = []

            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if not palette_area.collidepoint(position):
                    if drawing:
                        current_line.append(position)

                        if mode == 'eraser':
                            lines = erase_lines(lines, position, radius)


        screen.fill((255, 255, 255))

        for line_segment in lines:
            points, color_mode, line_width = line_segment
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], line_width, color_mode)
                i += 1

        if drawing and mode != 'eraser':
            i = 0
            while i < len(current_line) - 1:
                drawLineBetween(screen, i, current_line[i], current_line[i + 1], radius, mode)
                i += 1


        pygame.draw.rect(screen, (154, 154, 154), palette_area, border_radius=95)
        pygame.draw.circle(screen, pygame.Color('green'), green_but, radius)
        pygame.draw.circle(screen, pygame.Color('blue'), blue_but, radius)
        pygame.draw.circle(screen, pygame.Color('red'), red_but, radius)


        pygame.draw.rect(screen, (255, 165, 183), (110, 5, 20, 30), border_radius=95)

        if mode == 'red':
            pygame.draw.circle(screen, (255, 255, 255), red_but, radius + 2, 2)
        elif mode == 'green':
            pygame.draw.circle(screen, (255, 255, 255), green_but, radius + 2, 2)
        elif mode == 'blue':
            pygame.draw.circle(screen, (255, 255, 255), blue_but, radius + 2, 2)
        elif mode == 'eraser':
            pygame.draw.rect(screen, (255, 255, 255), (110, 5, 20, 30), 2, 95)

        pygame.display.flip()
        clock.tick(60)


def drawLineBetween(screen, index, start, end, width, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


def erase_lines(lines, position, radius):
    result = []
    for line_segment in lines:
        points, color_mode, line_width = line_segment
        keep_line = True
        for point in points:
            if ((point[0] - position[0]) ** 2 + (point[1] - position[1]) ** 2) <= radius ** 2:
                keep_line = False
                break

        if keep_line:
            result.append(line_segment)

    return result


main()
'''
'''
import sys,pygame,random
from pygame.math import Vector2 # если без этого то тогда будет

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.level = 1
        self.score = 0
        self.foods_to_next_level = 3
        self.base_speed = 150
        self.current_speed = self.base_speed

    def update(self):
        self.snake.snake_move()
        self.check_collision()
        self.check_fall()
        self.check_level_up()
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        self.draw_level()

    def draw_level(self):
        level_text = f"Level: {self.level}"
        level_surface = game_font.render(level_text, True, (56, 74, 12))
        level_x = int(cell_size * cell_number - 100)
        level_y = int(cell_size * cell_number - 40)
        level_rect = level_surface.get_rect(center=(level_x, level_y))

        screen.blit(level_surface, level_rect)
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            while self.fruit.pos in self.snake.body:
                self.fruit.randomize()
            self.snake.add_block()
            self.score += 1


    def check_level_up(self):
        if self.score >= self.level * self.foods_to_next_level:
            self.level += 1
            self.increase_speed()
            pygame.time.set_timer(SCREEN_UPDATE, self.current_speed)

    def increase_speed(self):
        new_speed = int(self.base_speed * (0.8 ** (self.level - 1)))
        self.current_speed = max(50, new_speed)


    def check_fall(self):
        if not 0 <= self.snake.body[0].x < cell_number:
            self.game_over()
        if not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_score(self):
        score_text = f"Score: {self.score}"
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size * cell_number - 100)
        score_y = int(cell_size * cell_number - 80)
        score_rect = score_surface.get_rect(center = (score_x,score_y))

        screen.blit(score_surface,score_rect)


    def draw_grass(self):
        grass_color = (167,209,61)
        for j in range(cell_number):
            if j % 2 == 0:
                for i in range(cell_number):
                    if i % 2 == 0:
                        grass_rect = pygame.Rect(i * cell_size, j * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for i in range(cell_number):
                    if i % 2 != 0:
                        grass_rect = pygame.Rect(i * cell_size, j * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

        self.head_up = pygame.image.load('верх.png').convert_alpha()
        self.head_up = pygame.transform.scale(self.head_up, (cell_size, cell_size))
        self.head_down = pygame.image.load('вниз.png').convert_alpha()
        self.head_down = pygame.transform.scale(self.head_down, (cell_size, cell_size))
        self.head_left = pygame.image.load('влево.png').convert_alpha()
        self.head_left = pygame.transform.scale(self.head_left, (cell_size, cell_size))
        self.head_right = pygame.image.load('Screenshot 2025-11-07 162901-fotor-bg-remover-20251107163352.png').convert_alpha()
        self.head_right = pygame.transform.scale(self.head_right, (cell_size, cell_size))

        self.tail_up = pygame.image.load('верх_змея.png').convert_alpha()
        self.tail_up = pygame.transform.scale(self.tail_up, (cell_size, cell_size))
        self.tail_down = pygame.image.load('вниз_змея.png').convert_alpha()
        self.tail_down = pygame.transform.scale(self.tail_down, (cell_size, cell_size))
        self.tail_left = pygame.image.load('Screenshot 2025-11-07 162934-fotor-bg-remover-20251107163518.png').convert_alpha()
        self.tail_left = pygame.transform.scale(self.tail_left, (cell_size, cell_size))
        self.tail_right = pygame.image.load('право_змея.png').convert_alpha()
        self.tail_right = pygame.transform.scale(self.tail_right, (cell_size, cell_size))

        self.body_vertical = pygame.image.load('вверх_тело.png').convert_alpha()
        self.body_vertical = pygame.transform.scale(self.body_vertical, (cell_size, cell_size))
        self.body_horizontal = pygame.image.load('Screenshot 2025-11-07 162917.png').convert_alpha()
        self.body_horizontal = pygame.transform.scale(self.body_horizontal, (cell_size, cell_size))

        self.body_ld = pygame.image.load('1.png').convert_alpha()
        self.body_ld = pygame.transform.scale(self.body_ld, (cell_size, cell_size))
        self.body_rd = pygame.image.load('2.png').convert_alpha()
        self.body_rd = pygame.transform.scale(self.body_rd, (cell_size, cell_size))
        self.body_lu = pygame.image.load('4.png').convert_alpha()
        self.body_lu = pygame.transform.scale(self.body_lu, (cell_size, cell_size))
        self.body_ru = pygame.image.load('3.png').convert_alpha()
        self.body_ru = pygame.transform.scale(self.body_ru, (cell_size, cell_size))
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_lu,block_rect)
                    if previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_ru, block_rect)
                    if previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_ld,block_rect)
                    if previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_rd, block_rect)
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1, 0): self.head = self.head_right
        elif head_relation == Vector2(0, 1): self.head = self.head_up
        elif head_relation == Vector2(0, -1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail= self.tail_left
        elif tail_relation == Vector2(-1, 0): self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1): self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1): self.tail = self.tail_down

    #def update_
    def snake_move(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
    def add_block(self):
        self.new_block = True
class FRUIT:
    def __init__(self):
        self.randomize() # написать pygame.math.Vector2(self.x,sel.y)
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x, self.y)




pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('001-apple.png').convert_alpha()
apple = pygame.transform.scale(apple, (cell_size, cell_size))
game_font = pygame.font.SysFont(None,30)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()
#W

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)

    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
'''