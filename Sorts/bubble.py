import pygame

clk = pygame.time.Clock()

def bubble(draw, grid):
    run = True
    slow = False

    length = len(grid)
    i = 0
    while i < length-1:
        if not slow:
            clk.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
                if event.key == pygame.K_EQUALS:
                    slow = not slow
        swapped = False
        for j in range(length-1 - i):
            if grid[j].value > grid[j+1].value:
                swapped = True
                grid[j].value, grid[j+1].value = grid[j+1].value, grid[j].value
                grid[j].make_green()
                grid[j+1].make_green()
                if slow:
                    draw()
        if not swapped:
            break
        draw()
        i += 1   
    return True