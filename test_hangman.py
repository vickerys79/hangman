import tkinter as tk
import pytest
from hangman import HangmanGame, choose_word


@pytest.fixture
def hangman_game_instance():
    root = tk.Tk()
    game_instance = HangmanGame(root)
    return game_instance


def test_initialization(hangman_game_instance):
    assert hangman_game_instance.word_to_guess is not None
    assert hangman_game_instance.guessed_letters == []
    assert hangman_game_instance.incorrect_guesses == 0
    assert hangman_game_instance.incorrect_guess_list == []
    assert isinstance(hangman_game_instance.hangman_canvas, tk.Canvas)
    assert isinstance(hangman_game_instance.word_label, tk.Label)
    assert isinstance(hangman_game_instance.incorrect_label, tk.Label)
    assert isinstance(hangman_game_instance.guess_header_label, tk.Label)
    assert isinstance(hangman_game_instance.guess_entry, tk.Entry)
    assert isinstance(hangman_game_instance.guess_button, tk.Button)
    assert isinstance(hangman_game_instance.hangman_parts, list)


def test_display_word(hangman_game_instance):
    hangman_game_instance.word_to_guess = "hangman"
    hangman_game_instance.guessed_letters = ['h', 'a', 'g']
    assert hangman_game_instance.display_word() == "h a _ g _ a _"


def test_make_correct_guess(hangman_game_instance, monkeypatch):
    hangman_game_instance.word_to_guess = "hangman"
    monkeypatch.setattr(hangman_game_instance.guess_entry, "get", lambda: "h")

    assert hangman_game_instance.guessed_letters == []
    assert hangman_game_instance.incorrect_guesses == 0
    assert hangman_game_instance.incorrect_guess_list == []

    hangman_game_instance.make_guess()

    assert hangman_game_instance.guessed_letters == ['h']
    assert hangman_game_instance.incorrect_guesses == 0
    assert hangman_game_instance.incorrect_guess_list == []
    assert hangman_game_instance.display_word() == "h _ _ _ _ _ _"
    assert hangman_game_instance.word_label.cget("text") == "h _ _ _ _ _ _"
    assert hangman_game_instance.incorrect_label.cget("text") == "Incorrect guesses: "


def test_make_incorrect_guess(hangman_game_instance, monkeypatch):
    hangman_game_instance.word_to_guess = "hangman"
    monkeypatch.setattr(hangman_game_instance.guess_entry, "get", lambda: "x")

    assert hangman_game_instance.guessed_letters == []
    assert hangman_game_instance.incorrect_guesses == 0
    assert hangman_game_instance.incorrect_guess_list == []

    hangman_game_instance.make_guess()

    assert hangman_game_instance.guessed_letters == ['x']
    assert hangman_game_instance.incorrect_guesses == 1
    assert hangman_game_instance.incorrect_guess_list == ['x']
    assert hangman_game_instance.display_word() == "_ _ _ _ _ _ _"
    assert hangman_game_instance.word_label.cget("text") == "_ _ _ _ _ _ _"
    assert hangman_game_instance.incorrect_label.cget("text") == "Incorrect guesses: x"


def test_restart_game(hangman_game_instance, monkeypatch, capsys):
    monkeypatch.setattr(hangman_game_instance.guess_entry, "get", lambda: "x")

    hangman_game_instance.word_to_guess = "hangman"
    hangman_game_instance.incorrect_guesses = 6

    assert hangman_game_instance.guessed_letters == []
    assert hangman_game_instance.incorrect_guesses == 6
    assert hangman_game_instance.incorrect_guess_list == []

    hangman_game_instance.restart_game(word="hangman")

    assert hangman_game_instance.guessed_letters == []
    assert hangman_game_instance.incorrect_guesses == 0
    assert hangman_game_instance.incorrect_guess_list == []
    assert hangman_game_instance.display_word() == "_ _ _ _ _ _ _"
    assert hangman_game_instance.word_label.cget("text") == "_ _ _ _ _ _ _"
    assert hangman_game_instance.incorrect_label.cget("text") == "Incorrect guesses: "


def test_choose_word():
    word = choose_word()
    assert isinstance(word, str)
    assert word.isalpha()
    assert len(word) > 0
