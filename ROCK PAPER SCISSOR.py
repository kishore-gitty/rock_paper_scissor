import random
import time
print("shall we begin the rock paper scissor game")
times=int(input("HOW MANY MATCH YOU NEED TO PLAY:"))
score = int(input("how many points you need for each win:"))
count = 0
for i in range(times):
    def choices():
        print("rock")
        print("paper")
        print("scissor")
    options = ['rock','scissor','paper']
    player = None
    computer = random.choice(options)
    player = input("enter a choice:")
    while player.lower() not in options:
        print("enter the correct choice..")
        print(f"here the {player} doesn't exist in the game")
        print("the choices are..")
        choices()
        player = input("enter a choice:")
        if player in options:
            break
        else:
            continue
    print(f"you : {player}")
    print(f"computer : {computer}")
    if computer == player.lower():
        print("match draw!!")
        count +=0
    elif player.lower() == "rock" and computer == "paper":
        print("computer wins!! \n you lost!!")
        count +=0
    elif player.lower() == "rock" and computer == "scissor":
        print("computer lost!! \n you wins!!")
        count +=score
    elif player.lower() == "paper" and computer == "rock":
        print("computer lost!! \n you wins!!")
        count +=score
    elif player.lower() == "scissor" and computer == "paper":
        print("computer lost!! \n you wins!!")
        count +=score
    elif player.lower() == "paper" and computer == "scissor":
        print("computer wins!! \n you lost!!")
        count +=0
    elif player.lower() == "scissor" and computer == "rock":
        print("computer wins!! \n you lost!!")
        count +=0
print(f"congratulations you had won {count} times out of {times*score} times!!")
    
    










