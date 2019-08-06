import threading
import time
import random

seconds_left = 60
correct_words = 0
incorrect_words = 0


def timer():
    global seconds_left

    while True:
        seconds_left -= 1
        time.sleep(1)


def get_word(low, high):
    while True:
        lines = open('words_alpha.txt').read().splitlines()
        my_line = random.choice(lines)
        my_line.strip()
        if low <= len(my_line) <= high:
            return my_line


def type_word(difficulty):
    global seconds_left
    global correct_words
    global incorrect_words

    if difficulty == 'easy':
        word = get_word(1, 5)
    elif difficulty == 'normal':
        word = get_word(4, 7)
    elif difficulty == 'hard':
        word = get_word(6, 12)
    elif difficulty == 'very_hard':
        word = get_word(8, 13)
    elif difficulty == 'insane':
        word = get_word(20, 25)

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
        return


def play_game():
    global seconds_left
    global correct_words
    global incorrect_words

    while seconds_left > 0:
        if correct_words < 7:
            type_word('easy')
        elif correct_words < 15:
            type_word('normal')
        elif correct_words < 20:
            type_word('hard')
        elif correct_words < 25:
            type_word('very_hard')
        else:
            print("FINAL BOSS\n\n")
            type_word('insane')
    print("Time is up!\n\n\n")
    print(f"Words typed: {correct_words}\n"
          f"Incorrect words: {incorrect_words}\n")


def intro():
    start_word = get_word(4, 6)
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

