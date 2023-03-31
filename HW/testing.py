import math
import numpy as np

from matplotlib import pyplot as plt, patches
from shapely.geometry import Point, LineString

from HW import geometry, graph, planning, obstacle, edge
from HW.geometry import Geometry
from planning import Planning
from vertex import Vertex
from graph import Graph
from edge import Edge

def makeAVertex(x, y, p):
    v = Vertex(x, y, p)
    return v

def printResultsWithPath(xmin, xmax, ymin, ymax, graph, start, goal, dt):
    # fig = plt.figure(figsize=(60, 10))
    # fix, ax = plt.subplots(figsize=(60,10))


    # set up the circle parameters
    circle1_center = [0, 1]
    circle2_center = [0, -1]
    circle_radius = 1 - dt

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

    # plot each vertex
    for v in graph.get_vertices():
        x1 = v._x
        y1 = v._y
        if v == goal:
            ax.plot(x1, y1, 'bx')
        elif v == start:
            ax.plot(x1, y1, 'bo')
        else:
            ax.plot(x1, y1, 'ko')

    # make sure to plot the goal
    # used for testing while reducing dt down to 0
    ax.plot(goal._x, goal._y, 'bx')

    # plot all the edges
    for e in graph.get_edges():
        first = [e.vertex1._x, e.vertex2._x]
        second = [e.vertex1._y, e.vertex2._y]
        ax.plot(first, second, color='k')

    # plot the path
    # find the goal in the graph
    goalVertex = None
    for v in graph.get_vertices():
        if v == goal:
            goalVertex = v
            break

    if goalVertex == None or goalVertex._parent == None:
        # pause here
        a = 1
    else:
        while goalVertex._parent is not None:
            #make the goalVertex a blue circle
            x1 = goalVertex._x
            y1 = goalVertex._y
            ax.plot(x1, y1, 'bo')

            # plot the edge in blue
            edge = Edge(goalVertex, goalVertex._parent)
            first = [edge.vertex1._x, edge.vertex2._x]
            second = [edge.vertex1._y, edge.vertex2._y]
            ax.plot(first, second, color='b')

            # reassign the goalVertex
            goalVertex = goalVertex._parent

    plt.show()

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
    # xmin, xmax, ymin, ymax = -3, 3, -1, 1
    #
    # # set up the circle parameters
    # circle1_center = [0, 1]
    # circle2_center = [0, -1]
    # circle_radius = .5
    #
    # # set up the x and y values for the circles
    # t = np.linspace(0, np.pi, 1000)
    # x1 = circle1_center[0] + circle_radius * np.cos(t)
    # y1 = circle1_center[1] + circle_radius * -np.sin(t)
    # x2 = circle2_center[0] + circle_radius * np.cos(t)
    # y2 = circle2_center[1] + circle_radius * np.sin(t)
    #
    # # create the plot
    # fig, ax = plt.subplots()
    # ax.set_xlim([xmin, xmax])
    # ax.set_ylim([ymin, ymax])
    #
    # # plot the circles
    # ax.plot(x1, y1, color='red')
    # ax.plot(x2, y2, color='red')
    #
    # # show the plot
    # plt.show()

    # obstacle = obstacle.CircularObstacle([0, 0], 1)
    # vertex1 = Vertex(-1, -2)
    # vertex2 = Vertex(1, -2)
    # edge = Edge(vertex1, vertex2)
    #
    # # Create a Point object for the center of the circle
    # center = Point(obstacle.center[0], obstacle.center[1])
    #
    # # Create a circle using the buffer method on the Point object
    # circle = center.buffer(obstacle.radius)
    #
    # # Create a LineString object using the points x1 and y1
    # point1 = Point(edge.vertex1.x, edge.vertex1.y)
    # point2 = Point(edge.vertex2.x, edge.vertex2.y)
    # line = LineString([point1, point2])
    #
    # if line.intersects(circle):
    #     print("True")
    # else:
    #     print("False")

    # TODO: Test collisionchecker and closestPoint to obstacle
    # xmin = -3
    # xmax = 3
    # ymin = -1
    # ymax = 1
    # start = Vertex(-3, -1)
    # goal = Vertex(2, -0.5)
    # stepSize = .1
    # dt = .1
    #
    # planning = Planning(xmin, xmax, ymin, ymax, start, goal, stepSize, dt)
    # ai = Vertex(0, -1)
    # collisionChecker = planning.collisionChecker.obstacleCollisionChecker(planning.obstacles, planning.stepSize)
    # edge = Edge(start, ai)
    # closestPoint = collisionChecker.findClosestVertexToObstacle(edge, planning.obstacles)
    # print(f"x: {closestPoint.x}, y: {closestPoint.y}")

    # xmin = -3
    # xmax = 3
    # ymin = -1
    # ymax = 1
    # start = Vertex(-3, -1)
    # goal = Vertex(2, -0.5)
    # stepSize = .1
    # dt = .1

    # planning = Planning(xmin, xmax, ymin, ymax, start, goal, stepSize, dt)
    # vertex1 = Vertex(-1.1, -0.5)
    # vertex2 = Vertex(-1.1, -0.8)
    # edge = Edge(vertex1, vertex2)
    # collisionChecker = planning.collisionChecker.obstacleCollisionChecker(planning.obstacles, planning.stepSize)
    # areWeInCollision = collisionChecker.isInCollision(edge)
    # print(areWeInCollision)
    # print()
    # closestPoint = collisionChecker.findClosestVertexToObstacle(edge, planning.obstacles)
    # print(f"x: {closestPoint.x}, y: {closestPoint.y}")

    # # TODO: testing upper circle
    # xmin = -3
    # xmax = 3
    # ymin = -1
    # ymax = 1
    # start = Vertex(-3, -1)
    # goal = Vertex(2, -0.5)
    # stepSize = .1
    # dt = .1
    #
    # planning = Planning(xmin, xmax, ymin, ymax, start, goal, stepSize, dt)
    # vertex1 = Vertex(-1.1, 1)
    # vertex2 = Vertex(-.5, 1)
    # edge = Edge(vertex1, vertex2)
    # collisionChecker = planning.collisionChecker.obstacleCollisionChecker(planning.obstacles, planning.stepSize)
    #
    # areWeInCollision = collisionChecker.isInCollision(edge)
    # print("Are we in collision, should be true")
    # print(areWeInCollision)
    # print()
    #
    # closestPoint = collisionChecker.findClosestVertexToObstacle(edge, planning.obstacles)
    # print("this is the closest point, should be to the left of (-0.9, 1)")
    # print(f"x: {closestPoint._x}, y: {closestPoint._y}")
    # print()

    # TODO: testing split edge
    xmin = -3
    xmax = 3
    ymin = -1
    ymax = 1
    start = Vertex(-3, 0.9)
    goal = Vertex(-1.1, 0)
    stepSize = .1
    dt = .1

    planning = Planning(xmin, xmax, ymin, ymax, start, goal, stepSize, dt)
    collisionChecker = planning.collisionChecker.obstacleCollisionChecker(planning.obstacles, planning.stepSize)

    #adding first edge
    firstVertex = Vertex(-1, 1, start)
    planning.graph.add_vertex(firstVertex)
    firstEdge = Edge(start, firstVertex)
    planning.connect(firstEdge.vertex1, firstEdge.vertex2)

    #adding second edge
    ai = Vertex(-2, -1)
    closestEdge = Geometry.findClosestEdgeOnGraph(planning.graph, ai, stepSize)
    closestPointOnEdge = Geometry.getNearestVertexOnLine(closestEdge.vertex1, closestEdge.vertex2, ai)
    ai = Vertex(ai._x, ai._y, closestPointOnEdge)
    splitEdges = closestEdge.split(closestPointOnEdge)
    for e in splitEdges:
        planning.connect(e.vertex1, e.vertex2)
    secondEdge = Edge(closestPointOnEdge, ai)
    planning.connect(secondEdge.vertex1, secondEdge.vertex2)

    # #adding third edge
    # ai = Vertex(2, 0)
    # closestEdge = Geometry.findClosestEdgeOnGraph(planning.graph, ai, stepSize)
    # closestPointOnEdge = Geometry.getNearestVertexOnLine(closestEdge.vertex1, closestEdge.vertex2, ai)
    # ai = Vertex(ai._x, ai._y, closestPointOnEdge)
    # splitEdges = closestEdge.split(closestPointOnEdge)
    # for e in splitEdges:
    #     planning.connect(e.vertex1, e.vertex2)
    # thirdEdge = Edge(closestPointOnEdge, ai)
    # planning.connect(thirdEdge.vertex1, thirdEdge.vertex2)
    #
    # #adding fourth edge
    # ai = Vertex(1.5, -1)
    # closestEdge = Geometry.findClosestEdgeOnGraph(planning.graph, ai, stepSize)
    # closestPointOnEdge = Geometry.getNearestVertexOnLine(closestEdge.vertex1, closestEdge.vertex2, ai)
    # ai = Vertex(ai._x, ai._y, closestPointOnEdge)
    # splitEdges = closestEdge.split(closestPointOnEdge)
    # for e in splitEdges:
    #     planning.connect(e.vertex1, e.vertex2)
    # fourthEdge = Edge(closestPointOnEdge, ai)
    # planning.connect(fourthEdge.vertex1, fourthEdge.vertex2)

    # add goal
    ai = goal
    closestEdge = Geometry.findClosestEdgeOnGraph(planning.graph, ai, stepSize)
    closestPointOnEdge = Geometry.getNearestVertexOnLine(closestEdge.vertex1, closestEdge.vertex2, ai)
    ai = Vertex(ai._x, ai._y, closestPointOnEdge)
    splitEdges = closestEdge.split(closestPointOnEdge)
    for e in splitEdges:
        planning.connect(e.vertex1, e.vertex2)
    # should these be flipped?
    planning.graph.add_vertex(ai)
    fifthEdge = Edge(closestPointOnEdge, ai)
    planning.connect(fifthEdge.vertex1, fifthEdge.vertex2)

    printResultsWithPath(xmin, xmax, ymin, ymax, planning.graph, start, goal, dt)
    a = 1








