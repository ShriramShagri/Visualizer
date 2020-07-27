import pygame
from random import randint, choice

clk = pygame.time.Clock()
row = 24
col = 49


def getboolean():
    if randint(0, 1) == 0:
        return True
    return False


class Cell:
    def __init__(self, a, b, s):
        self.x = a
        self.y = b
        self.right = False
        self.left = False
        self.down = False
        self.sets = set()
        self.setno = s


def joinright(draw, grid, r, mode):
    for i in range(1, len(r)):
        if r[i].setno == r[i-1].setno:
            r[i-1].right = False
            r[i].left = False
            continue
        if getboolean():
            r[i-1].right = True
            r[i].left = True
            j = r[i].setno
            k = r[i-1].setno
            for items in r:
                if items.setno == j:
                    items.setno = k
        else:
            r[i-1].right = False
            r[i].left = False
        drawright(draw, grid, r, mode)
    return r

def drawright(draw, grid, r, mode):
    for items in r:
        if items.right:
            grid[items.x*2][items.y*2].reset()
            if items.y*2+1 < 99:
                grid[items.x*2][items.y*2+1].reset()
        elif items.left:
            grid[items.x*2][items.y*2].reset()
            if items.y*2-1 > 0:
                grid[items.x*2][items.y*2-1].reset()
        else:
            grid[items.x*2][items.y*2].reset()
            if items.y*2+1 < 99:
                grid[items.x*2][items.y*2+1].barrier()
            
    if mode == 0:
        draw()

def sortcell(cell):
    l = {}
    for node in cell:
        if f'{node.setno}' in l.keys():
            l[f'{node.setno}'].append(node)
        else:
            l[f'{node.setno}'] = [node]
    return l 

def joindown(draw, grid, current, mode):
    a = sortcell(current)
    for val in a.values():
        l = len(val)
        if l == 1:
            val[-1].down = True
            drawdown(draw, grid, val[-1].x, val[-1].y, val[-1], mode)
        else:
            r = randint(1, l)
            while r != 0:
                g = choice(val)
                g.down = True
                r-=1
                drawdown(draw, grid, g.x, g.y, g, mode)
    return current
            
def setmanager(current, nextrow):
    for i in range(len(current)):
        if current[i].down == True:
            nextrow[i].setno = current[i].setno
    return nextrow

def drawdown(draw, grid, x, y, node, mode):
    if node.down == True:
        grid[x*2][y*2].reset()
        if x*2+1 < 48:
            grid[x*2+1][y*2].reset()
    if mode == 0:
        draw()

def ellers(draw, grid, mode):
    run = True
    for rw in grid:
        for node in rw:
            node.reset()
            node.invert()    
    if mode == 0:
        draw()

    s = 1
    celllist = []
    for b in range(row+1):
        celllist.append([])
        for j in range(col+1):
            celllist[b].append(Cell(b, j, s))
            s += 1  
    
    i = 0
    currrow = celllist[i]
    while i < row:
        clk.tick(30)
        # i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_CAPSLOCK:
                    if mode == 0:
                        mode = 1
                    else:
                        mode = 0
        
        currrow = joinright(draw, grid, currrow, mode)

        currrow = joindown(draw, grid, currrow, mode)
        currrow = setmanager(current=currrow, nextrow = celllist[i+1])
        i+=1
    joinrightlast(draw, grid, currrow, mode)
    if mode == 1:
        draw()
        
    return True

def joinrightlast(draw, grid, r, mode):
    for i in range(1, len(r)):
        if r[i].setno == r[i-1].setno:
            r[i-1].right = False
            r[i].left = False
        else:
            r[i-1].right = True
            r[i].left = True
            j = r[i].setno
            k = r[i-1].setno
            for items in r:
                if items.setno == j:
                    items.setno = k
        drawright(draw, grid, r, mode)