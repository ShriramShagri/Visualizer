import pygame
from random import randint, choice

extra_vis = False

row = 24
col = 49

clk = pygame.time.Clock()

def drawedge(draw, edge, grid, mode):
    """Connect the nodes(By removing barrier)

    Args:
        draw (func): Draws on screen
        edge (tuple): cordinates of the ends of the edge
        grid (2D list): Nodes on the screen
        mode (int): fast 1/0 slow
    """    
    # Get
    x1, y1, x2, y2, x, y = getcoordinate(edge)
    
    grid[x1*2][y1*2].remove_barrier()
    grid[x][y].remove_barrier()
    grid[x2*2][y2*2].remove_barrier()
    

    if mode == 0:
        draw()

def flash(draw, node, grid, mode):
    """draw the node on iteration 

    Args:
        draw (func): Draws on screen
        node (tuple): cordinates of the node
        grid (2D list): Nodes on the screen
        mode (int): fast 1/0 slow
    """    
    x1, y1 = node
    for rw in grid:
        for node in rw:
            if node.getwil1():
                node.reset()
    
    grid[x1*2][y1*2].wil1()
    if mode == 0:
        draw()

def getcoordinate(edge):
    """Get coordinates of the edge node between two nodes

    Args:
        edge (tuple): tuple of tuplescontaining two nodes
    """    
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
    """Get a random neighbouring node

    Args:
        node (tuple): x, y of the node

    Returns:
        tuple: a random neighbouring node
    """    
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
    """Get random neighbouring node which is not visited

    Args:
        node (tuple): x, y of the node
        visited (list): list of tuples of visited node

    Returns:
        list: first index as neighbours and second index as the node
    """    
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
    """Check if node exists

    Args:
        node (tuple): x, y of tuple if node exists

    Returns:
        boolean: true if exists false otherise
    """    
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
    run = True
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
    while len(visited) < (c//2 + 1)*(r//2 + 1) and run:
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
                if event.key == pygame.K_ESCAPE:
                    run = False
        if count <= 10:
            nextnode = getnextnode(prev)
        else:
            n = []
            while len(n) == 0:
                prev = choice(visited)
                
                n = getrandom(prev, visited)
            nextnode = n[-1]
            count = 0

        temp = grid
        flash(draw, nextnode, grid, mode)
        grid = temp

        if nextnode in visited:
            count += 1
            if mode == 0:
                draw()
        else:
            visited.append(nextnode)
            drawedge(draw, (prev, nextnode), grid, mode)
            prev = nextnode
        
    if mode == 1:
        draw()
        
    return True