from HW.geometry import Geometry
from shapely.geometry import LineString, Point
from shapely.ops import nearest_points


class Edge:
    def __init__(self, vertex1, vertex2):
        self.vertex1 = vertex1
        self.vertex2 = vertex2

    def __eq__(self, other):
        if isinstance(other, Edge):
            return (self.vertex1 == other.vertex1 and self.vertex2 == other.vertex2) or \
                   (self.vertex1 == other.vertex2 and self.vertex2 == other.vertex1)
        return False

    def __hash__(self):
        return hash((self.vertex1, self.vertex2))

    def reverse(self):
        return Edge(self.vertex2, self.vertex1)

    def getDiscritizedState(self):
        # TODO: implement getDiscritizedState in edge class
        raise NotImplementedError

    def getNearestPoint(self, point):
        # TODO: implement getNearestPoint in edge class
        # raise NotImplementedError

        p1 = Point(self.vertex1.x, self.vertex1.y)
        p2 = Point(self.vertex2.x, self.vertex2.y)
        p3 = Point(point.x, point.y)

        line = LineString([p1, p2])
        closest_point = line.interpolate(line.project(p3))

        return closest_point


    def split(self):
        # TODO: implement split in edge class
        raise NotImplementedError
        # parameters should be an edge and a point
        # should we remove the old edge and create two new edges with the 3 points or just add the new edges???

    def getLength(self):
        distance = Geometry.getEuclideanDistance(self.vertex1, self.vertex2)
        return distance
