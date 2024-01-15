'''function accepts a string that contains
all letters of the alphabet except one. Return
the missing letter with O(N) complexity

'''

def find_missing_letter(user_str):
    '''returns missing alphabet'''
    mod_string = list(user_str.replace(' ', ''))

    alphabet = [
        'a', 'b', 'c', 'd',
        'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p',
        'q', 'r', 's', 't',
        'u', 'v', 'w', 'x',
        'y', 'z'
    ]

    for i in mod_string:
        if i in alphabet:
            alphabet.remove(i)

    return alphabet

print(find_missing_letter('the quick brown fox jumps over the lay dog'))
