'''Implementation of the heap data structure'''

class Heap:
    '''implementation of a heap'''
    def __init__(self, data):
        self.data = []
        self.root_node = data[0]
        self.last_node = data[-1]


newHeap = Heap([5, 4, 3, 2, 1])
print(newHeap.root_node)
