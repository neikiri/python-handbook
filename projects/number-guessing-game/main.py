"""Number Guessing Game

A simple command-line game where the player tries to guess a random number.
"""

import random


def get_user_guess():
    """Get a valid number guess from the user."""
    while True:
        user_input = input("Enter your guess (1-100) or 'q' to quit: ").strip()
        
        if user_input.lower() == 'q':
            return None
        
        try:
            guess = int(user_input)
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")


def play_round():
    """Play a single round of the game."""
    secret_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    
    print("\nI'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")
    
    while attempts < max_attempts:
        guess = get_user_guess()
        
        if guess is None:
            print("Thanks for playing!")
            return False
        
        attempts += 1
        
        if guess == secret_number:
            print(f"\nCongratulations! You guessed the number in {attempts} attempts!")
            return True
        elif guess < secret_number:
            print(f"Too low! ({attempts}/{max_attempts} attempts used)")
        else:
            print(f"Too high! ({attempts}/{max_attempts} attempts used)")
    
    print(f"\nOut of attempts! The number was {secret_number}.")
    return False


def main():
    """Main function to run the number guessing game."""
    print("=" * 50)
    print("   Number Guessing Game")
    print("=" * 50)
    print("Try to guess the number I'm thinking of!")
    print()
    
    wins = 0
    losses = 0
    
    while True:
        result = play_round()
        
        if result:
            wins += 1
        else:
            losses += 1
        
        print(f"\nScore: Wins: {wins} | Losses: {losses}")
        
        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again not in ('y', 'yes'):
            break
    
    print("\nThanks for playing!")
    print(f"Final Score: Wins: {wins} | Losses: {losses}")


if __name__ == "__main__":
    main()