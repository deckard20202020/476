import math


class Geometry:
    def __init__(self):
        pass

    @staticmethod
    def getNearestPointOnLine(line_start, line_end, point):
        # TODO: implement getNearestPointOnLine in geometry class
        x1, y1 = line_start
        x2, y2 = line_end
        x3, y3 = point

        px = x2 - x1
        py = y2 - y1

        d = px * px + py * py

        u = ((x3 - x1) * px + (y3 - y1) * py) / float(d)

        if u > 1:
            u = 1
        elif u < 0:
            u = 0

        x = x1 + u * px
        y = y1 + u * py

        return x, y

    @staticmethod
    def getEuclideanDistance(point1, point2):
        x1, y1 = point1
        x2, y2 = point2

        dx = x2 - x1
        dy = y2 - y1

        return math.sqrt(dx * dx + dy * dy)

    @staticmethod
    def isInsideCircle(center, radius, point):
        # TODO: double check isInsideCircle method in geometry
        x1, y1 = center
        x2, y2 = point

        distance = Geometry.getEuclideanDistance((x1, y1), (x2, y2))

        if distance <= radius:
            return True
        else:
            return False
