import cv2

# Left eye landmark indices
LEFT_EYE = [33, 160, 158, 133, 153, 144]

# Right eye landmark indices
RIGHT_EYE = [362, 385, 387, 263, 373, 380]


class EyeDetector:

    def __init__(self):
        pass

    def draw_eye(self, frame, face, eye_points, width, height):

        """
        Draw eye landmarks and their indices.
        """

        for idx in eye_points:

            landmark = face.landmark[idx]

            x = int(landmark.x * width)
            y = int(landmark.y * height)

            # Draw landmark
            cv2.circle(
                frame,
                (x, y),
                4,
                (0, 255, 0),
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

            self.draw_eye(
                frame,
                face,
                LEFT_EYE,
                width,
                height,
            )

            self.draw_eye(
                frame,
                face,
                RIGHT_EYE,
                width,
                height,
            )

        return frame