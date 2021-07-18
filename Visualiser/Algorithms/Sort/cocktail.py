import pygame

clk = pygame.time.Clock()

def cocktail(draw, grid):
    temp = [i.value for i in grid]
    run = True
    slow = True

    length = len(grid)
    
    for i in range(len(temp) - 1, 0, -1):
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

        for j in range(i, 0, -1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False, False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True, False
                    if event.key == pygame.K_BACKSPACE:
                        slow = not slow
            if temp[j] < temp[j - 1]:
                temp[j], temp[j - 1] = temp[j - 1], temp[j]
                swapped = True
                grid[j].value = temp[j]
                grid[j - 1].value = temp[j - 1]
                grid[j].make_red()
                grid[j - 1].make_red()
                if slow:
                    draw()
        if not slow:
            draw()


        for j in range(i):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False, False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True, False
                    if event.key == pygame.K_BACKSPACE:
                        slow = not slow
            if temp[j] > temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]
                swapped = True
                grid[j].value = temp[j]
                grid[j + 1].value = temp[j + 1]
                grid[j].make_red()
                grid[j + 1].make_red()
                if slow:
                    draw()
        if not slow:
            draw()

        if not swapped:
            break
        
    return True, True