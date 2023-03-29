import math
from shapely.geometry import LineString, Point

from HW.vertex import Vertex


class Geometry:
    def __init__(self):
        pass

    @staticmethod
    def getNearestVertexOnLine(vertex1, vertex2, point):
        p1 = Point(vertex1.x, vertex1.y)
        p2 = Point(vertex2.x, vertex2.y)
        p3 = Point(point.x, point.y)

        line = LineString([p1, p2])
        closestPoint = line.interpolate(line.project(p3))

        #convert to a vertex
        closestVertex = Vertex(closestPoint.x, closestPoint.y)

        return closestVertex

    @staticmethod
    def getEuclideanDistance(vertex1, vertex2):

        x1 = vertex1.x
        y1 = vertex1.y
        x2 = vertex2.x
        y2 = vertex2.y

        dx = x2 - x1
        dy = y2 - y1

        return math.sqrt((dx * dx) + (dy * dy))

    @staticmethod
    def isInsideCircle(center, radius, vertex):

        # translate the center to a vertex
        centerAsVertex = Vertex(center[0], center[1])

        # get the distance between the center and the vertex
        distance = Geometry.getEuclideanDistance(centerAsVertex, vertex)

        # if the distance is less than the radius we are inside the circle
        # TODO: This will work if you subtract .1
        if distance <= radius:
            return True
        else:
            return False

    @staticmethod
    def findClosestEdgeOnGraph(graph, vertex, stepSize):
        # TODO: implement findClosestEdgeOnGraph
        shortestDistance = float('inf')
        closestEdge = None

        for edge in graph.get_edges():
            # discritize the edge
            segments = edge.getDiscritizedState(stepSize)


            for segment in segments:
                segmentVertex = Vertex(segment.x, segment.y)
                distance = Geometry.getEuclideanDistance(vertex, segmentVertex)
                if (distance < shortestDistance):
                    shortestDistance = distance
                    closestEdge = edge

        return closestEdge

