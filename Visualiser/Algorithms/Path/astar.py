import pygame
from queue import PriorityQueue

def reconstruct(came, end, draw):
    while end in came:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        end = came[end]
        end.make_path()
        draw()


def astar(draw, grid, start, end, mode):
    pygame.init()
    count = 0
    openset = PriorityQueue()
    openset.put((0, count, start))
    camefrom = {}
    gscore = {node : float('inf') for row in grid for node in row}
    gscore[start] = 0
    fscore = {node : float('inf') for row in grid for node in row}
    fscore[start] = h(start.get_pos(), end.get_pos())

    opensethash = {start}

    for row in grid:
        for node in row:
            node.update_neighbours(grid)

    while not openset.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if mode == 0:
                        mode = 1
                    else:
                        mode = 0
        
        current = openset.get()[2]
        opensethash.remove(current)

        if current == end:
            reconstruct(camefrom, end, draw)
            end.make_end()
            start.make_start()
            return True
        
        for neighbour in current.neighbours:
            tempgscore = gscore[current] + 1
            if tempgscore < gscore[neighbour]:
                camefrom[neighbour] = current
                gscore[neighbour] = tempgscore
                fscore[neighbour] = tempgscore + h(neighbour.get_pos(), end.get_pos())
                if neighbour not in opensethash:
                    count += 1
                    openset.put((fscore[neighbour], count, neighbour))
                    opensethash.add(neighbour)
                    neighbour.make_open()
        if mode == 0:
            draw()

        if current != start:
            current.make_closed()

    return True

def h(p, q): # L distance
    x1, y1 = p
    x2, y2 = q
    return abs(x1 - x2) + abs(y1 - y2)