import pygame
from random import randint, choice

clk = pygame.time.Clock()

def ellers(draw, grid, mode):
    run = True
    for row in grid:
        for node in row:
            node.reset()
            node.invert()
    for row in range(len(grid)):
        for node in range(len(grid[row])):
            if row % 2 == 1 and node % 2 ==1:
                grid[row][node].remove_barrier()
            
    if mode == 0:
        draw()
    i = 0

    while i < len(grid)//2 - 1:
        clk.tick(30)
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_CAPSLOCK:
                    if mode == 0:
                        mode = 1
                    else:
                        mode = 0
    if mode == 1:
        draw()
        
    return True