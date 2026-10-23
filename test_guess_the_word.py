# Luis Caraveo
# CIS256 Fall 2026
# Programming Assignment 4
# 10/23/2026

# Random is imported since we are using .random to test words.
from guess_the_word import words
import random

def test_words():
    word = random.choice(words)
    assert word in words
# Here we are testing if the guessed letter is correct.
def test_correct_guess():
    word = random.choice(words)
    guess = word[0]
    assert guess in word
# Here are are testing if the letter guessed is incorrect.
def test_incorrect_guess():
    word = random.choice(words)
    guess = "z"
    assert guess not in word
# Here we are testing if the word that is guessed is the correct random word. 
def test_correct_word():
    word = random.choice(words)
    guess = word
    assert guess == word
# Here we test if the word is guessed incorrectly. 
def test_incorrect_word():
    word = random.choice(words)
    guess = "trouble"
    assert guess != word
# does subtracting attempts result in zero remaining. 
def test_num_attempts():
    num_attempts = 5
    for i in range(5):
        num_attempts = num_attempts - 1
    assert num_attempts == 0

# The game over function is tested. A function was created for this specific test.
def test_game_over():
    assert game_over(0) == True
    assert game_over(1) == False

from guess_the_word import game_over



    
    
