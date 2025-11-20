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
        self.image = pygame.transform.scale(self.image, (90, 100),)
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
        self.speed = random.uniform(3, 6) # можно просто сделать self.speed = 5 or 3 or 4

    def respawn(self):
        self.rect.center = (random.randint(road_x + self.radius, road_x + road_width - self.radius), 0)
        self.speed = random.uniform(3, 6) # можно просто сделать self.speed = 5 or 3 or 4

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
        SPEED += 0.5
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