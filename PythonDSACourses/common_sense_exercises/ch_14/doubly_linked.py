'''Implementation of a doubly linked list'''

class Node:
    '''Implementation of a node'''
    def __init__(self, data, next_node=None, previous_node=None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node

class DoublyLinkedList:
    '''Implementation of a doubly linked list'''
    def __init__(self, first_node=None, last_node=None):
        self.first_node = first_node
        self.last_node = last_node

    def insert_at_end(self, value):
        '''takes an element and inserts it into the
        end of the the linked list
        '''
        new_node = Node(value)

        # If there are no elements yet in the linked list:
        if self.first_node is not True:
            self.first_node = new_node
            self.last_node = new_node

        # If linked list has at least 1 node:
        else:
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node  = new_node

    def remove_from_front(self):
        '''removes an element from the front of the
        doubly linked list
        '''
        removed_node = self.first_node
        self.first_node = self.first_node.next_node
        return removed_node

    # Exercise #2
    def reverse_print(self):
        '''prints in reverse all elements within linked list
        '''
        current_node = self.first_node

        while current_node:
            current_node = current_node.previous_node
            print(current_node.data)
            if current_node.data == self.first_node.data:
                break

class Queue:
    '''Implementation of a queue'''
    def __init__(self):
        self.data = DoublyLinkedList()

    def enqueue(self, element):
        '''adds an element to the back of the queue'''
        self.data.insert_at_end(element)

    def dequeue(self):
        '''takes an element off the front of the queue...
        Returns removed node.'''
        self.data.remove_from_front()

    def read(self):
        '''Returns all elements within the queue, until there's 
        nothing more to return'''
        while self.data.first_node:
            return self.data.first_node

node1 = Node('once')
node2 = Node('upon')
node3 = Node('a')
node4 = Node('time')

node1.previous_node = node4
node1.next_node = node2
node2.previous_node = node1
node2.next_node = node3
node3.previous_node = node2
node3.next_node = node4
node4.previous_node = node3
node4.next_node = node1

input_list = DoublyLinkedList(node1, node4)

input_list.reverse_print()
