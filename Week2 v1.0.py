__author__ = 'common'

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random

"""global variables:
        triesRemaining = How many tries the user has left
        gameType = 100 for 1-100 game / 1000 for 1-1000 game"""

#avoid repeated code by creating printing function    
def game_opener():
    print "Guess a number between 1 and " + str(gameType)
    print "Guesses left", triesRemaining
    print "---------------------------------------"
    print "\n"    

# helper function to start and restart the game
def new_game():
    # initialize global variables for very first game.
    global secret_number
    global triesRemaining
    global gameType
    gameType = 100
    triesRemaining = 7
    secret_number = int(random.randrange(0,100))
    game_opener()

def range100():
    # button that changes the range to [0,100) and starts a new game
    global secret_number
    global triesRemaining
    global gameType
    gameType = 100 #helper variable to begin next game with same type
    triesRemaining = 7
    secret_number = int(random.randrange(0,100))
    game_opener()


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global secret_number
    global triesRemaining
    global gameType
    gameType = 1000 #helper variable to begin next game with same type
    triesRemaining = 10
    secret_number = int(random.randrange(0,1000))
    game_opener()


def input_guess(guess):
    global secret_number
    global triesRemaining
    global gameType
    print "Guess was:", int(guess)
    if triesRemaining >= 1:
        if int(guess) > secret_number:
            #decrement remaining guesses by 1
            triesRemaining -= 1
            #print lower and remaining guesses
            print "Lower!"
            print "Guesses left", triesRemaining
            print "\n"
        elif int(guess) < secret_number:
            #decrement the remaining guesses by 1
            triesRemaining -= 1
            #print out higher and remaining guesses
            print "Higher!"
            print "Guesses left", triesRemaining
            print "\n"
        else:
            print "You are correct!"
            print "\n"
            if gameType == 100: #checks gameType and calls its function
                range100()
            else:
                range1000()
    else:
        print "No more guesses, game over!"
        print "=( =( =( =( =("
        print "\n"
        if gameType == 100:
            range100()
        else:
            range1000()




# create frame
frame = simplegui.create_frame("Guess the number!", 300, 300)

# register event handlers for control elements and start frame
button100 = frame.add_button("New game 1-100", range100, 200)
button1000 = frame.add_button("New game 1-1000", range1000, 200)
guess = frame.add_input("Enter your guess", input_guess, 100)

# call new_game
new_game()


# always remember to check your completed program against the grading rubric
