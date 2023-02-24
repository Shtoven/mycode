import requests
import time
import pyfiglet
from random import randint

# Generate a random Pokemon
pokemon_id = randint(1, 151)
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
pokemon = response.json()

# Display the Pokemon's name and ASCII art
print(f"A WILD {pokemon['name'].capitalize()} APPEARED!")
pokemon_ascii = pyfiglet.figlet_format(pokemon['name'].capitalize())
print(pokemon_ascii)(p

# Play Rock Paper Scissors
name = input("What's your name? ")
print("Hey, " + name + ", are you ready for the tournament?")
time.sleep(2)
print("I will take that as a yes. Let's get started!")
time.sleep(1)
print("The name of the game is Rock, Paper, Scissors. Best two out of three, wins!")

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False
playerscore= 0
compscore= 0

while playerscore < 2 and compscore <2:
    #set player to True
    player = input("Rock, Paper, Scissors?").capitalize()
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "Smothers you with the paper...Leaving your rock a shell of its former self. unable to effectivly bludgeon scissors for the round. Try again")
            compscore +=1 
        else:
            print("You win!", name, "You smashed the scissors untill they were an unrecognizable ball of cheaply produced metal and plastic. You also managed to break a few of the computers fingers in the proccess, I hope that was an accident.", player)
            playerscore += 1
    elif player == "Paper":

        if computer == "Scissors":
            print("You lose!", computer, "cut you down. While sliced in half, the two remaining peices ran back into the fight.  This went even worse than before.", name +".")
            compscore +=1
        else:
            print("You win!", name, "Draped the rock in an anti-rock coating, which they tactically applied to the paper beforehand.")
            playerscore +=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "Beat you to a pulp. While pulp is acceptable in Orange Juice, scissors should NEVER be considered as an acceptible replacement for O.J.")
            compscore +=1
        else:
            print("You win!", name, "cut a vital component of the extremely frail paper. Leaving it mortally wounded.")
            playerscore +=1
    else:
        print("Case sensitive.  I forgot how to do the '()' lower thing!")
    #player was set to True, but we want it to be False so the loop continues  player = False
    computer = t[randint(0,2)]

# after while loop ends, check if the player had a winning score
if playerscore >= 2:
    print("You won!  Here is a sweeeet Badge.  Post it on your Linkedin or somthing idk.")
else:
    print("You lost!")
