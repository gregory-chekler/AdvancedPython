#!/usr/bin/pyhon
# game.py

'''Short game for testing highscores module'''

__author__ = "Gregory Chekler"
__version__ = "1.0"

import random
import time
import string
import tkinter as tk
import high_scores as hs
from datetime import date


playing = True  # to figure out which action ENTER should take
DEBUG = True
alpha = string.ascii_uppercase


def get_word():
    '''gets random "word" to play the game with

    :return: creates a random word
    '''
    WORD_LENGTH = 10
    word = ""
    for i in range(WORD_LENGTH):
        choice = random.randint(0, 25)  # choose random letter
        word += alpha[choice]  # build string
    print(word)
    return word


def get_time():
    '''gets the time to determine score

    :return: defines start time
    '''
    global start_time
    start_time = time.time()
    return start_time


def go(event):
    '''need to have a separate function because binding requires event argument

    :param event: some click or input
    :return: calls get_and_show_score() function
    '''
    if DEBUG:
        print("go1")
    get_and_show_score()


def go2(event):
    """function that calls play function

    :param event: some click or input
    :return: calls play() function
    """
    if DEBUG:
        print("go2")
    play()


def get_and_show_score():
    '''gets wordchecks if they are the same, calculates and shows score

    :return: gives calculated score or says that the input was wrong
    '''

    if DEBUG:
        print("get and show score")
    global user_score, game_word, start_time, playing

    ans = answer.get().upper()  # get user answer
    word = game_word.get()  # get game word

    if ans == word:  # correct
        answer_entry.delete(0, 'end')  # clear word from entry box

        # instructions.focus()
        correct = True

        instructions.config(font=("Verdana", 28), text="RIGHT!!!")
        name_entry.focus_set()  # put cursor in name entry
        # calculate score:
        elapsed_time = time.time() - start_time
        user_score = 1000 - int(elapsed_time * 1000) / 100  # round time to two digits

        dates = date.today()  # SEE PROJECT DESCRIPTION FOR HOW TO GET REAL DATE

        # show score and ask for name
        game_word.set("Score: " + str(user_score) + "   " + str(dates) + "\n" + \
                      "Enter Your Name")

    else:  # wrong
        instructions.config(font=("Verdana", 28), text="WRONG!!!")


def save_score():
    '''saves score, name, and date to highscores file

    :return: saves the score of the attempt to a text file
    '''
    global user_score
    name = name_var.get()  # get name of entry box

    time = date.today()
    hs.add_score("scores.txt", user_score, name, time)

    name_entry.delete(0, 'end')  # clear name from entry box
    game_word_lbl.config(text=name + "'s score saved!")


def play():
    '''new game

    :return: begins/sets up the round
    '''
    if DEBUG:
        print("play")
    game_word.set(get_word())  # show the new word
    start_time = get_time()  # record the current time

    instructions.config(font=("Verdana", 28),
                        text="Type the word quickly and hit ENTER\n(lowercase okay)",
                        justify='center')

    game_word_lbl.config(text=game_word)

    answer.set("")
    answer_entry.delete(0, 'end')
    answer_entry.focus()


def reset():
    """resets the textfile by calling hs module

    :return: calls function from module that makes the textfile only contain ,,,
    """
    hs.clear_scores_default("scores.txt")

def del_name():
    """deletes all scores by certain user

    :return: calls a function that deletes all scores by certain user
    """
    name = name_var.get() #must input name so that code knows what name to remove
    hs.remove("scores.txt", name)
    name_entry.delete(0, 'end')

def show():
    """presents table of scores in the console and a new window/GUI

    :return: calls functions that present table of scores in the console and a new window/GUI
    """
    hs.show_scores("scores.txt")
    hs.show_scores_GUI("scores.txt")


def check_length(event):
    '''checks the length of the user-entered word to see when they have typed
    the same # of letters as the gameword - then confirm correct or not
    currently not working properly

    :return: calls function (if input and game_word) are same length to check if they are the same
    '''

    # print(answer.get(), game_word.get())   # for debugging purposes

    if len(answer.get()) == len(game_word.get()):
        get_and_show_score()

def sort(): #extra credit that sorts the data and gives the scores in order
    """sorts the data and gives the scores in order. Although, to see it, user must click show score

    :return: edits text file and makes data go in order from highest to lowest
    """
    hs.sort("scores.txt")

root = tk.Tk()
root.title("Word Game")
root.geometry("1500x600")
root.configure(background='black')

game_word = tk.StringVar(root)
answer = tk.StringVar(root)

# LABELS:
instructions = tk.Label(root, font=("Verdana", 28),
                        text="Type the word quickly and hit ENTER\n(lowercase okay)",
                        justify='center')
instructions.grid(row=0, column=1)
instructions.configure(foreground="red", background="black")

game_word_lbl = tk.Label(root, font=("Consolas", 50),
                         textvariable=game_word,
                         justify='right')
game_word_lbl.configure(background="yellow")
game_word_lbl.grid(row=1, column=1)

# ENTRY FOR ANSWER:
entry_lbl = tk.Label(root, text="Type letters and hit enter:", font=("Verdana", 18))
entry_lbl.grid(row=3, column=0)
entry_lbl.configure(foreground="red", background="black")

answer_entry = tk.Entry(root, width=30, font=("Verdana", 28), fg="red",
                        textvariable=answer)
answer_entry.grid(row=3, column=1)

answer_entry.bind('<Key>', check_length)  # every time a key is typed, check length of word
answer_entry.bind('<Return>', go)  # when ENTER is hit, check word for correctness
instructions.bind('<Shift_L>', go2)

# ENTRY FOR NAME:
name_lbl = tk.Label(root, text="Enter Name when game over (or if removing scores of person):")
name_lbl.grid(row=4, column=0)
name_lbl.configure(foreground="red", background="black", font=("Verdana", 18))

name_var = tk.StringVar(root)
name_var.set("")
name_entry = tk.Entry(root, width=30, font=("Verdana", 28), fg="red",
                      textvariable=name_var)
name_entry.grid(row=4, column=1)

# BUTTONS:
play_btn = tk.Button(root, text="==PLAY==", command=play)
play_btn.grid(row=2, column=1, padx=3, pady=3, ipadx=3, ipady=3)
save_btn = tk.Button(root, text="SAVE score info", command=save_score)
save_btn.grid(row=5, column=1, padx=5, pady=5, ipadx=5, ipady=5)
show_scores_btn = tk.Button(root, text="SHOW scores", command=show)
show_scores_btn.grid(row=6, column=1, padx=5, pady=5, ipadx=5, ipady=5)
reset_btn = tk.Button(root, text="RESET scores", command=reset)
reset_btn.grid(row=7, column=1, padx=5, pady=5, ipadx=5, ipady=5)
remove_btn = tk.Button(root, text="Delete name data", command=del_name)
remove_btn.grid(row=8, column=1, padx=5, pady=5, ipadx=5, ipady=5)
sort_btn = tk.Button(root, text="Sort high scores", command=sort)
sort_btn.grid(row=9, column=1, padx=5, pady=5, ipadx=5, ipady=5)

root.mainloop()