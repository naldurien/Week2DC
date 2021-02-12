# 1) Create function that takes a number as an arg, increments by +1 and returns
# the result.

def addition(num):
    return num + 1

# 2) You're a basketball statistician. Given the numbers of 2-pointers and 3-pointers scored, find the final points for the team and return that value.

def points(twos, threes):
    score = twos * 2 + threes * 3
    return score

# 3) Given an array of random integers, create a function that finds the sum of the three largest numbers in the array.
jenny = [8, 6, 7, 5, 3, 0, 9]

def find_sum(array):
    array.sort(reverse=True)
    sum = array[0] + array[1] + array[2]
    return sum


#4)  Compare triplets. Givn two 3-value arrays, a and b,  compare both at each index. Whichever index has a greater value gains a point for that array. Return an array that lists a's total score first, then b's total score.


a = [8, 3, 2]
b = [4, 4, 4]

def triplets(a, b):
    a_pts = 0
    b_pts = 0
    scores = []
    for i in range(len(a)):
        if a[i] > b[i]:
            a_pts +=1
        elif b[i] > a[i]:
            b_pts +=1
        elif b[i] == a[i]:
            continue
    scores.append(a_pts)
    scores.append(b_pts)
    return scores

print(triplets(a, b))

