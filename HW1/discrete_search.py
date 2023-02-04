import queue
from abc import abstractmethod

ALG_BFS = "bfs"
ALG_DFS = "dfs"
ALG_ASTAR = "astar"


class StateSpace:
    """A base class to specify a state space X"""
    """a list or set of goal states"""
    """initial state is a tuple"""
    """will we need a new class to represent a state?"""
    """a set or list of states"""
    """needs to be able to be searched quickly for contains method"""

    def __init__(self, initial_state, goal_states, states):
        self.initial_state = initial_state
        self.goal_states = set(goal_states)
        self.states = set(states)

    def __contains__(self, x):
        """Return whether the given state x is in the state space"""
        return x in self.states
        """raise NotImplementedError"""

    def get_distance_lower_bound(self, x1, x2):
        """Return the lower bound on the distance between the given states x1 and x2"""
        return 0


class ActionSpace:
    """A base class to specify an action space"""
    """A set of all actions"""

    def __call__(self, x):
        """ Return the list of all the possible actions at the given state x"""
        raise NotImplementedError


class StateTransition:
    """A base class to specify a state transition function"""

    def __call__(self, x, u):
        """Return the new state obtained by applying action u at state x"""
        raise NotImplementedError

class AbstractQueue:
    """A base class for a Queue"""

    @abstractmethod
    def pop(self):
        raise NotImplementedError

    @abstractmethod
    def insert(self, x, parent):
        raise NotImplementedError

    @abstractmethod
    def maintain_parent(self):
        raise NotImplementedError

    @abstractmethod
    def is_empty(self):
        raise NotImplementedError

class QueueBFS(AbstractQueue):

    def __int__(self):
        self.q = queue.Queue()
        # self.parent_map = {}

    def pop(self):
        return self.q.get()
        # x = self.q.get()
        # return x, self.parent_map[x]
    """x,y = q.pop()"""

    def insert(self, x, parent):
        self.q.put((x, parent))
        # self.parent_map[x] = parent

    def is_empty(self):
        return self.q.empty()


class QueueDFS(AbstractQueue):

    def __init__(self):
        self.s = queue.LifoQueue()
        # self.parent_map = {}

    def pop(self):
        # x = self.s.get()
        # self.s.get()
        return self.s.get()

    def insert(self, x, parent):
        self.s.put((x, parent))

    def is_empty(self):
        return self.q.empty()

class QueueAstar(AbstractQueue):

    def __init__(self):
        self.pq = queue.PriorityQueue

    def pop(self):
        return self.pq.get()

    def insert(self, x, parent):
        # I need to figure out distance
        self.pq.put((x, parent))

    def is_empty(self):
        return self.q.empty()


def fsearch(X, U, f, xI, XG, alg):
    """Return the list of visited nodes and a path from xI to XG based on the given algorithm
    This is the general template for forward search describe in Figure 2.4 in the textbook.
    @type X:   an instance of the StateSpace class (or its derived class) that represent the state space
    @type U:   an instance of the ActionSpace class (or its derived class) such that
               U(x) returns the list of all the possible actions at state x
    @type f:   an instance of the StateTransition class  (or its derived class) such that
               f(x, u) returns the new state obtained by applying action u at cell x
    @type xI:  an initial state such that xI in X
    @type XG:  a list of states that specify the goal set
    @type alg: a string in {"bfs", "dfs", "astar"} that specifies the discrete search algorithm to use
    @return:   a dictionary {"visited": visited_states, "path": path} where visited_states is the list of
               states visited during the search and path is a path from xI to a state in XG
    """
    # TODO: Implement this function
    """will I need a function generateQueue(algo) that generates the type of queue needed for each algo"""
    # some states in XG may not be in X and XG may be empty
    # just return the path to the first goal you find

    # get the queue you need
    if alg == "bfs":
        q = QueueBFS()
    elif alg == "dfs":
        q = QueueDFS
    else:
        q = QueueAstar

    # declare a set to keep track of our visited
    visited = set()

    # put the xI in our queue
    q.insert(xI, None)

    # while the q is not empty
    while not q.is_empty():
        # pop the queue
        node = q.pop()
        # mark as visited
        visited.add(node)
        # find the neighbors
        # check if they are in the state space
        # if they aren't visited'
        #      'add them to the q'


        # add the parent to our neighbors, which is node

        # add them to the queue






    raise NotImplementedError