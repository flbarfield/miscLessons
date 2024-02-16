'''Implementation of a Trie data structure'''

class TrieNode:
    '''Implementation of a TrieNode'''
    def __init__(self):
        self.children = {}

class Trie:
    '''Implementation of a Trie'''
    def __init__(self):
        self.root = TrieNode()
