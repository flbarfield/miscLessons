'''Implementation of a tree node'''

class TreeNode:
    '''implementation of a Treenode'''
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left_child = left
        self.right_child = right

    def search(self, search_value, node):
        '''implementation of a search'''
        # Base case: if the node is nonexistent or if we've
        # found the value we're looking for:
        if node is None or node.value == search_value:
            return node
        # If the value is less than the curent node, perform
        # search on the left child:
        if search_value < node.value:
            return self.search(search_value, node.left_child)

        # If the value is greater than the current node, perform
        # search on the right child...search_value > node.value
        return self.search(search_value, node.right_child)

# Building the tree's structure
node1 = TreeNode(25)
node2 = TreeNode(75)
root = TreeNode(50, node1, node2)
