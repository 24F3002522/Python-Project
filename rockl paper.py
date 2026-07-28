import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

emoji = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

while True:
    user_input = input("Type 🪨 Rock / 📄 Paper / ✂️ Scissors or ❌ Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        print("⚠️ Invalid choice! Try again.")
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2

    computer_pick = options[random_number]

    print(f"🤖 Computer picked {emoji[computer_pick]} {computer_pick.title()}.")

    if user_input == "rock" and computer_pick == "scissors":
        print(f"🎉 You picked {emoji[user_input]} Rock.")
        print("🔥 You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print(f"🎉 You picked {emoji[user_input]} Paper.")
        print("🔥 You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print(f"🎉 You picked {emoji[user_input]} Scissors.")
        print("🔥 You won!")
        user_wins += 1

    else:
        print(f"😢 You picked {emoji[user_input]} {user_input.title()}.")
        print("💀 You lost!")
        computer_wins += 1

print("\n🏆 Final Score")
print("🎮 You won", user_wins, "times.")
print("🤖 Computer won", computer_wins, "times.")
print("👋 Goodbye!")