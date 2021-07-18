import pygame

clk = pygame.time.Clock()

def heap(draw, grid):
    temp = [i.value for i in grid]
    run = True
    slow = True

    length = len(temp)
    for i in range(length // 2 - 1, -1, -1):
        heapify(draw, grid, temp, i, length, slow)

    for i in range(length - 1, 0, -1):

        if not slow:
            clk.tick(20)
        else:
            clk.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True, False
                if event.key == pygame.K_BACKSPACE:
                    slow = not slow

        temp[0], temp[i] = temp[i], temp[0]
        grid[0].value = temp[0]
        grid[0].make_red()
        grid[i].value = temp[i]
        grid[i].make_red()
        if slow:
            draw()
        heapify(draw, grid, temp, 0, i, slow)
        if not slow:
            draw()
        
    return True, True


def heapify(draw, grid, temp, index, heap_size, slow):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                slow = not slow
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and temp[left_index] > temp[largest]:
        largest = left_index

    if right_index < heap_size and temp[right_index] > temp[largest]:
        largest = right_index

    if largest != index:
        temp[largest], temp[index] = temp[index], temp[largest]
        grid[largest].value = temp[largest]
        grid[largest].make_red()
        grid[index].value = temp[index]
        grid[index].make_red()
        if slow:
            draw()
        heapify(draw, grid, temp, largest, heap_size, slow)