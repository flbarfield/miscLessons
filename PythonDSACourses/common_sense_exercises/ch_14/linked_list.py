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

    def index_of(self, value):
        '''given a value, will find the index of that value within
        the linked list
        '''
        # We begin at the first node of the list:
        current_node = self.first_node
        current_index = 0

        while current_node:
            # If we find the data we're looking for, we return the index:
            if current_node.data == value:
                return current_index
            # Otherwise, we move on to the next node:
            current_node = current_node.next_node
            current_index += 1
            # If we get through the entire list without finding the data,
            # we return None:
        return None

    def insert_at_index(self, index, value):
        '''given an index, will insert the given value at that index'''

        # We create the new node with the provided value:
        new_node = Node(value)

        # If starting at the begining of the list:
        if index == 0:
            # Have our new node link to what was the first node.
            new_node.next_node = self.first_node
            self.first_node = new_node
            return

        # If inserting anywhere other than the beginning:

        current_node = self.first_node
        current_index = 0

        # First, we access the node immediately before the new node will
        # go
        while current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1

        # Have the new node link to the next node:
        new_node.next_node = current_node.next_node

        # Modify the link of the previous node to point to our new node.
        current_node.next_node = new_node

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
print(input_list.index_of('time'))

input_list.insert_at_index(3, 'purple')
print(input_list.read(3))
