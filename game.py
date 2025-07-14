import random

def print_header():

    print("=" * 50)
    print("TU Berlin")
    print("Computer science – 2nd Semester")
    print("Number Guessing Game")
    print("=" * 50)
    print()

def choose_difficulty():

    print("Select difficulty level:")
    print("1 - Easy (1–10), 5 attempts")
    print("2 - Medium (1–50), 7 attempts")
    print("3 - Hard (1–100), 10 attempts")

    while True:
        choice = input("Enter 1, 2 or 3: ")
        if choice == '1':
            return 1, 10, 5
        elif choice == '2':
            return 1, 50, 7
        elif choice == '3':
            return 1, 100, 10
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

def play_game():

    print("Welcome to the Number Guessing Game!")
    low, high, max_attempts = choose_difficulty()
    
    number_to_guess = random.randint(low, high)
    attempts_used = 0
    max_score = 100
    score_penalty = max_score // max_attempts

    while attempts_used < max_attempts:
        try:
            guess = int(input(f"Enter a number between {low} and {high}: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        attempts_used += 1

        if guess == number_to_guess:
            final_score = max_score - score_penalty * (attempts_used - 1)
            print(f"Correct! You guessed the number in {attempts_used} attempt(s).")
            print(f"Score: {final_score}")
            break
        elif guess < number_to_guess:
            print("Too low.")
        else:
            print("Too high.")

    else:
        print(f"Out of attempts. The correct number was {number_to_guess}.")
        print("Score: 0")

def main():

    print_header()
    
    while True:
        play_game()
        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()