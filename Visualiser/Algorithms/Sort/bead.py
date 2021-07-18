import pygame

clk = pygame.time.Clock()

def bead(draw, grid):
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
                return False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True, False
                if event.key == pygame.K_BACKSPACE:
                    slow = not slow
        
        for a, (upper, lower) in enumerate(zip(temp, temp[1:])):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False, False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True, False
                    if event.key == pygame.K_BACKSPACE:
                        slow = not slow
            if upper > lower:
                temp[a] -= upper - lower
                temp[a + 1] += upper - lower
                for node in range(length):
                    if grid[node].value != temp[node]:
                        grid[node].value = temp[node]
                        grid[node].make_red()
                if slow:
                    draw()
        if not slow:
            draw()
        i += 1
        
    return True, True