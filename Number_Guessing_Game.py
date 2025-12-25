#Python Number Guessing Game
import random

lowest_value = int(input("Enter the lowest number: "))        
highest_value = int(input("Enter the highest number: "))
guesses=0                                                       
answer = random.randint(lowest_value,highest_value)
Wanna_Continue =True

while Wanna_Continue:
    guess = (input(f"Guess a number between {lowest_value} and {highest_value}: "))
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_value or guess > highest_value:
            print(f"Select a number within the range of {lowest_value} and {highest_value}")
        
        elif guess < answer:
            print(f"{guess} is too low. Try again!")
        
        elif guess > answer:
            print(f"{guess} is too high. Try Again!")
        
        else:
            print(f"Congratulations! You have guessed the correct number in {guesses} guesses.")
            play_again = input("Do you want to play again?(yes/no): ").lower()
            if play_again == "no":
                Wanna_Continue = False
                print("Thanks for playing! bye!")
            
            
    else:
        print(f"Enter a valid number. Between the given range{lowest_value} and {highest_value}")

