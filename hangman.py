#!/usr/local/bin/python3

#! AUTHOR WojciechSkumajTo

from optparse import check_choice
from secrets import choice
import random
import sys

number_of_tries = 5
password = ""
used_word = []

print("Author: WojciechSkumajTo\n")


def password_randomization():
    password_list = []
    with open("password.txt", "r") as f:
        content = f.read()
        password_list = content.split('\n')
    password = random.choice(password_list)
    return password


def create_game(pass_word):
    user_word = []
    for _ in pass_word:
        user_word.append("_")
    return user_word


def find_indexes(password, letter):
    indexes = []
    for index, letter_in_word in enumerate(password):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes


def show_statistics(user_word, used_word, letter, number_of_tries):
    print("\n")
    print("---------------------------------")
    print("PASSWORD: ", " ".join(user_word))
    print("---------------------------------")
    print("Picked a letter -->", letter)
    print("---------------------------------")
    print("Word List:", ", ".join(used_word))
    print("---------------------------------")
    print("Health: ", number_of_tries)
    print("---------------------------------")
    print("\n")


def drawing_picture():
    if number_of_tries == 4:
        print()
        print("____")
        print()

    elif number_of_tries == 3:
        print()
        print("__|__")
        print()

    elif number_of_tries == 2:
        print()
        print("  |")
        print("  |")
        print("  |")
        print("__|__")
        print()

    elif number_of_tries == 1:
        print()
        print("   _____")
        print("  |")
        print("  |")
        print("  |")
        print("__|__")
        print()

    elif number_of_tries == 0:
        print()
        print("   _____")
        print("  |     |")
        print("  |     0")
        print("  |    /|\\")
        print("  |     |")
        print("  |    / \\")
        print("  |")
        print("  |")
        print("__|__")
        print()


def check_password(password, user_passw):
    passw = "".join(user_passw)
    if passw == password:
        return True
    else:
        return False


def check_win(veryfication, number_of_tries, password):
    if veryfication:
        print("YOU WIN")
        sys.exit(1)
    elif number_of_tries == 0:
        print("GAME 0VER")
        print("PASSWORD: ", password)
        sys.exit(1)


def insert_letter(user_word, letter):
    indexes = find_indexes(password, letter)
    if len(indexes) != 0:
        for index in indexes:
            user_word[index] = letter
        used_word.append(letter)


def warning():
    print()
    print("##### WARNING #####")


def main():
    while True:
        global password, number_of_tries
        if not len(password):
            print("                         ##### HANGMAN #####             ")
            password = password_randomization()
            user_word = create_game(password)
            print("Password to guess:", " ".join(user_word))
            print("Passowrd lenght:", len(user_word), "\n")

        print("-----------------Please guess by pressing any letter-----------------")

        subst = "".join(used_word)
        letter = input()

        #! VALIDATION DATE
        if letter.isalpha():
            if len(letter) > 1:
                warning()
                print("Please enter only one letter!\n")
            elif len(letter) == 1:
                if used_word:
                    for w in used_word:
                        if letter == w:
                            warning()
                            print("Please enter new word!\n")
                            break
                        elif subst.find(letter) == -1:
                            used_word.append(letter)
                            indexes = find_indexes(password, letter)
                            if len(indexes) != 0:
                                for index in indexes:
                                    user_word[index] = letter
                            else:
                                number_of_tries -= 1
                            break
                else:
                    if password.find(letter) == -1:
                        number_of_tries -= 1
                        insert_letter(user_word, letter)
                    else:
                        insert_letter(user_word, letter)
        else:
            warning()
            print("Please enter string not NUMBER")

        show_statistics(user_word, used_word, letter, number_of_tries)
        drawing_picture()
        check = check_password(password, user_word)
        check_win(check, number_of_tries, password)


if __name__ == '__main__':
    main()
