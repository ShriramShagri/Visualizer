import pygame

clk = pygame.time.Clock()
l = 0

def bitonic(draw, grid):
    global l
    temp = [i.value for i in grid]
    # temp = temp[:256]
    run = True
    slow = True

    length = len(temp)
    l = length
    i = 0
    while i < 1:
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
        bitonic_sort(draw, grid,temp, 0, length, 1, slow)
        i += 1
        
    return True, True


def compAndSwap(draw, grid, temp, i, j, dire, slow):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True, False
            if event.key == pygame.K_BACKSPACE:
                slow = not slow
    if (dire == 1 and temp[i] > temp[j]) or (dire == 0 and temp[i] < temp[j]):
        temp[i], temp[j] = temp[j], temp[i]
        for node in range(l):
            if grid[node].value != temp[node]:
                grid[node].value = temp[node]
                grid[node].make_red()
        if slow:
            draw()

def bitonic_merge(draw, grid, temp, low, cnt, dire, slow):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True, False
            if event.key == pygame.K_BACKSPACE:
                slow = not slow
    if cnt > 1:
        k = int(cnt / 2)
        for i in range(low, low + k):
            compAndSwap(draw, grid, temp, i, i + k, dire, slow)
        bitonic_merge(draw, grid, temp, low, k, dire, slow)
        bitonic_merge(draw, grid, temp, low + k, k, dire, slow)
    if not slow:
        draw()

def bitonic_sort(draw, grid, temp, low, cnt, dire, slow):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True, False
            if event.key == pygame.K_BACKSPACE:
                slow = not slow
    if cnt > 1:
        k = int(cnt / 2)
        bitonic_sort(draw, grid, temp, low, k, 1, slow)
        bitonic_sort(draw, grid, temp, low + k, k, 0, slow)
        bitonic_merge(draw, grid, temp, low, cnt, dire, slow)
