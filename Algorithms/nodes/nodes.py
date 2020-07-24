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
LIGHTGREEN = (50,205,50)
LIGHTRED = (255, 127, 127)
LIGHTGREEN2 = (55,205,55)
LIGHTRED2 = (255, 130, 130)


class Nodes:
    def __init__(self, row, col, width, total_rows, total_cols, mode):
        self.row = row
        self.col = col
        self.y = row * width
        self.x = col * width
        self.colour = WHITE
        self.neighbours = []
        self.neighbournodes = []
        self.width = width
        self.total_rows = total_rows
        self.total_cols = total_cols
        self.mode = mode
        self.animator = 1

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
        self.animator = 7

    def make_closed(self):
        self.colour = RED
        self.animator = 7

    def make_open(self):
        self.colour = GREEN
        self.animator = 7

    def make_barrier(self):
        self.colour = BLACK
        self.animator = 7

    def make_start(self):
        self.colour = ORANGE
        self.animator = 7

    def make_end(self):
        self.colour = TURQUOISE
        self.animator = 7

    def make_path(self):
        self.colour = PURPLE
        self.animator = 7
    
    def remove_barrier(self):
        self.colour = WHITE
        self.animator = 8
        
    def leader(self):
        self.colour = GREEN
    
    def tracker(self):
        self.colour = LIGHTRED
        self.animator = 8

    def wil1(self):
        self.colour = LIGHTGREEN2
        self.animator = 1

    def wil2(self):
        self.colour = LIGHTRED2
        self.animator = 1

    def getwil1(self):
        return self.colour == LIGHTGREEN2

    def getwil2(self):
        return self.colour == LIGHTRED2

    def draw(self, win):
        noskip = True
        if self.mode == 1 and (self.colour == RED or self.colour == GREEN):
            self.colour = WHITE
        if self.animator == 8:
            pygame.draw.rect(win, LIGHTGREEN, (self.x, self.y, self.width, self.width))
            noskip = False
        if self.animator == 7 and (self.colour != WHITE or self.colour != LIGHTRED):
            pygame.draw.rect(win, WHITE, (self.x, self.y, self.width, self.width))
        gap = self.width / self.animator
        pos = (self.width - gap) / 2
        if noskip:
            pygame.draw.rect(win, self.colour, (self.x + pos, self.y + pos, gap, gap))
        if self.animator > 1:
            self.animator -= 1
    
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

        if self.col < self.total_cols - 1 and not grid[self.row][self.col + 1].is_barrier(): # right
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

            if self.col < self.total_cols - 1: # right
                self.neighbours.append(grid[self.row][self.col + 2])

            if self.col > 0: # left
                self.neighbours.append(grid[self.row][self.col - 2])

    def __lt__(self, other):
        return False