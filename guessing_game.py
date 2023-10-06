#!/usr/bin/python3
#Author: Colin McCoy
#Date: 11/10/2021
#Version: 1.0

from random import randint

upperbound = int(input("Select the upper boundry number: "))
guessCount = int(input("Select the number of guesses: "))
cpuGuess = randint(1, upperbound + 1)

while (guessCount !=0):
    userGuess = int(input("Pick a number between 1 and " + str(upperbound) + ": "))
    guessCount -= 1
    responses =("You correctly guessed the number " + str(userGuess) + "!",
                "Your guess was too high",
                "Your guess was too low",
                "Sorry you have run out of guesses, better luck next time.")
    if (userGuess == cpuGuess):
        print(responses[0])
        break
    elif (userGuess > cpuGuess):
        print(responses[1])
    else:
        print(responses[2])

if (guessCount == 0 and userGuess != cpuGuess):
    print(responses[3])