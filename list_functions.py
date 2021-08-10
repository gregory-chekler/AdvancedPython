def rotate_amt(shift, nums):
    copy = nums[:]
    for i in range(len(nums)):
        copy[i-shift-1] = nums[i]
    return copy
def is_paired_with_square(nums):
    for i in range(len(nums)):
        if nums[i] == (nums[i-1]**2 or nums[i+1]**2):
            return True
        else:
            return False
def number_of_evens(nums):
    return None
def longest_increasing(nums):
    best = []
    x = 0
    incr = [[] for i in range(len(nums))]
    for i in range(len(nums)):
        while (nums[i+x] > nums[i+x-1] and i+x+1 < len(nums)):
            incr[i].append(nums[i+x-1])
            x += 1
        x = 0
        if i+2 < len(nums):
            incr[i].append(nums[i+2])
    for i in range(len(incr)):
        if len(incr[i]) > len(best):
            best = incr[i]
    return best


def splittable(nums):
    one = []
    fir = 0
    sec = 0
    two = []
    for i in range((len(nums) // 2)):
        one.append(nums[i])
        fir = fir + nums[i]
    for i in range((len(nums) // 2), len(nums)):
        two.append(nums[i])
        sec = sec + nums[i]
    if fir == sec:
        return one, two
    else:
        return None
def tournament_winner(s1, b1, s2, b2):
    return None
def num_of_clumps(l):
    return None
def benefit_from_round(grades, names):
    return [None]
def my_fn():
    return None

n = [5, 7, 3, -1, 2]
n.sort()

print(-5//2)
