import math
import os
import pygame
from datetime import datetime

RES = WIDTH, HEIGHT = 1200, 800
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 50
radius_list = {'sec': RADIUS - 10, 'min': RADIUS - 55, 'hour': RADIUS - 100, 'digit': RADIUS - 30}
RADIUS_ARK = RADIUS - 8

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

clock12 = dict(zip(range(12), range(0, 360, 30)))
clock60 = dict(zip(range(60), range(0, 360, 6)))

font = pygame.font.SysFont('Verdana', 60)
digit_font = pygame.font.SysFont('Arial', 40, bold=True)


def get_clock_pos(clock_dict, clock_hand, key):
    x = H_WIDTH + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y


def draw_digits():
    for digit, pos in clock12.items():
        if digit == 0:
            digit_str = "12"
        else:
            digit_str = str(digit)

        x, y = get_clock_pos(clock12, digit, 'digit')
        digit_surface = digit_font.render(digit_str, True, pygame.Color('black'))
        digit_rect = digit_surface.get_rect(center=(x, y))
        surface.blit(digit_surface, digit_rect)


_image_library = {}


def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image


pygame.init()
screen = pygame.display.set_mode((1200, 800))
done = False
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    surface.fill(pygame.Color('white'))

    t = datetime.now()
    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second
    pygame.draw.circle(surface, pygame.Color('bisque'), (H_WIDTH, H_HEIGHT), RADIUS)

    screen.blit(get_image('Body.png'), (400, 140))

    hour_end = get_clock_pos(clock60, hour, 'hour')
    pygame.draw.line(surface, pygame.Color('black'), (H_WIDTH, H_HEIGHT), hour_end, 13)
    pygame.draw.circle(surface, pygame.Color('white'), (int(hour_end[0]), int(hour_end[1])), 10)

    min_end = get_clock_pos(clock60, minute, 'min')
    pygame.draw.line(surface, pygame.Color('black'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, minute, 'min'), 7)
    pygame.draw.circle(surface, pygame.Color('white'), (int(min_end[0]), int(min_end[1])), 10)

    sec_end = get_clock_pos(clock60, second, 'sec')
    pygame.draw.line(surface, pygame.Color('black'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, second, 'sec'), 4)
    pygame.draw.circle(surface, pygame.Color('white'), (int(sec_end[0]), int(sec_end[1])), 10)

    pygame.draw.circle(surface, pygame.Color('khaki'), (H_WIDTH, H_HEIGHT), 8)
    pygame.draw.circle(surface, pygame.Color('black'), (H_WIDTH, H_HEIGHT), RADIUS - 13, 11)
    pygame.draw.circle(surface, pygame.Color('gray'), (H_WIDTH, H_HEIGHT), RADIUS - 12, 5)

    time_render = font.render(f'{t:%H:%M:%S}', True, pygame.Color('white'), pygame.Color('white'))
    surface.blit(time_render, (0, 0))

    sec_angle = -math.radians(clock60[t.second]) + math.pi / 2

    pygame.draw.arc(surface, pygame.Color('orange red'),
                    (H_WIDTH - RADIUS_ARK, H_HEIGHT - RADIUS_ARK, 2 * RADIUS_ARK, 2 * RADIUS_ARK),
                    math.pi / 2, sec_angle, 8)

    draw_digits()

    pygame.display.flip()
    clock.tick(20)

'''
------------------------------------------
'''
import tkinter as t
import pygame
import os

pygame.mixer.init()
PLAYLIST_DIR = "playlist_music"
class SimpleAudioPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("music player")
        self.root.geometry("250x150")

        self.playlist = []

        for f in os.listdir(PLAYLIST_DIR):
            if f.endswith(('.mp3', '.mp4')):
                self.playlist.append(f)

        self.current_index = 0


        self.PlaY_but = t.Button(root, text="Play", width=16, command=self.play_audio)
        self.PlaY_but.pack(pady=5)

        self.StoP_but = t.Button(root, text="Stop", width=14, command=self.stop_audio)
        self.StoP_but.pack(pady=5)

        self.NexT_but = t.Button(root, text="Next", width=17, command=self.next_audio)
        self.NexT_but.pack(pady=5)

    def play_audio(self):
        if not self.playlist:
            return
        current_file = os.path.join(PLAYLIST_DIR, self.playlist[self.current_index])
        pygame.mixer.music.load(current_file)
        pygame.mixer.music.play()

    def stop_audio(self):
        pygame.mixer.music.stop()

    def next_audio(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play_audio()


root = t.Tk()
app = SimpleAudioPlayer(root)
root.mainloop()
'''
--------------------------------
'''
import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 600))
done = False
is_blue = True
x = 50
y = 50
radius = 25

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y = max(radius, y - 20)
    if pressed[pygame.K_DOWN]: y = min(600 - radius, y + 20)
    if pressed[pygame.K_LEFT]: x = max(radius, x - 20)
    if pressed[pygame.K_RIGHT]: x = min(1000 - radius, x + 20)

    screen.fill((0, 0, 0))
    if is_blue:
        color = pygame.Color("red")
    else:
        color = (255, 100, 0)
    pygame.draw.circle(screen, color, (x, y), radius)

    pygame.display.flip()
    clock.tick(60)