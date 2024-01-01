'''Implementation of a Stack in Python'''

class Stack():
    '''defines a Stack'''
    def __init__(self):
        self.items = []

    def push(self, item):
        '''Pushes element to the end of the
        stack
        '''
        self.items.append(item)

    def pop(self):
        '''pops an element from the end of the
        stack'''

        return self.items.pop()

    def is_empty(self):
        '''checks if stack is empty'''
        return not self.items

    def peek(self):
        '''checks top of the stack for value'''
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        '''returns stack contents'''
        return self.items


def convert_int_to_bin(dec_num):
    '''converts given int to binary'''

    new_stack = Stack()

    if dec_num == 0:
        return 0

    while dec_num > 0:
        remainder = dec_num % 2
        new_stack.push(remainder)
        dec_num = dec_num // 2


    binary = ''
    # originally tried this as a for e in newStack.get_stack(), but
    # I think the 0s were causing problems. Maybe returning a falsy?
    while not new_stack.is_empty():
        binary += str(new_stack.pop())

        return binary
