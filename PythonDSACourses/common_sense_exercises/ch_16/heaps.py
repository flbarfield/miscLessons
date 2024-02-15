'''Implementation of the heap data structure'''

class Heap:
    '''implementation of a heap'''
    def __init__(self, data):
        self.data = data

    def root_node(self):
        '''obtains to root node of an array'''
        return self.data[0]

    def left_child_index(self, index):
        '''based upon a formula for obtaining the
        left child from a heap's underlying array
        '''
        return (index * 2) + 1

    def right_child_index(self, index):
        '''based upon a formula for obtaining the
        right child from a heap's underlying array
        '''
        return (index * 2) + 2

    def parent_index(self, index):
        '''based upon a formula for obtaining the
        parent index from a heap's underlying array
        '''
        return (index -1) // 2

    def insert(self, value):
        '''algorithm for insertion within a heap'''
        # Turn value into last node by inserting it at the end
        # of the array.
        self.data.push(value)

        # Keep track of the index of the newly inserted node:
        new_node_index = len(self.data) - 1

        # The follow loop executes the 'trickle up' algorithm.

        # If the new node is not in the root position, and it's
        # greater than it's parent node:
        while new_node_index > 0 and self.data[new_node_index] > \
        self.data[self.parent_index(new_node_index)]:

        # Swap the new node with the parent node:
            self.data[self.parent_index(new_node_index),
                      self.data[new_node_index]] = self.data[new_node_index], \
                      self.data[self.parent_index(new_node_index)]

        # Update the index of the new node:
            new_node_index = self.parent_index(new_node_index)

newHeap = Heap([5, 4, 3, 2, 1])
print(newHeap.root_node)
