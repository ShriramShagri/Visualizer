import pygame

clk = pygame.time.Clock()

def stooge(draw, grid):
    temp = [i.value for i in grid]
    run = True
    slow = True

    length = len(temp)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True, False
            if event.key == pygame.K_BACKSPACE:
                slow = not slow
        
    stoogecal(draw, grid, temp, 0, length-1, slow)
    if not slow:
        draw()
        
    return True, True

def stoogecal(draw, grid, temp, i, h, slow):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True, False
            if event.key == pygame.K_BACKSPACE:
                slow = not slow
    if i >= h:
        return

    if temp[i] > temp[h]:
        temp[i], temp[h] = temp[h], temp[i]
        grid[h].value, grid[i].value = temp[h], temp[i]
        grid[h].make_red()
        grid[i].make_red()
        if slow:
            draw()

    
    if h - i + 1 > 2:
        t = (int)((h - i + 1) / 3)

        
        stoogecal(draw, grid, temp, i, (h - t), slow)

        
        stoogecal(draw, grid, temp, i + t, (h), slow)

        
        stoogecal(draw, grid, temp, i, (h - t), slow)