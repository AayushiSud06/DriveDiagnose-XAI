import math


class EARCalculator:

    def __init__(self):
        pass

    def distance(self, p1, p2):

        return math.sqrt(
            (p1[0] - p2[0]) ** 2 +
            (p1[1] - p2[1]) ** 2
        )

    def calculate(self, eye_points):

        p1 = eye_points[0]
        p2 = eye_points[1]
        p3 = eye_points[2]
        p4 = eye_points[3]
        p5 = eye_points[4]
        p6 = eye_points[5]

        vertical1 = self.distance(p2, p6)

        vertical2 = self.distance(p3, p5)

        horizontal = self.distance(p1, p4)

        ear = (vertical1 + vertical2) / (2 * horizontal)

        return ear