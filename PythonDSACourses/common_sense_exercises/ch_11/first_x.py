'''Use recursion to write a function that accepts a string
and returns the first index that contains the character 'x'
'''

def first_x(user_str):
    '''input is a string, returns the
    first index that an x is encountered.
    '''
    # signifies that x was found, and will stop the recursion
    if user_str[0] == 'x':
        return 0

    return first_x(user_str[1:(len(user_str))]) + 1

print(first_x('abcdefghijklmnopqrstuvwxyz'))
