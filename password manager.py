from cryptography.fernet import Fernet
import time
import random
import string
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    print("Encrypting password...")
    time.sleep(2)

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

    print("Password saved successfully!")
def view():
    print("Decrypting passwords...")
    time.sleep(2)

    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user,
                  "| Password:",
                  fer.decrypt(passw.encode()).decode())
            time.sleep(1)
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))
def add():
    name = input("Account Name: ")

    choice = input("Generate a random password? (yes/no): ").lower()

    if choice == "yes":
        pwd = generate_password()
        print("Generated Password:", pwd)
    else:
        pwd = input("Password: ")

    print("Encrypting password...")
    time.sleep(2)

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

    print("Password saved successfully!")
