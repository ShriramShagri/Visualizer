import pygame

clk = pygame.time.Clock()
t = []
# def quick(draw, grid):
#     global t
#     temp = [i.value for i in grid]
#     t = grid
#     run = True
#     slow = True


#     a = qsort(draw, grid, slow)
#     for i, nodes in enumerate(a):
#         nodes.make_red()
#         n = nodes.move(i+1)
#         if slow:
#             draw()
        
#     return True, True

# def qsort(draw, grid, slow):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_BACKSPACE:
#                 slow = not slow
#     length = len(grid)
#     if length <= 1:
#         return grid
#     else:
        
#         pivot = grid.pop()
        
#         greater, lesser = [], []
#         for element in grid:
#             if element.value > pivot.value:
#                 greater.append(element)
#             else:
#                 lesser.append(element)
#         a = qsort(draw, lesser, slow) + [pivot] + qsort(draw, greater, slow)
#         for i, nodes in enumerate(a):
#             nodes.make_red()
#             n = nodes.move(i+1)
#             if slow:
#                 draw()
#         if not slow:
#             draw()
#         return a

def partition(draw, grid, temp, low, high, slow): 
    i = (low - 1)         # index of smaller element 
    pivot = temp[high]     # pivot 
  
    for j in range(low, high): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    slow = not slow
   
        if temp[j] <= pivot: 
            i += 1
            temp[i], temp[j] = temp[j], temp[i] 
            grid[i].value, grid[j].value = temp[i], temp[j]
            grid[i].make_red()
            grid[j].make_red()
            if slow:
                draw()
  
    temp[i + 1], temp[high] = temp[high], temp[i + 1] 
    grid[i + 1].value, grid[high].value = temp[i + 1], temp[high]
    grid[i + 1].make_red()
    grid[high].make_red()
    draw()

    return (i + 1) 

def quickSort(draw, grid, temp, low, high, slow): 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True, False
            if event.key == pygame.K_BACKSPACE:
                slow = not slow
    if low < high: 
        pi = partition(draw, grid, temp, low, high, slow) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(draw, grid, temp, low, pi-1, slow) 
        quickSort(draw, grid, temp, pi + 1, high, slow) 

def quick(draw, grid):
    temp = [i.value for i in grid]
    run = True
    slow = True

    length = len(grid)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True, False
            if event.key == pygame.K_BACKSPACE:
                slow = not slow
        
    quickSort(draw, grid, temp, 0, length-1, slow)
        
    return True, True