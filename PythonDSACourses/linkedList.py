class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        curNode = self.head
        while curNode:
            print(curNode.data)
            curNode = curNode.next

    def append(self, data):
        newNode = Node(data)
        # handles if  there's no head present
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        # moves node to node until None is encountered
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode

    def prepend(self, data):
        newNode = Node(data)

        newNode.next = self.head
        self.head = newNode

    def insertAfterNode(self, prevNode, data):
        # check if node to be inserted after is in linked list or not. If not, we return, otherwise the newNode is created
        if not prevNode:
            print('Previous node does not exist.')
            return
        newNode = Node(data)
        #sets pointer of new node to what prev node was pointing to
        newNode.next = prevNode.next
        #sets pointer of prev node to new node
        prevNode.next = newNode

    def deleteNode(self, key):
        # declaring starting point of linked List
        curNode = self.head
        # handling case if head is deleted
        if curNode and curNode.data == key:
            self.head = curNode.next
            #deletes the curNode
            curNode = None
            return
        
        prev = None
        # runs to the end of the linked list OR stops if key is found
        while curNode and curNode.data != key:
            prev = curNode
            curNode = curNode.next
        
        # implies key did not match any of the data of the current node, and there's no need to delete.
        if curNode is None:
            return
        
        # sets previous pointer to going-to-be-deleted node's pointer
        prev.next = curNode.next
        # deletes node
        curNode = None
    
    def delete_node_pos(self, pos):
        # checks if linked list is empty or not
        if self.head:
            curNode = self.head
            if pos == 0:
                # declares the next node the head, and then deletes itself with None
                self.head = curNode.next
                curNode = None
                return
            
            prev = None
            count = 0
            # increments count until it equals pos
            while curNode and count != pos:
                prev = curNode
                curNode = curNode.next
                count += 1

            # position was never found after traversing list
            if curNode is None:
                return
            
            # moves pointer from the prev node from the currently selected node, and  affixes it to the next node, before it finally deletes itself.
            prev.next = curNode.next
            curNode = None