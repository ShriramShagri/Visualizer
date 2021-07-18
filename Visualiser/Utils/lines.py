import pygame

from ..constants import *

class Line():
    def __init__(self, x, no):
        """Draw lines for sorting

        Args:
            x (int): X coordinate
            no (int): position number
        """        
        self.value = x
        self.color = BLACK
        self.flash = 0
        self.no = no
        self.x = (no)*LINE_WIDTH
    
    def make_red(self):
        """Change line color to red
        """        
        self.color = RED
        self.flash = 1
    
    def make_green(self):
        """Change line color to Green
        """        
        self.color = GREEN
        self.flash = 1
    
    def reset(self):
        """Change line color to Black
        """        
        self.color = BLACK
        self.flash = 0
    
    def change(self, val):
        """Change the x coordinate and position value

        Args:
            val (int): Position Value
        """        
        self.no = val
        self.x = (val)*LINE_WIDTH
    
    def move(self, val):
        k = self.no+1
        self.no = val-1
        self.x = (val-1)*LINE_WIDTH
        return k
    
    def evalu(self, val):
        """set value

        Args:
            val (int): Value
        """        
        self.value = val
    
    def posvalue(self):
        """Get position value and number

        Returns:
            tuple: (position, no)
        """        
        return (self.value, self.no)

    def draw(self, win):
        """Draw line on specified position

        Args:
            win (pygame.Surface): Surface on which to draw
        """        
        if self.flash > 0:
            self.flash -= 1
        elif self.flash == 0:
            self.color = BLACK
        pygame.draw.rect(win, self.color, (self.x, HEIGHT-LINE_HEIGHT*self.value, WIDTH, LINE_HEIGHT*self.value))
