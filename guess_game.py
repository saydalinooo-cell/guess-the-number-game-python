# 🎮 Guess The Number Game
# Author: Dodo
# Description:
# A simple Python guessing game with score, timer, and limited attempts.
import random
import time

print("🎮 Welcome to Guess The Number Game! 🎮")
print("I am thinking of a number between 1 and 100 🤔")
# 🎯 Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)
attempts = 0
max_attempts = 10
score = 100

start_time = time.time()

while attempts < max_attempts:
    try:
        guess = int(input("\n👉 Enter your guess: "))
    except ValueError:
        print("❌ Please enter a valid number!")
        continue

    attempts += 1
    score -= 10

    if guess < number_to_guess:
        print("📉 Too low! Try again.")
    elif guess > number_to_guess:
        print("📈 Too high! Try again.")
    else:
        end_time = time.time()
        total_time = round(end_time - start_time, 2)

        print("\n🎉 CONGRATULATIONS! 🎉")
        print(f"✅ You guessed the number: {number_to_guess}")
        print(f"🔢 Attempts used: {attempts}")
        print(f"⏱️ Time taken: {total_time} seconds")
        print(f"🏆 Your score: {score}")
        break

else:
    print("\n💥 GAME OVER 💥")
    print(f"❌ The correct number was: {number_to_guess}")
    print("😢 Better luck next time!")

print("\n🎯 Thanks for playing Guess The Number!")
