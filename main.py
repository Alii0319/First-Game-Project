import random

choices = [1, -1, 0]
computer = random.choice(choices)
user_str = input("Enter your command (s for Snake, w for Water, g for Gun): ").lower()
youdict = {"s": 1, "w": -1, "g": 0}
reverse_dict = {1: "Snake", -1: "Water", 0: "Gun"}

if user_str in youdict:
    user = youdict[user_str]

    print(f"You chose {reverse_dict[user]}\nComputer chose {reverse_dict[computer]}")

    if computer == user:
        print("It's a Draw.")
    elif (user == 0 and computer == -1) or (user == 1 and computer == -1) or (user == 0 and computer == 1):
        print("You Win!")
    else:
        print("You Lose!")
else:
    print("Error: Invalid command.")
