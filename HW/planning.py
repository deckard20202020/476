import random

from shapely.geometry import Point, LineString

from HW.edge import Edge
from HW.geometry import Geometry
from HW.graph import Graph
from HW.obstacle import CircularObstacle
from HW.vertex import Vertex


class Planning:
    def __init__(self, xmin, xmax, ymin, ymax, start, goal, stepSize, dt):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.start = start
        self.goal = goal
        self.stepSize = stepSize
        self.dt = dt
        self.graph = Graph()
        circularObstacle1 = CircularObstacle([0, -1], 1- dt)
        circularObstacle2 = CircularObstacle([0, 1], 1 - dt)
        self.obstacles = [circularObstacle1, circularObstacle2]

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
            def __init__(self, obstacles):
                self.obstacles = obstacles

            def isInCollision(self, point):
                # this should always return false
                return False

        class obstacleCollisionChecker:
            def __init__(self, obstacles):
                self.obstacles = obstacles

            def isInCollision(self, edge):
                # TODO: implement isInCollision in planning class

                # for each of the obstacles-in this case circles
                for obstacle in self.obstacles:

                    # Create a Point object for the center of the circle
                    center = Point(obstacle.center[0], obstacle.center[1])

                    # Create a circle using the buffer method on the Point object
                    circle = center.buffer(obstacle.radius)

                    # Create a LineString object using the points x1 and y1
                    point1 = Point(edge.vertex1.x, edge.vertex1.y)
                    point2 = Point(edge.vertex2.x, edge.vertex2.y)
                    line = LineString([point1, point2])

                    if line.intersects(circle):
                        return False

                return True

            def findClosestPointToObstacle(self, edge, obstacle):

                # get a discritized state of the edge
                listOfVerticiesAlongEdge = Edge.getDiscritizedState(edge)

                closestVertex = Vertex()
                for vertex in listOfVerticiesAlongEdge:
                    if not obstacle.contains(vertex):
                        closestVertex = vertex

                return closestVertex



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

        randomNumber = self.getRandomNumber(1, 10)

        # this will allow us to check the goal 10% of the time
        if randomNumber == 1:
            vertex = self.goal
            return vertex
        else:
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

    def RRTWithoutCollision(self):

        collision_checker = self.collisionChecker.emptyCollisionChecker(self.obstacles)

        # G.init(q0);
        self.graph.add_vertex(self.start)

        ai = self.getRandomPoint()

        if collision_checker.isInCollision(ai):
            # discritise the line and find where we are not in collision
            a = 1
        else:
            # make an edge
            edge = Edge(self.start, ai)

            # add the edge to the graph
            self.graph.add_edge(edge)

        # Check to see if we have found the goal
        # if ai == self.goal:
        #     return self.graph


        # for i = 1 to k do
        for i in range(100):

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
            # if ai == self.goal:
            #     break

        return self.graph

    def RRTWithCollision(self):
        # TODO: implement RRT in planning class
        # raise NotImplementedError

        collision_checker = self.collisionChecker.obstacleCollisionChecker(self.obstacles)

        # G.init(q0);
        self.graph.add_vertex(self.start)

        # the first time around we don't have any edges so we need to add one.
        randomNumber = self.getRandomNumber(1, 10)
        if randomNumber == 1:
            ai = self.goal
        else:
            ai = self.getRandomPoint()

        edge = Edge(self.start, ai)

        if (collision_checker.isInCollision(edge) == True):
            closestPointToObstacle = collision_checker.findClosestPointToObstacle(edge, obstacle)
        else:
            self.graph.add_edge(edge)

        # Check to see if we have found the goal
        # if ai == self.goal:
        #     return self.graph


        # for i = 1 to k do
        for i in range(100):

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
