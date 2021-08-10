import random
class School:
    def __init__(self):
        self.capacity = random.randint(1000, 1500)

    def calc_years_to_max_capacity(self, enrollment):
        print("hi")
        self.years = (self.capacity - enrollment) // 100
        print(self.years)

cc = School()
cc.calc_years_to_max_capacity(1100)
print(str(cc.years) + "to max...")