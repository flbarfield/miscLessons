def double_array(array, index=0):
    if index >= len(array):
        return
    
    array[index] *= 2
    double_array(array, index + 1)