import random as rd

TRY = True
while TRY:
    user_action = input("Enter a choice (Rock, Paper, Scissors): ")
    list_actions = ["rock", "paper", "scissors"]
    computer_action = rd.choice(list_actions)
    print(f"You chose {user_action.capitalize()}, computer action {computer_action.capitalize()}.\n")
    
    
    # handle logic
    if user_action == computer_action:
        print(f"Both players selected {user_action.capitalize()}. It's Tie")
    elif user_action == "rock":
        if computer_action == "scissors":
            print(f"Rock smashes Scissors! You Win!")
        else:
            print(f"Paper covers Rock! You Lose!")
    elif user_action == "paper":
        if user_action == "rock":
            print(f"Paper covers Rock! You Win!")
        else:
            print(f"Scissors cuts Paper! You Lose!")
    elif user_action == "scissors":
        if user_action == "paper":
            print(f"Scissors cuts Paper! You Win!")
        else:
            print(f"Rock smashes Scissors! You Lose!")
            
    play_again = input("Play Again: (Y / N): ".upper())
    if play_again.capitalize() != "Y":
        break
