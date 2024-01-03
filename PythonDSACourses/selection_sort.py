'''implimentation of selection sort'''

def selection_sort(array):
    '''performs a selection sort. Lowest num's index is 
    captured and then brought to the beginning for each
    loop iteration.
    '''

    # doesn't have to run loop for the final time, as list
    # will be fully sorted by that point.
    for i in range(len(array) - 1):
        lowest_number_index = i

        # checks remaining values that other than the currently selected
        for j in range(i + 1, len(array)):
            # selects the minimum element in every iteration
            if array[j] < array[lowest_number_index]:
                lowest_number_index = j

            #swas the elements to sort the array
            if lowest_number_index != i:
                temp = array[i]
                array[i] = array[lowest_number_index]
                array[lowest_number_index] = temp

    return array

print(selection_sort([4, 6, 12, 321, 21, 5]))
