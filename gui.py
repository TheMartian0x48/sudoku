import pygame
from sudoko import Sudoko
from cell import Cell
from Time import Time

# ==========================================================================
# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (51, 50, 50)
LIGHTBLUE = (102, 131, 179)
DARKGRAY = (82, 84, 82)
# ==========================================================================
window_width = 504
window_height = 554
cell_width = 56
pygame.init()
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("SUDOKO")
font = pygame.font.SysFont("comicsans", 30, False);
clock = pygame.time.Clock()
# ==========================================================================
sudoko = None
timer = None
cells = []


def initiate():
    global sudoko
    global timer
    global cells
    cells = []
    x, y = 0, 0
    sudoko = Sudoko(1)
    print(sudoko)
    timer = Time()
    for r in range(9):
        cells.append([])
        for c in range(9):
            if sudoko.get(r, c) == -1:
                cells[-1].append(Cell(x, y, cell_width, False, WHITE, RED))
            else:
                cells[-1].append(Cell(x, y, cell_width, True, WHITE, BLACK))
            x += cell_width
        y += cell_width
        x = 0


# ==========================================================================
def draw(window, font):
    for r in range(9):
        for c in range(9):
            cells[r][c].draw(window, font, sudoko.grid[r][c])

    pos = cell_width
    for i in range(8):
        width = 1
        if i % 3 == 2:
            width = 2
        pygame.draw.line(window, BLACK, (0, pos), (window_width, pos), width)
        pygame.draw.line(window, BLACK, (pos, 0), (pos, window_width), width)
        pos += cell_width
    pygame.draw.line(window, BLACK, (0, window_width), (window_width, window_width), 2)

    global timer
    time = timer.time()
    timer_text = font.render("{0:2d}:{1:2d}".format(time[0], time[1]), True, BLACK)
    window.blit(timer_text, (window_width - 100, window_width + 20))


# ==========================================================================
def process_mouse(x, y, v):
    print(f"{x}, {y}")
    if v not in range(1, 10) or y > window_width:
        return
    r = y // cell_width
    c = x // cell_width
    print(f"\t{{{r}, {c}, {v}}}")
    if cells[r][c].fixed:
        return
    sudoko.set(r, c, v)


# ==========================================================================
initiate()
run = True
val = -1
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1] or keys[pygame.K_KP1]:
        val = 1
    elif keys[pygame.K_2] or keys[pygame.K_KP2]:
        val = 2
    elif keys[pygame.K_3] or keys[pygame.K_KP3]:
        val = 3
    elif keys[pygame.K_4] or keys[pygame.K_KP4]:
        val = 4
    elif keys[pygame.K_5] or keys[pygame.K_KP5]:
        val = 5
    elif keys[pygame.K_6] or keys[pygame.K_KP6]:
        val = 6
    elif keys[pygame.K_7] or keys[pygame.K_KP7]:
        val = 7
    elif keys[pygame.K_8] or keys[pygame.K_KP8]:
        val = 8
    elif keys[pygame.K_9] or keys[pygame.K_KP9]:
        val = 9
    else:
        val = -1

    if keys[pygame.K_TAB]:
        initiate()
        val = -1

    if val in range(1, 9):
        process_mouse(*pygame.mouse.get_pos(), val)

    window.fill(WHITE)
    draw(window, font)
    pygame.display.update()
    clock.tick(20)
