import cv2

from modules.camera import Camera
from utils.constants import *

camera = Camera()

while True:

    frame = camera.read()

    if frame is None:
        break

    cv2.imshow(WINDOW_NAME, frame)

    if cv2.waitKey(1) == ord("q"):
        break

camera.release()

cv2.destroyAllWindows()