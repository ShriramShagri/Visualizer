import pygame

clk = pygame.time.Clock()

def wiggle(draw, grid):
    temp = [i.value for i in grid]
    run = True
    slow = True

    length = len(grid)
    i = 0
    while i < length:
        if not slow:
            clk.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
                if event.key == pygame.K_BACKSPACE:
                    slow = not slow

        if (i % 2 == 1) == (grid[i - 1].value > grid[i].value):
            grid[i - 1].value, grid[i].value = grid[i].value, grid[i - 1].value
            grid[i - 1].make_red()
            grid[i].make_red()
            if not slow:
                draw()
        if slow:
            draw()
        i += 1
        
    return True