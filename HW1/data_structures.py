from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue

class QueueBFS:

    def __init__(self):
        self.q = Queue()
        # self.parent_map = {}

    def pop(self):
        return self.q.get()

    # def insert(self, x, parent):
    #     self.q.put((x, parent))

    def insert(self, x):
        self.q.put(x)

    def is_empty(self):
        return self.q.empty()


class QueueDFS:

    def __init__(self):
        self.s = LifoQueue()
        # self.parent_map = {}

    def pop(self):
        # x = self.s.get()
        # self.s.get()
        return self.s.get()

    # def insert(self, x, parent):
    #     self.s.put((x, parent))

    def insert(self, x):
        self.s.put(x)

    def is_empty(self):
        return self.s.empty()

# returns the cost to go
def findManDist(x, goals, stateSpace):
    dist = 0;
    for goal in goals:
        # xdist = abs(x[0] - goal[0])
        # ydist = abs(x[1] - goal[1])
        # totalDist = xdist + ydist
        # dist = min(dist, totalDist)

        lowerBound = stateSpace.get_distance_lower_bound(x,goal)
        dist = min(dist, lowerBound)

    return dist


class QueueAstar:

    def __init__(self, Goals, StateSpace):
        self.pq = PriorityQueue()
        self.goals = Goals
        self.stateSpace = StateSpace

    def pop(self):
        tuple = self.pq.get()[0]
        return tuple
        # return self.pq.get()

    # def insert(self, x, parent):
    #     # I need to figure out distance
    #     self.pq.put((x, parent))

    def insert(self, x):
        # I need to figure out distance

        # cost to go is manhattan distance
        manDist = findManDist(x, self.goals, self.stateSpace)

        # how to figure out cost to come???


        self.pq.put((x, manDist))

    def is_empty(self):
        return self.pq.empty()