from tkinter import *

root = Tk()
root.title("ListBox!")

def get_selected(e):
    '''called when a listbox element is selected
    e is the event sent to this function, but we don't need it'''
    global choice

    # NOTE: YOU DON'T NEED THE FOLLOWING IF YOU'RE JUST DISPLAYING INFO IN A TABLE!!!!

    selected = int(names_listb.curselection()[0]) # the position in the list is returned
    
    choice = choices[selected]  # get the name from that first column
    
    # TODO!!!!!! select corresponding age box on right

# variable to store what they have chosen:
choice = ""

# SILLY LIST OF CHOICES:
choices = ["Goblin", "Rabbit", "Master", "Dragon", "Cat", "Dog", "Bandos", 
           "Minnie Coop", "Kael’thas", "Vol’jin"]

ages = [1000, 2, 55, 125, 12, 13, 100, 3, 153, 83]

# CREATE THE ACTUAL LISTBOXES:
names_listb = Listbox(root)
ages_listb = Listbox(root)

# PUT THE ITEMS IN THE LISTBOX:
for item in choices:
    names_listb.insert(END, item)
for item in ages:
    ages_listb.insert(END, item)
    
# PACK THE LISTBOX INTO THE TK WINDOW:
names_listb.grid(row=0, column=0)
ages_listb.grid(row=0, column=1)

# BIND THE ACTION OF SELECTING A LISTBOX ITEM TO THE FUNCTION:
names_listb.bind("<<ListboxSelect>>", get_selected)


root.mainloop()