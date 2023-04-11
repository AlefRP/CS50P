import random

def play():
    # Print the game instructions
    print("Let's play Rock-Paper-Scissors!")
    print("The computer will randomly choose one of the three options: rock, paper, or scissors.")
    print("You will enter your choice through the terminal.")
    print("The program will compare the choices and determine the winner.")
    print("The program will display the winner and ask if you want to play again.")
    print()

    # Initialize variables
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    player_choice = input("Enter your choice (rock, paper, or scissors): ")

    # Compare the choices and determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print("You win! Rock beats scissors.")
    elif player_choice == 'paper' and computer_choice == 'rock':
        print("You win! Paper beats rock.")
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print("You win! Scissors beat paper.")
    else:
        print("You lose! " + computer_choice.capitalize() + " beats " + player_choice + ".")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == 'y':
        play()
    else:
        print("Thanks for playing!")

# Start the game
play()