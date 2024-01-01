'''Implementation of binary search'''

def binary_search(array, search_value):
    '''act of breaking array in half in order to
    quickly find search value's index
    '''
    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        midpoint = (upper_bound + lower_bound) // 2
        value_at_midpoint = array[midpoint]
        if search_value == value_at_midpoint:
            return midpoint
        if search_value < value_at_midpoint:
            upper_bound = midpoint - 1
        elif search_value > value_at_midpoint:
            lower_bound = midpoint +  1


print(binary_search([1,2,3,4,46,88,96,145], 88))
