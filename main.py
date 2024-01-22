from tkinter import * 
import random

# constant game variables
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED =  50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "FF00FF"
BACKGROUND_COLOR = "000000"

# define a snake object
class Snake:
    pass

# define a food object
class Food:
    pass

# define a turn function
def next_turn():
    pass

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

# start the game loop
window.mainloop()