import random

# Computer randomly chooses 1 (Snake), -1 (Water), or 0 (Gun)
computer = random.choice([1, -1, 0])

# Take user input
yourStr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Mapping user input to values
yourDict = {'s': 1, 'w': -1, 'g': 0}
revDict = {1: 'Snake', -1: 'Water', 0: 'Gun'}

# Check if input is valid
if yourStr not in yourDict:
    print("Invalid input! Please enter s, w, or g.")
else:
    you = yourDict[yourStr]

    # Show choices
    print(f"Computer chose: {revDict[computer]}")
    print(f"You chose: {revDict[you]}")

    # Determine result
    if computer == you:
        print("Match DRAW!")
    elif (computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1):
        print("You Lose!")
    else:
        print("You Win!")
