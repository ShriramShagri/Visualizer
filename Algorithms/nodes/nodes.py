import pygame

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (128,0,128)
ORANGE = (255,165,0)
GREY = (128,128,128)
TURQUOISE = (64,224,208)


class Nodes:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.colour = WHITE
        self.neighbours = []
        self.neighbournodes = []
        self.width = width
        self.total_rows = total_rows
        self.ani = 4

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.colour == RED

    def is_open(self):
        return self.colour == GREEN

    def is_barrier(self):
        return self.colour == BLACK

    def is_start(self):
        return self.colour == ORANGE

    def is_end(self):
        return self.colour == TURQUOISE

    def reset(self):
        self.colour = WHITE

    def make_closed(self):
        self.colour = RED

    def make_open(self):
        self.colour = GREEN

    def make_barrier(self):
        self.colour = BLACK

    def make_start(self):
        self.colour = ORANGE

    def make_end(self):
        self.colour = TURQUOISE

    def make_path(self):
        self.colour = PURPLE
    
    def remove_barrier(self):
        self.colour = WHITE

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))
    
    def invert(self):
        if self.colour == BLACK:
            self.colour = WHITE
        elif self.colour == WHITE:
            self.colour = BLACK

    def update_neighbours(self, grid):
        self.neighbours = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # down
            self.neighbours.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # up
            self.neighbours.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # right
            self.neighbours.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # left
            self.neighbours.append(grid[self.row][self.col - 1])

    def neighbour_node(self, grid):
        self.neighbournodes = []
        if self.row % 2 == 1 and self.col % 2 == 1:
            if self.row < self.total_rows - 1: # down
                self.neighbours.append(grid[self.row + 2][self.col])

            if self.row > 0: # up
                self.neighbours.append(grid[self.row - 2][self.col])

            if self.col < self.total_rows - 1: # right
                self.neighbours.append(grid[self.row][self.col + 2])

            if self.col > 0: # left
                self.neighbours.append(grid[self.row][self.col - 2])

    def __lt__(self, other):
        return False