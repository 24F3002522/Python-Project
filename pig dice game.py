import random
import time


def roll():
    return random.randint(1, 6)


print("=" * 50)
print("WELCOME TO THE PIG DICE GAME")
print("=" * 50)
time.sleep(1)

# Get number of players
while True:
    players = input("Enter the number of players (2 - 4): ")

    if players.isdigit():
        players = int(players)

        if 2 <= players <= 4:
            break
        else:
            print("Number must be between 2 and 4.\n")
    else:
        print("Invalid input! Enter a number.\n")

max_score = 50
player_scores = [0] * players

print("\nFirst player to reach 50 points wins!")
time.sleep(2)

# Main Game Loop
while max(player_scores) < max_score:

    for player_idx in range(players):

        print("\n" + "=" * 50)
        print(f"Player {player_idx + 1}'s Turn")
        print("=" * 50)
        print(f"Total Score: {player_scores[player_idx]}")
        time.sleep(1)

        print("Get Ready...")
        for i in range(3, 0, -1):
            print(i)
            time.sleep(0.7)

        current_score = 0

        while True:

            should_roll = input("\nRoll the dice? (y/n): ").lower()

            if should_roll != "y":
                break

            print("Rolling", end="", flush=True)

            for _ in range(3):
                print(".", end="", flush=True)
                time.sleep(0.5)

            value = roll()

            print(f"\nYou rolled a {value}!")

            if value == 1:
                print("You rolled a 1.")
                print("Turn Over! You lose the points earned this turn.")
                current_score = 0
                time.sleep(2)
                break

            current_score += value

            print(f"Current Turn Score: {current_score}")
            print(f"Total if you stop now: {player_scores[player_idx] + current_score}")

        player_scores[player_idx] += current_score

        print("\nScoreboard")
        print("-" * 25)

        for i, score in enumerate(player_scores):
            print(f"Player {i + 1}: {score}")

        time.sleep(2)

        if player_scores[player_idx] >= max_score:
            break

# Winner
winner = player_scores.index(max(player_scores))

print("\n" + "=" * 50)
time.sleep(1)
print("GAME OVER")
time.sleep(1)
print(f"\nPlayer {winner + 1} WINS!")
print(f"Final Score: {player_scores[winner]}")
print("=" * 50)