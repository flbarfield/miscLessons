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

    def delete_at_index(self, index):
        '''given an input, will delete value at index'''
        # If we're deleting the first node
        if index == 0:
            # Simply set the first node to be what is currently the
            # second node
            self.first_node = self.first_node.next_node

        current_node = self.first_node
        current_index = 0

        # First, we find the node immediately before the one we want
        # to delete and call it current node
        while current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1

        # We Find the node that comes after the one we're deleting:
        node_after_deleted_node = current_node.next_node

        # We change the link of the current_node to point to the
        # node_after_deleted_node, leave the node we want to delete
        # out of the list:
        current_node.next_node = node_after_deleted_node

    # Exercise #1:
    def print_all(self):
        '''prints all elements currently within the Linked List'''
        current_node = self.first_node

        while current_node:
            print(current_node.data)
            current_node = current_node.next_node

    # Exercise #3:
    def return_last(self):
        '''returns the last element within the linked list.'''
        current_node = self.first_node
        item_count = 0

        # obtains the number of items within linked list through
        # first loop
        while current_node:
            item_count += 1
            current_node = current_node.next_node

        current_node = self.first_node
        for i in range(item_count):
            current_node = current_node.next_node
            # The tail is going to be "None, and count stops at 4,
            # so the last actual element will be -2"
            if i == item_count - 2:
                return current_node.data

    # Exercise #4
    def reverse_list(self):
        '''returns the linked list in reversed order'''
        current_node = self.first_node
        previous_node = None

        while current_node:
            new_next = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = new_next
        self.first_node = previous_node
        self.print_all()

    def delete_middle_node(self, node):
        '''Given the name of an node, node will be deleted
        '''
        node.data = node.next_node.data
        node.next_node = node.next_node.next_node



node1 = Node('Once')
node2 = Node('upon')
node3 = Node('a')
node4 = Node('time')

node1.next_node = node2
node2.next_node = node3
node3.next_node = node4

input_list = LinkedList(node1)
# # print(input_list.first_node.data)
# print(input_list.read(3))
# print(input_list.index_of('time'))

# input_list.insert_at_index(3, 'purple')
# print(input_list.read(3))

# input_list.print_all()
# print(input_list.return_last())
input_list.reverse_list()
