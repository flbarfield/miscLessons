'''implementation of partitioning a sorted array.'''

class SortableArray:
    '''sortable array declaration'''
    def __init__(self, array):
        self.array = array

    def partition(self, left_pointer, right_pointer):
        '''implementation of a partition'''
        # We always choose the right-most element as the pivot.
        # We keep the index of the pivot for later use:
        pivot_index = right_pointer

        # We grab the pivot value itself:
        pivot = self.array[pivot_index]

        # We start the right pointer immediately to the left of the
        # pivot
        right_pointer -= 1

        while True:
            # Move the pointer to the right as long as it points
            # to value that is less than the pivot:
            while self.array[left_pointer] < pivot:
                left_pointer += 1

            # Move the left pointer to the left as long as it points
            # to value that is greater than pivot
            while self.array[right_pointer] > pivot:
                right_pointer -= 1

            # We've now reached the point where we've stopped moving
            # both the left and right pointers.

            # We check whether the left pointer has reached or gone beyond
            # the right pointer. If it has, we break out of the loop so we can
            # swap the pivot later on in our code:
            if left_pointer >= right_pointer:
                break

            # If the left pointer is still to the left of the right pointer, we
            # swap the values of the left and right pointers
            else:
                self.array[left_pointer], self.array[right_pointer] = \
                self.array[right_pointer], self.array[left_pointer]

            # We move the left pointer over to the right, gearing up for the next
            # round of left and right pointer movements:
                left_pointer += 1

    # As a final step of the partition, we swap the value of the left pointer
    # with the pivot:
        self.array[left_pointer], self.array[pivot_index] = \
        self.array[pivot_index], self.array[left_pointer]

    # We return the left_pointer for the sake of the quicksort method, which will appear
    # later in this chapter:
        return left_pointer

    def quicksort(self, left_index, right_index):
        '''Implementation of quicksort'''
        # Base case: the subarray has 0 or 1 elements:
        if right_index - left_index <= 0:
            return

        # Partition the range of elements and grab the index of the pivot:
        pivot_index = self.partition(left_index, right_index)

        # Recusively call this quicksort method on whatever is to the left
        # of the pivot
        self.quicksort(left_index, pivot_index - 1)

    def quickselect(self, kth_lowest_value, left_index, right_index):
        '''Implementation of quickselect'''
        # If we reach a base case - that is, if that subarray has one cell,
        # we know we've found the value we're looking for:
        if right_index - left_index <= 0:
            return self.array[left_index]

        # Partition the array and grab the index of the pivot:
        pivot_index = self.partition(left_index, right_index)

        # If what we're looking for is to the left of the pivot:
        if kth_lowest_value < pivot_index:
            # Recursively perform quickselect on the subarray to the left of
            # the pivot:
            self.quickselect(kth_lowest_value, left_index, pivot_index - 1)

        elif kth_lowest_value > pivot_index:
            # Recursively perform quickselect on the subarray to the right of
            # the pivot:
            self.quickselect(kth_lowest_value, pivot_index + 1, right_index)
        else: # If kth_lowest_value == pivot_index...
            # if after the partition, the pivot position is in the same spot
            # as the kth lowest value, we've found the value we're looking for
            return self.array[pivot_index]

input_array = [0, 5, 2, 1, 6, 3]
new_array = SortableArray(input_array)
new_array.quicksort(0, len(input_array) - 1)
print('quicksort result: ' + str(new_array.array))

input_array2 = [0, 50, 20, 10, 60, 30]
new_array2 = SortableArray(input_array2)
new_array2.quickselect(1, 0, len(new_array2.array) - 1)
print('quickselect result: ' + str(new_array2.array))
