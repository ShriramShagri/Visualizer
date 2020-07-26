import pygame
from random import randint, choice, shuffle

row = 24
col = 49
clk = pygame.time.Clock()

def update(node, visited):
    n = []
    x, y = node
    if x < row and x > 0: # down
        n.append((x + 1, y))
        n.append((x - 1, y))
    elif x == 0:
        n.append((x + 1, y))
    elif x == row:
        n.append((x - 1, y))
    if y < col and y > 0: # down
        n.append((x, y + 1))
        n.append((x, y - 1))
    elif y == 0:
        n.append((x, y + 1))
    elif y == col:
        n.append((x, y - 1))
    for nodes in visited:
        if nodes in n:
            n.remove(nodes)
    return n

def neighbours(visited):
    n = []
    for node in visited:
        fresh = []
        x, y = node
        if x < row and x > 0: # down
            fresh.append((x + 1, y))
            fresh.append((x - 1, y))
        elif x == 0:
            fresh.append((x + 1, y))
        elif x == row:
            fresh.append((x - 1, y))
        if y < col and y > 0: # down
            fresh.append((x, y + 1))
            fresh.append((x, y - 1))
        elif y == 0:
            fresh.append((x, y + 1))
        elif y == col:
            fresh.append((x, y - 1))
        for nodes in visited:
            if nodes in fresh:
                fresh.remove(nodes)
        n.extend(fresh)
    return n

def drawedge(draw, grid, node, visited, mode):
    x, y = node
    neigh = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    shuffle(neigh)
    for spot in neigh:
        if spot in visited:
            break
    drawsquare(draw, grid, spot, node, mode)
    

def gohunt(draw, grid, n, i, visited, mode):
    # if mode == 0:
        # drawrow(draw, grid, i, mode)
    for j in range(col+1):
        if (i, j) in n:
            return (i, j)
    return None

def drawrow(draw, grid, row, mode):
    row *= 2
    for rw in grid:
        for node in rw:
            if node.if_open_prev():
                node.do_open_prev()
    for nodes in grid[row]:
        nodes.open_prev()
    
    if mode == 0:
        draw()


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
    
    grid[x1*2][y1*2].remove_barrier()
    grid[x][y].remove_barrier()
    grid[x2*2][y2*2].remove_barrier()
    if mode == 0:
        draw()

def check(n):
    if len(n) != 0:
        return True
    return False

def getrow(visited):
    i = 0
    run = True
    for i in range(row + 1):
        for j in range(col + 1):
            if (i, j) not in visited:
                run = False
        if not run:
            break
    return i

def hunt(draw, grid, mode):
    run = True
    l = len(grid)
    for rw in grid:
        for node in rw:
            node.reset()
            node.invert()      
    if mode == 0:
        draw()
    
    i = 0
    stack = []
    x = randint(0, row-1)
    y = randint(0, col-1)
    stack.append((x, y)) 
    visited = {(x, y)}
    store = stack[-1]
    if mode == 0:
        draw()

    while run:
        # clk.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_BACKSPACE:
                    if mode == 0:
                        mode = 1
                    else:
                        mode = 0
        n = update(stack[-1], visited)

        if check(n):
            spot = choice(n)
            prev = stack[-1]
            stack.append(spot)
            visited.add(spot)
            drawsquare(draw, grid, spot, prev, mode)
        else:
            stack = []
            n = neighbours(visited)
            i = getrow(visited)
            while True:
                new = gohunt(draw, grid, n, i, visited, mode)
                i += 1
                if new != None:
                    break
                if new == None and i == row + 1:
                    run = False
                    break
            if run:
                stack.append(new)
                visited.add(new)
                drawedge(draw, grid, new, visited, mode)
    if mode == 1:
        draw()
        
    return True
