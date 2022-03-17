import time
from random_word import RandomWords
from loop import main_game_loop
import random

def main():
    words = ["assessment", "extraterrestrial", "raise", "secular", "potential", "disturbance", "nature", "definite", "superintendent", "round", "offline"]
    try:
        word = RandomWords().get_random_word()
        if word == None:
            word = random.choice(words)
    except:
        word = random.choice(words)
    word2 = word
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    limit = 5
    print("there are " + str(length) + " letters")
    main_game_loop(word, display, count, length, already_guessed, limit)
    print("Your word was " + word2)
    play_game = input("Do you want to play again? y = yes, n = no \n").lower()
    while play_game not in ["y", "n"]:
        play_game = input("Do you want to play again? y = yes, n = no \n").lower()
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thank you for playing")
        exit()

print("\nWelcome to The Hangman Game")
name = input("Enter your name: ")
print("Hello " + name + "! Good Luck")
time.sleep(2)
print("Game starting soon....")
time.sleep(3)
main()