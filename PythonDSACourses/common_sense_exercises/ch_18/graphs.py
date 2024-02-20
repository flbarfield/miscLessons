'''Implementation of a graph data structure.
in an object-oriented approach
'''

class Vertex:
    '''implementation of a Vertex'''
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
        '''implementation of add adjacent
        vertex
        '''
        if vertex in self.adjacent_vertices:
            return
        # Appends the vertex if it is not already
        # present. If this were an undirected graph,
        # only this line would be necessary.
        self.adjacent_vertices.append(vertex)

alice = Vertex('alice')
alice = Vertex('alice')
bob = Vertex('bob')
cynthia = Vertex('cynthia')

alice.add_adjacent_vertex('bob')
alice.add_adjacent_vertex('cynthia')
bob.add_adjacent_vertex('cynthia')
cynthia.add_adjacent_vertex('bob')
