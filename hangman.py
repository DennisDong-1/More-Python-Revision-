import random

# Word list (you can expand this)
words = ["python", "hangman", "developer", "openai", "programming", "keyboard"]

# Hangman stages
stages = [
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """
]

def hangman():
    word = random.choice(words)
    word_letters = set(word)
    guessed_letters = set()
    attempts = len(stages) - 1

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0 and word_letters:
        print(stages[attempts])
        print("Word: ", " ".join([letter if letter in guessed_letters else "_" for letter in word]))
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess!")

    # End of game
    if not word_letters:
        print(f"🎉 You guessed the word '{word}' correctly!")
    else:
        print(stages[0])
        print(f"💀 You lost! The word was '{word}'.")

# Run the game
if __name__ == "__main__":
    hangman()
