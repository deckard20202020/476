from HW.data_structures import QueueBFS, QueueDFS, QueueAstar

ALG_BFS = "bfs"
ALG_DFS = "dfs"
ALG_ASTAR = "astar"

class StateSpace:
    """A base class to specify a state space X"""

    def __init__(self, initial_state, goal_states, states):
        self.initial_state = initial_state
        self.goal_states = set(goal_states)
        self.states = set(states)

    def __contains__(self, x):
        """Return whether the given state x is in the state space"""
        raise NotImplementedError

    def get_distance_lower_bound(self, x1, x2):
        """Return the lower bound on the distance between the given states x1 and x2"""
        return 0


class ActionSpace:
    """A base class to specify an action space"""

    def __call__(self, x):
        """ Return the list of all the possible actions at the given state x"""
        raise NotImplementedError


class StateTransition:
    """A base class to specify a state transition function"""

    def __call__(self, x, u):
        """Return the new state obtained by applying action u at state x"""
        raise NotImplementedError


def reconstructPath(node, parents):
    path = []
    currentNode = node
    while currentNode is not None:
        # add the node to the path
        path.append(currentNode)
        currentNode = parents[currentNode]

    path.reverse()

    return path


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
    # some states in XG may not be in X and XG may be empty
    # just return the path to the first goal you find

    # get the queue you need
    if alg == "bfs":
        q1 = QueueBFS()
    elif alg == "dfs":
        q1 = QueueDFS()
    else:
        q1 = QueueAstar(XG, X, xI)

    # declare a set to keep track of our visited
    # visited = set()
    # a set would be faster for contains()
    # but we need to use a list for grading
    visited = []

    # put the xI in our queue
    q1.insert(xI, None)

    # mark starting state as visited
    # visited.add(xI)
    # a set would be faster for contains()
    # but we need to use a list for grading
    visited.append(xI)

    # # dict to keep track of path
    parents = {xI: None}

    # while the q is not empty
    while not q1.is_empty():

        # pop the queue
        node = q1.pop()

        # if node is in the goal state return SUCCESS XG is a list
        if (node in XG):
            # we should be returning a list of node we visited

            # and a path from xI to XG
            path = reconstructPath(node, parents)

            return {"visited": list(visited), "path": path}

        # find the neighbors (u in U(x) x' <- f(x,u)
        neighbors = U(node)

        # for each of the neighbors
        for neighbor in neighbors:
            # if neighbor not visited
            if (neighbor not in visited):
                # mark it as visited
                # visited.add(neighbor)
                visited.append(neighbor)
                # insert it in the q
                q1.insert(neighbor, node)
                # update the parent
                parents[neighbor] = node
            else:
            #     Resolve Duplicate x'
            #     need to update cost to come dictionary as well as distance in the pq
                q1.updateCostToCome(neighbor, node)

    # return FAILURE
    return {"visited": list(visited), "path": {}}

    # raise NotImplementedError
