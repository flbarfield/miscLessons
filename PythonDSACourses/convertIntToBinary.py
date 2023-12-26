class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items
    

newStack = Stack()


def convert_int_to_bin(dec_num):
  newStack = Stack()

  if dec_num == 0:
    return 0

  while dec_num > 0:
    remainder = dec_num % 2
    newStack.push(remainder)
    dec_num = dec_num // 2
    

  bin = ''
  # originally tried this as a for e in newStack.get_stack(), but I think the 0s were causing problems. Maybe returning a falsy?
  while not newStack.is_empty():
    bin += str(newStack.pop())

  return (bin) 