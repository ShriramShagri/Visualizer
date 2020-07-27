import pygame

RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

W = 1584
H = 784

WIDTH = 1584/396

HEIGHT = 784/396

class Line():
    def __init__(self, x, no):
        self.value = x
        self.color = WHITE
        self.flash = 0
        self.no = no
        self.x = (no)*WIDTH
    
    def make_red(self):
        self.color = RED
        self.flash = 1
    
    def make_green(self):
        self.color = GREEN
        self.flash = 1
    
    def reset(self):
        self.color = WHITE
        self.flash = 0
    
    def change(self, val):
        self.no = val
        self.x = (val)*WIDTH
    
    def evalu(self, val):
        self.value = val
    
    def posvalue(self):
        return (self.value, self.no)

    def draw(self, win):
        if self.flash > 0:
            self.flash -= 1
        elif self.flash == 0:
            self.color = WHITE
        pygame.draw.rect(win, self.color, (self.x, H-HEIGHT*self.value, WIDTH, HEIGHT*self.value))
