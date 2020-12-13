import pygame
import os

class button():
    def __init__(self, color, x,y,width,height, FILEPATH, textcolor, text='', size=60):
        """Button Class

        Args:
            color (tuple): Color (r, g, b)
            x (int): Button top left coordinate
            y (int): Button top left y coordinate
            width (int): Button width in px
            height (int): Button height in px
            FILEPATH (str): File path for fonts file
            textcolor (tuple): Text color in (r, g, b)
            text (str, optional): Text inside button. Defaults to ''.
            size (int, optional): Font size. Defaults to 60.
        """        
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.filepath = FILEPATH
        self.textcolor = textcolor
        self.size = size

    def draw(self,win,outline=None):
        """Call this method to draw the button on the screen

        Args:
            win (pygame.Surface): Surface on which buttons are drawn
            outline (tuple, optional): Button outline color(r, g, b). Defaults to None.
        """        
        if outline:
            # To draw an outline draw a darker, larger rectangle behind the actual Button
            # Size of the button is 4px hardcoded
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            # Print text if mentioned
            font = pygame.font.Font(os.path.join(self.filepath, 'Fonts', 'MaidenOrange.ttf'), self.size)
            text = font.render(self.text, 1, self.textcolor)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)+10))

    def isOver(self, pos):
        """Check if mouse is on top of the button or not to give hover effects.

        Args:
            pos (tuple): position of (x, y) of mouse pointer.

        Returns:
            Boolean: True if mouse is on top of button False otherwise.
        """        
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False