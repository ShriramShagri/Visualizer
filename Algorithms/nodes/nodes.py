import pygame
from pygame import gfxdraw

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
        self.prevcolour = None

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
    
    def barrier(self):
        self.colour = BLACK

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
        self.colour = YELLOW
        self.animator = 8

    def wil1(self):
        self.colour = LIGHTGREEN2
        self.animator = 1

    def wil2(self):
        self.colour = LIGHTRED2
        self.animator = 1
    
    def open_prev(self):
        self.prevcolour = self.colour
        self.colour = LIGHTGREEN
    
    def if_open_prev(self):
        return self.colour == LIGHTGREEN

    def do_open_prev(self):
        if self.prevcolour:
            self.colour = self.prevcolour
            self.prevcolour = None

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
            # self.aa_round_rect(win, LIGHTGREEN, (self.x, self.y, self.width, self.width), 30)
            noskip = False
        if self.animator == 7 and (self.colour != WHITE or self.colour != YELLOW):
            pygame.draw.rect(win, WHITE, (self.x, self.y, self.width, self.width))
            # self.aa_round_rect(win, WHITE, (self.x, self.y, self.width, self.width), 30)
        gap = self.width / self.animator
        pos = (self.width - gap) / 2
        if noskip:
            pygame.draw.rect(win, self.colour, (self.x + pos, self.y + pos, gap, gap))
            # self.aa_round_rect(win, self.colour, (self.x, self.y, self.width, self.width), 30)
        if self.animator > 1:
            self.animator -= 1
        if self.prevcolour:
            self.colour = self.prevcolour
            self.prevcolour = None
    
    def drawwil(self, win):
        noskip = True
        if self.mode == 1 and (self.colour == RED or self.colour == GREEN):
            self.colour = WHITE
        if self.animator == 8:
            pygame.draw.rect(win, LIGHTGREEN, (self.x, self.y, self.width, self.width))
            # self.round_rect(win, LIGHTGREEN, (self.x, self.y, self.width, self.width))
            noskip = False
        if self.animator == 7 and (self.colour != WHITE or self.colour != LIGHTRED):
            pygame.draw.rect(win, WHITE, (self.x, self.y, self.width, self.width))
            # self.round_rect(win, WHITE, (self.x, self.y, self.width, self.width))
        gap = self.width / self.animator
        pos = (self.width - gap) / 2
        if noskip:
            pygame.draw.rect(win, self.colour, (self.x + pos, self.y + pos, gap, gap))
            # self.round_rect(win, self.colour, (self.x, self.y, self.width, self.width))

        if self.animator > 1:
            self.animator -= 1
        if self.prevcolour:
            self.colour = self.prevcolour
            self.prevcolour = None
    
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

    

    def draw_rounded_rect(self, surface, color, rect, corner_radius):
        ''' Draw a rectangle with rounded corners.
        Would prefer this: 
            pygame.draw.rect(surface, color, rect, border_radius=corner_radius)
        but this option is not yet supported in my version of pygame so do it ourselves.

        We use anti-aliased circles to make the corners smoother
        '''
        if rect.width < 2 * corner_radius or rect.height < 2 * corner_radius:
            raise ValueError(f"Both height (rect.height) and width (rect.width) must be > 2 * corner radius ({corner_radius})")

        # need to use anti aliasing circle drawing routines to smooth the corners
        pygame.gfxdraw.aacircle(surface, rect.left+corner_radius, rect.top+corner_radius, corner_radius, color)
        pygame.gfxdraw.aacircle(surface, rect.right-corner_radius-1, rect.top+corner_radius, corner_radius, color)
        pygame.gfxdraw.aacircle(surface, rect.left+corner_radius, rect.bottom-corner_radius-1, corner_radius, color)
        pygame.gfxdraw.aacircle(surface, rect.right-corner_radius-1, rect.bottom-corner_radius-1, corner_radius, color)

        pygame.gfxdraw.filled_circle(surface, rect.left+corner_radius, rect.top+corner_radius, corner_radius, color)
        pygame.gfxdraw.filled_circle(surface, rect.right-corner_radius-1, rect.top+corner_radius, corner_radius, color)
        pygame.gfxdraw.filled_circle(surface, rect.left+corner_radius, rect.bottom-corner_radius-1, corner_radius, color)
        pygame.gfxdraw.filled_circle(surface, rect.right-corner_radius-1, rect.bottom-corner_radius-1, corner_radius, color)

        rect_tmp = pygame.Rect(rect)

        rect_tmp.width -= 2 * corner_radius
        rect_tmp.center = rect.center
        pygame.draw.rect(surface, color, rect_tmp)

        rect_tmp.width = rect.width
        rect_tmp.height -= 2 * corner_radius
        rect_tmp.center = rect.center
        pygame.draw.rect(surface, color, rect_tmp)


    def round_rect(self, surface, color,  rect, rad=20, border=0, inside=(0,0,0,0)):
        """
        Draw a rect with rounded corners to surface.  Argument rad can be specified
        to adjust curvature of edges (given in pixels).  An optional border
        width can also be supplied; if not provided the rect will be filled.
        Both the color and optional interior color (the inside argument) support
        alpha.
        """
        rect = pygame.Rect(rect)
        zeroed_rect = rect.copy()
        zeroed_rect.topleft = 0,0
        image = pygame.Surface(rect.size).convert_alpha()
        image.fill((0,0,0,0))
        self._render_region(image, zeroed_rect, color, rad)
        if border:
            zeroed_rect.inflate_ip(-2*border, -2*border)
            self._render_region(image, zeroed_rect, inside, rad)
        surface.blit(image, rect)


    def _render_region(self, image, rect, color, rad):
        """Helper function for round_rect."""
        corners = rect.inflate(-2*rad, -2*rad)
        for attribute in ("topleft", "topright", "bottomleft", "bottomright"):
            pygame.draw.circle(image, color, getattr(corners,attribute), rad)
        image.fill(color, rect.inflate(-2*rad,0))
        image.fill(color, rect.inflate(0,-2*rad))


    def aa_round_rect(self, surface, color, rect, rad=20, border=0, inside=(0,0,0)):
        """
        Draw an antialiased rounded rect on the target surface.  Alpha is not
        supported in this implementation but other than that usage is identical to
        round_rect.
        """
        rect = pygame.Rect(rect)
        self._aa_render_region(surface, rect, color, rad)
        if border:
            rect.inflate_ip(-2*border, -2*border)
            self._aa_render_region(surface, rect, inside, rad)


    def _aa_render_region(self, image, rect, color, rad):
        """Helper function for aa_round_rect."""
        corners = rect.inflate(-2*rad-1, -2*rad-1)
        for attribute in ("topleft", "topright", "bottomleft", "bottomright"):
            x, y = getattr(corners, attribute)
            gfxdraw.aacircle(image, x, y, rad, color)
            gfxdraw.filled_circle(image, x, y, rad, color)
        image.fill(color, rect.inflate(-2*rad,0))
        image.fill(color, rect.inflate(0,-2*rad))