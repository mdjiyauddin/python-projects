######### 

#########  WORKFLOW OF THE GAME PROJECT     #########
# first input from user 
# computer generates random number
# result is compared with user input

#case 1: user input is correct
#  Rock - Rock  -> Tie
# Rock - Paper -> Computer wins
# Rock - Scissors -> User wins

# case 2 Paper
# Paper - Paper -> Tie
# Paper - Rock -> User wins
# Paper - Scissors -> Computer wins

# case 3 Scissors
# Scissors - Scissors -> Tie
# Scissors - Rock -> Computer wins
# Scissors - Paper -> User wins

########################################################

import random 

item_list = ["Rock", "Paper", "Scissors"]

user_choise = input("Enter your choise (Rock, Paper, Scissors): ")
computer_choise = random.choice(item_list)

print(f"User choise is : {user_choise}, Computer choise is : {computer_choise}")

# user choices nad computer choices............................

if user_choise == computer_choise:
    print("Both chooses same : match Tie")

elif user_choise == "Rock":
    if computer_choise == "Paper":
        print("Computer wins")
    else:
        print("You win")

elif user_choise == "Paper":
    if computer_choise == "Scissors":
        print("Scissors cut the Paper , Computer win")
    else:
        print("Paper covers rock, You win")

elif user_choise == "Scissors":
    if computer_choise == "Paper":
        print("Scissors cuts paper , You win")
    else:
        print("Rock smashes scissors , Computer win")
