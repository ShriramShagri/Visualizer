import pygame

clk = pygame.time.Clock()
t = []
def quick(draw, grid):
    global t
    temp = [i.value for i in grid]
    t = grid
    run = True
    slow = True


    a = qsort(draw, grid, slow)
    for i, nodes in enumerate(a):
        nodes.make_red()
        n = nodes.move(i+1)
        if slow:
            draw()
        
    return True, True

def qsort(draw, grid, slow):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                slow = not slow
    length = len(grid)
    if length <= 1:
        return grid
    else:
        
        pivot = grid.pop()
        
        greater, lesser = [], []
        for element in grid:
            if element.value > pivot.value:
                greater.append(element)
            else:
                lesser.append(element)
        a = qsort(draw, lesser, slow) + [pivot] + qsort(draw, greater, slow)
        for i, nodes in enumerate(a):
            nodes.make_red()
            n = nodes.move(i+1)
            if slow:
                draw()
        if not slow:
            draw()
        return a
            