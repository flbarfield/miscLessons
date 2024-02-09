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

    def insert(self, value, node):
        '''implementation of insert'''
        if value < node.value:

        # If the left child does not exist, we want to insert the
        # value as the left child:
            if node.left_child is None:
                node.left_child = TreeNode(value)
            else:
                self.insert(value, node.left_child)
        elif value > node.value:

            # If the right child does not exist, we want to insert
            # the value as the right child:
            if node.right_child is None:
                node.right_child = TreeNode(value)
            else:
                self.insert(value, node.right_child)

    def lift(self, node, node_to_delete):
        '''lift is implemented more for the purpose of the delete method.
        It accomplishes 4 things. 

        1) It finds the successor node.

        2) It overwrites the value of node_to_delete and makes it the value
        of the successor node. This is how we get the successor node into the 
        correct spot. Note that we don't move the actual successor node object
        anywhere; we simply copy its value into the node we're deleting.

        3) To eliminate the original successor node object, the function then turns
        the original successor node's right child into it's parents left child.

        4) After all the recursion is said and done, it finally returns either the
        original right_child passed into it in the first place, or None if the original
        right_child ended up serving as a successor node (which would happen if it
        had no left children of its own).
        '''
        # If the current node of this function has a left child, we recursively
        # call this function to continue down the left subtree to find the
        # successor node.
        if node.left_child:
            node.left_child = self.lift(node.left_child, node_to_delete)
            return node

        # If the current node has no left child, that means the current node of
        # this fucntion is the successor node, and we take it's value. and make it
        # the new value of the node that we're deleting:
        else:
            node_to_delete.value = node.value
            # We return the successor node's right child to be now used as it's
            # parent's left child:
            return node.right_child

    def delete(self, value_to_delete, node):
        '''implementation of delete'''
        # The base case is when we've hit the bottom of the tree,
        # and the parent node has no children:
        if node is None:
            return None

        # If the value we're deleting is less or greater than the current
        # node, we set the left or right child respectively to be the return
        # value of a recursive call of this very method on the current node's
        # left or right subtree
        elif value_to_delete < node.value:
            node.left_child = self.delete(value_to_delete, node.left_child)

        # We return the current node (and it's subtree if existent) to
        # be used as the new value of it's parent's left or right child:
            return node
        elif value_to_delete > node.value:
            node.right_child = self.delete(value_to_delete, node.right_child)
            return node

        # If the current node is the one we want to delete:
        elif value_to_delete == node.value:
            # If the current node has no left child, we delete it by returning
            # it's right child (and it's subtree if existent) to be it's parent's
            # new subtree:
            if node.left_child is None:
                return node.right_child

                # (if the current node has no left OR right child, this ends up being None as
                # per the first line of code in this function)

            elif node.right_child is None:
                return node.left_child

            # If the current node has two children, we delete the current node
            # by calling the lift function (below), which changes the current
            # node's value to the value of it's sucessor node:
            else:
                node.right_child = self.lift(node.right_child, node)
                return node

    def traverse_and_print(self, node):
        '''Implementation of traverse and print'''
        if node is None:
            return
        self.traverse_and_print(node.left_child)
        print(node.value)
        self.traverse_and_print(node.right_child)

# Building the tree's structure
node1 = TreeNode(25)
node2 = TreeNode(75)
root = TreeNode(50, node1, node2)
