# !/usr/bin/python3
from tkinter import *

root = Tk()
canvas = Canvas(width=800, height=600, bg='blue')
canvas.pack()

num = 80


points = [200, 100, 300, 200]

canvas.create_oval(points, fill="yellow", outline="black",  width=1)

for i in range(0, 360, 40):
    canvas.create_polygon([0, 400+i, 800, 400+i, 800, 440+i, 0, 440+i], fill=('#00'+str(num)+"00"))
    num = int(str(num), 16)
    num = int(num - i/10)
    num = str(hex(num))[2:4]
    print(num)

root.mainloop()

