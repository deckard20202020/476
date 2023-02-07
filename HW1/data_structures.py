from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue

class QueueBFS:

    def __init__(self):
        self.q = Queue()

    def pop(self):
        return self.q.get()

    def insert(self, x):
        self.q.put(x)

    def is_empty(self):
        return self.q.empty()


class QueueDFS:

    def __init__(self):
        self.s = LifoQueue()

    def pop(self):
        return self.s.get()

    def insert(self, x):
        self.s.put(x)

    def is_empty(self):
        return self.s.empty()

# returns the cost to go by looping though the goals
def findManDist(x, goals, stateSpace):
    dist = 0;
    for goal in goals:
        lowerBound = stateSpace.get_distance_lower_bound(x, goal)
        dist = min(dist, lowerBound)

    return dist


class QueueAstar:

    def __init__(self, Goals, StateSpace):
        self.pq = PriorityQueue()
        self.goals = Goals
        self.stateSpace = StateSpace

    def pop(self):
        # we only return the grid tuple, not the distance
        tup = self.pq.get()[0]
        return tup

    def insert(self, x):

        # first element is two-tuple
        # second element = distance
        # how can I sort the PriorityQueue by the last elemnt?

        # I need to figure out distance

        # cost to go is manhattan distance
        manDist = findManDist(x, self.goals, self.stateSpace)

        # how to figure out cost to come???
        costToCome = 0

        # sum the cost to come and the cost to go
        totalCost = manDist + costToCome

        self.pq.put((x, totalCost))

    def is_empty(self):
        return self.pq.empty()