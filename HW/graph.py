from HW.edge import Edge
from HW.geometry import Geometry

class Graph:
    def __init__(self):
        self.vertices = {}
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = True
            self.adj_list[vertex] = []

    def add_edge(self, edge):
        self.add_vertex(edge.vertex1)
        self.add_vertex(edge.vertex2)
        if edge.vertex2 not in self.adj_list[edge.vertex1]:
            self.adj_list[edge.vertex1].append(edge.vertex2)
        if edge.vertex1 not in self.adj_list[edge.vertex2]:
            self.adj_list[edge.vertex2].append(edge.vertex1)

        # TODO: do we need to reverse the edge and add that as well???

    def get_adjacent_vertices(self, vertex):
        return self.adj_list[vertex]

    def getDistanceBetweenVertices(self, vertex1, vertex2):
        return Geometry.getEuclideanDistance((vertex1.x, vertex1.y), (vertex2.x, vertex2.y))

    def get_edges(self):
        edges = []
        for vertex in self.adj_list:
            for adj_vertex in self.adj_list[vertex]:
                edges.append(Edge(vertex, adj_vertex))
        return edges

    def get_vertices(self):
        return list(self.vertices.keys())




