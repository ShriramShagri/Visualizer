import pygame

clk = pygame.time.Clock()

def selection(draw, grid):
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
        l = i
        for k in range(i + 1, length):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False, False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True, False
                    if event.key == pygame.K_BACKSPACE:
                        slow = not slow
            if grid[k].value < grid[l].value:
                l = k
            if slow:
                grid[k].make_red()
                grid[l].make_red()
                draw()
        if l != i:
            grid[l].value, grid[i].value = grid[i].value, grid[l].value
            grid[l].make_red()
            grid[i].make_red()
            draw()
        i += 1
        
    return True, True