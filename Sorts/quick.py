import pygame

clk = pygame.time.Clock()

def quick(draw, grid):
    global t
    temp = [i.value for i in grid]
    t = grid
    run = True
    slow = True


    qsort(draw, grid, t, slow)
        
    return True, True

def qsort(draw, grid, temp, slow):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                slow = not slow
    length = len(temp)
    if length <= 1:
        return temp
    else:
        
        pivot = temp.pop()
        
        greater, lesser = [], []
        for element in temp:
            if element.value > pivot.value:
                greater.append(element)
            else:
                lesser.append(element)
        a = qsort(draw, grid, lesser, slow) + [pivot] + qsort(draw, grid, greater, slow)
        for nodes in a:
            nodes.make_red()
            n = nodes.move(nodes.value)
            for node in grid:
                if node.no == n:
                    node.move(n)

            if slow:
                draw()
        if not slow:
            draw()
        return a
            