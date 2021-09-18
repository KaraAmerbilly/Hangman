import random
from re import finditer

tries = 8
word_list = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(word_list)
dash = list((len(random_word)) * "-")
hint = dash
guessed = []

def menu():
    play_status = input("Type \"play\" to play the game, \"exit\" to quit: ")
    if play_status == "play":
        check()
    else:
        return

def check():
    while tries != 0 and ''.join(hint) != random_word:
        print(f"\n{''.join(hint)}")
        matcher()
    else:
        if tries == 0:
            print(f"You lost!")
        else:
            print("You guessed the word!")
            print("You survived!")

def matcher():
    global tries
    global hint
    letter = input(f"Input a letter: ")
    if len(letter) != 1 or letter == "":
        print("You should input a single letter")
    elif letter.islower() == False:
        print("Please enter a lowercase English letter")
    elif letter in guessed:
        print("You've already guessed this letter")
    elif letter in random_word and letter not in hint:
        matches = finditer(letter, random_word)
        matches_positions = [match.start() for match in matches]
        guessed.append(letter)
        for i in range(len(matches_positions)):
            hint[matches_positions[i]] = letter
    else:
        tries -= 1
        guessed.append(letter)
        print("That letter doesn't appear in the word")

print("H A N G M A N")
menu()
