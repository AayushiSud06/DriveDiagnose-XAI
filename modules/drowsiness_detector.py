class DrowsinessDetector:

    def __init__(self):

        self.threshold = 0.20

        self.closed_frames = 0

        self.warning_frames = 15

        self.drowsy_frames = 30

    def update(self, ear):

        if ear < self.threshold:
            self.closed_frames += 1
        else:
            self.closed_frames = 0

        if self.closed_frames >= self.drowsy_frames:
            return "DROWSY"

        elif self.closed_frames >= self.warning_frames:
            return "WARNING"

        return "SAFE"