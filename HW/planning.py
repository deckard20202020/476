class Planning:
    def __init__(self):
        pass

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

            def makeEdge(self, start, end):
                # TODO: implement makeEdge function in straight edge creator
                return (start, end)

    class distanceComputator:
        def __init__(self):
            pass

        def euclideanDistanceComputator(self, node1, node2):
            # TODO: implement euclideanDistanceComputator in planning class
            return ((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2) ** 0.5

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
                # ...
                return True

            def isCheckingRequired(self):
                # TODO: implement isCheckingRequired in planning class
                # When should we use this???
                #     do we use it if the newly created edge intersects an obstacle???
                # check if collision checking is required based on obstacle presence and position
                # ...
                return True