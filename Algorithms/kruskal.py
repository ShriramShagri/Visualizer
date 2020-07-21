import pygame
from random import randint, choice, shuffle

def findparent(v, parent):
    if parent[v] == v:
        return v
    return findparent(parent[v], parent)

def drawedge(draw, edge, grid, mode):
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
    if mode == 0:
        draw()

def kruskal(draw, grid, mode):
    Quit = False

    for row in grid:
        for node in row:
            node.reset()
            node.invert()
    if mode == 0:
        draw()

    edgelist = []
    for i in range(25):
        for j in range(25):
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
            drawedge(draw, current, grid, mode)
            count += 1
            parent[sourceparent] = destparent
        
        i += 1
    if mode == 1:
        draw()