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
            clk.tick(20)
            low = d
            high = d + i - 1
            mid = (low + high + 1) // 2
            temp = merge1(temp, low, mid, high)
            for node in range(length):
                if grid[node].value != temp[node]:
                    grid[node].value = temp[node]
                    grid[node].make_green()
            draw()
        # final merge of last two parts
        if i * 2 >= len(temp):
            mid = d
            temp = merge1(temp, 0, mid, len(temp) - 1)
            for node in range(0, len(temp)):
                grid[node].value = temp[node]
        i *= 2
    draw()  
    return True, grid

def merge1(temp, low, mid, high):
    result = []
    left, right = temp[low:mid], temp[mid : high + 1]
    while left and right:
        result.append((left if left[0] <= right[0] else right).pop(0))
    temp[low : high + 1] = result + left + right
    return temp

