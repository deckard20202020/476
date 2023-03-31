from HW.geometry import Geometry
from shapely.geometry import LineString, Point

from HW.vertex import Vertex


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

    def getDiscritizedState(self, stepSize):

        point1 = Point(self.vertex1._x, self.vertex1._y)
        point2 = Point(self.vertex2._x, self.vertex2._y)
        line = LineString([point1, point2])
        length = line.length
        num_segments = int(length / stepSize) + 1

        points = [line.interpolate(i * stepSize) for i in range(num_segments)]
        # Shapely points are represented as (x, y) tuples
        vertices = [Vertex(point.x, point.y) for point in points]

        return vertices

        # def getDiscritizedState(self, stepSize):
        #     # calculate the length of the edge
        #     length = self.getLength()
        #
        #     # calculate the number of steps needed
        #     num_steps = int(length / stepSize) + 1
        #
        #     # calculate the step size needed to get evenly spaced points on the edge
        #     dx = (self.vertex2[0] - self.vertex1[0]) / (num_steps - 1)
        #     dy = (self.vertex2[1] - self.vertex1[1]) / (num_steps - 1)
        #
        #     # create an array of vertices to store the discretized edge
        #     vertices = array.array('d')
        #
        #     # add the first vertex to the array
        #     vertices.append(self.vertex1[0])
        #     vertices.append(self.vertex1[1])
        #
        #     # add the rest of the vertices to the array
        #     for i in range(1, num_steps - 1):
        #         x = self.vertex1[0] + i * dx
        #         y = self.vertex1[1] + i * dy
        #         vertices.append(x)
        #         vertices.append(y)
        #
        #     # add the last vertex to the array
        #     vertices.append(self.vertex2[0])
        #     vertices.append(self.vertex2[1])
        #
        #     return vertices

    def getNearestPoint(self, point):
        closest_point = Geometry.getNearestVertexOnLine(self.vertex1, self.vertex2, point)
        return closest_point


    def split(self, midVertex):

        # vertex1 should already have a parent

        # make the parent of the midpoint the first vertex
        midVertex = Vertex(midVertex._x, midVertex._y, self.vertex1)

        # make the parent of vertex2 the midpoint
        rightVertex = Vertex(self.vertex2._x, self.vertex2._y, midVertex)

        # make two new edges
        firstEdge = Edge(self.vertex1, midVertex)
        secondEdge = Edge(midVertex, rightVertex)

        return [firstEdge, secondEdge]

    def getLength(self):
        distance = Geometry.getEuclideanDistance(self.vertex1, self.vertex2)
        return distance
