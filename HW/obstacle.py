from HW.geometry import Geometry

class Obstacle:
    def __init__(self, name):
        self.name = name
        # TODO: implement Obstacle init in edge class
        raise NotImplementedError

    def contains(self, point):
        raise NotImplementedError


class CircularObstacle(Obstacle):
    def __init__(self, name, center, radius):
        super().__init__(name)
        self.center = center
        self.radius = radius

    def getBoundaries(self):
        # TODO: implement getBoundaries
        # what do I need this for???
        return self.center, self.radius

    def contains(self, point):
        # TODO: implement contains in circle obstacle class
        distance = Geometry.getEuclideanDistance(point, self.center)
        # distance = ((point[0] - self.center[0]) ** 2 + (point[1] - self.center[1]) ** 2) ** 0.5
        if distance <= self.radius:
            return True
        return False


class WorldBoundary2D(Obstacle):
    def __init__(self, name, x_min, x_max, y_min, y_max):
        super().__init__(name)
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def contains(self, point):
        if self.x_min <= point[0] <= self.x_max and self.y_min <= point[1] <= self.y_max:
            return True
        return False