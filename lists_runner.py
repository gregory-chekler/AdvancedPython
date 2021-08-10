import list_functions as LF

def main():
    list_arg  = [-5, 3, 5, 25, 77, 5, 99]
    list_arg2 = [99, 101, -4, 5, 10001, 50, 71, 99]
    list_arg3 = [6, 5, 2]
    list_arg4 = [5, 7, 1, 99, 101, 500, 3, 4, 5]  
    # rotate:
    print("\n",4)

    print("\n",list_arg2, "rotated by 4 = ", LF.rotate_amt(4, list_arg2))

    # pair w/square:
    print("\n",5)
    ans = LF.is_paired_with_square(list_arg)
    if ans:
        print("\n",list_arg, "has a number next to it's square!")
    elif ans != None:
        LF.is_paired_with_square(list_arg2)
        print("\n",list_arg2, "does not have a number next to it's square :(")

    # longest increasing
    print("\n",6)
    print("\n","In", list_arg4,
          "the longest string of increasing values is",
          LF.longest_increasing(list_arg4))
    
    #splittable
    print("\n", 7)
    print("\n", "Should be: [1,  1, 1], [2, 1]:")
    print(LF.splittable([1, 1, 1, 2, 1]))
    print("\n", "Should be: None")
    print(LF.splittable([20, 1, 1, 2, 1]))
    print("\n", "Should be: [10]")
    print(LF.splittable([10, 10]))

    # tournament_winner
    print("\n",8)
    score1 = [55, 23, 655]
    score2 = [33, 100, 500]
    bonus_mult1 = [1, 2, 3]
    bonus_mult2 = [3, 2, 1]
    print("\n","Team #", LF.tournament_winner(score1,
                                         bonus_mult1,
                                         score2,
                                         bonus_mult2))
          
    # number of clumps
    print("\n",9)
    c = [35, 5, 5, 7, 93, 54, 2, 2, 2, 4, 4, 1, 2, 2]
    print("\n","In", c, "there are", LF.num_of_clumps(c), "clumps of numbers")

    # benefit from round
    print("\n",10)
    names = ["Joe", "Mary", "Ichabod"]
    grades = [76.6, 99.0, 82.1, 89.9, 92.8]
    results = LF.benefit_from_round(grades, names)
    for i in range(len(results)):
        if results[i] == True:
            print("\n",names[i], "will benefit from rounding", grades[i])
        elif results[i] != None:
            print("\n",names[i], "will NOT benefit from rounding", grades[i])
###############
main()