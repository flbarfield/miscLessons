'''Write a function that returns the first
non duplicated character in a string

steps:
loop through input string
    if there's an error (not existing)
        add character to dict with value of 
        false
    if there's not an error (signifies existing)
        increase value by one
loop through dict keys
    if value = 1
    return key
'''

def non_dupe(input_str):
    '''givin a word, returns the first non
    duplicated character'''

    characters = {}

    for letter in input_str:
        try:
            characters[letter] += 1
        except KeyError:
            characters[letter] = 1
    for key, value in characters.items():
        if value == 1:
            return key

print(non_dupe('minimum'))
