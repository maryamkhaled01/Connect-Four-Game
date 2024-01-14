# Game Dimensions
ROW_COUNT = 6
COLUMN_COUNT = 7

# Colors in the game
BLUE = (0,74,173)
BLUE_BORDER = (0,56,132)
BLACK = (0,0,0)
RED = (225,0,0)
RED_BORDER = (190,0,0)
YELLOW = (255,255,0)
YELLOW_BORDER = (255,210,0)
GREY = (150,150,150)
WHITE = (255,255,255)
LIGHT_GREEN = (136,255,85)

# FONTS
F1 = "Courier New"
F2 = "stylus"
F3 = "arialblack"

# Initializing the game dimensions
SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)
WIDTH = COLUMN_COUNT * SQUARESIZE
HEIGHT = (ROW_COUNT+1) * SQUARESIZE

# adding additional space next to the board to display the scores in the screen size
SIZE = (WIDTH + SQUARESIZE*4 , HEIGHT) 

AI_PIECE=2
PLAYER_PIECE = 1

PLAYER = 0
AGENT = 1
