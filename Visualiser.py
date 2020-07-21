import pygame
import argparse

from Algorithms.nodes.nodes import *
from Algorithms.prims import *
from Algorithms.astar import *
from Algorithms.dijkstra import  *
from Algorithms.kruskal import  *

WIDTH = 800
ROWS = 50
GREY = (128,128,128)
WHITE = (255,255,255)

MODE = 0

WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Visualiser")


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Nodes(i, j, gap, rows, MODE)
            grid[i].append(node)
    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i*gap), (width, i*gap))
        pygame.draw.line(win, GREY, (i*gap, 0), (i*gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

def main(args):
    global MODE
    if args.mode != 0:
        MODE = 1
    grid = make_grid(ROWS, WIDTH)
    pygame.init()

    start = None
    end = None

    run = True
    started = False
    sim = False

    while run:
        if not started:
            draw(WIN, grid, ROWS, WIDTH)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0] and not started:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked(pos, ROWS, WIDTH)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()
            
                elif not end and spot != start:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start:
                    spot.make_barrier()
                   

            elif pygame.mouse.get_pressed()[2]and not started:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked(pos, ROWS, WIDTH)
                spot = grid[row][col] 
                spot.reset()

                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and not started and start and end:
                    started = True
                    astar(lambda : draw(WIN, grid, ROWS, WIDTH), grid, start, end, MODE)
                    started = False
                    sim = True

                if event.key == pygame.K_d and not started and start and end:
                    started = True
                    dijkstra(lambda : draw(WIN, grid, ROWS, WIDTH), grid, start, end, MODE)
                    started = False
                    

                if event.key == pygame.K_p and not started and not start and not end:
                    started = True
                    prims(lambda : draw(WIN, grid, ROWS, WIDTH), grid, MODE)
                    started = False
                
                if event.key == pygame.K_k and not started and not start and not end:
                    started = True
                    kruskal(lambda : draw(WIN, grid, ROWS, WIDTH), grid, MODE)
                    started = False


                if event.key == pygame.K_BACKSPACE:
                    start = None
                    end = None
                    grid = make_grid(ROWS, WIDTH)
                    pygame.display.set_caption("Visualiser")

    pygame.quit()

def parse():
    parser = argparse.ArgumentParser(
        description="Starts ")
    parser.add_argument(
        "-m", help="Mode: 0 for slow 1 for fast"
        "(default is slow)", type=int, default=0, dest="mode")
    return parser.parse_args()



main(parse())