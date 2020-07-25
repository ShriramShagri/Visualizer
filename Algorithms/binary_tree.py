import pygame
from random import randint

# clk = pygame.time.Clock()
row = 24
col = 49

def rand():
    return randint(0,1)

def binary(draw, grid, mode):
    run = True
    l = len(grid)
    for rw in grid:
        for node in rw:
            node.reset()
            node.invert()      
    if mode == 0:
        draw()
    current = None
    for j in grid[0]:
        j.remove_barrier()
        if mode == 0:
            draw()

    i = 1
    while run and i != row + 1:
        # clk.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_BACKSPACE:
                    if mode == 0:
                        mode = 1
                    else:
                        mode = 0
        for j in range(col+ 1):
            
            current = (i, j)
            if rand() == 1:
                drawedge(draw, grid, current, mode, 'north')
                
            else:
                if movewest(current):
                    drawedge(draw, grid, current, mode, 'west')
                else:
                    drawedge(draw, grid, current, mode, 'north')
        i += 1
    if mode == 1:
        draw()
        
    return True

def movewest(node):
    x, y = node
    if y < col:
        return True
    return False
    
def drawedge(draw, grid, current, mode, direc):
    x, y = current
    grid[x*2][y*2].remove_barrier()
    if direc == 'north':
        grid[x*2-1][y*2].remove_barrier()
    elif direc == 'west':
        grid[x*2][y*2+1].remove_barrier()
    if mode == 0:
        draw()