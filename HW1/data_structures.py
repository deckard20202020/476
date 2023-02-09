from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue
import heapq
import sys

class QueueBFS:

    def __init__(self):
        self.q = Queue()
        # self.costToCome = {}

    def pop(self):
        return self.q.get()

    def insert(self, node, parent):
        self.q.put(node)

    def is_empty(self):
        return self.q.empty()

    def updateCostToCome(self, node, parent):
        a = "We Don't need anything here"


class QueueDFS:

    def __init__(self):
        self.s = LifoQueue()
        # self.parents = {}

    def pop(self):
        return self.s.get()

    def insert(self, node, parent):
        self.s.put(node)

    def is_empty(self):
        return self.s.empty()

    def updateCostToCome(self, node, parent):
        a = "We dont need anything here"

# returns the cost to go by looping though the goals
def findManDist(x, goals, stateSpace):
    dist = sys.maxsize;
    for goal in goals:
        lowerBound = stateSpace.get_distance_lower_bound(x, goal)
        dist = min(dist, lowerBound)

    return dist


class QueueAstar:

    def __init__(self, Goals, StateSpace, xI):
        # self.pq = PriorityQueue()
        self.min_heap = []
        self.goals = Goals
        self.stateSpace = StateSpace
        self.costToCome = {}
        self.initialState = xI

    def pop(self):
        # we only return the grid tuple, not the distance
        # tup = self.pq.get()[0]
        entry = self.min_heap.pop()
        tup = entry[1][0]
        return tup

    def insert(self, node, parent):

        # first element is two-tuple
        # second element = distance
        # how can I sort the PriorityQueue by the last element?

        costToCome = 0
        # check for initial state
        if node == self.initialState:
            # update the cost to come
            self.costToCome[node] = 0
        else:
            costToComeOfParent = self.costToCome[parent]
            costToCome = costToComeOfParent + 1
            self.costToCome[node] = costToCome

        # cost to go is manhattan distance
        manDist = findManDist(node, self.goals, self.stateSpace)

        # sum the cost to come and the cost to go
        totalCost = manDist + costToCome

        # self.pq.put(node, totalCost)
        entry = (node, totalCost)
        heapq.heappush(self.min_heap, (entry[1], entry))

    def is_empty(self):
        # return self.pq.empty()
        return len(self.min_heap) == 0

    def updateCostToCome(self, node, parent):
        currentCostToCome = self.costToCome[node]
        possibleNewCostToCome = self.costToCome[parent] + 1
        newCostToCome = min(currentCostToCome, possibleNewCostToCome)
        self.costToCome[node] = newCostToCome

