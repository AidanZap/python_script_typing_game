import threading
import time
import random

seconds_left = 60
correct_words = 0
incorrect_words = 0
words_list = []


def timer():
    global seconds_left

    while True:
        time.sleep(1)
        seconds_left -= 1


def get_word(low, high):
    while True:
        lines = open('words_alpha.txt').read().splitlines()
        my_line = random.choice(lines)
        my_line.strip()
        if low <= len(my_line) <= high:
            return my_line


def load_dictionary():
    global words_list

    for n in range(6):
        words_list.append(get_word(1,5))
    for n in range(9):
        words_list.append(get_word(4, 7))
    for n in range(8):
        words_list.append(get_word(6, 12))
    for n in range(6):
        words_list.append(get_word(8, 14))
    words_list.append(get_word(17, 25))

def type_word(word):
    global seconds_left
    global correct_words
    global incorrect_words

    print(f"Your word is:\n{word}\n")
    response = input("Type here:")
    if response == word:
        if seconds_left > 0:
            correct_words += 1
            print(f"Nice!     {seconds_left} seconds remaining.\n")
            return
        else:
            print("Correct... but too slow!")
    else:
        incorrect_words += 1
        print(f"Whoops! Not quite right..     {seconds_left} seconds remaining.\n")


def play_game():
    global seconds_left
    global correct_words
    global incorrect_words

    for word in words_list:
        if correct_words + incorrect_words == 29:
            print("FINAL BOSS \n\n")
            type_word(word)
            print("End of challenge reached.\n\n\n")
            break
        type_word(word)
        if seconds_left <= 0:
            print("Time is up!\n\n\n")
            break

    print(f"Words typed: {correct_words}\n"
          f"Incorrect words: {incorrect_words}\n")
    if 10 <= correct_words <= 17:
        print("Bronze Medal: 10 or more words achieved")
    elif correct_words <= 25:
        print("Silver Medal: 18 or more words achieved")
    elif correct_words <= 29:
        print("Gold Medal: 26 or more words achieved")
    elif correct_words == 30:
        print("Platinum Medal: All words correct")
    else:
        print("No medals earned")


def intro():
    start_word = get_word(4, 6)
    print("Loading words... this make take around a minute...")
    load_dictionary()
    print(f"Welcome to a python scripted typing test. When you are ready to begin,"
          f" please type the word below!\nYour word is:        {start_word}\n")
    start_response = input("Type here:")
    while True:
        if start_response == start_word:
            print("Nice!     Starting the game in...")
            time.sleep(1)
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            break
        else:
            start_response = input("Whoops.. try typing that again: ")


timer_thread = threading.Thread(target=timer, name="Countdown")
intro()
timer_thread.start()
play_game()

