import random

def get_choices():
    player_choice = input("enter a choice(rock,paper,scissors) : ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice,"computer": computer_choice}
    return choices

def check_win(player, computer):
    print("you chose " + player + ", computer chose " + computer)
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "rock will smash the scissors! You Won!"
        elif computer == "paper":
            return "paper covers rock! You Lose."
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock! You Won."
        elif computer == "scissors":
            return "scissors will cut the paper! You Lose"
    elif player == "scissors":
        if computer == "paper":
            return "scissors will cut the paper! You Won!"
        elif computer == "rock":
            return "rock will smash the scissors! You Lose!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)