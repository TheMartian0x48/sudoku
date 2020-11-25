from Time import Time
from sudoko import Sudoko
from cell import Cell
import pygame

# ======================================================================
# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (51, 50, 50)
LIGHTBLUE = (102, 131, 179)
DARKGRAY = (82, 84, 82)
# ======================================================================
window_dimension = (504, 554)
pygame.init()
win = pygame.display.set_mode(window_dimension)
pygame.display.set_caption("SUDOKO")
font = pygame.font.SysFont("comicsans", 30, False)
clock = pygame.time.Clock()

# ======================================================================
sudoko = Sudoko(1)
timer = Time()
cells = []
x, y = 0, 0
for r in range(9):
    cells.append([])
    for c in range(9):
        if sudoko.get(r, c) == -1:
            cells[-1].append(Cell(x, y, 56, 56, False))
        else:
            cells[-1].append(Cell(x, y, 56, 56, True))
        x += 56
    y += 56
    x = 0
# ======================================================================
def draw(win, font):
    for r in range(9):
        for c in range(9):
            cells[r][c].draw(win, font, sudoko.grid[r][c])
    x, y = 56, 56
    for r in range(8):
        thick = 1
        if r % 3 == 2:
            thick = 2
        pygame.draw.line(win, BLACK, (0, y), (504, y), thick)
        y += 56
    for c in range(8):
        thick = 1
        if c % 3 == 2:
            thick = 2
        pygame.draw.line(win, BLACK, (x, 0), (x, 504), thick)
        x += 56
    pygame.draw.line(win, BLACK, (0, 504), (504, 504), 2)
    t = timer.time()
    timer_text = font.render("{0:2d}:{1:2d}".format(t[0], t[1]), True, BLACK)
    menu = font.render("New Game", True, BLACK)
    win.blit(timer_text, (400, 520))
    win.blit(menu, (20, 520))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill(WHITE)
    draw(win, font)
    pygame.display.update()
    clock.tick(20)
