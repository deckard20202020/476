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


class QueueAstar:

    def __init__(self):
        self.pq = PriorityQueue()

    def pop(self):
        return self.pq.get()

    # def insert(self, x, parent):
    #     # I need to figure out distance
    #     self.pq.put((x, parent))

    def insert(self, x):
        # I need to figure out distance

        self.pq.put(x)

    def is_empty(self):
        return self.pq.empty()