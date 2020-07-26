import pygame
from random import randint, choice, shuffle

row = 24
col = 49
GREEN = (0,255,0)
# clk = pygame.time.Clock()

def findparent(v, parent):
    if parent[v] == v:
        return v
    return findparent(parent[v], parent)

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

def drawedge(draw, edge, grid, mode):
    x1, y1, x2, y2, x, y = getcoordinate(edge)
    
    grid[x1*2][y1*2].remove_barrier()
    grid[x][y].remove_barrier()
    grid[x2*2][y2*2].remove_barrier()
    if mode == 0:
        draw()

def flash(draw, edge, grid, mode):
    x1, y1, x2, y2, x, y = getcoordinate(edge)
    
    grid[x1*2][y1*2].getwil1()
    grid[x][y].getwil1()
    grid[x2*2][y2*2].getwil1()
    if mode == 0:
        draw()

def kruskal(draw, grid, mode):
    pygame.init()
    r = len(grid)
    c = len(grid[0])
    for rw in grid:
        for node in rw:
            node.reset()
            node.invert()
    if mode == 0:
        draw()

    edgelist = []
    for i in range(row + 1):
        for j in range(col + 1):
            if i == row and j == col:
                continue
            elif j == col:
                edgelist.append(((i, j), (i+1, j)))
            elif i == row:
                edgelist.append(((i, j), (i, j+1)))
            else:
                edgelist.append(((i, j), (i+1, j)))
                edgelist.append(((i, j), (i, j+1)))
    shuffle(edgelist)

    parent = [i for i in range((c//2 + 1)*(r//2 + 1))]

    count = 0
    while count != (c//2 + 1)*(r//2 + 1) - 1:
        # clk.tick(45)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if mode == 0:
                        mode = 1
                    else:
                        mode = 0
        try:
            current = edgelist.pop()
        except:
            break
        x1, y1 = current[0]
        x2, y2 = current[1]

        sourceparent = findparent(y1*(r//2 + 1) - ((c//2 + 1) - x1), parent)
        destparent = findparent(y2*(r//2 + 1) - ((c//2 + 1) - x2), parent)
        temp = grid
        grid = temp

        if sourceparent != destparent:
            flash(draw, current, grid, mode)
            drawedge(draw, current, grid, mode)
            count += 1
            parent[sourceparent] = destparent
        
    if mode == 1:
        draw()
    return True