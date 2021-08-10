import tkinter as tk
import random

root = tk.Tk()

circle = []

colors = ["red", "blue", "orange", "black", "pink", "green"]

def go():
    for i in range(20):
        x = random.randint(20, 400)
        y = random.randint(20, 400)
        size = random.randint(10, 50)
        col = colors[random.randint(0, 5)]
        ID = canvasL.create_oval(x, y, x + size, y + size, fill=col)
        circle.append(ID)

def go_two():
    for i in range(20):
        x = random.randint(20, 400)
        y = random.randint(20, 400)
        size = random.randint(10, 50)
        col = colors[random.randint(0, 5)]
        ID = canvasR.create_oval(x, y, x + size, y + size, fill=col)
        circle.append(ID)

def ClearAll():
    canvasR.delete("all")
    canvasL.delete("all")
    canvasL.delete(circle)
    canvasR.delete(circle)

def ClearLast():
    canvasR.delete("last")
    canvasL.delete("last")
    canvasL.delete(circle[-1])
    canvasR.delete(circle[-1])
    del circle[-1]

root.title("CircleMania")
root.geometry("900x500+20+20")
tk.Button(root, text="Left", command=go).pack()
tk.Button(root, text="Right", command=go_two).pack()
tk.Button(root, text="Clear All", command=ClearAll).pack()
tk.Button(root, text="Clear Last", command=ClearLast).pack()
# btn = tk.Button(root, text="Click me!")
# btn.pack()
canvasL = tk.Canvas(root, bg="red", width=440, height=300)
canvasL.pack(side=tk.LEFT)
canvasR = tk.Canvas(root, bg="blue", width=440, height=300)
canvasR.pack(side=tk.RIGHT)



root.mainloop()
