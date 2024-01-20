'''The number sequence called 'Triangular Numbers' is a pattern
in which the Nth number in the pattern is N+ the previous number

Write a function that accepts a number for N and returns the correct 
number for the series. That is, if the function was passed the number
7, the function would return 28
'''

def tri_num(user_num):
    '''takes in a value, returns the triangular value of the inputted 
    num'''
    # adds numbers backwards, until you reach the first digit, 1
    if user_num == 1:
        return 1

    # each iteration, usernum return total is added to a decrementing user num
    return user_num + tri_num(user_num - 1)

print(tri_num(7))
