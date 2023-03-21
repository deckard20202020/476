from Vertex import Vertex
from Graph import Graph
from Edge import Edge

def makeAVertex(x, y, p):
    v = Vertex(x, y, p)
    return v

if __name__ == "__main__":
    vertex1 = makeAVertex(0, 0, None)
    vertex2 = makeAVertex(0, 1, vertex1)
    edge1 = Edge(vertex1, vertex2)

    graph = Graph()

    graph.add_vertex(vertex1)
    graph.add_vertex(vertex2)
    graph.add_edge(edge1)

    print("Here are the vertices")
    # print(graph.vertices)
    for v in graph.vertices:
        print(v.x, v.y, v.parent)
    print()

    print("Here are the Edges")
    # print(graph.edges)
    for e in graph.edges:
        print(e.vertex1.x, e.vertex1.y, e.vertex2.x, e.vertex2.y)
    print()

    if (vertex1 == vertex2):
        print("Vertex1 and Vertex2 are equal")
    else:
        print("Vertex1 and Vertex2 are not equal")
    print()

    vertex3 = Vertex(0,0, vertex2)
    if (vertex1 == vertex3):
        print("Vertex1 and Vertex3 are equal")
    else:
        print("Vertex1 and Vertex3 are not equal")
    print()

    edge2 = Edge(vertex2, vertex1)
    print(edge1 == edge2)
    print()



