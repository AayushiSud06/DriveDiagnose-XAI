import cv2

from modules.camera import Camera
from modules.face_mesh import FaceMeshDetector
from utils.constants import *

camera = Camera()

face_mesh = FaceMeshDetector()

while True:

    frame = camera.read()

    if frame is None:
        break

    results = face_mesh.process(frame)

    frame = face_mesh.draw(frame, results)

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

    cv2.imshow(WINDOW_NAME, frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()

cv2.destroyAllWindows()