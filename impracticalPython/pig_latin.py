'''
Objective/

write a program that takes a word as an input, and uses indexing
and slicing to return it's pig latin equivalent.
---------

Pseudocode:

Consonant definition: non-vowels

if word begins with a consonant, move that consonant to the end 
If the word begins with a vowel, you simply add 'way' to the end of the word.
else add 'ay' to the end of the word. 

Steps:
* define a 'phrase' variable
* loop through each word, where each word has been split by spaces
    * capture first letter
    * if word[1] = vowels:
        * add captured first letter to the end of the string, and add a 'way' at 
            the end of the word
        * else:
            add captured first letter to the end of the string and add an 'ay' at
            the end of the word
* print(phrase)   

'''

def make_pig_latin (words):
    '''doing the thing'''
    phrase = ''
    for word in words.split():
        f_letter = word[0].lower()
        if word[1] in ['a', 'e', 'i', 'o', 'u']:
            phrase += word[1:len(word)] + f_letter + 'way '
        else:
            phrase += word[1:len(word)] + f_letter + 'ay '
    print(phrase)

make_pig_latin("Hey Im Bob")