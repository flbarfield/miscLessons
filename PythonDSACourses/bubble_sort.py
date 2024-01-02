'''Sorting algorithm that "bubbles up" the highest
value into the correct position one at a time.
'''

def bubble_sort(input_list):
    '''executes bubble_sort'''
    unsorted_until_index = len(input_list) - 1
    sorted_check = False

    while not sorted_check:
        sorted_check = True
        for i in range(unsorted_until_index):
            if input_list[i] > input_list[i+1]:
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
                sorted_check = False
        unsorted_until_index -= 1
    return input_list

print(bubble_sort([10, 231, 20, 11, 1]))
