'''
The objective:

Randomly generate funny sidekick names using Python code that conforms to established 
style guidelines.

The strategy:
* start with two lists, one with first name, other with last
* randomly generate an element from one, then the other
    * print result (in red, that's the point of file=sys.stderr)
* have an option to repeat the process, or exit the program.
'''
import sys
import random

first_names = ['Bobby', 'Sugar', 'Grog', 'Vlad', 'The', 'Alfred', 'Bop',
              'Bad News', 'Baby Oil', 'Chewy']
last_names = ['Bodankins', 'Strongjaw', 'Wilafred', 'the Impaler',
             'Supafly', 'Boomstick', 'Bojangles', 'Wellington', 'Bears'] 

def prompt_choice ():
    '''logic for handling user input'''
    choice = input('>>> Y to repeat --- N to exit \n')
    if choice.lower() == 'y':
        generate_name(first_names, last_names)
    elif choice.lower() == 'n':
        sys.exit()
    else:
        print('\n Invalid input.')
        prompt_choice()


def generate_name (f_name_list, l_name_list):
    '''main function'''
    f_name_index = int(random.random() * len(f_name_list))
    l_name_index = int(random.random() * len(l_name_list))

    print(f'\n Your name is: {f_name_list[f_name_index]} {l_name_list[l_name_index]}\
           \n \n Would you like to generate another name?\n', file=sys.stderr)
    prompt_choice()

generate_name(first_names, last_names)
