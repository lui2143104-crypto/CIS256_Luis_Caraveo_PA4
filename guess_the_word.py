# Luis Caraveo
# CIS256 Fall 2026
# 10/22/2026
#Python Word Guessing Game


import random

words = [
    "apple",
    "chair",
    "desk",
    "mouse",
    "monitor",
    "keyboard",
    "pad",
    "cat",
    "dog",
    "child"
]

print("Guess the word and win a prize...")
print("A virtual prize")
print("You will have only 5 attempts")
print("A hint, the words are related to what you might find at your desk")
print("Or around it...")
print("Good Luck!")

# Random prizes from https://www.asciiart.eu/art/261a86e8957ccf33
random_prize = [
            r"""
         ___________
        '._==_==_=_.'
        .-\:      /-.
       | (|:.     |) |
        '-|:.     |-'
          \::.    /
           '::. .'
             ) (
           _.' '._
          `"""""""`
        """,
            r"""  /^ ^\
                / 0 0 \
                V\ Y /V
                / - \
                /    |
                V__) ||
                """,
                r"""                    *****************
               ******               ******
           ****                           ****
        ****                                 ***
      ***                                       ***
     **           ***               ***           **
   **           *******           *******          ***
  **            *******           *******            **
 **             *******           *******             **
 **               ***               ***               **
**                                                     **
**       *                                     *       **
**      **                                     **      **
 **   ****                                     ****   **
 **      **                                   **      **
  **       ***                             ***       **
   ***       ****                       ****       ***
     **         ******             ******         **
      ***            ***************            ***
        ****                                 ****
           ****                           ****
               ******               ******
                    *****************"""

  


]






# This def is where the function is made. 
# It will display the guessed letters revealed and keep hidden the unguessed letters. 
def guess_word(secret_word, letter_used):
    # Display starts empty and is filled as the game progresses.
    display = ""
    # For loop goes through each letter in the secret word and checks if it has been guessed.
    for letter in secret_word:
        # if the letter in the secret word is in the letters that the player has just used
        # display is now updated to include that letter. 
        if letter in letter_used:
            display = display + letter
        # If the letter in the word is not guessed yet, an underscore takes its place. 
        else:
            display = display + "_"
    return display
# Here we display the begining of the secret word with all the letters hidden
# As underscores.


def main():
    random_word = random.choice(words)
    secret_word = random_word
    letter_used = set()
    num_attempts = 5
    


# This is the main loop for the game. A while loop is used to check 
# the user input, and update the game as needed. 
# This loop will run as long as the number of attempts remaining are
# Still greater than 0.
    while num_attempts > 0:
        print(guess_word(secret_word, letter_used))
        print("Guess a letter or...")
        print("You can guess the entire word, but risk losing it all.")
        print()
        guess = input().lower()
    

# If player guessed the entire word correctly, random prize is given, and game ends.
        if guess == secret_word:
            print(f"You guessed '{secret_word.upper()}' ")
            print("Nice job, you must have cheated somehow!")
            print(f"Your random prize is: {random.choice(random_prize)}")
            break

# Player enters more than one letter counts as trying to guess the whole word. 
# check if the player guessed the word wrong, and end the game
        elif len(guess) > 1:
            print("Wrong word")
            print("You played and lost.")
            print(f"The secret word was: {secret_word}")
            break

# if the player guessed a letter correctly
        elif guess in secret_word and len(guess) == 1:
            print("Correct!")
            print()
            letter_used.add(guess)

# This checks to see if the player has guessed all the letters correctly. 
            if guess_word(secret_word, letter_used) == secret_word:
                print(f"You guessed '{secret_word.upper()}' ")
                print("Congratulations!")
                print(f"Your random prize is: {random.choice(random_prize)}")
                break
        

# If the player hits enter and does not enter anything,
# it will count as a guess. 
        elif len(guess) == 0:
            print("You didn't enter anything.")
            num_attempts = num_attempts - 1
            print(f"Now you have: {num_attempts} attempts remaining")
            print("what a waste...")
            print()


# If the player guessed incorrectly, and only entered a single letter.
# Also runs an if statement if there are no attempts remaining. 
        elif guess not in secret_word and len(guess) == 1:
            print("Incorrect!")
            num_attempts = num_attempts - 1
            print(f"Now you have: {num_attempts} attempts remaining")
            print()

        # Runs if the player is out of attempts. Gives the secret word. 
            if num_attempts == 0:
                print("No more attempts remaining")
                print("Better luck next time!")
                print(f"The secret word was: {secret_word}")

if __name__ == "__main__":
    main()


    

