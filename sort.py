import pygame
from Algorithms.nodes.lines import Line
from Sorts.selection import selection
from Sorts.bubble import bubble
from Sorts.iterativemerge import iterativemerge


from random import shuffle, randint, choice


pygame.init()

infoObject = pygame.display.Info()

WIDTH = 1584
COLUMNS = 396

HEIGHT = 784
ROWS = 49

BLACK = (0,0,0)

WIN = pygame.display.set_mode((1584, 784))
pygame.display.set_caption("Visualiser: Edit")

def make_lines():
    grid = []
    for i in range(1, COLUMNS+1):
        node = Line(i, i-1)
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

def sortloop():
    print((infoObject.current_w, infoObject.current_h))
    
    grid = make_lines()
    pygame.init()
    run = True
    started = False
    already = False

    l = [i for i in range(1,COLUMNS+1)]
    shuffle(l)
    for node in grid:
        g = choice(l)
        node.evalu(g)
        l.remove(g)

    while run:
        if not started:
            draw(WIN, grid)
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Selection Sort")
                    run = selection(lambda : draw(WIN, grid), grid)
                    already = True
                    started = False

                if event.key == pygame.K_2 and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Selection Sort")
                    run = bubble(lambda : draw(WIN, grid), grid)
                    already = True
                    started = False
                
                if event.key == pygame.K_3 and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Selection Sort")
                    run = iterativemerge(lambda : draw(WIN, grid), grid)
                    already = True
                    started = False

                if event.key == pygame.K_SPACE:
                    l = [i for i in range(1,COLUMNS+1)]
                    shuffle(l)
                    for node in grid:
                        g = choice(l)
                        node.evalu(g)
                        l.remove(g)
                    already = False
        pygame.display.set_caption("Visualiser:")
sortloop()