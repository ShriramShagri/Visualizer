import pygame
import argparse
import os
import sys

from Algorithms.nodes.nodes import *
from Algorithms.nodes.button import *
from Algorithms.prims import prims
from Algorithms.astar import astar
from Algorithms.dijkstra import dijkstra
from Algorithms.kruskal import kruskal
from Algorithms.sidewinder import sidewinder
from Algorithms.recursive_backtracking import backtrack
from Algorithms.ellers import ellers
from Algorithms.aldous_broder import aldous
from Algorithms.wilson import wilson
from Algorithms.hunt_and_kill import hunt
from Algorithms.growing_tree import tree
from Algorithms.binary_tree import binary
from Algorithms.recursive_division import division

FILEPATH = os.getcwd()

WIDTH = 1584
COLUMNS = 99

HEIGHT = 784
ROWS = 49

GREY = (128,128,128)
WHITE = (255,255,255)

stage = 3
rainbow = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (150, 0, 255)]
col1, col2, col3 = rainbow[stage]
count = 6

MODE = 0

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visualiser")
pygame.display.set_icon(pygame.image.load(os.path.join(FILEPATH, 'Fonts', 'icon.png')))

def make_grid():
    grid = []
    gap = WIDTH // COLUMNS
    for i in range(ROWS):
        grid.append([])
        for j in range(COLUMNS):
            node = Nodes(i, j, gap, ROWS, COLUMNS, MODE)
            grid[i].append(node)
    return grid

def draw_grid(win):
    gap = WIDTH // COLUMNS
    for i in range(ROWS):
        pygame.draw.line(win, GREY, (0, i*gap), (WIDTH, i*gap))
    for i in range(COLUMNS):
        pygame.draw.line(win, GREY, (i*gap, 0), (i*gap, WIDTH))

def draw(win, grid, t, w=''):
    for row in grid:
        for node in row:
            if w == 'wil':
                # node.drawwil(win)
                node.draw(win)
            else:
                node.draw(win)
    if t:
        draw_grid(win)
    pygame.display.update()

def get_clicked(pos):
    gap = WIDTH // COLUMNS
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

def main(args):
    global MODE
    if args.mode != 0:
        MODE = 1
    grid = make_grid()
    pygame.init()
    start = None
    end = None
    togglegrid = True

    run = True
    started = False
    sim = False

    while run:
        if not started:
            draw(WIN, grid, togglegrid)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True 

            if pygame.mouse.get_pressed()[0] and not started:
                if sim:
                    start = None
                    end = None
                    grid = make_grid()
                    pygame.display.set_caption("Visualiser: Edit")
                    sim = False
                pos = pygame.mouse.get_pos()
                row, col = get_clicked(pos)
                spot = grid[col][row]
                if not start and spot != end:
                    start = spot
                    start.make_start()
            
                elif not end and spot != start:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start:
                    spot.make_barrier()
                   

            elif pygame.mouse.get_pressed()[2]and not started:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked(pos)
                spot = grid[col][row] 
                spot.reset()

                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and not started and start and end:
                    started = True
                    pygame.display.set_caption("Visualiser: A * Algorithm")
                    astar(lambda : draw(WIN, grid, togglegrid), grid, start, end, MODE)
                    started = False
                    sim = True

                if event.key == pygame.K_d and not started and start and end:
                    started = True
                    pygame.display.set_caption("Visualiser: Dijkstra Algorithm")
                    dijkstra(lambda : draw(WIN, grid, togglegrid), grid, start, end, MODE)
                    started = False
                    sim = True
                    

                if event.key == pygame.K_r and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Recursive backtracking Algorithm")
                    run = backtrack(lambda : draw(WIN, grid, togglegrid), grid, MODE)
                    started = False
                
                if event.key == pygame.K_k and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Kruskal's Algorithm")
                    run = kruskal(lambda : draw(WIN, grid, togglegrid), grid, MODE)
                    started = False
                
                if event.key == pygame.K_s and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Sidewinder Algorithm")
                    run = sidewinder(lambda : draw(WIN, grid, togglegrid), grid, MODE)
                    started = False
                
                if event.key == pygame.K_p and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Prims's Algorithm")
                    run = prims(lambda : draw(WIN, grid, togglegrid), grid, MODE)
                    started = False
                
                if event.key == pygame.K_e and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Ellers's Algorithm")
                    run = ellers(lambda : draw(WIN, grid, togglegrid), grid, MODE)
                    started = False
                
                if event.key == pygame.K_u and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Aldous Broder Algorithm(VERY SLOW!!!)")
                    run = aldous(lambda : draw(WIN, grid, togglegrid), grid, MODE)
                    started = False
                
                if event.key == pygame.K_w and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Wilson's Algorithm")
                    run = wilson(lambda : draw(WIN, grid, togglegrid, 'wil'), grid, MODE)
                    started = False
                
                if event.key == pygame.K_h and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Hunt and Kill algorithm")
                    run = hunt(lambda : draw(WIN, grid, togglegrid), grid, MODE)
                    started = False

                if event.key == pygame.K_g and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Growing Tree algorithm")
                    run = tree(lambda : draw(WIN, grid, togglegrid), grid, MODE)
                    started = False
                
                if event.key == pygame.K_b and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Binary Tree algorithm")
                    run = binary(lambda : draw(WIN, grid, togglegrid), grid, MODE)
                    started = False
                
                if event.key == pygame.K_q and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Recursive Division algorithm")
                    run = division(lambda : draw(WIN, grid, togglegrid), grid, MODE)
                    started = False


                if event.key == pygame.K_BACKSPACE:
                    start = None
                    end = None
                    grid = make_grid()
                    pygame.display.set_caption("Visualiser: Edit")
                    sim = False
                
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Visualiser: Main Page")
                    return False

                if event.key == pygame.K_TAB:
                    togglegrid = not togglegrid

        pygame.display.set_caption("Visualiser: Edit")
    return True

def parse():
    parser = argparse.ArgumentParser(
        description="Starts Algorithm Visualiser!----> Set mode using flag to get step by step visualisation")
    parser.add_argument(
        "-m", help="Mode: 0 for slow 1 for fast(no visualiation during iterations)"
        "(default is slow)", type=int, default=0, dest="mode")
    return parser.parse_args()

def mainpage(args):
    global stage, col1, col2, col3
    Quit = False
    pygame.init()
    invp = False
    invh = False

    background = pygame.image.load(os.path.join(FILEPATH, 'Fonts', 'background.jpg'))
    pygame.display.set_caption("Visualiser: Main Page")
    platbtn = button((0, 0, 0), 175, 500, 200, 100, FILEPATH, (0, 0, 0), text='Start')
    helpbtn = button((0, 0, 0), 385, 500, 200, 100, FILEPATH, (0, 0, 0), text='Help')

    while not Quit:
        WIN.blit(background, (0, 0))
        filltext(invp, platbtn, invh, helpbtn)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                Quit = True
                continue
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if platbtn.isOver(pos):
                        pygame.display.set_caption("Visualiser: Edit")
                        Quit = main(args)
                        invp = False
                    if helpbtn.isOver(pos):
                        pygame.display.set_caption("Visualiser: Help")
                        helppage()
                        invh = False
                if event.button == 4:
                    stage = (stage + 1) % 6
                    col1, col2, col3 = rainbow[stage]
                if event.button == 5:
                    stage = (stage - 1) % 6
                    col1, col2, col3 = rainbow[stage]

            if event.type == pygame.MOUSEMOTION:
                if platbtn.isOver(pos):
                    invp = True
                else:
                    invp = False

                if helpbtn.isOver(pos):
                    invh = True
                else:
                    invh = False
            
        

def filltext(inv, btn, inv2, btn2):
    color = getcolor()
    Maintext = pygame.font.Font(os.path.join(FILEPATH, 'Fonts', 'Milton Keynes.ttf'), 78)
    welcome = Maintext.render("Algorithm Visualiser", True, color)
    s = pygame.Surface((720,700))  
    s.set_alpha(200)                
    s.fill(WHITE)        
    WIN.blit(s, (40,50))

    s = pygame.Surface((740,720))  
    s.set_alpha(10)                
    s.fill(invert(color))           
    WIN.blit(s, (30,40))

    s = pygame.Surface((760,740))  
    s.set_alpha(5)                
    s.fill(invert(color))           
    WIN.blit(s, (20,30))

    s = pygame.Surface((780,760))  
    s.set_alpha(2)                
    s.fill(invert(color))           
    WIN.blit(s, (10,20))

    WIN.blit(welcome, (75,100))

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

    pygame.display.update()


def invert(color):
    a, b, c = color
    return (abs(255 - a), abs(255 - b), abs(255 - c))

def getcolor():
    global col1, col2, col3, count, stage
    count -= 1
    if count == 0:
        count = 6
        if stage == 0:
            if col2 < 255:
                col2 += 1
            if col2 == 255 :
                stage = 1
                col1 = 255
                col2 = 255
                col3 = 0

        elif stage == 1:
            if col1 > 0:
                col1 -= 1
            if col1 == 0:
                col1 = 0
                col2 = 255
                col3 = 0
                stage = 2

        elif stage == 2:
            if col3 < 255:
                col3 +=1
            if col2 > 0:
                col2 -= 1
            if col2 == 0 or col3 == 255:
                stage = 3
                col1 = 0
                col3 = 255
                col2 = 0

        elif stage == 3:
            if col1 < 75:
                col1 += 0.6
            if col3 > 130:
                col3 -= 1
            if col1 == 75 or col3 == 130:
                stage = 4
                col1 = 75
                col3 = 130
                col2 = 0

        elif stage == 4:
            if col3 < 255:
                col3 += 1 
            if col1 < 150:
                col1 += 0.6
            if col1 == 150 or col3 == 255:
                stage = 5
                col1 = 150
                col3 = 255
                col2 = 0

        elif stage == 5:
            if col3 > 0:
                col3 -= 1
            if col1 < 254:
                col1 += 0.41
            if col3 == 0 and col1 <= 255:
                stage = 0
                col1 = 255
                col3 = 0
                col2 = 0

    return (col1, col2, col3)

def helppage():
    pygame.init()
    global stage, col1, col2, col3
    Quit = False
    inv = False
    invh = False
    page = 1

    background = pygame.image.load(os.path.join(FILEPATH, 'Fonts', 'background.jpg'))
    backbtn = button((0, 0, 0), 650, 665, 100, 75, FILEPATH, (0, 0, 0), text='Back', size= 40)
    nextpage = button((0, 0, 0), 660, 350, 75, 100, FILEPATH, (0, 0, 0), text='>')
    prevpage = button((0, 0, 0), 65, 350, 75, 100, FILEPATH, (0, 0, 0), text='<')
    while not Quit:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if backbtn.isOver(pos):
                        pygame.display.set_caption("Visualiser: Main Page")
                        Quit = True
                    if nextpage.isOver(pos):
                        page = 2
                        invh = False
                    if prevpage.isOver(pos):
                        page = 1
                        invh = False
                if event.button == 4:
                    stage = (stage + 1) % 6
                    col1, col2, col3 = rainbow[stage]
                if event.button == 5:
                    stage = (stage - 1) % 6
                    col1, col2, col3 = rainbow[stage]

            if event.type == pygame.MOUSEMOTION:
                if backbtn.isOver(pos):
                    inv = True
                else:
                    inv = False
                if nextpage.isOver(pos) and page == 1:
                    invh = True
                elif prevpage.isOver(pos) and page == 2:
                    invh = True
                else:
                    invh = False

                
        WIN.blit(background, (0, 0))
        fillhelp(inv, backbtn, invh, nextpage, prevpage, page)
    
def fillhelp(inv, btn, inv2, btn2, btn3, page):
    color = getcolor()
    Maintext = pygame.font.Font(os.path.join(FILEPATH, 'Fonts', 'Milton Keynes.ttf'), 40)
    welcome = Maintext.render("Help:", True, color)
    helptext = pygame.font.Font(os.path.join(FILEPATH, 'Fonts', 'Milton Keynes.ttf'), 20)
    lines = []
    lines.append(helptext.render("Different coloured squares represents the following:", True, color))
    lines.append(helptext.render("Color    -> Representation", True, color))
    lines.append(helptext.render("------------------------", True, color))
    lines.append(helptext.render("White    -> Empty Square", True, color))
    lines.append(helptext.render("Black    -> Barrier", True, color))
    lines.append(helptext.render("Red      -> Visited", True, color))
    lines.append(helptext.render("Green    -> To be visited", True, color))
    lines.append(helptext.render("Orange  -> Start Node", True, color))
    lines.append(helptext.render("Teal      -> End Node", True, color))
    lines.append(helptext.render("Purple   -> Shortest Path", True, color))
    lines.append(helptext.render("", True, color))
    lines.append(helptext.render("", True, color))
    lines.append(helptext.render("", True, color))
    lines.append(helptext.render("", True, color))
    lines.append(helptext.render("", True, color))
    lines.append(helptext.render("", True, color))
    lines.append(helptext.render("1)Draw starting and ending nodes", True, color))
    lines.append(helptext.render("2)Draw obstacles as you please or leave it to the pros(maze algorithms) ", True, color))
    lines.append(helptext.render("3)Use a path finding algorithm to find shortest path", True, color))
    line1 = []
    line1.append(helptext.render("Keys:", True, color))
    line1.append(helptext.render("Key                   Function", True, color))
    line1.append(helptext.render("------------------------------", True, color))
    line1.append(helptext.render("Mouse Scroll          -> Change Color(Initial pages only.", True, color))
    line1.append(helptext.render("                         Doesn't work in visualiser)", True, color))
    line1.append(helptext.render("Tab                    -> Switch off or on grid", True, color))
    line1.append(helptext.render("Escape                 -> Previous page", True, color))
    line1.append(helptext.render("Backspace             -> Clear Screen", True, color))
    line1.append(helptext.render("Mouse Right Click    -> Clear node or obstacle", True, color))
    line1.append(helptext.render("Mouse Left Click     -> Add Node or obstacle", True, color))
    line1.append(helptext.render("p                      ->  Draw maze using Prim'salgorithm", True, color))
    line1.append(helptext.render("k                      -> Draw maze using Kruskal's algorithm", True, color))
    line1.append(helptext.render("s                      -> Draw maze using Sidewinder algorithm", True, color))
    line1.append(helptext.render("b                      -> Draw maze using Recursive backtracking algorithm", True, color))
    line1.append(helptext.render("a                      ->  Run A* algorithm", True, color))
    line1.append(helptext.render("d                      ->  Run Dijkstra algorithm", True, color))
    line1.append(helptext.render("", True, color))
    line2 = []
    line2.append(helptext.render("", True, color))
    line2.append(helptext.render("", True, color))
    line2.append(helptext.render("Note:", True, color))
    line2.append(helptext.render("1) Maze algorithms don't work if start and end nodes are mentioned already.", True, color))
    line2.append(helptext.render("2) Path finding algorithms work only if start and end nodes are mentioned.", True, color))
    s = pygame.Surface((720,700))  
    s.set_alpha(150)                
    # s.fill(insvert(color))      
    s.fill(WHITE)            
    WIN.blit(s, (40,50))

    s = pygame.Surface((740,720))  
    s.set_alpha(10)                
    s.fill(invert(color))           
    WIN.blit(s, (30,40))

    s = pygame.Surface((760,740))  
    s.set_alpha(5)                
    s.fill(invert(color))           
    WIN.blit(s, (20,30))

    s = pygame.Surface((780,760))  
    s.set_alpha(2)                
    s.fill(invert(color))           
    WIN.blit(s, (10,20))

    WIN.blit(welcome, (75,50))
    x = 160 
    y = 70
    if page == 1:
        for li in lines:
            y += 25
            WIN.blit(li, (x, y))
    elif page == 2:
        for li in line1:
            y += 25
            WIN.blit(li, (x, y))
        x = 75
        for li in line2:
            y += 25
            WIN.blit(li, (x, y))

    if inv:
        btn.textcolor = invert(color)
        btn.color = color
    else:
        btn.textcolor = color
        btn.color = invert(color)
    btn.draw(WIN, btn.textcolor)

    if page == 1:
        if inv2:
            btn2.textcolor = invert(color)
            btn2.color = color
        else:
            btn2.textcolor = color
            btn2.color = invert(color)
        btn2.draw(WIN, btn2.textcolor)  
    elif page == 2:
        if inv2:
            btn3.textcolor = invert(color)
            btn3.color = color
        else:
            btn3.textcolor = color
            btn3.color = invert(color)
        btn3.draw(WIN, btn3.textcolor) 

    pygame.display.update()


main(parse())