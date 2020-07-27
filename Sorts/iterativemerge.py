import pygame




clk = pygame.time.Clock()
BLACK = (0,0,0)

def iterativemerge(draw, grid):
    temp = [i.value for i in grid]
    run = True
    slow = False
    
    length = len(grid)
    i = 2
    while i < length:
        # if not slow:
        #     clk.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
                if event.key == pygame.K_EQUALS:
                    slow = not slow
        
        for d in range(0, length, i):
            if 100//i > 7:
                clk.tick(100//i)
            else:
                clk.tick(10)
            l = d
            h = d + i - 1
            m = (l + h + 1) // 2
            temp = merge1(temp, l, m, h)
            for node in range(length):
                if grid[node].value != temp[node]:
                    grid[node].value = temp[node]
                    grid[node].make_green()
            draw()
        
        if i * 2 >= len(temp):
            m = d
            temp = merge1(temp, 0, m, len(temp) - 1)
            for node in range(0, len(temp)):
                grid[node].value = temp[node]
        i *= 2
    draw()  
    return True, grid

def merge1(temp, l, m, h):
    result = []
    left, right = temp[l : m], temp[m : h + 1]
    while left and right:
        if left[0] <= right[0]:
            t = left
        else:
            t = right
        result.append(t.pop(0))

    temp[l : h + 1] = result + left + right
    return temp

