import time

print("🔥" * 60)
print("💻🧠      WELCOME TO THE ULTIMATE COMPUTER QUIZ      🧠💻")
print("🔥" * 60)
print("😎 Test your Computer IQ...")
print("🤖 CPU? GPU? RAM? PSU?")
print("💀 Let's see if you're a Certified Tech Rizzler!")
print()

print("⏳ Booting Quiz...")
for i in [3, 2, 1]:
    print(f"⌛ {i}...")
    time.sleep(0.3)

print("🚀 SYSTEM ONLINE!\n")

playing = input("🎮 Do you want to play? (yes/no): ").lower()

if playing != "yes":
    print("😭 Maybe next time, NPC!")
    quit()

print("\n🎉 Let's Go! The Tech Gods Are Watching You .... 👀\n")

score = 0

# ------------------ Question 1 ------------------

print("📝 Question 1/4")
answer = input("💻 What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("✅ Correct! +1000 Aura 🌟\n")
    score += 1
else:
    print("❌ Incorrect! CPU = Central Processing Unit 💀\n")

# ------------------ Question 2 ------------------

print("📝 Question 2/4")
answer = input("🎮 What does GPU stand for? ").lower()

if answer == "graphics processing unit":
    print("✅ Correct! W Rizz 😎\n")
    score += 1
else:
    print("❌ Incorrect! GPU = Graphics Processing Unit 💀\n")

# ------------------ Question 3 ------------------

print("📝 Question 3/4")
answer = input("⚡ What does RAM stand for? ").lower()

if answer == "random access memory":
    print("✅ Correct! Sigma Grindset 📈\n")
    score += 1
else:
    print("❌ Incorrect! RAM = Random Access Memory 💀\n")

# ------------------ Question 4 ------------------

print("📝 Question 4/4")
answer = input("🔌 What does PSU stand for? ").lower()
if answer == "power supply":
    print("✅ Correct! Infinite Aura Achieved 🔥\n")
    score += 1
else:
    print("❌ Incorrect! PSU = Power Supply 💀\n")

# ------------------ Final Score ------------------

percentage = (score / 4) * 100

print("\n" + "🏆" * 20)
print("🎯 QUIZ COMPLETE!")
print("🏆" * 20)

print(f"✅ Correct Answers : {score}/4")
print(f"📊 Score : {percentage:.0f}%\n")

# ------------------ Rank ------------------

if score == 4:
    print("👑 LEGENDARY TECH RIZZLER 👑")
    print("🔥 +999999 Aura")
    print("🗿 Sigma Level: MAX")
    print("💯 Bro owns the motherboard.")
    print("🚀 Intel wants to hire you!")

elif score == 3:
    print("😎 W RIZZ PROGRAMMER")
    print("✨ +500 Aura")
    print("💻 You're farming Aura every compile.")
    print("📈 Almost Sigma.")

elif score == 2:
    print("🙂 Average NPC Coder")
    print("📚 +100 Aura")
    print("⚡ Touch VS Code a little more.")

elif score == 1:
    print("💀 Lost all your Aura")
    print("-1000 Aura")
    print("🤡 The Compiler is laughing at you.")

else:
    print("☠️ BRO IS THE FINAL NPC ☠️")
    print("-999999 Aura")
    print("🚫 Error 404: Computer Knowledge Not Found.")
    print("🪦 Even Windows XP is disappointed.")

print("\n❤️ Thanks for playing!")
print("🎮 GG! See you in the next quiz.")