'''This algorithm can be used instead of
doing nested for loops'''

def has_duplicate_value(array):
    '''this creates an array and inserts '1' at index
    positions that match the [i]. If there's already a 
    '1' present, True returns showing a duplicate has
    been found.
    '''
    existing_numbers = []

    for i in array:
        if existing_numbers[array[i]] == 1:
            return True
        else:
            existing_numbers[array[i]] = 1
    return False
