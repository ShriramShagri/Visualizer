import pygame

clk = pygame.time.Clock()

def gnome(draw, grid):
    temp = [i.value for i in grid]
    run = True
    slow = False

    length = len(grid)
    i = 1
    while i < length:
        if not slow:
            clk.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True, False
                if event.key == pygame.K_BACKSPACE:
                    slow = not slow
        if temp[i - 1] <= temp[i]:
            i += 1
        else:
            temp[i - 1], temp[i] = temp[i], temp[i - 1]
            grid[i].value = temp[i]
            grid[i].make_red()
            grid[i - 1].value = temp[i - 1]
            grid[i - 1].make_red()
            if slow:
                draw()

            i -= 1
            if i == 0:
                i = 1
        if not slow:
            grid[i].make_red()
            grid[i - 1].make_red()
            draw()
                
    return True, True