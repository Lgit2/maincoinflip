import random

def coin_flip():
    """Simulates a coin flip."""
    return random.choice(['heads', 'tails'])

def main():
    print("Welcome to the Coin Flip Game!")
    print("I will flip a coin, and you'll guess heads or tails.")
    print()

    while True:
        user_guess = input("Enter your guess (heads or tails): ").lower()
        if user_guess not in ['heads', 'tails']:
            print("Invalid input. Please enter 'heads' or 'tails'.")
            continue
        
        computer_choice = coin_flip()
        print("Flipping the coin...")
        print(f"The coin shows: {computer_choice.capitalize()}")

        if user_guess == computer_choice:
            print("Congratulations! You guessed correctly.")
        else:
            print("Oops! You guessed incorrectly.")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print()

if __name__ == "__main__":
    main()
