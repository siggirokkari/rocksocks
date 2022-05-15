import random

player_score = 0
comp_score = 0

choice = ["rock", "paper", "scissors"]

while True:
    player_input = input("Type Rock/Paper/Scissors or Q to quit? ").lower()
    
    if player_input == "q":
        break

    if player_input not in choice:
        continue

    com_choice = choice[random.randint(0,2)]

    if player_input == "rock" and com_choice == "scissors":
        print("Computer chose:", com_choice, "You won!")
        player_score += 1

    elif player_input == "paper" and com_choice == "rock":
        print("Computer chose:", com_choice, "You won!")
        player_score += 1
    
    elif player_input == "scissors" and com_choice == "paper":
        print("Computer chose:", com_choice, "You won!")
        player_score +=1
    
    elif player_input == com_choice:
        print("Computer chose:", com_choice, "It's a tie!")
    
    else:
        print("Computer chose:", com_choice, "You lost!")
        comp_score += 1

print("Game over!")
print("You scored:", player_score,)
print("Computer scored:", comp_score)
