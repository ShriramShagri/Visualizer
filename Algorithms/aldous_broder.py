import pygame
from random import randint, choice

extra_vis = False

row = 24
col = 49

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

def getnextnode(node):
    x, y = node
    neighbours = []
    if x < row:
        neighbours.append((x+1, y))
    if x > 0:
        neighbours.append((x-1, y))
    if y < col:
        neighbours.append((x, y+1))
    if y > 0:
        neighbours.append((x, y-1))

    return choice(neighbours)

def getrandom(node, visited):
    try:
        x, y = node
    except:
        return []
    neighbours = []
    if x < row:
        if (x+1, y) not in visited:
            neighbours.append((x+1, y))
    if x > 0:
        if (x-1, y) not in visited:
            neighbours.append((x-1, y))
    if y < col:
        if (x, y+1) not in visited:
            neighbours.append((x, y+1))
    if y > 0:
        if (x, y-1) not in visited:
            neighbours.append((x, y-1))

    return neighbours, node

def checkprev(node):
    try:
        x, y = node
        return True
    except:
        return False

''' Function takes an average of 11000 iterations to complete NOT RECOMMENDED TO RUN'''
def aldous(draw, grid, mode):
    ''' Function takes an average of 11000 iterations to complete NOT RECOMMENDED TO RUN'''
    r = len(grid)
    c = len(grid[0])
    global extra_vis
    for row in grid:
        for node in row:
            node.reset()
            node.invert()
       
    if mode == 0:
        draw()
    i = 0
    x = randint(0, r//2-1)
    y = randint(0, c//2-1)
    prev = (x,y)
    visited = list()

    count = 0

    nextnode = None
    while len(visited) < (c//2 + 1)*(r//2 + 1):
    # while c != 625:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if mode == 0:
                        mode = 1
                    else:
                        mode = 0
        if count <= 10:
            nextnode = getnextnode(prev)
        else:
            n = []
            while len(n) == 0:
                prev = choice(visited)
                
                n = getrandom(prev, visited)
            nextnode = n[-1]
            count = 0
        if nextnode in visited:
            count += 1
            if mode == 0:
                draw()
        else:
            visited.append(nextnode)
            drawedge(draw, (prev, nextnode), grid, mode)
            prev = nextnode
    print(len(visited))
        
    if mode == 1:
        draw()
        
    return True