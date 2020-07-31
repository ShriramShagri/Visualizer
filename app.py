import pygame
import os

import sort
from Algorithms.nodes.button import *
import Visualiser

os.environ['SDL_VIDEO_CENTERED'] = '1'

FILEPATH = os.getcwd()

WIDTH = 1584
COLUMNS = 99

HEIGHT = 784
ROWS = 49

GREY = (199,199,199)
WHITE = (255,255,255)

stage = 3
rainbow = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (150, 0, 255)]
col1, col2, col3 = rainbow[stage]
count = 6

MODE = 0

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visualiser")
pygame.display.set_icon(pygame.image.load(os.path.join(FILEPATH, 'Fonts', 'icon.png')))

clock = pygame.time.Clock()

def mainpage():
    Quit = False
    pygame.init()
    invp = False
    invs = False
    invh = False

    pygame.display.set_caption("Visualiser: Main Page")
    platbtn = button((0, 0, 0), 175+270, 500, 200, 100, FILEPATH, (0, 0, 0), text='Maze')
    sortbtn = button((0, 0, 0), 385+270, 500, 200, 100, FILEPATH, (0, 0, 0), text='Sort')
    helpbtn = button((0, 0, 0), 595+270, 500, 200, 100, FILEPATH, (0, 0, 0), text='Help')

    while not Quit:
        WIN.fill(GREY)
        filltext(invp, platbtn, invs, sortbtn, invh, helpbtn)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                Quit = True
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if platbtn.isOver(pos):
                        pygame.display.set_caption("Visualiser: Edit")
                        Quit = Visualiser.main()
                        invp = False
                    if sortbtn.isOver(pos):
                        pygame.display.set_caption("Visualiser: Help")
                        Quit = sort.sortloop()
                        invs = False
                    if helpbtn.isOver(pos):
                        pygame.display.set_caption("Visualiser: Help")
                        Quit = helppage()
                        invh = False

            if event.type == pygame.MOUSEMOTION:
                if platbtn.isOver(pos):
                    invp = True
                else:
                    invp = False

                if sortbtn.isOver(pos):
                    invs = True
                else:
                    invs = False
                
                if helpbtn.isOver(pos):
                    invh = True
                else:
                    invh = False
        
        pygame.display.update()
            
        

def filltext(inv, btn, inv2, btn2, inv3, btn3):
    color = WHITE
    Maintext = pygame.font.Font(os.path.join(FILEPATH, 'Fonts', 'Milton Keynes.ttf'), 78)
    welcome = Maintext.render("Algorithm Visualiser", True, (0, 0, 0))

    WIN.blit(welcome, (450,100))

    if inv:
        btn.textcolor = invert(color)
        btn.color = color
    else:
        btn.textcolor = color
        btn.color = invert(color)
    btn.draw(WIN, btn.textcolor)

    if inv2:
        btn2.textcolor = invert(color)
        btn2.color = color
    else:
        btn2.textcolor = color
        btn2.color = invert(color)
    btn2.draw(WIN, btn2.textcolor)

    if inv3:
        btn3.textcolor = invert(color)
        btn3.color = color
    else:
        btn3.textcolor = color
        btn3.color = invert(color)
    btn3.draw(WIN, btn3.textcolor)

    pygame.display.update()


def invert(color):
    a, b, c = color
    return (abs(255 - a), abs(255 - b), abs(255 - c))


def helppage():
    pygame.init()
    Quit = False
    inv = False

    background1 = pygame.image.load(os.path.join(FILEPATH, 'Fonts', 'Help1.png'))

    nextpage = button((0, 0, 0), 1440, 350, 75, 100, FILEPATH, (0, 0, 0), text='>')
    while not Quit:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainpage()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if nextpage.isOver(pos):
                        helppage2()

            if event.type == pygame.MOUSEMOTION:
                if nextpage.isOver(pos):
                    inv = True
                else:
                    inv = False
        WIN.blit(background1, (0, 0))
        fillhelp(inv, nextpage)
    
def helppage2():
    pygame.init()
    Quit = False
    inv = False
    inv1 = False
    page = 1

    background2 = pygame.image.load(os.path.join(FILEPATH, 'Fonts', 'Help2.png'))
   
    prevpage = button((0, 0, 0), 1440, 350, 75, 100, FILEPATH, (0, 0, 0), text='<')
    while not Quit:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainpage()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if prevpage.isOver(pos):
                        page = 1
                        helppage()
                        
            if event.type == pygame.MOUSEMOTION:
                if prevpage.isOver(pos):
                    inv1 = True
                else:
                    inv1 = False
        WIN.blit(background2, (0, 0))
        fillhelp(inv1, prevpage)
    
def fillhelp(inv2, btn2):
    color = WHITE

    if inv2:
        btn2.textcolor = invert(color)
        btn2.color = color
    else:
        btn2.textcolor = color
        btn2.color = invert(color)
    btn2.draw(WIN, btn2.textcolor)  


    pygame.display.update()


if __name__ == "__main__":
    
    mainpage()