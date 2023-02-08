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

    def updateQueue(self, node, parent):
        a = None


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

    def updateQueue(self, node, parent):
        a = None

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
        tup = self.min_heap.pop()[1][0]
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

        # tuples = [((1, 2), 100), ((3, 4), 5), ((5, 6), 1), ((7, 8), 8), ((9, 10), 4)]

        #
        # for t in tuples:
        #     heapq.heappush(min_heap, (t[1], t))

    def is_empty(self):
        # return self.pq.empty()
        return len(self.min_heap) == 0

    def updateQueue(self, node, parent):
        costToComeOfParent = self.costToCome[parent]
        costToCome = costToComeOfParent + 1

        # cost to go is manhattan distance
        manDist = findManDist(node, self.goals, self.stateSpace)

        # sum the cost to come and the cost to go
        totalCost = manDist + costToCome

        # find the node in the min_heap and update it
        for i in range(len(self.min_heap)):
            possibleMatch = self.min_heap[i][1][0]
            if possibleMatch == node:
                currTotalCost = self.min_heap[i][1][2]
                totalCost = min(totalCost, currTotalCost)
                self.min_heap[i] = (self.min_heap[i][1], totalCost)

        heapq.heapify(self.min_heap)

