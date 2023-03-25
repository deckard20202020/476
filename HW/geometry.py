import math
from shapely.geometry import LineString, Point


class Geometry:
    def __init__(self):
        pass

    @staticmethod
    def getNearestPointOnLine(vertex1, vertex2, point):
        p1 = Point(vertex1.x, vertex1.y)
        p2 = Point(vertex2.x, vertex2.y)
        p3 = Point(point.x, point.y)

        line = LineString([p1, p2])
        closest_point = line.interpolate(line.project(p3))

        return closest_point

    @staticmethod
    def getEuclideanDistance(point1, point2):
        x1, y1 = point1
        x2, y2 = point2

        dx = x2 - x1
        dy = y2 - y1

        return math.sqrt(dx * dx + dy * dy)

    @staticmethod
    def isInsideCircle(center, radius, point):

        x1, y1 = center
        x2, y2 = point

        distance = Geometry.getEuclideanDistance((x1, y1), (x2, y2))

        if distance <= radius:
            return True
        else:
            return False
