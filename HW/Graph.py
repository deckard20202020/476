class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = set()

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def add_edge(self, edge):
        self.edges.add(edge)

    def remove_vertex(self, vertex):
        self.vertices.remove(vertex)

    def remove_edge(self, edge):
        self.edges.remove(edge)

    def get_adjacent_vertices(self, vertex):
        adjacent_vertices = set()
        for edge in self.edges:
            if edge.vertex1 == vertex:
                adjacent_vertices.add(edge.vertex2)
            elif edge.vertex2 == vertex:
                adjacent_vertices.add(edge.vertex1)
        return adjacent_vertices