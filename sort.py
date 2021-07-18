import pygame
import os

from Visualiser import *
from random import shuffle, randint, choice

pygame.init()

# infoObject = pygame.display.Info()

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
    # print((infoObject.current_w, infoObject.current_h))
    
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
                
                if event.key == pygame.K_r and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Merge Sort")
                    run, already = iterativemerge(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False
                
                if event.key == pygame.K_u and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Odd Even Sort")
                    run, already = oddeven(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False

                if event.key == pygame.K_y and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Pancake Sort")
                    run, already = pancake(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False

                if event.key == pygame.K_u and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Pigeonhole Sort")
                    run, already = pigeon(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False
                
                if event.key == pygame.K_i and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Quick Sort")
                    run, already = quick(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False

                if event.key == pygame.K_o and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Radix Sort")
                    run, already = radix(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False
                
                if event.key == pygame.K_a and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Shell Sort")
                    run, already = shell(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False
                
                if event.key == pygame.K_p and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Selection Sort")
                    run, already = selection(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False
                
                if event.key == pygame.K_s and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Sleep Sort")
                    run, already = sleepsort(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False
                
                if event.key == pygame.K_d and not started and not already:
                    started = True
                    pygame.display.set_caption("Visualiser: Stooge Sort")
                    run, already = stooge(lambda : draw(WIN, grid, togglegrid), grid)
                    started = False

                if event.key == pygame.K_f and not started:
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

                if event.key == pygame.K_RSHIFT:
                    l = [i for i in range(1,COLUMNS+1)]
                    l = l[::-1]
                    for node in grid:
                        g = l.pop(0)
                        node.evalu(g + 1)
                    pygame.display.set_caption("Visualiser: Inverted")
                    already = False

                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Visualiser: Main Page")
                    return False

                if event.key == pygame.K_TAB:
                    togglegrid = not togglegrid
                
                if event.key == pygame.K_h:
                    helppage()

def invert(color):
    a, b, c = color
    return (abs(255 - a), abs(255 - b), abs(255 - c))


def helppage(k=False):
    pygame.init()
    Quit = False
    inv = False

    background1 = pygame.image.load(os.path.join(FILEPATH, 'Fonts', 'Help1.png'))

    nextpage = button((0, 0, 0), 1440, 350, 75, 100, FILEPATH, (0, 0, 0), text='>')
    while not Quit:
        if k:
            return
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if nextpage.isOver(pos):
                        k = helppage2()
                        continue

            if event.type == pygame.MOUSEMOTION:
                if nextpage.isOver(pos):
                    inv = True
                else:
                    inv = False
        WIN.blit(background1, (0, 0))
        fillhelp(inv, nextpage)
    
def helppage2():
    pygame.init()
    Quit = False
    inv = False
    inv1 = False

    background2 = pygame.image.load(os.path.join(FILEPATH, 'Fonts', 'Help2.png'))
   
    prevpage = button((0, 0, 0), 1440, 350, 75, 100, FILEPATH, (0, 0, 0), text='<')
    while not Quit:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if prevpage.isOver(pos):
                        return True
                        
            if event.type == pygame.MOUSEMOTION:
                if prevpage.isOver(pos):
                    inv1 = True
                else:
                    inv1 = False
        WIN.blit(background2, (0, 0))
        fillhelp(inv1, prevpage)
    
def fillhelp(inv2, btn2):
    color = WHITE

    if inv2:
        btn2.textcolor = invert(color)
        btn2.color = color
    else:
        btn2.textcolor = color
        btn2.color = invert(color)
    btn2.draw(WIN, btn2.textcolor)  


    pygame.display.update()

if __name__ == "__main__":
    sortloop()