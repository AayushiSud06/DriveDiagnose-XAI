class YawnDetector:

    def __init__(
        self,
        mar_threshold=0.6,
        consecutive_frames=15,
    ):

        self.mar_threshold = mar_threshold
        self.consecutive_frames = consecutive_frames

        self.open_frames = 0
        self.yawn_count = 0
        self.is_yawning = False

    def update(self, mar):

        # Mouth is open
        if mar > self.mar_threshold:

            self.open_frames += 1

            if self.open_frames >= self.consecutive_frames:
                self.is_yawning = True

        # Mouth has closed
        else:

            if self.is_yawning:
                self.yawn_count += 1

            self.open_frames = 0
            self.is_yawning = False

        return self.yawn_count, self.is_yawning