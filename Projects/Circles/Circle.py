#!/usr/bin/python
#Circle.py

'''Creates a game where the user can click on circles for 30 seconds and the closer the user
gets to the center, the more points they earn'''

__version__ = "1.0.0"
__author__ = 'Gregory Chekler'

import tkinter as tk
import random
import math
import time

root = tk.Tk()



circle = []
slopes = []
coords = []
colors = ["red", "blue", "orange", "black", "pink", "green"]
global points
points = 0
play = False

scoreLabel = tk.Label(root, text="Your score: " + str(int(points)))#prevents error that there is no scoreboard

def randxy(a, b):
    """creates a random xy that is used in other functions

    :param a: a number
    :param b: a number
    :return: xy value used for slope in other function
    """
    return (random.randint(a, b), random.randint(a, b))

def setup():
    """makes circles at random locations with random slopes they'll move in'''

    :return: makes circles with certain slopes
    """
    button_countdown(counter, button_label)
    for i in range(20): #20 circles are created
        x = random.randint(20, 800)
        y = random.randint(20, 400)
        size = random.randint(10, 50)
        col = colors[random.randint(0, 5)]
        ID = canvas.create_oval(x, y, x + size, y + size, fill=col)#creaates oval
        coords.append([((2*x + size)/2), ((2*y + size)/2), size])#averges the ends of the circle to get the middle
        circle.append(ID)#adds circle ID to list
        dx, dy = randxy(-6, 6)#sets the slope of the cirlce which makes circle move in certain slopes
        slopes.append((dx, dy))#adds slope to list

def start():
    '''moves all circles'

    :return: makes circles move in certain direction
    '''
    for i in range(len(circle)):
        canvas.move(circle[i],
                    slopes[i][0],
                    slopes[i][1])
        # go to random location at random times:
        if random.randint(1, 100) < 2:
            x, y = randxy(100, 700)
            canvas.coords(i, x, y, x + 30, y + 30)
        #sets new coords
        coords[i][0] = slopes[i][0]
        coords[i][1] = slopes[i][1]
    # every 10 ms call this function again
    root.after(10, start)

def clicked(event):
    """clicks on circles and then calculates the points depending on circles

    :param event: object that provides xy coordinates of click
    :return: gives calculated points for clicking inside a specific circle
    """
    # the "event object" is automatically passed to the clicked function
    #  ...and it provides a way to get x and y coords of where click happened:
    global points

    xloc = event.x
    yloc = event.y
    #calculates if click was inside a circle
    for i in range(len(circle)):
        coords[i] = [(canvas.coords(circle[i])[0] + canvas.coords(circle[i])[2])/2, (canvas.coords(circle[i])[1] + canvas.coords(circle[i])[3])/2, coords[i][2]] #determines x and y middle of circle
        if ((coords[i][0] <= xloc + coords[i][2]/2) and (coords[i][0] >= xloc - coords[i][2]/2)) and ((coords[i][1] <= yloc + coords[i][2]/2) and (coords[i][1] >= yloc - coords[i][2]/2)): #determins if inside circle
            points += coords[i][2] - math.sqrt((xloc - coords[i][0]) ** 2 + (yloc - coords[i][1]) ** 2)#calculates and adds points

            #deletes all traces of circle
            canvas.delete(circle[i])
            del circle[i]
            del coords[i]
            label()#updates label
            break#if circle is clicked, breaks function to prevent error


def label():
    """updates the score of the player after clicking circle

    :return: returns the score of the player after clicking circle
    """
    global scoreLabel
    scoreLabel.pack_forget()#delets previous score
    scoreLabel = tk.Label(root, text="Your score: " + str(int(points)))#adds new score
    scoreLabel.pack()

def button_countdown(i, label):
    """countdown timer for the game

    :param i: the counter for amt of time
    :param label: the label where the score is displayed
    :return: gives the time left on the clock for the player
    """
    #counts down from the timer
    if i > 0:
        i -= 1
        label.set(i)
        root.after(1000, lambda: button_countdown(i, label))
    else:
        stop()#stops timer and calls function when time = 0

def stop():
    """resets the timer and deletes all of the circles

    :return:gives back original values so that game can be replayed
    """
    global circle
    global coords
    global points
    global slopes
    points = 0
    label()
    canvas.delete("all")

    #resets all variables
    circle = []
    coords = []
    slopes = []
    i = 0

#code for the score
counter = 30#time of game
button_label = tk.StringVar()
button_label.set(counter)
tk.Button(root, textvariable=button_label, command=stop).pack()

#sets up the window, proportions and buttons
root.title("Circles")
root.geometry("1100x500+20+20")#proportions of windows
tk.Button(root, text="make circles", command=setup).pack()
startbtn = tk.Button(root, text="move", command=start)
startbtn.pack()
canvas = tk.Canvas(root, bg="white", width=880, height=300)
canvas.pack(side=tk.LEFT)
canvas.bind("<Button-1>", clicked)

root.mainloop()