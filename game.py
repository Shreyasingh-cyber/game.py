import random

# List of possible moves
moves = ['rock', 'paper', 'scissors']

def get_computer_choice():
    return random.choice(moves)

def get_player_choice():
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while player_choice not in moves:
        print("Invalid choice. Please choose again.")
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return player_choice

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    while True:
        print("\nRock, Paper, Scissors Game")
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
play_game()
