import random

def roll_dice():
    return random.randint(1, 99)

def dice_simulator():
    print("Welcome to the Dice Simulator!")
    while True:
        roll = input("Press Enter to roll the dice or type 'exit' to quit: ")
        if roll.lower() == 'exit':
            print("Thanks for playing!")
            break
        result = roll_dice()
        print(f"You rolled a {result}!")
if __name__ == "__main__":
    dice_simulator()