import pygame

clk = pygame.time.Clock()

def bubble(draw, grid):
    run = True
    slow = True

    length = len(grid)
    i = 0
    while i < length-1:
        if not slow:
            clk.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True, False
                if event.key == pygame.K_BACKSPACE:
                    slow = not slow
        swapped = False
        for j in range(length-1 - i):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False, False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True, False
                    if event.key == pygame.K_BACKSPACE:
                        slow = not slow
            if grid[j].value > grid[j+1].value:
                swapped = True
                grid[j].value, grid[j+1].value = grid[j+1].value, grid[j].value
                grid[j].make_red()
                grid[j+1].make_red()
                if slow:
                    draw()
        if not swapped:
            break
        if not slow:
            draw()
        i += 1   
    return True, True