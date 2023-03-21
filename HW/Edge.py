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