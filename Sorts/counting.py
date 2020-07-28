import pygame

clk = pygame.time.Clock()

def counting(draw, grid):
    temp = [i.value for i in grid]
    run = True
    slow = True

    temp_len = len(temp)
    temp_max = max(temp)
    temp_min = min(temp)

    counting_arr_length = temp_max + 1 - temp_min
    counting_arr = [0] * counting_arr_length

    for number in temp:
        counting_arr[number - temp_min] += 1
    
    for i in range(1, counting_arr_length):
        counting_arr[i] = counting_arr[i] + counting_arr[i - 1]
    
    ordered = [0] * temp_len

    for i in reversed(range(0, temp_len)):
        if not slow:
            clk.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True, False
                if event.key == pygame.K_BACKSPACE:
                    slow = not slow
        grid[counting_arr[temp[i] - temp_min] - 1].value = temp[i]
        grid[counting_arr[temp[i] - temp_min] - 1].make_red()
        if slow:
            draw()
        counting_arr[temp[i] - temp_min] -= 1
    if not slow:
        draw()
        
    return True, True