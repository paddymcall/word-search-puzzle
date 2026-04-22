# Constants and Global Variables
LOGFILE = 'LOGFILE'
WORDS_FILE = 'words.txt'
GAME_BOARDS_DIR = 'game_boards/'
WSP = 'IKGA Buddhist Word Search Puzzle'

# Boolean flags
PDFLATEX = False
# SHOW_ANSWERS = True

# Board dimension
ROWS = 12
COLS = 12

# Should we add numbers around the table?
WITH_NUMBERS=False

# Directions allowed for words
NORTH = True
SOUTH = True
EAST = True
WEST = True
DIAGONALS = False

MAXIMAL_NUMBER_OF_TRIES = 800

added_words = []
skipped_words = []
used_positions = {}
used_vector_positions = {}

DIR_OFFSETS = {
    "N": lambda r, c, i: (r - i,     c),
    "S": lambda r, c, i: (r + i,     c),
    "E": lambda r, c, i: (r,         c + i),
    "W": lambda r, c, i: (r,         c - i),
    "NE": lambda r, c, i: (r - i,     c + i),
    "SE": lambda r, c, i: (r + i,     c + i),
    "NW": lambda r, c, i: (r - i,     c - i),
    "SW": lambda r, c, i: (r + i,     c - i),
}
