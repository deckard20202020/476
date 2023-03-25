class Edge:
    def __init__(self, vertex1, vertex2):
        self.vertex1 = vertex1
        self.vertex2 = vertex2

    def __eq__(self, other):
        if isinstance(other, Edge):
            return (self.vertex1 == other.vertex1 and self.vertex2 == other.vertex2) or \
                   (self.vertex1 == other.vertex2 and self.vertex2 == other.vertex1)
        return False

    def __hash__(self):
        return hash((self.vertex1, self.vertex2))

    def reverse(self):
        # TODO: implement reverse in edge class
        raise NotImplementedError

    def getDiscritizedState(self):
        # TODO: implement getDiscritizedState in edge class
        raise NotImplementedError

    def getNearestPoint(self):
        # TODO: implement getNearestPoint in edge class
        raise NotImplementedError

    def split(self):
        # TODO: implement split in edge class
        raise NotImplementedError

    def getLength(self):
        # TODO: implement getLength in edge class
        raise NotImplementedError
