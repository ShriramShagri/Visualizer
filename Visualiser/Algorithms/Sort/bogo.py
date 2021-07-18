import pygame
import random

clk = pygame.time.Clock()

def bogo(draw, grid):
    temp = [i.value for i in grid]
    run = True
    slow = True

    length = len(grid)

    while True:
        if not slow:
            clk.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return (False, False)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return (True, False)
                # if event.key == pygame.K_BACKSPACE:
                #     slow = not slow
        def is_sorted(temp):
            if len(temp) < 2:
                return True
            for i in range(len(temp) - 1):
                if temp[i] > temp[i + 1]:
                    return False
            return True

        if not is_sorted(temp):
            random.shuffle(temp)
            for node in range(length):
                if grid[node].value != temp[node]:
                    grid[node].value = temp[node]
            if slow:
                draw()
        else:
            return (True, True)
        
    return (True, True)