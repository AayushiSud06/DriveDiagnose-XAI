import math


class MARCalculator:

    def __init__(self):
        pass

    def distance(self, p1, p2):
        return math.dist(p1, p2)

    def calculate(self, mouth_points):

        left = mouth_points[0]
        top = mouth_points[1]
        right = mouth_points[2]
        bottom = mouth_points[3]

        vertical = self.distance(top, bottom)
        horizontal = self.distance(left, right)

        if horizontal == 0:
            return 0

        mar = vertical / horizontal

        return mar