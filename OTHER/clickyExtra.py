import tkinter as tk

root = tk.Tk()
root.title("Clicky")
root.geometry("500x500")
root.config(bg="black")


def something_occurred(event):
    # x_ and y_root give location within root window:
    print("Location within tk window:       (" + str(event.x_root) + ", " + str(event.y_root) + ")")

    # get name of whatever widget is involved in the event:
    print("\tWIDGET:", str(event.widget)[2:])  # THIS IS A STRING, NOT AN INT!!!!!

    # event.x and .y give the location of the event within the bound widget:
    xloc = event.x
    yloc = event.y
    print("\tlocation within widget:    (" + str(xloc) + ", " + str(yloc) + ")")

    print("type of event", event.type)

    print("=========================================================")


root.bind("<Motion>", something_occurred)

root.bind("<Button-1>", something_occurred)  # to see type of event

canvas = tk.Canvas()
canvas.pack()
canvas.config(bg="black", width=500, height=380)
canvas.create_text(40, 30, fill="white", font=("Verdana"), text="canvas")

canvas2 = tk.Canvas()
canvas2.config(bg="red", width=500, height=50)
canvas2.pack()
canvas2.create_text(40, 30, fill="white", font=("Verdana"), text="canvas2")

canvas3 = tk.Canvas()
canvas3.config(bg="blue", width=300, height=70)
canvas3.pack()
canvas3.create_text(40, 30, fill="white", font=("Verdana"), text="canvas3")

root.mainloop()