import random
#import hangman_words_list
#or we can write
from hangman_words_list import word_list  # this way we dont have to write hangman_words_list.word_list

hangman_stages = [
    """
     -----
     |   |
     |
     |
     |
     |
    ---""",
    """
     -----
     |   |
     |   O
     |
     |
     |
    ---""",
    """
     -----
     |   |
     |   O
     |   |
     |
     |
    ---""",
    """
     -----
     |   |
     |   O
     |  /|
     |
     |
    ---""",
    """
     -----
     |   |
     |   O
     |  /|\\
     |
     |
    ---""",
    """
     -----
     |   |
     |   O
     |  /|\\
     |  /
     |
    ---""",
    """
     -----
     |   |
     |   O
     |  /|\\
     |  / \\
     |
    ---"""
]

lives = 6
chosen_word = random.choice(word_list)

placeholder = ""
for char in chosen_word:
    placeholder += "_"
print(placeholder)

end_of_game = False
correct_letters = []

while not end_of_game:
    guess = input("Enter a one alphabet: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for alphabet in chosen_word:
        if alphabet == guess:
            display += guess
            correct_letters.append(guess)
        elif alphabet in correct_letters:
            display += alphabet
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose\n")

    if "_" not in display:
        end_of_game = True
        print("You Win\n")


    print(hangman_stages[lives])