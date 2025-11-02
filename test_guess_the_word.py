import guess_the_word
import random

def test_word():
    # Making sure the random word is picked from the list of words.
    words =["Arizona", "College", "Football", "Homework", "United States", "Mesa", "Python"]
    word_to_guess = random.choice(words)
    assert word_to_guess in words

def test_guess():
    # Test guessing loic for the word "college".
    word = "College"
    guessed = ['o', 'v', 'g']

    # Correctly guessed letters are shown.
    show_word = [letter if letter in guessed else "_" for letter in word]
    assert show_word == ['_', 'o', '_', '_', '_', 'g', '_']
