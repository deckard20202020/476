import math

from shapely.geometry import Polygon, Point

from geometry import is_inside_circle


class Obstacle:
    def contain(self, s):
        return False

class PolygonObstacle(Obstacle):
    """A class representing a polygon obstacle"""

    # def __int__(self, vertex1, vertex2, vertex3, vertex4):
    #     self.vertex1 = vertex1
    #     self.vertex2 = vertex2
    #     self.vertex3 = vertex3
    #     self.vertex4 = vertex4

    def __init__(self, listOfVertices):
        self.listOfVertices = listOfVertices

    def get_list_of_vertices(self):
        return self.listOfVertices

    def contain(self, v):
        # Create a list of (x, y) tuples from the input vertices
        coordinates = [(x, y) for x, y in self.listOfVertices]

        # Create a Polygon object from the list of coordinates
        polygon = Polygon(coordinates)

        # Create a Point object from the input vertex
        point = Point(v)

        # Check if the polygon contains the point
        return polygon.contains(point)

    # def contain(self, v):
    #     """Return whether a point s is inside this obstacle"""
    #     """Determine whether v is in the polygon with the given vertices (assumed to be given in the CC order)
    #
    #     @type v: a tuple (x, y)
    #     @type vertices: a list [p1, ..., p_{m+1}] where p_i is the position (x,y) of the i^{th} vertex.
    #     """
        # vertices = [self.vertex1, self.vertex2, self.vertex3, self.vertex4]
        #
        # for i in range(len(vertices)):
        #     v1 = vertices[i]
        #     v2 = vertices[0]
        #     if i + 1 < len(vertices):
        #         v2 = vertices[i + 1]
        #     if not self.is_in_half_space(v, v1, v2):
        #         return False
        # return True

    # def is_in_half_space(v, v1, v2):
    #     """Determine whether v is in the half space to the left of the vector from v1 to v2
    #
    #     @type v, v1, v2: a tuple (x, y) that indicates the x and y coordinates of the corresponding points.
    #
    #     """
    #     x = v[0]
    #     y = v[1]
    #     x1 = v1[0]
    #     y1 = v1[1]
    #     x2 = v2[0]
    #     y2 = v2[1]
    #
    #     a = y2 - y1
    #     b = x1 - x2
    #     c = x2 * y1 - x1 * y2
    #
    #     return a * x + b * y + c <= 0


class CircularObstacle(Obstacle):
    """A class representing a circular obstacle"""

    def __init__(self, center, radius, theta_lim):
        self.center = center
        self.radius = radius
        self.theta_min = theta_lim[0]
        self.theta_max = theta_lim[1]

    def get_boundaries(self):
        """Return the list of coordinates (x,y) of the boundary of the obstacle"""
        num_theta = 100
        theta_inc = (self.theta_max - self.theta_min) / num_theta
        theta_range = [self.theta_min + theta_inc * i for i in range(num_theta + 1)]
        return [
            (
                self.radius * math.cos(theta) + self.center[0],
                self.radius * math.sin(theta) + self.center[1],
            )
            for theta in theta_range
        ]

    def contain(self, s):
        """Return whether a point s is inside this obstacle"""
        return is_inside_circle(self.center, self.radius, s)


class WorldBoundary2D(Obstacle):
    """A class representing the world"""

    def __init__(self, xlim, ylim):
        self.xmin = xlim[0]
        self.xmax = xlim[1]
        self.ymin = ylim[0]
        self.ymax = ylim[1]

    def contain(self, s):
        """Return True iff the given point is not within the boundary (i.e., the point is
        "in collision" with an obstacle.).
        """
        return (
            s[0] < self.xmin or s[0] > self.xmax or s[1] < self.ymin or s[1] > self.ymax
        )


def construct_circular_obstacles(dt):
    r = 1 - dt  # the radius of the circle
    c = [(0, -1), (0, 1)]  # the center of each circle
    t = [(0, math.pi), (-math.pi, 0)]  # range of theta of each circle
    obstacles = []
    for i in range(len(c)):
        obstacles.append(CircularObstacle(c[i], r, t[i]))
    return obstacles

def construct_polygon_obstacles(listOfObstacleVerticies):
    obstacles = []
    for list in listOfObstacleVerticies:
        obstacle = PolygonObstacle(list)
        obstacles.append(obstacle)
    return obstacles
