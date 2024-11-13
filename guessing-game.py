import os
import random
import uuid
os.system("cls")

random_number = random.randint(1, 101)
guess = 0

print("Guess the number game! Press 0 to quit.")



while True: 
        try:
            tries = int(input(f"How many tries do you need: "))
            continue 
        except:
            print("Please use numbers! >:(")
        if tries <= 0:
            print("You have quit the game!")
            exit()
        while guess != random_number and tries >= 1: 
            try:
                guess = int(input("Guess my number: "))

            except Exception as error_code:
                print("Please input a number! ")
                continue

            if guess == random_number: 
                print(f"You found my secret number which was {random_number} with {tries} tries left.")        
                break
            elif guess > random_number:
                print("Too high number! Try again. ")
            elif guess < random_number:
                print("Too low number! Try again. ")

                    

            tries = tries - 1
            print(f"You got {tries} tries left") 

            if tries == 0:
                print(f"You lost the number was {random_number}.")
                break
            
        again = input("Do you want play again? ").upper()
        if again == 'N':
            exit()

                



               














    








