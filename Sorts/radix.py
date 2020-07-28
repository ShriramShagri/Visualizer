import pygame

clk = pygame.time.Clock()

def radix(draw, grid):
    temp = [i.value for i in grid]
    run = True
    slow = True

    RADIX = 10
    placement = 1
    max_digit = max(temp)
    length = len(grid)

    while placement < max_digit:
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
        
        buckets = [list() for _ in range(RADIX)]
        # split list_of_ints between the buckets
        for i in temp:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        # put each buckets' contents into temp
        a = 0
        for b in range(RADIX):
            for i in buckets[b]:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False, False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return True, False
                        if event.key == pygame.K_BACKSPACE:
                            slow = not slow
                temp[a] = i
                grid[a].value = temp[a]
                grid[a].make_red()
                if slow:
                    draw()
                a += 1
            if not slow:
                draw()
        # move to next
        placement *= RADIX
        
    return True, True