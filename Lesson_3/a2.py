# 1) Import the `random` module to let the computer make a random choice.
import random
# 2) Start an infinite loop using `while True` so the game can repeat for multiple rounds.
while True:
   user_action = input("Pick your choice: Rock, Paper or scissors:  ")
# 3) Take the user's choice as input and store it in `user_action`.
#    (Expected inputs: "rock", "paper", or "scissors".)
# 4) Create a list `possible_actions` containing the three valid moves.
possible_actions = ["rock", "paper", "scissors"]
# 5) Use `random.choice(possible_actions)` to randomly select the computer’s move
#    and store it in `computer_action`.
    computer_action = random.choice (possible_actions)
# 6) Display both choices (user and computer) using an f-string.
    print (f"\n You chose: {user_action}, computer chose: {computer_action}")
# 7) Compare `user_action` and `computer_action` to decide the result:
#    a) If both are the same, print that it’s a tie.
#    b) Else if the user chose "rock":
#       i) If computer chose "scissors", user wins.
#       ii) Otherwise, user loses (computer chose "paper").
#    c) Else if the user chose "paper":
#       i) If computer chose "rock", user wins.
#       ii) Otherwise, user loses (computer chose "scissors").
#    d) Else if the user chose "scissors":
#       i) If computer chose "paper", user wins.
#       ii) Otherwise, user loses (computer chose "rock").
    if user_action == computer_action:
         print ("Tie")
    elif user_action == 'rock':
        if computer_action == 'scissors':
           print ("You win")
        else:
           print ("You lose")
    elif user_action == 'paper':
        if computer_action == 'rock':
            print ("You win")
        else:
           print ("You lose")
    elif user_action == 'scissors':
        if  computer_action == 'paper':
            print ("You win")
        else:
           print ("You lose")
# 8) After showing the result, ask the user if they want to play again
#    and store the input in `play_again`.
    play_again = input("Would you like to play again? (Y/N): ")
# 9) If `play_again` is not "y", stop the game using `break`.
#    Otherwise, the loop continues and a new round starts.
    if play_again != 'y':
        break