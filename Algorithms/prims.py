import pygame
from random import choice, shuffle

def getneighbour(node, visited):
    neighbours = []
    a, b = node
    if a + 1 != len(grid)//2:
        neighbours.append((a+1, b))
    if b + 1 != len(grid)//2:
        neighbours.append((a, b+1))
    if a != 0 :
        neighbours.append((a-1, b))
    if b != 0 :
        neighbours.append((a, b-1))
    
    for spot in neighbours:
        x, y = spot
        if visited[x * len(grid)//2 + y]:
            neighbours.remove(spot)
        else:
           visited[x * len(grid)//2 + y] = True
    return neighbours, visited 
    

def prims(draw, grid, mode):
    for row in grid:
        for node in row:
            node.reset()
            node.invert()
    if mode == 0:
        draw()

    nodelist = [(i, j) for i in range(len(grid)//2) for j in range(len(grid)//2)]
    visited = [False for i in range(len(nodelist))]

    start = choice(nodelist)
    x,y = start
    g = [start]
    visited[ x * len(grid)//2 + y] = True

    count = 0

    while count != (len(grid)//2)**2 - 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        node = choice(g)
        n, visited = getneighbour(node, visited)
        g.remove(node)
        g.extend(n)
        shuffle(g)

    if mode == 1:
        draw()
        
    return True