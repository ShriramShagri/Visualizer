import pygame
from random import randint, choice, shuffle

def findparent(v, parent):
    if parent[v] == v:
        return v
    return findparent(parent[v], parent)

def drawedge(draw, edge, grid):
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
    
    grid[x1*2][y1*2].remove_barrier()
    grid[x][y].remove_barrier()
    grid[x2*2][y2*2].remove_barrier()

    draw()

def kruskal(draw, grid):
    Quit = False

    for row in grid:
        for node in row:
            node.invert()
    draw()

    edgelist = []
    for i in range(24):
        for j in range(24):
            if i == 24 and j == 24:
                continue
            elif j == 24:
                edgelist.append(((i, j), (i+1, j)))
            elif i == 24:
                edgelist.append(((i, j), (i, j+1)))
            else:
                edgelist.append(((i, j), (i+1, j)))
                edgelist.append(((i, j), (i, j+1)))
    shuffle(edgelist)

    parent = [i for i in range(625)]

    i = 0
    count = 0

    while count != 624 and not Quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit = True
        
        current = edgelist[i]
        x1, y1 = current[0]
        x2, y2 = current[1]

        sourceparent = findparent(x1*25 - (25 - y1), parent)
        destparent = findparent(x2*25 - (25 - y2), parent)

        if sourceparent != destparent:
            drawedge(draw, current, grid)
            count += 1
            parent[sourceparent] = sourceparent
        
        i += 1