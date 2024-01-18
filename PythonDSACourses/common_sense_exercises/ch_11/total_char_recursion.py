'''Write a recursive function that accepts an array
of strings and returns the total number of characters
across all the strings
'''

def total_char(arr):
    '''input: array of strings, returns total num
    of characters'''

    # setting base-case
    if len(arr) == 0:
        return 0
    # adding len of first string to the results of
    # calling total_char on subproblem
    return len(arr[0]) + total_char(arr[1:len(arr)])

print(total_char(['ab', 'c', 'def', 'ghij']))
