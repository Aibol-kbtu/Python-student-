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
        self.randomize()

        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, 3000)  # 3 секунды

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == main_game.fruit.timer_event:
            main_game.fruit.randomize()
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