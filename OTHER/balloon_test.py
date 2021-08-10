# NOTE: MUST USE Python 3.6 or higher

import Pmw
import tkinter as tk
root = tk.Tk()
root.title("Balloon example")
root.geometry("300x300")
# make a balloon object:
balloon = Pmw.Balloon(root)

button = tk.Button(root, text="Hover!")
button.pack(ipadx=10, ipady=10, padx=10, pady=10)

# bind hovering on th ebutton to this message:
balloon.bind(button, "This is a 'balloon' \n it acts like a popup window,  \n" +
               "  sometimes called 'tooltiptext'.\n"+
             "  As you can see, you can put a lot"+
             "  of text in this thing...")
'' \

info = tk.Label(root, text="see me")
info.pack()
balloon.bind(root, "To find treasure go to castle\n\n\nThis is cool")
button2 = tk.Button(root, text="More!")
button2.pack(ipadx=10, ipady=10, padx=10, pady=10)

# bind hovering on th ebutton to this message:
balloon.bind(button2, "You could put all kinds of interesting" +
             " and useful information here.\n"+
             " Or, you could put 'easter eggs in these...")
tk.mainloop()