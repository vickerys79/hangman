# Hangman Game

This is a simple Hangman game implemented in Python using the Tkinter library for the graphical user interface.

## How to Play

1. Run the `hangman_game.py` file to start the game.
2. The game will choose a random word, and you have to guess it by entering letters.
3. You can input a letter by typing it in the "Enter a letter:" box and pressing the "Guess" button or hitting Enter.
4. The Hangman figure will be drawn based on your incorrect guesses.
5. The word to guess is displayed with spaces between each letter, and correctly guessed letters are filled in.
6. The game will display a message when you win or lose, and for incorrect guesses, it will show the correct word.
7. After running out of attempts, the game will display a message indicating the correct word and then restart.

## Files

- `hangman_game.py`: The main Python script containing the Hangman game implementation.
- `random_word.py`: A Python script using the `random-word` library to generate a random word.

## Dependencies

- Tkinter library: This is a standard GUI toolkit for Python, and it is usually included with Python installations.
- Random Word library: This is used to generate a random word for the game. Install it using:

```bash
pip install Random-Word
