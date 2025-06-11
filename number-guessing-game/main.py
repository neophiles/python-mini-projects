# CLI Number Guessing Game
# Created by Marc Neil Tagle, June 2025
# For educational purposes

import random as rd

round = 1
while True:
    print(f"Number Guessing Game: Round {round}\n")

    while True:
        try:
            max_num = int(input("Enter maximum range value: "))

            if max_num <= 1:
                print("Invalid input: Must be greater than 1!")
                continue
            
            print(f"Range: (1-{max_num})\n")
            rd_num = rd.randint(1, max_num)
            break
        except:
            print("Invalid input: Not a number!")

    lives = 5
    while lives > 0:
        try:
            guess = int(input("Guess: "))

            if guess not in range(1, max_num+1):
                print("Invalid guess: Out of range!")
                continue

            if guess == rd_num:
                print("You guess it!\n")
                break
            else:
                if guess < rd_num:
                    print("Higher!", end=' ')
                elif guess > rd_num:
                    print("Lower!", end=' ')
                lives -= 1
                print(f"Lives left: {lives}")
        except:
            print("Invalid guess: Not a number!")

    if lives == 0:
        print("Game over!\n")

    while True:
        proceed = input("Go again? (y/n): ").lower()
        if proceed in ['y','n']:
            print("-" * 30)
            break
        print("Invalid response!")
    
    if proceed == 'n':
        print("Thank you for playing!")
        break

    round += 1