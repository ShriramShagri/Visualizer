import pygame

clk = pygame.time.Clock()

def selection(draw, grid, mode):
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
                if event.key == pygame.K_BACKSPACE:
                    if mode == 0:
                        mode = 1
                    else:
                        mode = 0
                if event.key == pygame.K_EQUALS:
                    slow = not slow
        least = i
        for k in range(i + 1, length):
            if grid[k].value < grid[least].value:
                least = k
            if slow:
                grid[k].make_red()
                grid[least].make_green()
                draw()
        if least != i:
            grid[least].value, grid[i].value = (grid[i].value, grid[least].value)
            grid[least].make_green()
            grid[i].make_green()
            if mode == 0:
                draw()
        i += 1
    
    if mode == 1:
        draw()
        
    return True