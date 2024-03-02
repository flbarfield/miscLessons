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

    def dfs_traverse(self, vertex, visted_vertices=None):
        '''Implementation of dfs traverse, not fully understanding
          the ruby syntax however in my translation attempt, so the 
          code may not be fucntional until a revist. The pseudo code 
          is probably what's important.
          '''
        visted_vertices = {}
        # Mark vertex as visited by adding it to the
        # hash table:
        visted_vertices[vertex.value] = True

        # Print the vertex's value, so we can make sure
        # our traversal really works:
        print(vertex.value)

        # Iterate through the current vertex's adjacent
        # vertices:
        for adjacent_vertex in vertex.adjacent_vertices:
            # Ignore an adjacent vertex if we've already
            # visited it:
            if visted_vertices[adjacent_vertex]:
                continue
            # Recursively call this method on the adjacent
            # vertex
            self.dfs_traverse(vertex, visted_vertices)

    def dfs(self, vertex, search_value, visted_vertices):
        '''like the dfs traverse function, but motified to actually
        search for a particular vertex.
        '''
        visted_vertices = {}
        # Return the original vertex if it happens to be
        # the one we're searching for
        if vertex.value == search_value:
            return vertex

        visted_vertices[vertex.value] = True

        for adjacent_vertex in vertex.adjacent_vertices:
            if visted_vertices[adjacent_vertex]:
                continue

            # If the adjacent vertex is the vertex we're searching
            # for, just return that vertex:
            if adjacent_vertex.value == search_value:
                return adjacent_vertex

            # Attempt to find the vertex we're searching for by
            # recursively calling this method on adjacent vertex:
            vertex_were_searching_for = \
                self.dfs(adjacent_vertex, search_value, \
                        visted_vertices)

            # if we were able to find the correct vertex using the
            # above recursion, return the currect vertex:
            if vertex_were_searching_for:
                return vertex_were_searching_for

    def bfs_traverse(self, starting_vertex):
        '''breadth-first search'''
        queue = []
        visited_vertices = {}

        visited_vertices[starting_vertex.value] = True
        queue.append(starting_vertex)

        # While the queue is not empty:
        while queue:

            # Remove the first vertex off the queue and make it
            # the current vertex:
            current_vertex = queue.pop(1)

            # Print the current vertex's value:
            print(current_vertex.value)

            # Iterate over current vertex's adjacent vvertices:
            for adjacent_vertex in self.adjacent_vertices[current_vertex]:

                # If we have not yet visited the adjacent vertex:
                if not visited_vertices[adjacent_vertex.value]:

                    # Mark the adjacent vertex as visited:
                    visited_vertices[adjacent_vertex.value] = True

                    # Add the adjacent vertex to the queue:
                    queue.append(adjacent_vertex)

class WeightedGraphVertex:
    '''Note that this uses a hash table rather than an array
    for adjacent verticies. The adjacent vertex is the key and 
    the weight (of the edge from this vertex to the adjacent vertex)
    is the value 
    '''
    def __init__(self, value):
        self.value = value
        self.adjacent_verticies = {}

    def add_adjacent_vertex(self, vertex, weight):
        '''implementation of adding adjacent vertexes'''
        self.adjacent_verticies[vertex] = weight

# For dijkstra's algorithm below
class City:
    '''implementation of a city'''
    def __init__(self, name):
        self.name = name
        self.routes = {}

    def add_route(self, city, price):
        '''implementation of adding a route'''
        self.routes[city] = price



alice = Vertex('alice')
alice = Vertex('alice')
bob = Vertex('bob')
cynthia = Vertex('cynthia')

alice.add_adjacent_vertex('bob')
alice.add_adjacent_vertex('cynthia')
bob.add_adjacent_vertex('cynthia')
cynthia.add_adjacent_vertex('bob')

dallas = WeightedGraphVertex('Dallas')
toronto = WeightedGraphVertex('Toronto')

dallas.add_adjacent_vertex(toronto, 138)
toronto.add_adjacent_vertex(dallas, 216)
