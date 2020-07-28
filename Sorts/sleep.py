from threading import Timer
from time import sleep
import pygame

clk = pygame.time.Clock()

def sleepsort(draw, grid):
    temp = [i.value for i in grid]
    run = True

    sleepsort.result = []

    def append_to_result(x, grid, draw):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
        sleepsort.result.append(x)
        ind = sleepsort.result.index(x)
        grid[ind].value = x
        grid[ind].make_red()
        draw()
        

    mx = temp[0]
    for value in temp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True, False
        
        if mx < value:
            mx = value
        Timer(value, append_to_result, [value, grid, draw]).start()

    pygame.time.wait((mx + 1))
             
    return True, True

