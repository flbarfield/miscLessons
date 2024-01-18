'''Use recursion to write a function that accepts an array
of numbers and returns a new array containing just the even
numbers
'''

def only_evens(arr):
    '''takes an arrays of nums and an index, returns
    only even numbers that are within that array'''
    # base case
    if arr == []:
        return []

    # if value of index 0 is even, calls funct again until
    # len of array is reached. Each being checked for
    # evens along the way.
    if arr[0] % 2 == 0:
        return [arr[0]] + only_evens(arr[1:len(arr)])

    return only_evens(arr[1:len(arr)])

print(only_evens([1,2,3,4,5,6,7,8,9]))
