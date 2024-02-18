'''Implementation of a Trie data structure'''

class TrieNode:
    '''Implementation of a TrieNode'''
    def __init__(self):
        self.children = {}

class Trie:
    '''Implementation of a Trie'''
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        '''Implementation of a search feature'''
        current_node = self.root

        for char in word:
            # If the current node has child key with current
            # character:
            if current_node.children.get(char):
                # Follow the child node:
                current_node = current_node.children[char]
            else:
                # If the current character isn't found among the
                # current node's children, our search word must
                # not be in the trie:
                return None

        return current_node
