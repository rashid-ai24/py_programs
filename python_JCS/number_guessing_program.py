
import random

while True:
    print("Welcome to number guessing game!")
    num = random.randint(1, 50)

    print("Guess the correct number (from 1-50) within 8 attempts▪︎")

    attempt = 0
    max_attempt = 8
    rem_attempts = max_attempt

    while attempt < max_attempt:
        try:
            guess = int(input("\nEnter the guessed number: "))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        attempt += 1
        rem_attempts -= 1

        if guess > num:
            print(f"\nAttempt={attempt}")
            print(f"The guessed number is higher, \nremaining {rem_attempts} attempts.")
        elif guess < num:
            print(f"\nAttempt={attempt}")
            print(f"The guessed number is lower, \nremaining {rem_attempts} attempts.")
        else:
            print(f"\nAttempt={attempt}")
            print(f"Yeah!! it's {guess}. \nYou guessed the correct number in {attempt} attempts!!")
            break
    else:
        print(f"Attempts={attempt}, The correct number is {num}")
        
    play_again = input("\nDo you want to play again? (yes/no): \n").lower()
    if play_again != 'yes':
        print("👋 Thanks for playing! Bye!")
        break
