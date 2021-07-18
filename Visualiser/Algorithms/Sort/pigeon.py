import pygame

clk = pygame.time.Clock()

def pigeon(draw, grid):
    temp = [i.value for i in grid]
    slow = False

    min_val = min(temp)  
    max_val = max(temp) 

    size = max_val - min_val + 1  
    holes = [0] * size

    for x in temp:
        holes[x - min_val] += 1
    i = 0
    for count in range(size):
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
        while holes[count] > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False, False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True, False
                    if event.key == pygame.K_BACKSPACE:
                        slow = not slow
            holes[count] -= 1
            temp[i] = count + min_val
            grid[i].value = temp[i]
            grid[i].make_red()
            if slow:
                draw()
            i += 1
        if not slow:
            draw()
        
        
    return True, True