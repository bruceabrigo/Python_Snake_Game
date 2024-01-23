from tkinter import * 
import random

# constant game variables
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 30
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
    # coord[x coord]
    if x == food.coordinates[0] and y == food.coordinates[1]: # this means the snake and food are overlapping

        global score

        score += 1

        label.config(text='score:{}'.format(score)) # add to score if snake is in contact with food

        canvas.delete("food") # delete the existing food object on contact

        food = Food() # create new food object after deleting old food object on contact
    
    else: # only delete last body part of our snake if we did not eat a food object

        # before updating next turn delete last body part of the snake
        del snake.coordinates[-1] # delete the last body part at the last index of our coordinates

        # update the canvas
        canvas.delete(snake.squares[-1]) # delete the snake from the last index for our canvas coordinates
        del snake.squares[-1]

    # generate boolean conditonal to check for collission
    if check_collisions(snake):
        game_over() # call game over function on wall collission

    else:
        # call the next turn function again
        window.after(SPEED, next_turn, snake, food)

# deifne a direction function
# direction function should include a new direction parameter
def change_direction(new_direction):
    
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction
    
# define a collision dectection funciton
# collission should take in snake class as a paremeter
def check_collisions(snake):
    
    # unpack head of the snake
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH: # conditional to check contact with left or right walls
        return True
    elif y < 0 or y >= GAME_HEIGHT: # conditional to check contact with top or bottom walls
        return True
    
    # conditional to check of the snake comes into contact with itself
    # we can do so by using a for lo
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]: # if the range from tail(body_part[0] and head(body_part[1]))
            print('GAME OVER')
            return True # return true
# define a game_over function
# Define play_again_button as a global variable
play_again_button = None

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), text="GAME OVER", fill='red', tag='game_over')

    # Create a Play Again button
    global play_again_button
    global game_over_message
    play_again_button = Button(window, text="Play Again", font=('consolas', 20), command=reset_game)
    game_over_message = canvas.create_window(canvas.winfo_width()/2, canvas.winfo_height()/2 + 100, window=play_again_button, tag='play again')

# create a reset game function
def reset_game():
    canvas.delete('game_over') # when this function is called remove the game over text via the game_over tag

    if play_again_button: # if there is a play button
        play_again_button.destroy() # destroy the canvas for the button if the reset_game func is called

    # Reset game variables
    global score, direction
    score = 0
    direction = 'down'

    # Update score label
    label.config(text='Score: {}'.format(score))

    # Create new snake and food objects
    snake = Snake()
    food = Food()

    # Start the game loop again
    next_turn(snake, food)


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

# find keys to control snake
window.bind('<KeyPress-a>', lambda event: change_direction('left'))
window.bind('<KeyPress-d>', lambda event: change_direction('right'))
window.bind('<KeyPress-w>', lambda event: change_direction('up'))
window.bind('<KeyPress-s>', lambda event: change_direction('down'))

# define/call our snake and food objects
snake = Snake()
food = Food()

# define/call next turn objects
# call snake and food objects for our parameters
next_turn(snake, food)

# start the game loop
window.mainloop()