import random

def get_computer_choice():
    """Randomly selects rock, paper, or scissors for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    """Gets and validates the user's input."""
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")

def determine_winner(user_choice, computer_choice):
    """Determines the winner of the round."""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Plays a single round of Rock Paper Scissors."""
    print("Welcome to Rock Paper Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print(result)

    while True:
        play_again = input("Play again? (yes/no): ").lower()
        if play_again == 'yes':
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            result = determine_winner(user_choice, computer_choice)
            print(result)
        elif play_again == 'no':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    play_game()
    