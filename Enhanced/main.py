import random

print("Welcome to ROCK PAPER SCISSORS Game.")
gameCount = 0
while True:
    if (gameCount == 0):
        stinp = input("Start the game?(Y/N): ")
    else:
        stinp = input("Play again?(Y/N): ")
    if (stinp.lower() == "y"):
        rules = [
            "Rule 1: If you choose ROCK, you can defeat scissors and paper can defeat you!\n",
            "Rule 2: If you choose PAPER, you can defeat rock and scissors can defeat you!\n",
            "Rule 3: If you choose SCISSORS, you can defeat paper and rock can defeat you!"
        ]
        if (gameCount == 0):
            print("Please read the rules before playing...\n")
            for rule in rules:
                print(rule)

        userinp = input('\nType "Rock" for choosing ROCK, "Paper" for choosing PAPER and "Scissors" for choosing SCISSORS: ')
        rps = ["Rock", "Paper", "Scissors"]
        compinp = random.choice(rps)
        userinp = userinp.title()

        # Tie
        if (userinp == compinp):
            print(f"\nYour input was {userinp}\nComputer's input was {compinp}\nSo, it's a tie!")

        # Rock defeats scissors
        elif (userinp == "Rock" and compinp == "Scissors"):
            print(f"\nYour input was {userinp}\nComputer's input was {compinp}\nSo, You Won!")

        elif (compinp == "Rock" and userinp == "Scissors"):
            print(f"\nYour input was {userinp}\nComputer's input was {compinp}\nSo, Computer Won!")

        # Paper defeats Rock
        elif (userinp == "Paper" and compinp == "Rock"):
            print(f"\nYour input was {userinp}\nComputer's input was {compinp}\nSo, You Won!")

        elif (compinp == "Paper" and userinp == "Rock"):
            print(f"\nYour input was {userinp}\nComputer's input was {compinp}\nSo, Computer Won!")

        # Scissors defeating Paper
        elif (userinp == "Scissors" and compinp == "Paper"):
            print(f"\nYour input was {userinp}\nComputer's input was {compinp}\nSo, You Won!")

        elif (compinp == "Scissors" and userinp == "Paper"):
            print(f"\nYour input was {userinp}\nComputer's input was {compinp}\nSo, Computer Won!")

        else:
            print("\nInvalid Input, Try again!")
        
        # Played 1 more time so added 1 to the gameCount variable
        gameCount = gameCount + 1
    elif (stinp.lower() == "n"):
        if(gameCount == 0):
            print("Exiting...!")
            break
        else:
            print("Thanks for playing ROCK PAPER SCISSORS.")
            print("Exiting...!")
            break
    else:
        print("Invalid Input, Try again!")
