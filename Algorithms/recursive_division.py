import pygame
from random import randint, choice

row = 24
col = 49

def rd(draw, grid, r, c, sr, sc, m, mode):
    if m == 'row' and sr > 1:
        r1 = r - randint(1, r-1)
    elif m == 'col':
        pass

def division(draw, grid, mode):
    run = True
    l = len(grid)
    t = ['row', 'col']
    while run:
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
        rd(draw, grid, row+1, col+1, row+1, col+1, choice(t), mode)
    if mode == 1:
        draw()
        
    return True