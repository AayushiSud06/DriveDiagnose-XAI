import cv2

# Left eye landmark indices
LEFT_EYE = [33, 160, 158, 133, 153, 144]

# Right eye landmark indices
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

# Mouth landmark indices
MOUTH = [61, 13, 291, 14]


class EyeDetector:

    def __init__(self):
        pass

    def draw_landmarks(
        self,
        frame,
        face,
        landmark_indices,
        width,
        height,
        color=(0, 255, 0),
    ):
        """
        Draw facial landmarks and their indices.
        """

        for idx in landmark_indices:

            landmark = face.landmark[idx]

            x = int(landmark.x * width)
            y = int(landmark.y * height)

            # Draw landmark
            cv2.circle(
                frame,
                (x, y),
                4,
                color,
                -1,
            )

            # Draw landmark number
            cv2.putText(
                frame,
                str(idx),
                (x + 5, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.4,
                (0, 255, 255),
                1,
            )

    def draw(self, frame, results):

        if not results.multi_face_landmarks:
            return frame

        height, width, _ = frame.shape

        for face in results.multi_face_landmarks:

            # Left eye
            self.draw_landmarks(
                frame,
                face,
                LEFT_EYE,
                width,
                height,
                (0, 255, 0),
            )

            # Right eye
            self.draw_landmarks(
                frame,
                face,
                RIGHT_EYE,
                width,
                height,
                (0, 255, 0),
            )

            # Mouth
            self.draw_landmarks(
                frame,
                face,
                MOUTH,
                width,
                height,
                (0, 0, 255),
            )

        return frame

    def get_landmark_points(
        self,
        face,
        landmark_indices,
        width,
        height,
    ):

        points = []

        for idx in landmark_indices:

            landmark = face.landmark[idx]

            x = int(landmark.x * width)
            y = int(landmark.y * height)

            points.append((x, y))

        return points