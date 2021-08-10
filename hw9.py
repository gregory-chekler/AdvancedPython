#Use list comprehension to create a list of all the numbers from 500 to 1000
#that are divisible by 5, but not by 3

def pr0():
    nums = []
    [nums.append(i) for i in range(500, 1001) if (i % 5 == 0) and (i % 3 != 0)]
    print(nums)

#pr0()


#Use list comprehension to create a list with all the perfect cubes from 1
#cubed to 100 cubed

def pr1():
    cubes = [i**3 for i in range(1, 101)]
    print(cubes)

#pr1()

#Use list comprehension to create a list with all the perfect cubes from 1
#cubed to 100 cubed that are divisible by 5, but not by 3

def pr2():
    cubes = [i ** 3 for i in range(1, 101) if (i % 5 == 0) and (i % 3 != 0)]
    print(cubes)

#pr2()

#Use list comprehension to create a list of 100 random numbers between 9000 and
#99000. It should be one line and should start with: rand_nums = [random.

def pr3():
    import random
    rands = [random.randint(9000, 99000) for i in range(100)]
    print(rands)

#pr3()

#Use list comprehension to take a variable called text (a string variable) and
#from it create a list with all of the words in the text that have between 4 and 8
#letters (HINT: use .split() - look at notes in this packet or look it up if
#you're not sure)

def pr4(text):
    char = []
    words = text.split()
    [char.append(words[i]) for i in range(len(words)) if (4 <= len(words[i])) and (8 >= len(words[i]))]

    print(char)

#pr4('Use list comprehension to take a variable called text')

#Use list comprehension to create a 2D list that is 8x8 and has "R" stored in
#the 1st, 3rd, 5th, etc. positions and "B" stored in the even positions

def pr5():
    twod = [[],[],[],[],[],[],[],[]]
    [[twod[n].append('B') for i in range(4)] for n in range(8)]
    n = 0
    [[twod[n].insert(i, 'R') for i in range(8) if i % 2 == 0] for n in range(8)]
    [print(twod[x]) for x in range(8)]

#pr5()

#More challenging: Write a function that will use list comprehension to create
#a 2D nxn board where the colors are in a checkerboard configuration (i.e. black
#in 1st, 3rd, 5th of the first row, but then 2nd, 4th, 6th of the 2nd row, and
#repeat) Give this a shot - it's okay if you can't get it!

def pr6(rows, columns): ###Got it to work for even numbers
    grid = [[] for i in range(columns)]
    #First rows
    [[grid[n].append('B') for i in range(rows//2)] for n in range(columns) if n % 2 ==0]
    [[grid[n].insert(i, 'W') for i in range(columns) if i % 2 == 0] for n in range(columns) if n % 2 ==0]
    #Second Rows
    [[grid[n].append('B') for i in range(rows//2)] for n in range(columns) if n % 2 == 1]
    [[grid[n].insert(i + 1, 'W') for i in range(columns) if i % 2 == 0] for n in range(columns) if n % 2 == 1]
    [print(grid[x]) for x in range(columns)]

#pr6(4,4)

n = [-3, 4, 7, 155, 190, -100]
del n[3:6]
print(n)