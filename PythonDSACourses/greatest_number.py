'''Exercise: rewrite this function that finds the greatest single 
number within an array, but does not have the effciency of O(N2)

def greatestNumber(array):
    for i in array:
        isIvalTheGreatest = True
    
    for j in array:
        if j > i:
            isIvalTheGreatest = False
    
    if isIValTheGreatest:
        return i


'''

def greatest_number(array):
    '''finds the greatest number within the array, speed
    of O(N)
    '''
    greatest_num = 0
    for i in array:
        if i > greatest_num:
            greatest_num = i
    return greatest_num

print(greatest_number([5, 6, 192, 5, 33, 5, 2]))
