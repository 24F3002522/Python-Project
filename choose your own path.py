import time
import random

print("Loading Adventure...")
time.sleep(2)

name = input("Type your name: ")

print("Welcome", name, "to this adventure!")
time.sleep(1)

answer = input(
    "You are on a dirt road. You can go left or right: "
).lower()

if answer == "left":
    answer = input(
        "You come to a river. Walk around or swim? (walk/swim): "
    ).lower()

    if answer == "swim":
        print("You jump into the river...")
        time.sleep(2)

        if random.choice([True, False]):
            print("You escaped the alligator!")
            treasure = random.randint(50, 200)
            print("You found", treasure, "gold coins. You WIN!")
        else:
            print("An alligator attacked you. You lose!")

    elif answer == "walk":
        print("You start walking around the river...")
        time.sleep(2)

        if random.randint(1, 3) == 1:
            print("You found a village and were rescued. You WIN!")
        else:
            print("You ran out of water and lost.")

    else:
        print("Invalid choice.")

elif answer == "right":
    print("You walk toward the bridge...")
    time.sleep(2)

    answer = input("Cross or go back? (cross/back): ").lower()

    if answer == "cross":
        print("Crossing...")
        time.sleep(2)

        stranger = random.choice(["friendly", "enemy"])

        if stranger == "friendly":
            print("The stranger gives you treasure. You WIN!")
        else:
            print("The stranger robs you. You lose.")

    elif answer == "back":
        print("You went back and got lost.")
    else:
        print("Invalid choice.")

else:
    print("Invalid direction.")

print("\nThanks for playing,", name)