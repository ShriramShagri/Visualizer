import pygame
from random import choice, shuffle, randint

row = 24
col = 49

def getneighbour(node, visited):
    x, y = node
    neighbours = []
    popy = []
    if x < row:
        if (x+1, y) in visited:
            popy.append((x+1, y))
        else:
            neighbours.append((x+1, y))
    if x > 0:
        if (x-1, y) in visited:
            popy.append((x-1, y))
        else:
            neighbours.append((x-1, y))
    if y < col:
        if (x, y+1) in visited:
            popy.append((x, y+1))
        else:
            neighbours.append((x, y+1))
    if y > 0:
        if (x, y-1) in visited:
            popy.append((x, y-1))
        else:
            neighbours.append((x, y-1))

    return neighbours, popy

def drawedge(draw, edge, grid, mode):
    x1, y1, x2, y2, x, y = getcoordinate(edge)
    
    grid[x1*2][y1*2].remove_barrier()
    grid[x][y].remove_barrier()
    grid[x2*2][y2*2].remove_barrier()
    if mode == 0:
        draw()

def getcoordinate(edge):
    a, b = edge
    x1, y1 = a
    x2, y2 = b
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
    return(x1, y1, x2, y2, x, y)
    

def prims(draw, grid, mode):
    r = len(grid)
    c = len(grid[0])
    for row in grid:
        for node in row:
            node.reset()
            node.invert()
    if mode == 0:
        draw()

    x = randint(0, r//2-1)
    y = randint(0, c//2-1)
    start = (x, y)
    visited = {start}
    tovisit, p = getneighbour(start, visited)
    tovisit = set(tovisit)
    count = 1

    while count < (c//2 + 1)*(r//2 + 1) :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if mode == 0:
                        mode = 1
                    else:
                        mode = 0
        
        p = []
        n = []
        nextnode = choice(list(tovisit))
        n , p = getneighbour(nextnode, visited)
        tovisit.remove(nextnode)
        visited.add(nextnode)
        count += 1
        
        for nodes in n:
            if nodes != None:
                tovisit.add(nodes)
        
        drawedge(draw, (choice(p), nextnode), grid, mode)
            
        
    if mode == 1:
        draw()

    return True