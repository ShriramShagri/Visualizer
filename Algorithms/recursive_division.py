import pygame
from random import randint, choice, randrange

row = 50
col = 100
mode = 0

def division(draw, grid, m):
    global mode
    run = True
    for rw in grid:
        for node in rw:
            node.reset()


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
        recurs(draw, grid, row-1, -1, -1, col-1)
        run = False
    if mode == 1:
        draw()
    mode = 0
        
    return True

def recurs(draw, grid, top, bottom, left, right):
    global mode
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_BACKSPACE:
                if mode == 0:
                    mode = 1
                else:
                    mode = 0
    start_range = bottom + 2
    end_range = top - 1
    y = randrange(start_range, end_range, 2)

    for column in range(left + 1, right):
        grid[y][column].barrier()
        if mode == 0:
            draw()

    start_range = left + 2
    end_range = right - 1
    x = randrange(start_range, end_range, 2)

    for row in range(bottom + 1, top):
        grid[row][x].barrier()
        if mode == 0:
            draw()
        
    wall = randrange(4)
    if wall != 0:
        gap = randrange(left + 1, x, 2)
        grid[y][gap].remove_barrier()

    if wall != 1:
        gap = randrange(x + 1, right, 2)
        grid[y][gap].remove_barrier()

    if wall != 2:
        gap = randrange(bottom + 1, y, 2)
        grid[gap][x].remove_barrier()

    if wall != 3:
        gap = randrange(y + 1, top, 2)
        grid[gap][x].remove_barrier()
    if mode == 0:
        draw()
    
    if top > y + 3 and x > left + 3:
        recurs(draw, grid, top, y, left, x)

    if top > y + 3 and x + 3 < right:
        recurs(draw, grid, top, y, x, right)

    if bottom + 3 < y and x + 3 < right:
        recurs(draw, grid, y, bottom, x, right)

    if bottom + 3 < y and x > left + 3:
        recurs(draw, grid, y, bottom, left, x)
    