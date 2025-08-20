import random

print("welcome to number guessing game!")
num=random.randint(1,50)

print("guess the correct number(from 1-50) within 8 attempts▪︎")

attempt=0
max_attempt=8
rem_attempts=max_attempt

while attempt<max_attempt:
    guess=int(input("\n Enter the guessed number: "))
    attempt+=1 
    rem_attempts-=1
    if guess>num:
        print(f"\n Attempt={attempt}")
        print(f"The guessed number is higher, \n remaining {rem_attempts} attempts.")
    elif guess<num:
        print(f"\n Attempt={attempt}")
        print(f"The guessed number is lower, \n  remaining {rem_attempts} attempts.")
    elif guess==num:
        print(f"\n Attempt={attempt}")
        print(f"Yeah!! its {guess}. \n You guessed the correct number in {attempt} attempts!!")
        break
else:
    print(f"Attempts={rem_attempts}, The correct number is {num}")