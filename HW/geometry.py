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
    def getEuclideanDistance(point1, point2):
        # x1, y1 = point1
        # x2, y2 = point2

        x1 = point1.x
        y1 = point1.y
        x2 = point2.x
        y2 = point2.y

        dx = x2 - x1
        dy = y2 - y1

        return math.sqrt(dx * dx + dy * dy)

    @staticmethod
    def isInsideCircle(center, radius, point):

        # x1, y1 = center
        # x2, y2 = point
        #
        # distance = Geometry.getEuclideanDistance((x1, y1), (x2, y2))

        distance = Geometry.getEuclideanDistance(center, point)

        if distance <= radius:
            return True
        else:
            return False

    @staticmethod
    def findClosestEdgeOnGraph(graph, point, stepSize):
        # TODO: implement findClosestEdgeOnGraph
        shortestDistance = float('inf')
        closestEdge = None

        for edge in graph.get_edges():
            # discritize the edge
            segments = edge.getDiscritizedState(stepSize)


            for segment in segments:
                segmentPoint = Vertex(segment.x, segment.y)
                distance = Geometry.getEuclideanDistance(point, segmentPoint)
                if (distance < shortestDistance):
                    shortestDistance = distance
                    closestEdge = edge

        return closestEdge

