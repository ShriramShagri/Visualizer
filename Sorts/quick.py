import pygame

clk = pygame.time.Clock()
t = []
def quick(draw, grid):
    global t
    temp = [i.value for i in grid]
    t = temp
    run = True
    slow = True

    qsort(draw, grid, slow)
        
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
        # Use the last element as the first pivot
        pivot = grid.pop()
        # Put elements greater than pivot in greater list
        # Put elements lesser than pivot in lesser list
        greater, lesser = [], []
        for element in grid:
            if element.value > pivot.value:
                greater.append(element)
            else:
                lesser.append(element)
        a = qsort(draw, lesser, slow) + [pivot] + qsort(draw, greater, slow)
        for nodes in a:
            nodes.make_red()
            if slow:
                draw()
        if not slow:
            draw()
        return a
            