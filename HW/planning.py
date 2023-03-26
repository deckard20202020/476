import random

from HW.edge import Edge
from HW.geometry import Geometry
from HW.graph import Graph
from HW.vertex import Vertex


class Planning:
    def __init__(self, xmin, xmax, ymin, ymax, start, goal, stepSize):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
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
            return Geometry.getEuclideanDistance(vertex1, vertex2)
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
        # TODO: Do I need to gt random points based on the random method in class???
        # this implementation will give a precision of x.x

        # get a random x value
        x = self.getRandomNumber(self.xmin * 10, self.xmax * 10)
        xvalue = x / 10

        # get a random y value
        y = self.getRandomNumber(self.ymin * 10, self.ymax * 10)
        yvalue = y / 10

        # make a new vertex
        vertex = Vertex(xvalue, yvalue)
        return vertex


    def getRandomNumber(self, min, max):
        return random.randint(min, max)

    # def stopConfiguration(self):
    #     # figure out if we are close enough to the goal
    #     for vertex in self.graph.vertices:
    #         distance = Geometry.getEuclideanDistance(vertex, self.goal)
    #         if distance <= self.goalRadius:
    #             return True
    #
    #     return False


    def connect(self, vertex1, vertex2):
        # connects two points after we find them with RRT or PRM

        # make a vertex3 using the points of vertex2 and assigning its parent as vertex 1
        vertex2WithParent = Vertex(vertex2.x, vertex2.y, vertex1)

        # make an edge with vertex1 and our new vertex
        edge = Edge(vertex1, vertex2WithParent)

        # edd the edge to the graph
        self.graph.add_edge(edge)

    def RRT(self):
        # TODO: implement RRT in planning class
        # raise NotImplementedError

        collision_checker = self.collisionChecker.emptyCollisionChecker()


        # G.init(q0);
        self.graph.add_vertex(self.start)

        # the first time around we don't have any edges so we need to add one.
        randomNumber = self.getRandomNumber(1, 10)
        if randomNumber == 1:
            ai = self.goal
        else:
            ai = self.getRandomPoint()

        if (collision_checker.isInCollision(ai) == True):
            # discritise the line and find where we are not in collision
            a = 1
        else:

            # make an edge
            edge = Edge(self.start, ai)
            # add the edge to the graph
            self.graph.add_edge(edge)

        # Check to see if we have found the goal
        if ai == self.goal:
            return self.graph


        # for i = 1 to k do
        for i in range(1000):

            # qn ← nearest(S, α(i));
            ai = -1
            # we should use the goal as ai 10% of the time
            randomNumber = self.getRandomNumber(1, 10)
            if randomNumber == 1:
                ai = self.goal
            else:
                ai = self.getRandomPoint()

            # if we are in collision
            if (collision_checker.isInCollision(ai) == True):
                #discritise the line and find where we are not in collision
                a = 1
            else:
                # find the closest edge on the graph
                closestEdge = Geometry.findClosestEdgeOnGraph(self.graph, ai, self.stepSize)

                # find the closest point on the edge sending the step size
                closestPointOnEdge = Geometry.getNearestVertexOnLine(closestEdge.vertex1, closestEdge.vertex2, ai)

                # split the edge
                splitEdges = closestEdge.split(closestPointOnEdge)

                # add the split edges to the graph
                for e in splitEdges:
                    self.graph.add_edge(e)

                # add the edge from the split point to the ai
                newEdge = Edge(closestPointOnEdge, ai)
                self.graph.add_edge(newEdge)

            # Check to see if we have found the goal
            if ai == self.goal:
                break

        return self.graph

            # qs ← stopping - configuration(qn, α(i));
            # if qs != qn then
                # G.add vertex(qs);
                # G.add edge(qn, qs);

    def PRM(self):
        # TODO: implement PRM in planning class
        raise NotImplementedError
