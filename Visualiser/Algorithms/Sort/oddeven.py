import pygame

clk = pygame.time.Clock()

def oddeven(draw, grid):
    temp = [i.value for i in grid]
    run = True
    slow = True

    length = len(grid)
    isSorted = 0
    while isSorted == 0:
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
        
        isSorted = 1
        for i in range(1, length-1, 2): 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False, False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True, False
                    if event.key == pygame.K_BACKSPACE:
                        slow = not slow
            if temp[i] > temp[i+1]: 
                temp[i], temp[i+1] = temp[i+1], temp[i] 
                grid[i].value = temp[i]
                grid[i].make_red()
                grid[i+1].value = temp[i+1]
                grid[i+1].make_red()
                if slow:
                    draw()
                isSorted = 0
                  
        for i in range(0, length-1, 2): 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False, False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True, False
                    if event.key == pygame.K_BACKSPACE:
                        slow = not slow
            if temp[i] > temp[i+1]: 
                temp[i], temp[i+1] = temp[i+1], temp[i] 
                grid[i].value = temp[i]
                grid[i].make_red()
                grid[i+1].value = temp[i+1]
                grid[i+1].make_red()
                if slow:
                    draw()
                isSorted = 0
        if not slow:
            draw()
        
    return True, True