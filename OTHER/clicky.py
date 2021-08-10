import tkinter as tk

root = tk.Tk()
root.title("Clicky")
root.geometry("700x700")
root.config(bg="black")


def clicked(event):
    # the "event object" is automatically passed to the clicked function
    #  ...and it provides a way to get x and y coords of where click happened:
    xloc = event.x
    yloc = event.y

    print("clicked at (", xloc, ",", yloc, ")")

    # make a small square centered at that point:
    canvas.create_rectangle(xloc - 4, yloc - 4, xloc + 4, yloc + 4, fill="lightgreen")


canvas = tk.Canvas()
canvas.pack(pady=100)  # pushes the canvas away from the top of the root window

canvas.config(bg="black", width=600, height=600)

canvas.bind("<Button-1>", clicked)

root.mainloop()