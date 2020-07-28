import pygame

clk = pygame.time.Clock()

def pancake(draw, grid):
    temp = [i.value for i in grid]
    run = True
    slow = True

    length = len(grid)
    l = length
    while length > 1:
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
        mi = temp.index(max(temp[0:length]))

        temp = temp[mi::-1] + temp[mi + 1 : len(temp)]
        for node in range(l):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False, False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True, False
                    if event.key == pygame.K_BACKSPACE:
                        slow = not slow
            if grid[node].value != temp[node]:
                grid[node].value = temp[node]
                grid[node].make_red()
                if slow:
                    draw()

        temp = temp[length - 1 :: -1] + temp[length : len(temp)]
        for node in range(l):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False, False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True, False
                    if event.key == pygame.K_BACKSPACE:
                        slow = not slow
            if grid[node].value != temp[node]:
                grid[node].value = temp[node]
                grid[node].make_red()
                if slow:
                    draw()
        length -= 1
        if not slow:
            draw()

        

        
    return True, True