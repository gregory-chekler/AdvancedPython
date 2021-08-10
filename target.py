# !/usr/bin/python3
from tkinter import *

root = Tk()
canvas = Canvas(width=800, height=600, bg='white')
canvas.pack()

points = [300, 200, 500, 400]
canvas.create_oval(points, fill="yellow", outline="black",  width=1)

points = [325, 225, 475, 375]
canvas.create_oval(points, fill="red", outline="black",  width=1)

points = [350, 250, 450, 350]
canvas.create_oval(points, fill="green", outline="black",  width=1)

points = [375, 275, 425, 325]
canvas.create_oval(points, fill="blue", outline="black",  width=1)



root.mainloop()