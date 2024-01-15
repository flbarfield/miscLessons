'''Write a function that accepts an array of strings
and returns first dubplicate value it finds.

Make sure it has the efficientcy of O(n)
'''

def find_dupe(arr):
    '''finds dupes within array'''
    values = {}

    for i in arr:
        try:
            # if element already exists, it will be marked as True,
            # immediately short circuiting if it's a dupe.
            if values[i] is True:
                return i
        # if key is not found, adds the key with the value of True
        except KeyError:
            values[i] = True

    return 'No duplicates found'

print(find_dupe(['a', 'b', 'c', 'b']))
