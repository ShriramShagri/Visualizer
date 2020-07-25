import pygame
from random import randint, choice

# clk = pygame.time.Clock()
row = 24
col = 49

def noneb(stack, visited):
    # x, y = node
    neighbours = []
    for node in stack:
        count = 0
        x, y = node
        if (x+1, y) in visited and x < row:
            count += 1
        if (x-1, y) in visited and x > 0:
            count += 1
        if (x, y+1) in visited and y < row:
            count += 1
        if (x, y-1) in visited and y > 0:
            count += 1
        if count == 4:
            neighbours.append(node)
    return neighbours

def update(node, visited):
    n = []
    x, y = node
    if x < row and x > 0: # down
        n.append((x + 1, y))
        n.append((x - 1, y))
    elif x == 0:
        n.append((x + 1, y))
    elif x == row:
        n.append((x - 1, y))
    if y < col and y > 0: # down
        n.append((x, y + 1))
        n.append((x, y - 1))
    elif y == 0:
        n.append((x, y + 1))
    elif y == col:
        n.append((x, y - 1))
    for nodes in visited:
        if nodes in n:
            n.remove(nodes)
    return n

def check(n):
    if len(n) != 0:
        return True
    return False

def drawsquare(draw, grid, spot, prev, mode, color = ''):
    x1, y1 = prev
    x2, y2 = spot
    if x1 == x2:
        if y1 > y2:
            y = y1*2 - 1
        else:
            y = y1*2 + 1
        x = x1 * 2
    elif  y1 == y2:
        if x1 > x2:
            x = x1*2 - 1
        else:
            x = x1*2 + 1
        y = y1 * 2
    
    if color != '':
        grid[x][y].tracker()
        grid[x2*2][y2*2].tracker()
    else:
        grid[x][y].remove_barrier()
        grid[x2*2][y2*2].remove_barrier()
    if mode == 0:
        draw()

def tree(draw, grid, mode):
    run = True
    l = len(grid)
    for rw in grid:
        for node in rw:
            node.reset()
            node.invert()      
    if mode == 0:
        draw()
    
    stack = []
    x = randint(0, row-1)
    y = randint(0, col-1)
    stack.append((x, y)) 
    visited = {(x, y)}
    c = 0

    while run and c != 1249:
        # clk.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_BACKSPACE:
                    if mode == 0:
                        mode = 1
                    else:
                        mode = 0
        # try:
        n = update(stack[-1], visited)
        nebless = noneb(stack, visited)

        for nodes in stack:
            if nodes in nebless:
                stack.remove(nodes)
        
        if not stack:
            break

        if check(n):
            spot = choice(n)
            prev = stack[-1]
            stack.append(spot)
            visited.add(spot)
            drawsquare(draw, grid, spot, prev, mode, color='')
            c += 1

        else:
            a = choice(stack)
            stack.remove(a)
            stack.append(a)
            
    if mode == 1:
        draw()
        
    return True