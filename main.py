from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

words = ["hero", "public", "again", "extraordinary", "confusion", "better", "explain", "banana"]
hidden_word = words[randrange(len(words))]
guessed_letters = ["_" for i in range(len(hidden_word))]
last_choices = []  # Saves all the previous letters that player chose

for turn in range(10):

    # Prints the round
    print(f"ROUND {turn + 1}")

    # Letter input
    letter = input("Enter a letter: ").strip().lower()
    while not letter.isalpha() or len(letter) != 1 or letter in last_choices:
        letter = input("Enter a letter, please: ").strip().lower()

    # Add letter in history
    last_choices.append(letter)

    # Information about how many times letter exists in the hidden_word
    print(f"The letter '{letter}' exists {hidden_word.count(letter)} times in the hidden word!")

    # Replace underscore in guessed_letters with letter that found
    for i in range(len(hidden_word)):
        if hidden_word[i] == letter:
            guessed_letters[i] = hidden_word[i]

    # Prints the guessing situation
    for char in guessed_letters:
        print(char, end="")
    print()

    # Checks if player wins
    if "_" not in guessed_letters:
        print("Congratulations!!! You've found it!")
        break
else:
    print("You lost. You override the max tries -_-")
