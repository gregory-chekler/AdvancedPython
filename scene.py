# !/usr/bin/python3
from tkinter import *

root = Tk()
canvas = Canvas(width=800, height=600, bg='blue')
canvas.pack()

num = 80

x=40

points = [200, 100, 300, 200]

canvas.create_oval(points, fill="yellow", outline="black",  width=1)

for i in range(0, 360, 40):
    canvas.create_polygon([0, 400+i, 800, 400+i, 800, 440+i, 0, 440+i], fill=('#00'+str(num)+"00"))
    num = int(str(num), 16)
    num = int(num - i/10)
    num = str(hex(num))[2:4]
    print(num)


canvas.create_polygon([300, 800, 390, 400], fill="yellow", outline="black",  width=1)
canvas.create_polygon([500, 800, 410, 400], fill="yellow", outline="black",  width=1)
canvas.create_polygon([300, 800, 390, 400, 410, 400, 500, 800], fill="yellow", outline="black",  width=1)
for i in range(0, 4):
    canvas.create_polygon([390+2*i, 600 - i*20 + x, 390+2+2*i, 550 - i*20 + x, 410-2-2*i, 550 - i*20 + x, 410-2*i, 600 - i*20 + x], fill="black")
    x -= 40

root.mainloop()