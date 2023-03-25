class Vertex:

    def __init__(self, x, y, parent = None):
        self.x = x
        self.y = y
        self.parent = parent

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))

    def getX(self, vertex):
        return vertex.x

    def getY(self, vertex):
        return vertex.y

    def getParent(self, vertex):
        return vertex.parent

    def setParent(self, vertex, parent):
        vertex.parent = parent