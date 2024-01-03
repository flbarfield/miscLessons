'''implimentation of selection sort'''

def selection_sort(array):
    '''performs a selection sort. Lowest num's index is 
    captured and then brought to the beginning for each
    loop iteration.
    '''
    for index_a, item_a in enumerate(array):
        lowest_number_index = index_a

        for index_b, item_b in enumerate(array):
            if array[index_b] < array[index_a]:
                lowest_number_index = index_b
            if lowest_number_index != index_a:
                temp = array[index_a]
                array[index_a] = array[lowest_number_index]
                lowest_number_index = temp

    return array

print(selection_sort([4, 6, 12, 321, 21, 5]))
