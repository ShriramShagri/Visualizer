import pygame
from queue import PriorityQueue

def reconstruct(came, end, draw):
    while end in came:
        end = came[end]
        end.make_path()
        draw()


def astar(draw, grid, start, end, mode):
    pygame.init()
    run = True

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

    return True
