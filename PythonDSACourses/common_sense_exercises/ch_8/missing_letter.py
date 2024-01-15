'''function accepts a string that contains
all letters of the alphabet except one. Return
the missing letter with O(N) complexity

'''

# ---first attempt---
# def find_missing_letter(user_str):
#     '''returns missing alphabet'''
#     mod_string = list(user_str.replace(' ', ''))

#     alphabet = [
#         'a', 'b', 'c', 'd',
#         'e', 'f', 'g', 'h',
#         'i', 'j', 'k', 'l',
#         'm', 'n', 'o', 'p',
#         'q', 'r', 's', 't',
#         'u', 'v', 'w', 'x',
#         'y', 'z'
#     ]

#     for i in mod_string:
#         if i in alphabet:
#             alphabet.remove(i)

#     return alphabet

#------------------------------
# Hashtable O(N) attempt
def find_missing_letter(user_str):
    '''returns missing letter'''
    hash_table = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for letter in user_str:
        hash_table[letter] = True

    for test_letter in alphabet:
        try:
            hash_table[test_letter]
        # exception is thrown when the key isn't found,
        # signifying that it doesn't exist in string
        except KeyError:
            return test_letter

    return 'No duplicates found.'


print(find_missing_letter('the quick brown fox jumps over the lay dog'))
