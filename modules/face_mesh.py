import cv2
import mediapipe as mp


class FaceMeshDetector:

    def __init__(self):

        self.mp_face_mesh = mp.solutions.face_mesh

        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        )

        self.drawer = mp.solutions.drawing_utils

        self.drawing_spec = self.drawer.DrawingSpec(
            thickness=1,
            circle_radius=1,
        )

    def process(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.face_mesh.process(rgb)

        return results
    
    def draw(self, frame, results):

     if results.multi_face_landmarks:

        for face in results.multi_face_landmarks:

            self.drawer.draw_landmarks(
                frame,
                face,
                self.mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=self.drawing_spec,
                connection_drawing_spec=self.drawing_spec,
            )

     return frame
    
    def count_faces(self, results):

     if results.multi_face_landmarks:
        return len(results.multi_face_landmarks)

     return 0