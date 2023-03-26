import math
import numpy as np

from matplotlib import pyplot as plt, patches

from HW import geometry, graph, planning
from HW.geometry import Geometry
from planning import Planning
from vertex import Vertex
from graph import Graph
from edge import Edge

def makeAVertex(x, y, p):
    v = Vertex(x, y, p)
    return v

if __name__ == "__main__":
    # vertex1 = makeAVertex(0, 0, None)
    # vertex2 = makeAVertex(0, 1, vertex1)
    # edge1 = Edge(vertex1, vertex2)
    #
    # graph = Graph()
    #
    # graph.add_vertex(vertex1)
    # graph.add_vertex(vertex2)
    # graph.add_edge(edge1)
    #
    # print("Here are the vertices")
    # # print(graph.vertices)
    # for v in graph.vertices:
    #     print(v.x, v.y, v.parent)
    # print()
    #
    # print("Here are the Edges")
    # # print(graph.edges)
    # for e in graph.edges:
    #     print(e.vertex1.x, e.vertex1.y, e.vertex2.x, e.vertex2.y)
    # print()
    #
    # if (vertex1 == vertex2):
    #     print("Vertex1 and Vertex2 are equal")
    # else:
    #     print("Vertex1 and Vertex2 are not equal")
    # print()
    #
    # vertex3 = Vertex(0,0, vertex2)
    # if (vertex1 == vertex3):
    #     print("Vertex1 and Vertex3 are equal")
    # else:
    #     print("Vertex1 and Vertex3 are not equal")
    # print()
    #
    # edge2 = Edge(vertex2, vertex1)
    # print(edge1 == edge2)
    # print()

    # g = Graph()
    #
    # vertex1 = makeAVertex(-1, 0, None)
    # vertex2 = makeAVertex(-1.2, 0, vertex1)
    # edge = Edge(vertex1, vertex2)
    # point = makeAVertex(0, 1, None)
    # print(edge.getNearestPoint(point))
    #
    # listOfVerticies = edge.getDiscritizedState(.1)
    # # for i in range(listOfVerticies):
    # #     print(listOfVerticies[i].x + " " + listOfVerticies[i].y)
    # for vertex in listOfVerticies:
    #     print(f"x: {vertex.x}, y: {vertex.y}")

    # for i in range(100):
    #     randomNumber = Planning.getRandomNumber(1, 10)
    #     print(randomNumber)

    # for i in range(100):
    #     planning = Planning(-3, 3, -1, 1)
    #     randomVertex = planning.getRandomPoint()
    #     print(f"x: {randomVertex.x}, y: {randomVertex.y}")

    # point1 = Vertex(0,1)
    # point2 = Vertex(0,0)
    # dist = Geometry.getEuclideanDistance(point1, point2)
    # print(dist)

    # start = Vertex(0,0)
    # goal = Vertex(0,1)
    # planning = Planning(-3, 3, -1, 1, .5, start, goal)
    # point1 = Vertex(0, .1)
    # edge = Edge(start, point1)
    # planning.graph.add_edge(edge)
    # haveWeMadeIt1 = planning.stopConfiguration()
    # print(haveWeMadeIt1)
    # print()
    # point2 = Vertex(0, .6, point1)
    # edge2 = Edge(point1, point2)
    # planning.graph.add_edge(edge2)
    # haveWeMadeIt2 = planning.stopConfiguration()
    # print(haveWeMadeIt2)

    # start = Vertex(0,0)
    # goal = Vertex(0,1)
    # planning = Planning(-3, 3, -1, 1, .5, start, goal)
    # point2 = Vertex(0, .6, start)
    # planning.connect(start, point2)
    # haveWeMadeIt = planning.stopConfiguration()
    # print(haveWeMadeIt)

    # graph = Graph()
    # stepSize = .1
    #
    # point1 = Vertex(0, 0)
    # point2 = Vertex(1, 0)
    # point3 = Vertex(2, 0)
    # edge1 = Edge(point1, point2)
    # edge2 = Edge(point2, point3)
    # graph.add_edge(edge1)
    # graph.add_edge(edge2)
    #
    # randomPoint1 = Vertex(2, 1)
    # closest_edge = Geometry.findClosestEdgeOnGraph(graph, randomPoint1, stepSize)
    # vertex1 = closest_edge.vertex1
    # vertex2 = closest_edge.vertex2
    # print(f"x: {vertex1.x}, y: {vertex1.y}")
    # print(f"x: {vertex2.x}, y: {vertex2.y}")

    # set up the bounds of the window
    xmin, xmax, ymin, ymax = -3, 3, -1, 1

    # set up the circle parameters
    circle1_center = [0, 1]
    circle2_center = [0, -1]
    circle_radius = .5

    # set up the x and y values for the circles
    t = np.linspace(0, np.pi, 1000)
    x1 = circle1_center[0] + circle_radius * np.cos(t)
    y1 = circle1_center[1] + circle_radius * -np.sin(t)
    x2 = circle2_center[0] + circle_radius * np.cos(t)
    y2 = circle2_center[1] + circle_radius * np.sin(t)

    # create the plot
    fig, ax = plt.subplots()
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])

    # plot the circles
    ax.plot(x1, y1, color='red')
    ax.plot(x2, y2, color='red')

    # show the plot
    plt.show()






