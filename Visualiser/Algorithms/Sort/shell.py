import pygame

clk = pygame.time.Clock()

def shell(draw, grid):
    temp = [i.value for i in grid]
    run = True
    slow = True

    length = len(grid)

    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:

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

        for i in range(gap, length):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False, False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True, False
                    if event.key == pygame.K_BACKSPACE:
                        slow = not slow

            j = i
            while j >= gap and temp[j] < temp[j - gap]:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False, False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return True, False
                        if event.key == pygame.K_BACKSPACE:
                            slow = not slow

                temp[j], temp[j - gap] = temp[j - gap], temp[j]
                grid[j].value, grid[j - gap].value = temp[j], temp[j - gap]
                grid[j].make_red()
                grid[j - gap].make_red()
                if slow:
                    draw()
                j -= gap
        if not slow:
            draw()
        
        
        
    return True, True