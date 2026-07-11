class BlinkDetector:

    def __init__(self):

        self.threshold = 0.20

        self.eye_closed = False

        self.blink_count = 0

    def update(self, ear):

        # Eye closes
        if ear < self.threshold:

            self.eye_closed = True

        # Eye opens again
        elif self.eye_closed:

            self.blink_count += 1

            self.eye_closed = False

        return self.blink_count