import random

print("🔥" * 60)
print("🎯 WELCOME TO THE ULTIMATE NUMBER GUESSING CHALLENGE 🎯")
print("💀 Can you outsmart the Random Number Generator?")
print("😎 Let's find out...")
print("🔥" * 60)
print()

top_of_range = input("🎲 Pick the max number (Example: 100): ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("🤦 Bro really picked 0 or less... Try a number bigger than 0 next time.")
        quit()
else:
    print("🚨 That's not even a number, my guy 💀")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

print()
print(f"🤖 I've locked a secret number between 0 and {top_of_range}.")
print("🧠 Time to cook... Good luck!")
print()

while True:
    guesses += 1

    user_guess = input("👉 Drop your guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("💀 Numbers only, chief.")
        continue

    if user_guess == random_number:
        print("\n🎉 SHEEEESH!! YOU COOKED! 🔥")
        print("🏆 Random Number Generator has been defeated.")
        break
    elif user_guess > random_number:
        print("📈 Too high! Bro aimed for the moon 🚀")
    else:
        print("📉 Too low! Aim a little higher 📈")

print()
print("✨ You cracked the code in", guesses, "guesses!")

if guesses == 1:
    print("👑 Nahhh... First try?? You're built different.")
elif guesses <= 5:
    print("😎 W rizz. That was smooth.")
elif guesses <= 10:
    print("👍 Solid performance. We take those.")
else:
    print("💀 That RNG had you fighting for your life.")