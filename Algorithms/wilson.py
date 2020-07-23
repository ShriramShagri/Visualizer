import pygame
from random import randint, shuffle, choice

d = ['n', 's', 'e', 'w']
clk = pygame.time.Clock()

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

def getedge(draw, frm, to, direc, grid, mode):
    if direc == 'n':
        edge = (to, frm)
    elif direc == 's':
        edge = (frm, to)
    elif direc == 'e':
        edge = (frm, to)
    elif direc == 'w':
        edge = (to, frm)
    drawedge(draw, edge, grid, mode)

def north(node):
    x, y = node
    if y > 0:
        return (x, y-1)
    return None

def east(node):
    x, y = node
    if x < 24:
        return (x+1, y)
    return None

def south(node):
    x, y = node
    if y < 24:
        return (x, y+1)
    return None

def west(node):
    x, y = node
    if x > 0:
        return (x-1, y)
    return None

def wilson(draw, grid, mode):
    run = True
    l = len(grid)
    directions = {'n': north, 'e': east, 's' : south, 'w': west}
    for row in grid:
        for node in row:
            node.reset()
            node.invert()      
    if mode == 0:
        draw()
    nodelist = [(i,j) for j in range(l//2) for i in range(l//2)]
    shuffle(nodelist)
    path = False
    span = []
    cache = {
        "node" : [],
        "dir" : []
    }
    x = randint(0, l//2-1)
    y = randint(0, l//2-1)
    span.append((x, y))
    nodelist.remove((x, y))

    grid[x*2][y*2].remove_barrier()
    if mode == 0:
        draw()

    start = choice(nodelist)
    prev = start

    while run:
        clk.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        if path:
            direc = cache['dir'][cache['node'].index(start)]
            nextnode = directions[direc](start)
            edge = getedge(draw, start, nextnode, direc, grid, mode)
            span.append(start)
            nodelist.remove(start)
            if nextnode in span:
                path = False
                try:
                    start = choice(nodelist)
                    prev = start
                    cache['dir'] = []
                    cache['node'] = []
                except:
                    run = False
                    continue
            else:
                start = nextnode
        else:
            while True:
                direc = choice(d)
                nextnode = directions[direc](prev)
                if nextnode:
                    break 
            
            if nextnode in span:
                path = True

            if prev in cache['node']:
                index = cache['node'].index(prev)
                cache['node'].pop(index)
                cache['dir'].pop(index)

            cache['node'].append(prev)
            cache['dir'].append(direc)
            prev = nextnode
        if mode == 0:
            draw()

    if mode == 1:
        draw()
        
    return True