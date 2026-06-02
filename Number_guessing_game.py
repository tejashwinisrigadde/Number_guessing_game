import random

MAX_NUM = 100
computer = random.randint(0, MAX_NUM)
attempts = 0

while True:
    try:
        user = int(input(f"Guess any number ranging from 0 to {MAX_NUM}: "))

        if user < 0 or user > MAX_NUM:
            print(f"❌ Please enter a number from 0 to {MAX_NUM}")
            continue

        attempts += 1

        if computer == user:
            print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
            break
        elif computer > user:
            print("📉 You guessed low.\nTry again! 🎯")
        else:
            print("📈 You guessed high.\nTry again! 🚀")

    except ValueError:
        print("❌ Enter a valid integer.")