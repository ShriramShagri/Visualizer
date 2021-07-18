import pygame




clk = pygame.time.Clock()
BLACK = (0,0,0)

def iterativemerge(draw, grid):
    temp = [i.value for i in grid]
    run = True
    slow = True
    
    length = len(grid)
    i = 2
    while i < length:
        # if not slow:
        #     clk.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True, False
                if event.key == pygame.K_BACKSPACE:
                    slow = not slow
        
        for d in range(0, length, i):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False, False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True, False
                    if event.key == pygame.K_BACKSPACE:
                        slow = not slow
            if 100//i > 15:
                clk.tick(100//i)
            else:
                clk.tick(20)
            l = d
            h = d + i - 1
            m = (l + h + 1) // 2
            temp = merge1(draw, temp, l, m, h, grid, slow)
            for node in range(length):
                if grid[node].value != temp[node]:
                    grid[node].value = temp[node]
            #         grid[node].make_green()
            # draw()
        
        if i * 2 >= len(temp):
            m = d
            temp = merge1(draw, temp, 0, m, len(temp) - 1, grid, slow)
            for node in range(0, len(temp)):
                grid[node].value = temp[node]
        i *= 2
    draw()  
    return True, False

def merge1(draw, temp, l, m, h, grid, slow):
    result = []
    left, right = temp[l : m], temp[m : h + 1]
    while left and right:
        pygame.event.pump()
        if left[0] <= right[0]:
            t = left.pop(0)
        else:
            t = right.pop(0)
        result.append(t)
        grid[temp.index(t)].make_red()
        if slow:
            draw()
    if not slow:
        draw()

    temp[l : h + 1] = result + left + right
    return temp

