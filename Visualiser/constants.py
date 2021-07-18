# --------------------------------------------------
# Colours
# --------------------------------------------------

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

# --------------------------------------------------
# DIMENTIONS
# --------------------------------------------------

WIDTH = 1584
COLUMNS = 99

HEIGHT = 784
ROWS = 49 

MAZE_ABSOLUTE_ROWS, MAZE_ABSOLUTE_COLUMNS = 24, 49

# --------------------------------------------------
# SORTING LINE DIMENTIONS
# --------------------------------------------------

LINE_WIDTH = 1584/256
LINE_HEIGHT = 784/256

import os 
FILEPATH = os.getcwd()
ICON = os.path.join(FILEPATH, 'Fonts', 'icon.png')
HELP1 = os.path.join(FILEPATH, 'Fonts', 'Help1.png')
HELP2 = os.path.join(FILEPATH, 'Fonts', 'Help2.png')