import random

Options = ["rock", "paper", "scissor"]
Computer = random.choice(Options)
Player = None
Wanna_Continue = True

while Wanna_Continue:
    Player = input("Choose Rock, Paper or Scissor: ").lower()
    if Player in Options:
                print(f"Computer chose: {Computer}")
                print(f"You chose: {Player}")
                if Player == Computer:
                    print("It's a tie!")
                
                elif Player == "rock" and Computer == "Scissor":
                    print("You won! Rock smashes Scissor")
                
                elif Player == "paper" and Computer == "Rock":
                    print("You won! Paper covers Rock")
                
                elif Player ==  "scissor" and Computer == "Paper":
                    print("You won! Scissor cuts Paper")
                
                else:
                    print(f"You lost! {Computer} beats {Player}")   

    else:
            print("Invalid choice! Please choose rock, paper or scissor.")

    Wanna_Continue = input("Do you want to play again?(yes/no):").lower()
    if Wanna_Continue == "no":
            Wanna_Continue = False
            print("Thanks for playing! bye!")
