import pygame
from random import shuffle, randint, choice

def rand():
    return randint(0,1)

def movenorth(draw, grid, node, mode):
    x, y = node

    grid[x*2-1][y*2].remove_barrier()
    if mode == 0:
        draw()

def connectset(draw, grid, run, mode):
    for node in run:
        x, y = node
        grid[x*2][y*2].remove_barrier()
        if node != run[-1]:
            if y != len(grid[x]) - 1:
                grid[x*2][y*2+1].remove_barrier()
        if mode == 0:
            draw()

def sidewinder(draw, grid, mode):
    pygame.init()
    run = []

    for row in grid:
        for node in row:
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

    while i != len(grid)//2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
        
        for j in range(len(grid[i])//2):
            
            current = (i, j)
            run.append(current)
            if rand() == 1:
                node = choice(run)
                movenorth(draw, grid, node, mode)
                connectset(draw, grid, run, mode)
                run = []
            else:
                continue
        if len(run) != 0:
            node = choice(run)
            movenorth(draw, grid, node, mode)
            connectset(draw, grid, run, mode)
            run = []
        i += 1
    if mode == 1:
        draw()
    return True
