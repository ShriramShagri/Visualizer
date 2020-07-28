import pygame

clk = pygame.time.Clock()
l = 0
temp1 = []
def recursivemerge(draw, grid):
    global l, temp1
    temp = [i.value for i in grid]
    temp1 = temp
    run = True
    slow = True
    l = len(grid)

    mergemain(grid, draw, temp, slow)
        
    return True, True

def mergemain(grid, draw, temp, slow):

    def merge(grid, draw, temp, left, right, slow):
        result = []
        i = 0
        while grid[i].value == temp[0]:
            i+=len(temp)
        while left and right:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        slow = not slow

            if left[0] <= right[0]:
                t = left.pop(0)
            else:
                t = right.pop(0)
            result.append(t)
            grid[i+temp.index(t)].value = t
            grid[temp1.index(t)].make_red()
            if slow:
                draw()
        if not slow:
            draw()
        return result + left + right

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                slow = not slow
                
    if len(temp) <= 1:
        return temp
    mid = len(temp) // 2
    return merge(grid, draw, temp, mergemain(grid, draw, temp[:mid], slow), mergemain(grid, draw, temp[mid:], slow), slow)