class Student:

    def __init__(self, name, x_pos, y_pos, room):
        self.name = name
        self.x = x_pos
        self.y = y_pos
        self.room = room

    def move(self, position, room):
        ###moves small amoutn and then if statement that uses bounce(direction)
        pass

    def bounce(self, direction):
        pass
    ###this need to get other characters coords and go opposite


class Room:
    def __init__(self, name, min_x, min_y, max_x, max_y):
        self.name = name
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y


#need to figure out how to objects not have collisions
#idea - using tkinter circles and use areas to figure out areas although may be slow
