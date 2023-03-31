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
                # I don't think I ever use this
                edge = Edge(start, end)
                graph.add_edge(edge)

    class distanceComputator:
        def __init__(self):
            pass

        def euclideanDistanceComputator(self, vertex1, vertex2):
            # I don't think I ever use this
            return Geometry.getEuclideanDistance(vertex1, vertex2)

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

                # for each of the obstacles-in this case circles
                for obstacle in self.obstacles:

                    # Create a Point object for the center of the circle
                    center = Point(obstacle.center[0], obstacle.center[1])

                    # Create a circle using the buffer method on the Point object
                    circle = center.buffer(obstacle.radius)

                    #Create two points for a LineString object
                    x1 = edge.vertex1._x
                    y1 = edge.vertex1._y
                    x2 = edge.vertex2._x
                    y2 = edge.vertex2._y
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

                # initialize our closest vertex
                closestVertex = edge.vertex1

                #boolean value to determine if we have hit an obstacle
                hitsObstacle = False

                # scroll thorugh the discritized edge starting at the first vertex
                for vertex in listOfVerticiesAlongEdge:
                    # we want to check to see if we hit any of the obstacles
                    for obstacle in obstacles:
                        # if at any time we hit an obstacle
                        if obstacle.contains(vertex):
                            # update our boolean value
                            hitsObstacle = True
                    # if we have not hit an obstacle yet
                    if hitsObstacle == False:
                        # update our closest vertex and keep going
                        closestVertex = vertex
                    else:
                        # otherwise stop and return our closest vertex so far
                        closestVertex._parent = edge.vertex1
                        return closestVertex

                return closestVertex

            def isCheckingRequired(self):
                # TODO: implement isCheckingRequired in planning class
                # When should we use this???
                #     do we use it if the newly created edge intersects an obstacle???
                # check if collision checking is required based on obstacle presence and position
                # ...
                return True


    def getRandomPoint(self):
        # get a random number between 1 and 10 inclusive
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
        vertex2WithParent = Vertex(vertex2._x, vertex2._y, vertex1)

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
            self.connect(e.vertex1, e.vertex2)

        # add the edge from the split point to the ai
        newEdge = Edge(closestPointOnEdge, ai)
        self.connect(newEdge.vertex1, newEdge.vertex2)

    def findClosestEdgeAndSplit(self, ai):
        # find the closest edge on the graph
        closestEdge = Geometry.findClosestEdgeOnGraph(self.graph, ai, self.stepSize)

        # find the closest point on the edge sending the step size
        closestPointOnEdge = Geometry.getNearestVertexOnLine(closestEdge.vertex1, closestEdge.vertex2, ai)

        # split the edge
        splitEdges = closestEdge.split(closestPointOnEdge)

        # add the split edges to the graph
        for e in splitEdges:
            self.connect(e.vertex1, e.vertex2)

        # add the edge from the split point to the new ai
        newEdge = Edge(closestPointOnEdge, ai)
        self.connect(newEdge.vertex1, newEdge.vertex2)

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
            self.connect(edge.vertex1, edge.vertex2)

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
                    self.connect(e.vertex1, e.vertex2)

                # add the edge from the split point to the ai
                newEdge = Edge(closestPointOnEdge, ai)
                self.connect(newEdge.vertex1, newEdge.vertex2)

            # # Check to see if we have found the goal
            # if ai == self.goal:
            #     break

        return self.graph

    def RRTExplorationWithCollision(self):

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
            self.connect(edge.vertex1, edge.vertex2)

        else:
            # otherwise just add the edge to our graph
            self.connect(edge.vertex1, edge.vertex2)

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
                    self.connect(e.vertex1, e.vertex2)

                # add the edge from the split point to the new ai
                newEdge = Edge(closestPointOnEdge, ai)
                self.connect(newEdge.vertex1, newEdge.vertex2)

            else: # we are not in collision with our new edge

                # find the closest edge on the graph
                closestEdge = Geometry.findClosestEdgeOnGraph(self.graph, ai, self.stepSize)

                # find the closest point on the edge sending the step size
                closestPointOnEdge = Geometry.getNearestVertexOnLine(closestEdge.vertex1, closestEdge.vertex2, ai)

                # split the edge
                splitEdges = closestEdge.split(closestPointOnEdge)

                # add the split edges to the graph
                for e in splitEdges:
                    self.connect(e.vertex1, e.vertex2)

                # add the edge from the split point to the ai
                newEdge = Edge(closestPointOnEdge, ai)
                self.connect(newEdge.vertex1, newEdge.vertex2)

            # # Check to see if we have found the goal
            # if ai == self.goal:
            #     break

        return self.graph

    def RRTPathfindingWithCollision(self):

        collision_checker = self.collisionChecker.obstacleCollisionChecker(self.obstacles, self.stepSize)

        # G.init(q0);
        self.graph.add_vertex(self.start)

        # the first time around we don't have any edges so we need to add one.
        ai = self.getRandomPoint()
        # add the parent to ai
        ai = Vertex(ai._x, ai._y, self.start)

        edge = Edge(self.start, ai)

        # if the new point creates a line that is in collision
        if (collision_checker.isInCollision(edge) == True):

            # find the closest point to the obstacle
            closestPointToObstacle = collision_checker.findClosestVertexToObstacle(edge, self.obstacles)

            # create a new edge
            edge = Edge(self.start, closestPointToObstacle)

            # add the edge to our graph
            self.connect(edge.vertex1, edge.vertex2)

            #reassign ai
            ai = closestPointToObstacle

        else:
            # otherwise just add the edge to our graph
            self.connect(edge.vertex1, edge.vertex2)

        # Check to see if we have found the goal
        if ai == self.goal:
            return self.graph


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
                ai = Vertex(closestPointToObstacle._x, closestPointToObstacle._y, closestPointOnEdge)

                # find the closest edge on the graph
                closestEdge = Geometry.findClosestEdgeOnGraph(self.graph, ai, self.stepSize)

                # find the closest point on the edge sending the step size
                closestPointOnEdge = Geometry.getNearestVertexOnLine(closestEdge.vertex1, closestEdge.vertex2, ai)

                # split the edge
                splitEdges = closestEdge.split(closestPointOnEdge)

                # add the split edges to the graph
                for e in splitEdges:
                    self.connect(e.vertex1, e.vertex2)

                # add the edge from the split point to the new ai
                newEdge = Edge(closestPointOnEdge, ai)
                self.connect(newEdge.vertex1, newEdge.vertex2)

            else: # we are not in collision with our new edge

                # split the edge
                splitEdges = closestEdge.split(closestPointOnEdge)

                # add the split edges to the graph
                for e in splitEdges:
                    self.connect(e.vertex1, e.vertex2)

                # add the edge from the split point to the ai
                newEdge = Edge(closestPointOnEdge, ai)
                self.connect(newEdge.vertex1, newEdge.vertex2)

            # Check to see if we have found the goal
            if ai == self.goal:
                break

        return self.graph

    def getRandomPointNoGoal(self, obstacles):

        # get a random x value
        x = self.getRandomNumber(self.xmin * 100, self.xmax * 100)
        xvalue = x / 100

        # get a random y value
        y = self.getRandomNumber(self.ymin * 100, self.ymax * 100)
        yvalue = y / 100

        # make a new vertex
        vertex = Vertex(xvalue, yvalue)

        isInObstacle = False

        #check to see if it is in an obstacle
        for obstacle in obstacles:
            if obstacle.contains(vertex):
                isInObstacle = True

        while isInObstacle == True:
            # get a random x value
            x = self.getRandomNumber(self.xmin * 100, self.xmax * 100)
            xvalue = x / 100

            # get a random y value
            y = self.getRandomNumber(self.ymin * 100, self.ymax * 100)
            yvalue = y / 100

            # make a new vertex
            vertex = Vertex(xvalue, yvalue)

            isInObstacle = False

            # check to see if it is in an obstacle
            for obstacle in obstacles:
                if obstacle.contains(vertex):
                    isInObstacle = True

        return vertex

    def combineGraphs(self, graph1:Graph, graph2:Graph):
        returnGraph = Graph()

        # TODO: what if our graph has no edges, our start or end graphs

        # add all the edges of the graphs
        # this will also add all the verticies
        for e in graph1.get_edges():
            returnGraph.add_edge(e)
        for e in graph2.get_edges():
            returnGraph.add_edge(e)

        return returnGraph

    def findClosestNeighbor(self, randomVertex, setOfComponents):
        shortestDist = float('inf')
        closestVertex = None

        for graph in setOfComponents:
            for vertex in graph.get_vertices():
                dist = Geometry.getEuclideanDistance(randomVertex, vertex)
                if dist < shortestDist:
                    closestVertex = vertex

        return closestVertex

    def PRM(self):
        # TODO: implement PRM in planning class
        # raise NotImplementedError
        setOfComponents = set()
        closestNeighborGoal = 15

        # G.init();i ← 0;
        # initialize our start and end points as a graph
        startGraph = Graph()
        startGraph.add_vertex(self.start)
        setOfComponents.add(startGraph)

        endGraph = Graph()
        endGraph.add_vertex(endGraph)
        setOfComponents.add(startGraph)

        for i in range(100):
            # choose a random point that is not in an obstacle
            randomVertex = self.getRandomPointNoGoal(self.obstacles)

            numberOfConnectedNeighbors = 0
            setOfGraphsWeAreConnectingTo = set()
            while numberOfConnectedNeighbors < 15:
                # find the closest neighbor
                closestNeighbor = self.findClosestNeighbor(randomVertex, setOfComponents)
                # get the closest graph
                closestGraph = closestNeighbor.connectedComponent
                # add a new edge to the existing graph
                edge = Edge(randomVertex, closestNeighbor)
                # check to see if we haven't hit an obstacle

                closestGraph.add_edge()
                # increment
                numberOfConnectedNeighbors = numberOfConnectedNeighbors + 1

                #check to see if we need to connect graphs











        # add this to our graph
        # while i < N
        #     if α(i) ∈ Cfree then
        #         G.add vertex(α(i)); i ← i + 1;
        #         for each q ∈ neighborhood(α(i),G)
        #             if ((not G.same component(α(i), q)) and connect(α(i), q)) then
        #                 G.add edge(α(i), q);
