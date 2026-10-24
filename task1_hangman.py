
# TASK 1: Hangman Game

import random

# List of 5 predefined words
words = ["apple", "python", "mango", "tiger", "chair"]

# Select a random word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("===== WELCOME TO HANGMAN GAME =====")
print("Guess the hidden word one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

# Main game loop
while incorrect_guesses < max_attempts:

    # Display the word with hidden letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)

    # Check whether the player has guessed the word
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word:", word)
        print("YOU WIN!")
        break

    guess = input("Guess a letter: ").lower().strip()

    # Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter!\n")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in word:
        print("Correct guess!\n")
    else:
        incorrect_guesses += 1
        print("Wrong guess!\n")

# Check whether the player lost
if incorrect_guesses == max_attempts:
    print("Word:", " ".join(word))
    print("GAME OVER! You have used all 6 incorrect guesses.")
    print("The correct word was:", word)
