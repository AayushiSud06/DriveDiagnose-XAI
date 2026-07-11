import cv2

from modules.camera import Camera
from modules.face_mesh import FaceMeshDetector
from modules.eye_detector import *
from modules.ear import EARCalculator
from modules.blink_detector import BlinkDetector
from utils.constants import *

camera = Camera()
face_mesh = FaceMeshDetector()
eye_detector = EyeDetector()
ear = EARCalculator()
blink_detector = BlinkDetector()

blink_count = 0

while True:

    frame = camera.read()

    if frame is None:
        break

    results = face_mesh.process(frame)

    frame = face_mesh.draw(frame, results)
    frame = eye_detector.draw(frame, results)

    faces = face_mesh.count_faces(results)

    cv2.putText(
        frame,
        f"Faces Detected : {faces}",
        (30, 170),
        FONT,
        0.8,
        CYAN,
        2,
    )

    h, w, _ = frame.shape

    if results.multi_face_landmarks:

        face = results.multi_face_landmarks[0]

        left_points = eye_detector.get_eye_points(
            face,
            LEFT_EYE,
            w,
            h,
        )

        right_points = eye_detector.get_eye_points(
            face,
            RIGHT_EYE,
            w,
            h,
        )

        left_ear = ear.calculate(left_points)
        right_ear = ear.calculate(right_points)

        average_ear = (left_ear + right_ear) / 2

        cv2.putText(
            frame,
            f"Left EAR : {left_ear:.2f}",
            (30, 210),
            FONT,
            0.7,
            GREEN,
            2,
        )

        cv2.putText(
            frame,
            f"Right EAR : {right_ear:.2f}",
            (30, 250),
            FONT,
            0.7,
            GREEN,
            2,
        )

        cv2.putText(
            frame,
            f"Average EAR : {average_ear:.2f}",
            (30, 290),
            FONT,
            0.7,
            CYAN,
            2,
        )

        blink_count = blink_detector.update(average_ear)

    cv2.putText(
        frame,
        f"Blinks : {blink_count}",
        (30, 330),
        FONT,
        0.7,
        GREEN,
        2,
    )

    cv2.imshow(WINDOW_NAME, frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()