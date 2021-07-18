import pygame

clk = pygame.time.Clock()

def insertion(draw, grid):
    temp = [i.value for i in grid]
    run = True
    slow = True

    length = len(grid)

    for i in range(1, length):
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
        
        i_index = i
        while (i_index > 0 and temp[i_index - 1] > temp[i_index]):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False, False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True, False
                    if event.key == pygame.K_BACKSPACE:
                        slow = not slow
            temp[i_index], temp[i_index - 1] = temp[i_index - 1], temp[i_index],
            grid[i_index].value = temp[i_index]
            grid[i_index].make_red()
            grid[i_index - 1].value = temp[i_index - 1]
            grid[i_index - 1].make_red()
            if slow:
                draw()
            i_index -= 1
        if not slow:
            draw()
        
    return True, True