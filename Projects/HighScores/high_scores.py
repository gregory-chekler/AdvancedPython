#!/usr/bin/pyhon
# high_scores.py

'''modules that make calculations and add scores as well as help display users score data'''

__author__ = "Gregory Chekler"
__version__ = "1.0"


from tkinter import *
import pandas as pd

root = Tk()
root.title("ListBox!")
root.withdraw()

def read_scores(file_name):
    """reads text file that holds scoring data such as username, score, date

    :param file_name: text file with score data
    :return: lists of scores, names, and dates
    """
    file = open(file_name, 'r')
    text = file.read()
    list = text.split(",")#splits text up by comma which makes a list
    score = [list[i] for i in range(1, len(list), 3)]
    names = [list[i] for i in range(0, len(list), 3)]
    dates = [list[i] for i in range(2, len(list), 3)]
    file.close()
    return score, names, dates

def show_scores(file_name):
    """shows the scores data in the console using a dataframe

    :param file_name: text file with score data
    :return: a dataframe containg the scores data in a nice format
    """
    data = []
    #takes return values (which are lists) from read_scores and sets them equal to variables
    scores = read_scores(file_name)[0]
    names = read_scores(file_name)[1]
    dates = read_scores(file_name)[2]
    for i in range(len(scores)): # creates data frame using pandas
        data.append([names[i], dates[i], scores[i]])
        df = pd.DataFrame(data, columns=['Name', 'Date', 'Score']) #makes data look nice through columns
    print(df)

#shows a simple table of scores in console (uses read_scores())
def show_scores_GUI(file_name):
    """creates a popup window that contains scores data

    :param file_name: text file with score data
    :return: window with scores data
    """
    # takes return values (which are lists) from read_scores and sets them equal to variables
    scores = read_scores(file_name)[0]
    names = read_scores(file_name)[1]
    dates = read_scores(file_name)[2]
    root.deiconify() #shows scores table

    # CREATE THE ACTUAL LISTBOXES:
    names_listb = Listbox(root)
    dates_listb = Listbox(root)
    scores_listb = Listbox(root)

    # PUT THE ITEMS IN THE LISTBOX:
    for item in names:
        names_listb.insert(END, item)
    for item in dates:
        dates_listb.insert(END, item)
    for item in scores:
        scores_listb.insert(END, item)

    # PACK THE LISTBOX INTO THE TK WINDOW:
    names_listb.grid(row=0, column=0)
    dates_listb.grid(row=0, column=1)
    scores_listb.grid(row=0, column=2)

    # BIND THE ACTION OF SELECTING A LISTBOX ITEM TO THE FUNCTION:
    names_listb.bind("<<ListboxSelect>>")

    root.mainloop()

def add_score(file_name, score, name, date):
    """adds score to text file after playing

    :param file_name: text file with score data
    :param score: the score received from playing the game
    :param name: the users name
    :param date: the date the game was played
    :return: adds this data to the text file
    """
    file = open(file_name, "a+")#used for appending strings
    text = file.read()
    file.write(text)
    file.write(str(name) + "," + str(score) + "," + str(date) + ",") #appends string to text file
    file.close()

def clear_scores_default(file_name):
    """deletes all of the scores on the text file

    :param file_name: text file with score data
    :return: a file that contains ',,,'
    """
    file = open(file_name, "w")
    file.write(",,,")#the reason this is done is to prevent errors in the data frame and when showing window
    file.close()

def remove(file_name, name_to_delete):
    """delets all scores entered by a specific user

    :param file_name: text file with score data
    :param name_to_delete: username
    :return: edits the text file to not contain any data added by a specific username
    """
    file = open(file_name, 'r')
    text = file.read() #saves data in text variable so it is not destroyed later on
    file.close()
    file = open(file_name, 'w+')#be careful as this will automatically delete all scores.txt data
    list = text.split(",")
    for i in range(len(list)):
        try:
            if (list[i] == name_to_delete):
                del list[i+2], list[i+1], list[i]#goes from name to score to date as to not mess with the for loop
        except:
            break
    # since a username will most likely be deleted along with other data and make the length smaller,
    # the try and except in this function make sure an error does not occur and instead the function
    # just moves on

    string = ','.join([str(x) for x in list]) #takes the list of data and converts it into string format
    file.write(string)
    file.close()

def sort(file_name): #extra credit
    """

    :param file_name:
    :return:
    """
    string = ''#empty string that gets appended to later on
    scores = read_scores(file_name)[0]
    names = read_scores(file_name)[1]
    dates = read_scores(file_name)[2]
    data = []
    file = open(file_name, 'w+')
    for i in range(len(scores)):
        data.append([names[i], scores[i], dates[i]])

    data.sort(key=lambda tup: tup[1], reverse=True) #lambda function that sorts by score using index 1

    for i in range(len(data)): #puts data into string format
        for x in range(3):
            string = string + data[i][x] + ","

    file.write(string)#puts sorted string into txt file
    file.close()

