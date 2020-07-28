import pygame

clk = pygame.time.Clock()

def double(draw, grid):
    temp = [i.value for i in grid]
    run = True
    slow = True

    length = len(temp)
    i = 0
    for i in range(0, int(((length - 1) / 2) + 1)):
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
        
        for j in range(0, length - 1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False, False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True, False
                    if event.key == pygame.K_BACKSPACE:
                        slow = not slow
            if (temp[j + 1] < temp[j]):
                temp[j + 1], temp[j] = temp[j], temp[j + 1]
                grid[j].value = temp [j]
                grid[j].make_red()
                grid[j + 1].value = temp[j + 1]
                grid[j + 1].make_red()
                if slow:
                    draw()

            if (temp[length - 1 - j] < temp[length - 2 - j]):
                temp[length - 1 - j], temp[length - 2 - j] = temp[length - 2 - j], temp[length - 1 - j]
                grid[length - 1 - j].value = temp[length - 1 - j]
                grid[length - 1 - j].make_red()
                grid[length - 2 - j].value = temp[length - 2 - j]
                grid[length - 2 - j].make_red()
                if slow:
                    draw()
        if not slow:
            draw()
    return True, True