import pygame
from random import randint, choice

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

def drawsquare(draw, grid, spot, prev):
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

    draw()

def prims(draw, grid):
    for row in grid:
        for node in row:
            node.invert()
    draw()
    stack = []
    Quit = False
    x = randint(0, 24)
    y = randint(0, 24)
    stack.append((x, y)) 
    visited = {(x, y)}
    grid[x*2][y*2].remove_barrier()
    draw()

    while len(visited) < 25*25 and not Quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit = True
        n = update(stack[-1], visited)

        if check(n):
            spot = choice(n)
            prev = stack[-1]
            stack.append(spot)
            visited.add(spot)
            drawsquare(draw, grid, spot, prev)

        else:
            stack.pop()
