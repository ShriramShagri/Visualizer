import pygame

clk = pygame.time.Clock()

def comb(draw, grid):
    temp = [i.value for i in grid]
    run = True
    slow = True

    n = len(temp) 
    gap = n 
    swp = True
  
    while gap !=1 or swp == 1: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True, False
                if event.key == pygame.K_BACKSPACE:
                    slow = not slow

        gap = getNextGap(gap) 
        swp = False
  
        for i in range(0, n-gap): 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False, False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True, False
                    if event.key == pygame.K_BACKSPACE:
                        slow = not slow
            if temp[i] > temp[i + gap]: 
                temp[i], temp[i + gap]=temp[i + gap], temp[i] 
                grid[i].value = temp[i]
                grid[i + gap].value = temp[i + gap]
                grid[i].make_red()
                grid[i + gap].make_red()
                if slow:
                    draw()
                swp = True
        if not slow:
            draw()

        
    return True, True

def getNextGap(gap): 
  
    gap = (gap * 10)/13
    if gap < 1: 
        return 1
    return int(gap)