import pygame

# clk = pygame.time.Clock()

def test(draw, grid, mode):
    run = True
    l = len(grid)
    for row in grid:
        for node in row:
            node.reset()
            node.invert()      
    if mode == 0:
        draw()
    


    while run:
        # clk.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
    if mode == 1:
        draw()
        
    return True