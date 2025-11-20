import pygame
import math
pygame.init()

screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()

screen.fill((255,255,255))

drawing = False
start_pos = None
tool = "rect"
color = pygame.Color(0,0,0)
line_width = 3

shapes = []

def draw_rectangle(surface, start, end, color, width):
    x1, y1 = start
    x2, y2 = end
    rect = pygame.Rect(min(x1, x2), min(y1, y2),
                       abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(surface, color, rect, width)

def draw_tringle(surface, start, end, color, width):
    x1, y1 = start
    x2, y2 = end

    pygame.draw.polygon(surface,color,[((x1+x2) // 2, y1), (x1, y2), (x2, y2)],width)

def draw_equilateral_tringle(surface, start, end, color, width):
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
    base = math.hypot(dx, dy)

    h = (math.sqrt(3) / 2) * base

    correcting = 5
    if base < correcting:
        base = correcting
    nx = -dy / base
    ny = dx / base

    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2

    x3 = mx + nx * h
    y3 = my + ny * h

    points = [(x1, y1), (x2, y2), (x3, y3)]
    pygame.draw.polygon(surface,color,points,width)
def draw_rhombus(surface, start, end, color, width):
    x1, y1 = start
    x2, y2 = end

    pygame.draw.polygon(surface, color, [((x1 + x2) // 2, y1),(x2, (y1+y2) // 2),((x1 + x2) // 2, y2), (x1, (y1+y2) // 2) ], width)
def draw_circle(surface, start, end, color, width):
    x1, y1 = start
    x2, y2 = end
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2
    radius = int((((x2 - x1)**2 + (y2 - y1)**2)**0.5) / 2)
    pygame.draw.circle(surface, color, (cx, cy), radius, width)

palette = [
    (40, 40, 15, (255, 0, 0)),
    (80, 40, 15, (0, 255, 0)),
    (120, 40, 15, (0, 0, 255)),
    (160, 40, 15, (0, 0, 0)),
    (200, 40, 15, (255, 255, 0)),
    (240, 40, 15, (255, 255, 255))

]

tools_buttons = [
    (280, 40, 15, "rect"),
    (320, 40, 15, "circle"),
    (360, 40, 15, "triangle"),
    (400, 40, 15, "rhombus"),
    (440, 40, 15, "equilateral_triangle"),
    (480, 40, 15, "eraser")
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            for cx, cy, r, col in palette:
                if (x - cx)**2 + (y - cy)**2 <= r**2:
                    color = col
                    break
            else:
                for tx, ty, tr, tname in tools_buttons:
                    if (x - tx)**2 + (y - ty)**2 <= tr**2:
                        tool = tname
                        break
                else:
                    drawing = True
                    start_pos = event.pos
                    if tool == "eraser":
                        shapes.append(("eraser", event.pos, event.pos, (255,255,255), 40))

        if event.type == pygame.MOUSEBUTTONUP:
            if drawing and tool != "eraser":
                end_pos = event.pos
                shapes.append((tool, start_pos, end_pos, color, line_width))
            drawing = False

    screen.fill(pygame.Color("white"))

    for s in shapes:
        t, start, end, col, w = s
        if t == "rect":
            draw_rectangle(screen, start, end, col, w)
        elif t == "circle":
            draw_circle(screen, start, end, col, w)
        elif t == "triangle":
            draw_tringle(screen, start, end, col, w)
        elif t == "equilateral_triangle":
            draw_equilateral_tringle(screen, start, end, col, w)
        elif t == "rhombus":
            draw_rhombus(screen, start, end, col, w)
        elif t == "eraser":
            pygame.draw.circle(screen, (255,255,255), start, 20)

    if tool == "eraser" and pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (236,60,119), (mx, my), 15)
        shapes.append(("eraser", (mx, my), (mx, my), (255,255,255), 40))

    if drawing and tool != "eraser":
        end_pos = pygame.mouse.get_pos()
        if tool == "rect":
            draw_rectangle(screen, start_pos, end_pos, color, line_width)
        if tool == "circle":
            draw_circle(screen, start_pos, end_pos, color, line_width)
        if tool == "triangle":
            draw_tringle(screen, start_pos, end_pos, color, line_width)
        if tool == "equilateral_triangle":
            draw_equilateral_tringle(screen, start_pos, end_pos, color, line_width)
        if tool == "rhombus":
            draw_rhombus(screen, start_pos, end_pos, color, line_width)
    pygame.draw.rect(screen, (180,180,180), (10, 10, 460, 60), border_radius=10)


    for cx, cy, r, col in palette:
        pygame.draw.circle(screen, col, (cx, cy), r)
        pygame.draw.circle(screen, (0,0,0), (cx, cy), r, 2)

    for tx, ty, tr, tname in tools_buttons:
        if tname == "rect":
            pygame.draw.rect(screen, (0,0,0), (tx-tr, ty-tr, tr*2, tr*2), 2)
        elif tname == "triangle":
            pygame.draw.polygon(screen,color,[(tx, ty - tr),(tx - tr, ty + tr),(tx + tr, ty + tr) ],2)
        elif tname == "equilateral_triangle":
            h = tr * math.sqrt(3)
            pygame.draw.polygon(screen,color,[(tx, ty - h/2),(tx - tr, ty + h/2),(tx + tr, ty + h/2) ],2)
        elif tname == "circle":
            pygame.draw.circle(screen, (0,0,0), (tx, ty), tr, 2)
        elif tname == "rhombus":
            pygame.draw.polygon(screen, color, [(tx, ty - tr), (tx - tr, ty ), (tx , ty + tr),(tx + tr, ty  )], 2)
        elif tname == "eraser":
            pygame.draw.rect(screen, (236,60,119), (tx-tr, ty-tr, tr * 1.5, tr*2))
            pygame.draw.rect(screen, (0,0,0), (tx-tr, ty-tr, tr * 1.5, tr*2), 2)

    pygame.display.flip()
    clock.tick(60)
