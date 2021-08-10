class school:
    def __init__(self, name, floors=4, rooms_per_floor=12, has_gallery=False):
        '''constructor'''
        self.name = name
        self.floors = floors
        self.rooms_per_floor = rooms_per_floor
        self.has_gallery = has_gallery
        self.room_nums = []

        for i in range(self.floors * self.rooms_per_floor):
            self.room_nums.append(i)

        self.students = []

    def add_students(self, num_students):
        '''creates random students for school'''
        for i in range(num_students):
            self.students.append(chr(65+i))

    def __str__(self):
        '''you'll see'''
        return self.name + " is a school with " + str(self.floors) + " floors"

    def show_students(self):
        for i in range(len(self.students)):
            print(i, self.students[i])

