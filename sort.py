import pygame
from Algorithms.nodes.lines import Line

from Sorts.bead import bead
from Sorts.bitonic import bitonic
from Sorts.bogo import bogo
from Sorts.bubble import bubble
from Sorts.bucket import bucket
from Sorts.cocktail import cocktail
from Sorts.comb import comb
from Sorts.counting import counting
from Sorts.cycle import cycle
from Sorts.double import double
from Sorts.gnome import gnome
from Sorts.heap import heap
from Sorts.insertion import insertion
from Sorts.iterativemerge import iterativemerge
from Sorts.selection import selection
from Sorts.wiggle import wiggle


from random import shuffle, randint, choice


pygame.init()

infoObject = pygame.display.Info()

WIDTH = 1584
COLUMNS = 256

HEIGHT = 784

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
                    pygame.display.set_caption("Visualiser: Bead Sort")
                    run, already = bead(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False
                
                if event.key == pygame.K_2 and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Bitonic Sort")
                    run, already = bitonic(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False
                
                if event.key == pygame.K_3 and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Bogo Sort")
                    run, already = bogo(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False

                if event.key == pygame.K_4 and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Bubble Sort")
                    run, already = bubble(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False
                
                if event.key == pygame.K_5 and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Bucket Sort")
                    run, already = bucket(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False

                if event.key == pygame.K_6 and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Cocktail Shaker Sort")
                    run, already = cocktail(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False
                
                if event.key == pygame.K_7 and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Comb Sort")
                    run, already = comb(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False
                
                if event.key == pygame.K_8 and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Counting Sort")
                    run, already = counting(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False
                
                if event.key == pygame.K_9 and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Cycle Sort")
                    run, already = cycle(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False
                
                if event.key == pygame.K_0 and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Double Sort")
                    run, already = double(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False

                if event.key == pygame.K_q and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Gnome Sort")
                    run, already = gnome(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False
                
                if event.key == pygame.K_w and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Heap Sort")
                    run, already = heap(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False
                
                if event.key == pygame.K_e and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Insertion Sort")
                    run, already = insertion(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False
                
                if event.key == pygame.K_g and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Merge Sort(Iterative)")
                    run, already = iterativemerge(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False
                
                if event.key == pygame.K_h and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Selection Sort")
                    run, already = selection(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False
                
                if event.key == pygame.K_j and not started:
                    started = True
                    pygame.display.set_caption("Visualiser: Wiggle Sort")
                    run = wiggle(lambda : draw(WIN, grid, togglegrid), grid)
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
                        node.evalu(g + 1)
                    pygame.display.set_caption("Visualiser: Inverted")
                    already = False
                if event.key == pygame.K_TAB:
                    togglegrid = not togglegrid
sortloop()