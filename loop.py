import time

def main_game_loop(word, display, count, length, already_guessed, limit):
    print(already_guessed)
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    guess = guess.lower()
    if len(guess) != 1:
        print("Invalid Input, One letter at a time\n")
        main_game_loop(word, display, count, length, already_guessed, limit)
    elif guess.isalpha() == False:
        print("Invalid Input, Need to be a letter\n")
        main_game_loop(word, display, count, length, already_guessed, limit)
    elif guess in already_guessed:
        print("Already guessed, Try another letter.\n")
    elif guess in word:
        already_guessed.extend([guess])
        i = word.count(guess)
        while i != 0:
            index = word.find(guess)
            word = word[:index] + "_" + word[index + 1:]
            display = display[:index] + guess + display[index + 1:]
            print(display + "\n")
            i = i - 1
    else:
        already_guessed.extend([guess])
        count += 1
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            return(word, display, count, length, already_guessed, limit)
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        return(word, display, count, length, already_guessed, limit)
    elif count != limit:
        main_game_loop(word, display, count, length, already_guessed, limit)