import random

from HW import geometry
from HW.edge import Edge
from HW.geometry import Geometry
from HW.graph import Graph
from HW.vertex import Vertex


class Planning:
    def __init__(self, xmin, xmax, ymin, ymax, goalRadius, start, goal, stepSize):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.goalRadius = goalRadius
        self.start = start
        self.goal = goal
        self.stepSize = stepSize
        self.graph = Graph()

    class EdgeCreator:
        def __init__(self):
            pass

        def makeEdge(self, start, end):
            # TODO: implement makeEdge function in planning
            # dont we just use pass here?
            # I dont think we will ever use this
            raise NotImplementedError

        class StraightEdgeCreator:
            def __init__(self):
                pass

            def makeEdge(self, start, end, graph):
                edge = Edge(start, end)
                graph.add_edge(edge)

    class distanceComputator:
        def __init__(self):
            pass

        def euclideanDistanceComputator(self, vertex1, vertex2):
            # TODO: implement euclideanDistanceComputator in planning class
            # what will I use this for???
            return geometry.getEuclideanDistance(vertex1, vertex2)
            # return ((vertex1[0] - vertex2[0]) ** 2 + (vertex1[1] - vertex2[1]) ** 2) ** 0.5

    class collisionChecker:
        def __init__(self):
            pass

        class emptyCollisionChecker:
            def __init__(self):
                pass

            def isInCollision(self, point):
                # this should always return false
                return False

        class obstacleCollisionChecker:
            def __init__(self):
                pass

            def isInCollision(self, point):
                # TODO: implement isInCollision in planning class
                # check if point is within obstacle boundaries
                # check to see if we have hit any obstacles
                # find closest point
                # ...
                # for each of the obstacles-in this case circles
                    #check to see if the point or edge (after discritized) is in collision

                return True

            def isCheckingRequired(self):
                # TODO: implement isCheckingRequired in planning class
                # When should we use this???
                #     do we use it if the newly created edge intersects an obstacle???
                # check if collision checking is required based on obstacle presence and position
                # ...
                return True


    def getRandomPoint(self):
        # this implementation will give a precision of x.x

        # get a random x value
        x = Planning.getRandomNumber(self.xmin * 10, self.xmax * 10)
        xvalue = x / 10

        # get a random y value
        y = Planning.getRandomNumber(self.ymin * 10, self.ymax * 10)
        yvalue = y / 10

        # make a new vertex
        vertex = Vertex(xvalue, yvalue)
        return vertex


    def getRandomNumber(min, max):
        return random.randint(min, max)

    def stopConfiguration(self):
        # figure out if we are close enough to the goal
        for vertex in self.graph.vertices:
            distance = Geometry.getEuclideanDistance(vertex, self.goal)
            if distance <= self.goalRadius:
                return True

        return False


    def connect(self, vertex1, vertex2):
        # connects two points after we find them with RRT or PRM

        # make a vertex3 using the points of vertex2 and assigning its parent as vertex 1
        vertex2WithParent = Vertex(vertex2.x, vertex2.y, vertex1)

        # make an edge with vertex1 and our new vertex
        edge = Edge(vertex1, vertex2WithParent)

        # edd the edge to the graph
        self.graph.add_edge(edge)

    # def RRT(self):
    #     # TODO: implement RRT in planning class
    #     # raise NotImplementedError
    #
    #     collision_checker = Planning.collisionChecker.emptyCollisionChecker()
    #
    #     # RDT(q0):
    #         # G.init(q0);
    #         self.graph.add_vertex(self.start)
    #         # for i = 1 to k do
    #         for i in range(1000):
    #
    #             # qn ← nearest(S, α(i));
    #             ai = self.getRandomPoint()
    #
    #             # if we are in collision
    #             if (collision_checker(ai) == True):
    #                 a = 1
    #                 #discritise the line and find where we are not in collision
    #             else:
    #                 # find the closest edge on the graph
    #                 # find the closest point on the edge sending the step size
    #                 # split the edge
    #                 #
    #
    #             # qs ← stopping - configuration(qn, α(i));
    #             # if qs != qn then
    #                 # G.add vertex(qs);
    #                 # G.add edge(qn, qs);

    def PRM(self):
        # TODO: implement PRM in planning class
        raise NotImplementedError
