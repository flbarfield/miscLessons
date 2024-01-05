''' 1) Starts with index 1 temp-removed and stored. 

2) Shifting phase begins where each value to the left of the gap is compared 
to the temp variable, and is shifted to the right if larger. Once variable 
lower than temp-value is encountered or the end of the array is reached, 
phase is over. 

3) Temp-removed value is then inserted into the current gap.

4) Steps 1-3 are then repeated as subsequent pass-throughs are done, sorting
is finished noce the pass-through begins at the final index of the array; 
signifying that the array has been fully sorted.
'''

def insertion_sort(array):
    '''Implementation'''
    for index in range(1, len(array)):
        temp_value = array[index]
        # Position always starts to the left of curr index
        # Keeps moving left with each pass-through as we compare
            # each value to the temp value
        position = index - 1

        while position >= 0:
            if array[position] > temp_value:
                # Shifts the left left value to the right
                array[position + 1] = array[position]
                # Decrements "position" counter by 1
                position = position - 1
            else:
                break

        # Moves the temp value into the gap
        array[position +  1] = temp_value

    return array

print(insertion_sort([2, 5, 88, 3, 1, 43, 2121]))
