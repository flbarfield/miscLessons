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

    def has_greater_child (self, index):
        '''helper fucntion for the delete method'''
        # We check whether the node at the index has left or right children,
        # and if either of those children are greater tha nthe node at index
        check = (self.data[self.left_child_index(index)] and \
                self.data[self.left_child_index(index)] > self.data[index]) or \
                (self.data[self.right_child_index(index)] and \
                self.data[self.right_child_index(index)]) > self.data[index]

        return check

    def calculate_larger_child_index(self, index):
        '''helper fucntion for the delete method'''
        # If there is no child:
        if not self.data[self.right_child_index(index)]:
            # Return left child index:
            return self.left_child_index(index)

        if self.data[self.right_child_index(index)] > self.data[self.left_child_index]:
            return self.right_child_index(index)
        else: # If the child value is greater or equal to right child:
            # Return the left child index:
            return self.left_child_index(index)

    def delete(self):
        '''implements the deletion algorithm'''
        # We only ever delete the root node of a heap, so we pop
        # the last node from the array and make it the root node:
        self.data[0] = self.data.popitem()
        # Track the current index of the 'trickle node':
        trickle_node_index = 0

        # The following loop executes the 'trickle down' algorithm:

        # We run the loop as long as the trickle node has a child
        # that is greater than it:
        while self.has_greater_child(trickle_node_index):
            # Save larger child index in variable:
            larger_child_index = self.calculate_larger_child_index(trickle_node_index)

            # Swap the trickle node with its larger child:
            self.data[trickle_node_index], self.data[larger_child_index] = \
            self.data[larger_child_index], self.data[trickle_node_index]

            # Update trickle node's new index:
            trickle_node_index = larger_child_index

newHeap = Heap([5, 4, 3, 2, 1])
print(newHeap.root_node)
