import pygame
from Algorithms.nodes.lines import Line

from Sorts.bead import bead
from Sorts.bitonic import bitonic
from Sorts.bubble import bubble
from Sorts.iterativemerge import iterativemerge
from Sorts.selection import selection
from Sorts.wiggle import wiggle


from random import shuffle, randint, choice


pygame.init()

infoObject = pygame.display.Info()

WIDTH = 1584
COLUMNS = 512

HEIGHT = 784
ROWS = 49

WHITE = (255,255,255)
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
        pygame.draw.line(win, WHITE, (i*gap, 0), (i*gap, HEIGHT))

def draw(win, grid, t):
    win.fill(WHITE)
    for row in grid:
        row.draw(WIN)
    if t:
        draw_grid(win)
    pygame.display.update()

def sortloop():
    print((infoObject.current_w, infoObject.current_h))
    
    grid = make_lines()
    pygame.init()
    run = True
    started = False
    already = False
    togglegrid = True

    l = [i for i in range(1,COLUMNS+1)]
    shuffle(l)
    for node in grid:
        g = choice(l)
        node.evalu(g)
        l.remove(g)

    while run:
        if not started:
            draw(WIN, grid, togglegrid)
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Selection Sort")
                    run = selection(lambda : draw(WIN, grid, togglegrid), grid)
                    already = True
                    started = False
                
                if event.key == pygame.K_5 and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Bead Sort")
                    run = bead(lambda : draw(WIN, grid, togglegrid), grid)
                    already = True
                    started = False
                
                if event.key == pygame.K_6 and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Bitonic Sort")
                    run = bitonic(lambda : draw(WIN, grid, togglegrid), grid)
                    already = True
                    started = False

                if event.key == pygame.K_2 and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Bubble Sort")
                    run = bubble(lambda : draw(WIN, grid, togglegrid), grid)
                    already = True
                    started = False
                
                if event.key == pygame.K_3 and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Merge Sort(Iterative)")
                    run = iterativemerge(lambda : draw(WIN, grid, togglegrid), grid)
                    already = True
                    started = False
                
                if event.key == pygame.K_4 and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Wiggle Sort")
                    run = wiggle(lambda : draw(WIN, grid, togglegrid), grid)
                    # already = True
                    started = False

                if event.key == pygame.K_SPACE:
                    l = [i for i in range(1,COLUMNS+1)]
                    shuffle(l)
                    for node in grid:
                        g = choice(l)
                        node.evalu(g)
                        l.remove(g)
                    pygame.display.set_caption("Visualiser: Shuffled")
                    already = False
                if event.key == pygame.K_i:
                    l = [i for i in range(1,COLUMNS+1)]
                    l = l[::-1]
                    for node in grid:
                        g = l.pop(0)
                        node.evalu(g)
                    pygame.display.set_caption("Visualiser: Inverted")
                    already = False
                if event.key == pygame.K_TAB:
                    togglegrid = not togglegrid
sortloop()