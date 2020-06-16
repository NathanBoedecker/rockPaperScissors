'''
Created on Apr 24, 2020

@author: ITAUser
'''
#import random function
import random

#set variable keepPlaying to true
keepPlaying = True
#while keepPlaying is true
while keepPlaying == True:
    #print welcome statement and rules
    print("Welcome to Rock, Paper, Scissors. The rules are simple. Rock beats Scissors, Scissors beats Paper, Paper beats Rock. Whoever wins the best two out of three games wins. Good luck. To quite press q")
#set computer and play score to 0
def setscore(player, computer):
    computer = 0
    player = 0
    return setscore
#when both scores are less than two 
while (computer < 2 and player < 2):
    #ask for input
    computerChoice = random.randint(1,3)
    1 = "rock"
    2 = "paper"
    3 = "scissors"
    playerChoice = input ("choose (rock, paper, or scissors:")
    playerChoice = playerChoice.lower()
    #if player inputs q
    if(playerChoice == "q" or "Q"):
        keepPlaying = False
    break
if ((playerChoice == "rock" and computerChoice == "rock") or (playerChoice == "scissors" and computerChoice == "scissors") or (playerChoice == "paper" and computerChoice == "paper") or (playerChoice == "gun" and computerChoice == "gun")):
    print("Draw")
    print("player score = " + player.__str__() + "computer score = " + computer.__str__())
elif ((playerChoice == "rock" and computerChoice == "scissors") or (playerChoice == "scissors" and computerChoice == "paper") or (playerChoice == "paper" and computerChoice == "rock") or (playerChoice == "gun" and computerChoice == "rock" or "paper" or "scissors")):
    player = player + 1
    print("player score = " + player.__str__() + "computer score = " + computer.__str__())
elif ((computerChoice == "rock" and playerChoice == "scissors") or (computerChoice == "scissors" and playerChoice == "paper") or (computerChoice == "paper" and playerChoice == "rock") or (computerChoice == "gun" and playerChoice == "rock" or "paper" or "scissors")):
    computer = computer + 1
    print("player score = " + player.__str__() + "computer score = " + computer.__str__())
else:
    print("Invalid input, please try again")
print("Thank you for playing!")
    