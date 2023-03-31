class Vertex:

    def __init__(self, x, y, parent = None):
        self._x = x
        self._y = y
        self._parent = parent
        self.connectedComponent = None

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self._x == other._x and self._y == other._y
        return False

    def __hash__(self):
        return hash((self._x, self._y))

    def getX(self, vertex):
        return vertex._x

    def getY(self, vertex):
        return vertex._y

    def getParent(self, vertex):
        return vertex._parent

    def setParent(self, vertex, parent):
        vertex._parent = parent