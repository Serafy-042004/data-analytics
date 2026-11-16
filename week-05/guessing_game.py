
import time

number_pool = list(range(1, 21))

for i in range(len(number_pool) - 1, 0, -1):
    j = time.time_ns() % (i + 1)
    number_pool[i], number_pool[j] = number_pool[j], number_pool[i]

secret_number = number_pool[0]

guesses = []
guessed_numbers = set()
guess_count = 0

print("Welcome to the Guessing Game!")
print("Guess a number between 1 and 20.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        guess_count += 1

        guesses.append(guess)
        guessed_numbers.add(guess)

        if guess < secret_number:
            print("Higher!")

        elif guess > secret_number:
            print("Lower!")

        else:
            print("Correct! You guessed it!")
            break

    except ValueError:
        print("Please enter a valid number.")

print(f"\nYou got it in {guess_count} guesses!")
print(f"Your guesses were: {guesses}")

if guess_count < 5:
    print("Awesome! You're a great guesser!")
