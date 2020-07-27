import pygame
from Algorithms.nodes.lines import Line
from Sorts.selection import selection
from random import shuffle, randint, choice

MODE = 0

WIDTH = 1584
COLUMNS = 198

HEIGHT = 784
ROWS = 49

BLACK = (0,0,0)

WIN = pygame.display.set_mode((1584, 784))
pygame.display.set_caption("Visualiser: Edit")

def make_lines():
    grid = []
    for i in range(1, 199):
        node = Line(i, i-1, MODE)
        grid.append(node)
    return grid

def draw_grid(win):
    gap = WIDTH / COLUMNS
    for i in range(COLUMNS+1):
        pygame.draw.line(win, BLACK, (i*gap, 0), (i*gap, HEIGHT))

def draw(win, grid):
    win.fill(BLACK)
    for row in grid:
        row.draw(WIN)
    draw_grid(win)
    pygame.display.update()

def sortloop(mode):
    global MODE
    MODE = mode

    grid = make_lines()
    pygame.init()
    run = True
    started = False
    already = True

    while run:
        if not started:
            draw(WIN, grid)
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and not started:
                    started = True
                    pygame.display.set_caption("Visualiser: Selection Sort")
                    run = selection(lambda : draw(WIN, grid), grid, MODE)
                    started = False

                if event.key == pygame.K_SPACE:
                    l = [i for i in range(1,199)]
                    shuffle(l)
                    for node in grid:
                        g = choice(l)
                        node.evalu(g)
                        l.remove(g)
sortloop(0)