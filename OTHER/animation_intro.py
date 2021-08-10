import tkinter as tk
import random

root = tk.Tk()
root.title("Moving")
root.geometry('900x600')
canvas = tk.Canvas(root, bg="red", width=800, height=500)
canvas.pack()


def randxy(a, b):
    return (random.randint(a, b), random.randint(a, b))


squares = []
slopes = []
NUM_SQUARES = 20


def setup():
    '''makes squares at random locations with random slopes they'll move in'''
    for i in range(NUM_SQUARES):
        x, y = randxy(100, 400)
        s = canvas.create_rectangle(x, y, x + 15, y + 15, fill="blue")
        squares.append(s)
        dx, dy = randxy(-6, 6)
        slopes.append((dx, dy))


def start():
    '''moves all squares'''
    for sq in range(NUM_SQUARES):
        canvas.move(squares[sq],
                    slopes[sq][0],
                    slopes[sq][1])
        # go to random location at random times:
        if random.randint(1, 100) < 2:
            x, y = randxy(100, 700)
            canvas.coords(sq, x, y, x + 15, y + 15)
    # every 5 ms call this function again
    root.after(5, start)

startbtn = tk.Button(root, text="move", command=start)
startbtn.pack()

setup()
root.mainloop()