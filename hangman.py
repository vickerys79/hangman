import tkinter as tk
from random_word import RandomWords


class HangmanGame:
    def __init__(self, master):
        """
        Initialize the Hangman game.
        """
        self.master = master
        self.master.title("Hangman Game")

        self.word_to_guess = choose_word()
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.incorrect_guess_list = []

        self.hangman_canvas = tk.Canvas(self.master, width=200, height=250)
        self.hangman_canvas.grid(row=0, column=0, columnspan=2)

        self.word_label = tk.Label(self.master, text=self.display_word())
        self.word_label.grid(row=1, column=0, columnspan=2)

        self.incorrect_label = tk.Label(self.master, text="Incorrect guesses: ")
        self.incorrect_label.grid(row=2, column=0, columnspan=2)

        self.guess_header_label = tk.Label(self.master, text="Enter a letter:")
        self.guess_header_label.grid(row=3, column=0, columnspan=2)

        self.guess_entry = tk.Entry(self.master)
        self.guess_entry.grid(row=4, column=0, columnspan=2)
        self.guess_entry.bind("<Return>", lambda event: self.make_guess())  # Bind Enter key to make_guess

        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess)
        self.guess_button.grid(row=5, column=0, columnspan=2)
        self.hangman_parts = [
            self.hangman_canvas.create_line(50, 200, 150, 200),  # Base
            self.hangman_canvas.create_line(100, 200, 100, 50),  # Vertical pole
            self.hangman_canvas.create_line(100, 50, 150, 50),  # Top horizontal pole
            self.hangman_canvas.create_line(100, 50, 100, 75),  # Rope
            self.hangman_canvas.create_oval(95, 75, 105, 85),  # Head
            self.hangman_canvas.create_line(100, 85, 100, 125),  # Body
            self.hangman_canvas.create_line(100, 95, 75, 105),  # Left arm
            self.hangman_canvas.create_line(100, 95, 125, 105),  # Right arm
            self.hangman_canvas.create_line(100, 125, 75, 150),  # Left leg
            self.hangman_canvas.create_line(100, 125, 125, 150)  # Right leg
        ]
        self.hide_hangman_parts()
        self.update_hangman()

    def display_word(self):
        """
        Display the current state of the word to guess, with spaces between each letter.
        """
        display = " ".join(letter if letter in self.guessed_letters else "_" for letter in self.word_to_guess)
        return display

    def update_hangman(self):
        """
        Update the Hangman figure on the canvas.
        """
        self.hide_hangman_parts()

        for i in range(self.incorrect_guesses + 1):
            self.hangman_canvas.itemconfig(self.hangman_parts[i], state=tk.NORMAL)

    def make_guess(self):
        """
        Process a user's guess.
        """
        guess = self.guess_entry.get().lower()

        if guess in self.guessed_letters:
            self.display_message("You already guessed that letter. Try again.")
            self.guess_entry.delete(0, tk.END)  # Clear the entry after each guess
        elif guess.isalpha() and len(guess) == 1:
            self.guessed_letters.append(guess)

            if guess not in self.word_to_guess:
                self.incorrect_guesses += 1
                self.incorrect_guess_list.append(guess)
                self.display_message("Incorrect guess!")

            self.guess_entry.delete(0, tk.END)  # Clear the entry after each guess
            self.update_hangman()
            self.word_label.config(text=self.display_word())
            self.incorrect_label.config(text="Incorrect guesses: {}".format(", ".join(self.incorrect_guess_list)))

            if self.display_word() == self.word_to_guess:
                self.display_message("Congratulations! You guessed the word: {}".format(self.word_to_guess))
            elif self.incorrect_guesses == len(self.hangman_parts) - 1:
                self.display_message("Sorry, you ran out of attempts. The word was: {}".format(self.word_to_guess))
                self.restart_game()
        else:
            self.display_message("Invalid input. Please enter a single letter.")
            self.guess_entry.delete(0, tk.END)  # Clear the entry after each guess

    def display_message(self, message):
        """
        Display a message in a popup window.
        """
        popup = tk.Toplevel(self.master)
        popup.title("Message")
        tk.Label(popup, text=message).pack()
        tk.Button(popup, text="OK", command=popup.destroy).pack()
        popup.bind("<Return>", lambda event: popup.destroy())  # Bind Enter key to close the popup

    def hide_hangman_parts(self):
        """
        Hide all Hangman parts on the canvas.
        """
        for part in self.hangman_parts:
            self.hangman_canvas.itemconfig(part, state=tk.HIDDEN)

    def restart_game(self, word=None):
        """
        Restart the game by choosing a new word and resetting game state.
        """
        self.display_message("Let's play again :)")
        self.word_to_guess = word if word else choose_word()
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.incorrect_guess_list = []
        self.update_hangman()
        self.word_label.config(text=self.display_word())
        self.incorrect_label.config(text="Incorrect guesses: ")


def choose_word():
    """
    Choose a random word using the random-word library.
    """
    r = RandomWords()
    return r.get_random_word()


if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGame(root)
    root.mainloop()
