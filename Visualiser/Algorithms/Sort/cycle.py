import pygame

clk = pygame.time.Clock()

def cycle(draw, grid):
    temp = [i.value for i in grid]
    run = True
    slow = True

    length = len(temp)

    for cycle_start in range(0, length - 1):
        if not slow:
            clk.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True, False
                if event.key == pygame.K_BACKSPACE:
                    slow = not slow
        
        item = temp[cycle_start]

        pos = cycle_start
        for i in range(cycle_start + 1, length):
            if temp[i] < item:
                pos += 1

        if pos == cycle_start:
            continue

        while item == temp[pos]:
            pos += 1

        temp[pos], item = item, temp[pos]
        grid[pos].value = temp[pos]
        grid[pos].make_red()
        if slow:
            draw()

        while pos != cycle_start:
            if not slow:
                clk.tick(5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False, False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True, False
                    if event.key == pygame.K_BACKSPACE:
                        slow = not slow

            pos = cycle_start
            for i in range(cycle_start + 1, length):
                if temp[i] < item:
                    pos += 1

            while item == temp[pos]:
                pos += 1

            temp[pos], item = item, temp[pos]
            grid[pos].value = temp[pos]
            grid[pos].make_red()
            if slow:
                draw()
        
        if not slow:
            draw()
        
    return True, True