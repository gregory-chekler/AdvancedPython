# !/usr/bin/python3
from tkinter import *

root = Tk()
canvas = Canvas(width=800, height=600, bg='blue')
canvas.pack()
points = [200, 100, 300, 200, 300, 400, 200, 300]
pointstwo = [300, 200, 500, 200, 500, 400, 300, 400]
pointsthree = [200, 100, 400, 100, 500, 200, 300, 200]
canvas.create_polygon(points, fill="#bebfc1", outline="black" ,  width=1)
canvas.create_polygon(pointstwo, fill="#ababad", outline="black" ,  width=1)
canvas.create_polygon(pointsthree, fill="#858587", outline="black" ,  width=1)
root.mainloop()
