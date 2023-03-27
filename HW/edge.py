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

        point1 = Point(self.vertex1.x, self.vertex1.y)
        point2 = Point(self.vertex2.x, self.vertex2.y)
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


    def split(self, point):

        # make two new edges
        firstEdge = Edge(self.vertex1, point)
        secondEdge = Edge(point, self.vertex2)

        # TODO: when you use split in algorigthm
        # add those two edges to the graph
        # first edge has the parent of the original edge
        # second edge has the first edge as a parent
        # should we remove the old edge and create two new edges with the 3 points or just add the new edges???

        return [firstEdge, secondEdge]

    def getLength(self):
        distance = Geometry.getEuclideanDistance(self.vertex1, self.vertex2)
        return distance
