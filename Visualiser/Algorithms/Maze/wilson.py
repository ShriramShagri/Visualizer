import pygame
from random import randint, shuffle, choice

row = 24
col = 49
LIGHTGREEN = (55,205,55)
LIGHTRED = (255, 130, 130)

d = ['n', 's', 'e', 'w']
clk = pygame.time.Clock()

def drawedge(draw, edge, grid, mode):
    x1, y1, x2, y2, x, y = getcoordinate(edge)
    
    grid[x1*2][y1*2].remove_barrier()
    grid[x][y].remove_barrier()
    grid[x2*2][y2*2].remove_barrier()
    if mode == 0:
        draw()

def drawedgetemp(draw, edge, grid, mode):
    x1, y1, x2, y2, x, y = getcoordinate(edge)
    
    grid[x][y].wil2()
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
    if x < row:
        return (x+1, y)
    return None

def south(node):
    x, y = node
    if y < col:
        return (x, y+1)
    return None

def west(node):
    x, y = node
    if x > 0:
        return (x-1, y)
    return None

def wilson(draw, grid, mode):
    run = True
    directions = {'n': north, 'e': east, 's' : south, 'w': west}
    for rw in grid:
        for node in rw:
            node.reset()
            node.invert()      
    if mode == 0:
        draw()
    nodelist = [(i,j) for i in range(row+1) for j in range(col+1)]
    shuffle(nodelist)

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

    path = False
    span = []
    cache = {
        "node" : [],
        "dir" : []
    }
    x = randint(0, row)
    y = randint(0, col)
    span.append((x, y))
    nodelist.remove((x, y))
    ex = 0

    grid[x*2][y*2].remove_barrier()
    if mode == 0:
        draw()

    start = choice(nodelist)
    prev = start

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if mode == 0:
                        mode = 1
                    else:
                        mode = 0
        if path:
            direc = cache['dir'][cache['node'].index(start)]
            nextnode = directions[direc](start)
            getedge(draw, start, nextnode, direc, grid, mode)
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

            if prev in cache['node']:
                index = cache['node'].index(prev)
                cache['node'].pop(index)
                cache['dir'].pop(index)

            cache['node'].append(prev)
            cache['dir'].append(direc)
            drawmap(draw, grid, cache, edgelist, mode)
            prev = nextnode

            if nextnode in span:
                drawwil(draw, grid, cache, mode)
                path = True
                
        if mode == 0:
            draw()

    if mode == 1:
        draw()
    return True
    
def drawmap(draw, grid, cache, edgelist, mode):
    x1, y1 = cache['node'][-1]
    grid[x1*2][y1*2].wil1()
    if len(cache['node']) > 1:
        x2, y2 = cache['node'][-2]
        grid[x2*2][y2*2].wil2()
        if ((x1, y1), (x2, y2)) in edgelist:
            edge = ((x1, y1), (x2, y2))
        elif ((x2, y2), (x1, y1)) in edgelist:
            edge = ((x2, y2), (x1, y1))
        if mode == 0:
            drawedgetemp(draw, edge, grid, mode)

    if mode == 0:
        draw()

def drawwil(draw, grid, cache, mode):
    for rw in grid:
        for node in rw:
            if node.colour == LIGHTGREEN or node.colour == LIGHTRED:
                node.make_barrier()

        
    