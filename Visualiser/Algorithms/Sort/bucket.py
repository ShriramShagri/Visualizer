import pygame

clk = pygame.time.Clock()

def bucket(draw, grid):
    temp = [i.value for i in grid]
    run = True
    slow = True
    bucket_size = 16

    while True:
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

        minval, maxval = (min(temp), max(temp))
        bucket_count = (maxval - minval) // bucket_size + 1
        buckets = [[] for _ in range(int(bucket_count))]

        for i in range(len(temp)):
            buckets[int((temp[i] - minval) // bucket_size)].append(temp[i])
        
        ind = 0
        for i in range(len(buckets)):
            if not slow:
                clk.tick(10)
            else:
                clk.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False, False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True, False
                    if event.key == pygame.K_BACKSPACE:
                        slow = not slow
            a = [buckets[i][j] for j in range(len(buckets[i]))]
            for node in a:
                grid[ind].value = node
                grid[ind].make_red()
                ind += 1
                if slow:
                    draw()
            if not slow:
                draw()

        ind = 0
        for i in range(len(buckets)):
            if not slow:
                clk.tick(10)
            else:
                clk.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False, False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True, False
                    if event.key == pygame.K_BACKSPACE:
                        slow = not slow
            a = sorted(buckets[i][j] for j in range(len(buckets[i])))
            for node in a:
                grid[ind].value = node
                grid[ind].make_red()
                ind += 1
                if slow:
                    draw()
            if not slow:
                draw()
        break
        
    return True, True