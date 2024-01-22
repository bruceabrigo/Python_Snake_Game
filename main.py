from tkinter import * 
import random

# constant game variables
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED =  50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF00FF"
BACKGROUND_COLOR = "#000000"

# define a snake class
class Snake:
    
    # define the snake constructor
    def __init__(self):
        # snake body constuctor should take in body_parts, coordinates, and squars
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # generate coordinates list with a for loop
        # start the for loop from 0 to the length of BODY_PARTS variable
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0]) # start the snake's coordinates in the top left corner of x=0, y=0. These coordinates will be appended to the coordinates constructor

        # generate the squares list with another for loop
        for x, y in self.coordinates:
            # (starting corner, starting corner)
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square) # append the square calculator to the squre list

# define a food class
class Food:
    
    # define the snake constructor
    def __init__(self):
        # ensure food spawns at random x and y coordinates
        # x and y math explained (start range at 0, WIDTH/HEIGHT divided by GAMESPACE = 14. Leaving 14 possible random spots on the board)
        # multiplying by space size will convert the randomizer to select random pixels
        # ensure random operator is not using a float vairable by using int operand
        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE

        # food coordinates should take a list of x and y
        self.coordinates = [x, y]

        # generate food to the canvas
        # (starting corner, starting corner, ending corner, ending corner, fill color, tag)
        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

# define a turn function
# next turn function will take snake, and food as paremeters
def next_turn(snake, food):
    
    x, y = snake.coordinates[0] # head of the snake

    # generate conditonals to direct the snake 
    if direction == "up":
        y -= SPACE_SIZE # will move snake one space up
    elif direction == "down":
        y += SPACE_SIZE # will move snake one space down
    elif direction == "left":
        x -= SPACE_SIZE # will move snake one space to the left
    elif direction == "right":
        x += SPACE_SIZE # will move snake one space to the rightdsss

    snake.coordinates.insert(0, (x, y))
    
    # generate new graphic for the head of the snake
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    # update new snake squares
    snake.squares.insert(0, square)

    # call the next turn function again
    window.after(SPEED, next_turn, snake, food)

# deifne a direction function
# direction function should include a new direction parameter
def change_direction(new_direction):
    pass

# define a collision dectection funciton
def check_collisions():
    pass

# define a game_over function
def game_over():
    pass

# create a gui window
window = Tk()
window.title('Slinky Snek')
window.resizable(False, False)

# define non-constant game variables 
score = 0 # start game with a score of 0
direction = 'down' # game should start with snake moving down

# define game label
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

# make a game canvas
# game canvas should take in window, as well as our game constants for background color, game height and width.
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# center the window to the screen 
window.update()

# we can ensure the window is centered the the screen by taking in the screen window info 
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# calculate the x axis
# window geometry cannot use floats
# we must specifiy x and y variables as strict integers
x = int((screen_width/2) - (window_width/2))
# calculate the y axis
y = int((screen_height/2) - (window_height/2))

# utilize window geometry to center window
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# define/call our snake and food objects
snake = Snake()
food = Food()

# define/call next turn objects
# call snake and food objects for our parameters
next_turn(snake, food)

# start the game loop
window.mainloop()