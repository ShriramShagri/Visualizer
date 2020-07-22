import pygame
from random import randint, choice

store = ()

def update(node, visited):
    n = []
    x, y = node
    if x < 24 and x > 0: # down
        n.append((x + 1, y))
        n.append((x - 1, y))
    elif x == 0:
        n.append((x + 1, y))
    elif x == 24:
        n.append((x - 1, y))
    if y < 24 and y > 0: # down
        n.append((x, y + 1))
        n.append((x, y - 1))
    elif y == 0:
        n.append((x, y + 1))
    elif y == 24:
        n.append((x, y - 1))
    for nodes in visited:
        if nodes in n:
            n.remove(nodes)
    return n

def check(n):
    if len(n) != 0:
        return True
    return False

def drawsquare(draw, grid, spot, prev, mode):
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
    
    grid[x][y].remove_barrier()
    grid[x2*2][y2*2].remove_barrier()
    if mode == 0:
        draw()

def drawnode(draw, grid, node, mode):
    global store
    a, b = node
    if store != node:
        c, d = store
        grid[c*2][d*2].remove_barrier()
        store = node
    if mode == 0:
        grid[a*2][b*2].leader()
        draw()

def prims(draw, grid, mode):
    global store
    pygame.init()
    for row in grid:
        for node in row:
            node.reset()
            node.invert()
    if mode == 0:
        draw()
        
    stack = []
    Quit = False
    x = randint(0, 24)
    y = randint(0, 24)
    stack.append((x, y)) 
    visited = {(x, y)}
    grid[x*2][y*2].remove_barrier()
    store = stack[-1]
    if mode == 0:
        draw()

    while len(visited) < 25*25 and not Quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        n = update(stack[-1], visited)
        drawnode(draw, grid, stack[-1], mode)

        if check(n):
            spot = choice(n)
            prev = stack[-1]
            stack.append(spot)
            visited.add(spot)
            drawsquare(draw, grid, spot, prev, mode)

        else:
            stack.pop()
    c, d = store
    grid[c*2][d*2].remove_barrier() 

    if mode == 1:
        draw()
    return True