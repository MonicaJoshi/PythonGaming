# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# global variables
allowed_attempts = 7
num_range = 100
secret_number = 0
retry_num = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    print ""
    global retry_num
    retry_num = 0
    print "New Game, range is from 0 to " + str(num_range)
    print "Number of remaining guesses is " + str(allowed_attempts)
    global secret_number
    secret_number = random.randint(0, num_range)
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    global allowed_attempts
    allowed_attempts = 7
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    global allowed_attempts
    allowed_attempts = 10
    new_game()
    
def input_guess(guess):
    print ""
    print "Guess was " + guess
    
    # format the input
    guess = int(guess)
    
    # increment the retry count    
    global retry_num   
    retry_num = retry_num + 1

    # guess must be in valid range
    if guess < 0 or guess > num_range:
        print "Input of out range, pick number between 0 - " + str(num_range)
        print "OR reset by clicking one of the range buttons."
        return

    remainder = allowed_attempts - retry_num
    if secret_number < int(guess):
        print "Lower !"
    elif secret_number > int(guess):
        print "Higher !"
    elif secret_number == int(guess):
        print "Correct !"
        new_game()
        return

    # check if can allow more guesses
    if (retry_num >= allowed_attempts) or remainder == 0:
        print "You ran out of guesses. " \
              "The number was " + str(secret_number)
        new_game()
    else:
        print "Number of remaining guesses is " + str(remainder)

# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100]", range100, 200)
frame.add_button("Range is [0, 1000]", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()


