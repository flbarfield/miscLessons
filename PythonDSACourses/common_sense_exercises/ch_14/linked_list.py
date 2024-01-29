'''implementation of linked list'''

class Node:
    '''implementation of a node'''
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    '''implementation of linked list'''
    def __init__(self, first_node):
        self.first_node = first_node

    def read(self, index):
        '''reads data from inputted node index.'''
        # We begin at the first node of the list
        current_node = self.first_node
        current_index = 0

        try:
            while current_index < index:
                # We keep following the links of each node until
                # we get the index we're searching for:
                current_node = current_node.next_node
                current_index += 1
        except AttributeError:
            return 'Input index out of range.'
        # If we're past the end of the list, that means the
        # value cannot be found in the list, so it returns none
        return current_node.data

node1 = Node('Once')
node2 = Node('upon')
node3 = Node('a')
node4 = Node('time')

node1.next_node = node2
node2.next_node = node3
node3.next_node = node4

input_list = LinkedList(node1)
# print(input_list.first_node.data)
print(input_list.read(3))
