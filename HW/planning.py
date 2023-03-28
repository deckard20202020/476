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
        circularObstacle1 = CircularObstacle([0, -1], 1 - dt)
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
            def __init__(self, obstacles, stepSize):
                self.obstacles = obstacles
                self.stepSize = stepSize

            def isInCollision(self, edge):
                # TODO: implement isInCollision in planning class

                # for each of the obstacles-in this case circles
                for obstacle in self.obstacles:

                    # Create a Point object for the center of the circle
                    center = Point(obstacle.center[0], obstacle.center[1])

                    # Create a circle using the buffer method on the Point object
                    circle = center.buffer(obstacle.radius)

                    #Create two points for a LineString object
                    x1 = edge.vertex1.x
                    y1 = edge.vertex1.y
                    x2 = edge.vertex2.x
                    y2 = edge.vertex2.y
                    point1 = Point(x1, y1)
                    point2 = Point(x2, y2)

                    # Create a LineString object using the points x1 and y1
                    line = LineString([point1, point2])

                    # Use shapely to check to see if our line intersects the circle
                    if line.intersects(circle):
                        return True

                return False

            def findClosestVertexToObstacle(self, edge, obstacles):

                # get a discritized state of the edge
                listOfVerticiesAlongEdge = edge.getDiscritizedState(self.stepSize)

                closestVertex = edge.vertex1

                #boolean value to determine if we have hit an obstacle
                hitsObstacle = False

                # scroll thorugh the discritized edge starting at the first vertex
                for vertex in listOfVerticiesAlongEdge:
                    # we want to check to see if we hit any of the obstacles
                    for obstacle in obstacles:
                        if obstacle.contains(vertex):
                            return closestVertex
                        else:
                            closestVertex = vertex
                        #     hitsObstacle = True
                        # # if the vertex hasn't hit any of the obstacles
                        # if hitsObstacle == False:
                        #     # updatate our closest vertex
                        #     closestVertex = vertex
                        # else:
                        #     # otherwise we have hit something so we want to return the last vertex
                        #     return closestVertex

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

    def addSplitEdges(self, ai):
        # find the closest edge on the graph
        closestEdge = Geometry.findClosestEdgeOnGraph(self.graph, ai, self.stepSize)

        # find the closest point on the edge
        closestPointOnEdge = Geometry.getNearestVertexOnLine(closestEdge.vertex1, closestEdge.vertex2, ai)

        # split the edge
        splitEdges = closestEdge.split(closestPointOnEdge)

        # add the split edges to the graph
        for e in splitEdges:
            self.graph.add_edge(e)

        # TODO: we should replace this with our connect method
        # add the edge from the split point to the ai
        newEdge = Edge(closestPointOnEdge, ai)
        self.graph.add_edge(newEdge)

    def RRTExplorationWithoutCollision(self):

        collision_checker = self.collisionChecker.emptyCollisionChecker(self.obstacles)

        # G.init(q0);
        self.graph.add_vertex(self.start)

        ai = self.getRandomPoint()

        edge = Edge(self.start, ai)

        if collision_checker.isInCollision(edge):
            # we will never enter this
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

            # find the closest edge on the graph
            closestEdge = Geometry.findClosestEdgeOnGraph(self.graph, ai, self.stepSize)

            # find the closest point on the edge
            closestPointOnEdge = Geometry.getNearestVertexOnLine(closestEdge.vertex1, closestEdge.vertex2, ai)

            edge = Edge(closestPointOnEdge, ai)

            # if we are in collision
            if (collision_checker.isInCollision(edge) == True):
                # we will never enter this
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

            # # Check to see if we have found the goal
            # if ai == self.goal:
            #     break

        return self.graph

    def RRTExplorationWithCollision(self):
        # TODO: implement RRT in planning class
        # raise NotImplementedError

        collision_checker = self.collisionChecker.obstacleCollisionChecker(self.obstacles, self.stepSize)

        # G.init(q0);
        self.graph.add_vertex(self.start)

        # the first time around we don't have any edges so we need to add one.
        ai = self.getRandomPoint()

        edge = Edge(self.start, ai)

        # if the new point creates a line that is in collision
        if (collision_checker.isInCollision(edge) == True):

            # find the closest point to the obstacle
            closestPointToObstacle = collision_checker.findClosestVertexToObstacle(edge, self.obstacles)

            # create a new edge
            edge = Edge(self.start, closestPointToObstacle)

            # add the edge to our graph
            self.graph.add_edge(edge)
        else:
            # otherwise just add the edge to our graph
            self.graph.add_edge(edge)

        # Check to see if we have found the goal
        # if ai == self.goal:
        #     return self.graph


        # for i = 1 to k do
        for i in range(100):

            # find a random point
            ai = self.getRandomPoint()

            # find the closest edge on the graph
            closestEdge = Geometry.findClosestEdgeOnGraph(self.graph, ai, self.stepSize)

            # find the closest point on the edge
            closestPointOnEdge = Geometry.getNearestVertexOnLine(closestEdge.vertex1, closestEdge.vertex2, ai)

            # make a new edge
            edge = Edge(closestPointOnEdge, ai)

            # if we are in collision with our new edge
            if (collision_checker.isInCollision(edge) == True):

                # find the closest point to the obstacle
                closestPointToObstacle = collision_checker.findClosestVertexToObstacle(edge, self.obstacles)

                #reassign our random point
                ai = closestPointToObstacle

                # find the closest edge on the graph
                closestEdge = Geometry.findClosestEdgeOnGraph(self.graph, ai, self.stepSize)

                # find the closest point on the edge sending the step size
                closestPointOnEdge = Geometry.getNearestVertexOnLine(closestEdge.vertex1, closestEdge.vertex2, ai)

                # split the edge
                splitEdges = closestEdge.split(closestPointOnEdge)

                # add the split edges to the graph
                for e in splitEdges:
                    self.graph.add_edge(e)

                # add the edge from the split point to the new ai
                newEdge = Edge(closestPointOnEdge, ai)
                self.graph.add_edge(newEdge)

            else: # we are not in collision with our new edge

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

            # # Check to see if we have found the goal
            # if ai == self.goal:
            #     break

        return self.graph

    def RRTPathfindingWithCollision(self):
        # TODO: implement RRT in planning class
        raise NotImplementedError

    def PRM(self):
        # TODO: implement PRM in planning class
        raise NotImplementedError
