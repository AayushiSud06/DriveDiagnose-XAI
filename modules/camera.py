import cv2
import time
from datetime import datetime

from utils.constants import *


class Camera:

    def __init__(self):

        self.cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
        print("Camera opened:", self.cap.isOpened())

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

        self.prev_time = time.time()

    def read(self):

        success, frame = self.cap.read()

        if not success:
            return None

        # -----------------------------
        # FPS
        # -----------------------------
        current_time = time.time()
        fps = 1 / (current_time - self.prev_time)
        self.prev_time = current_time

        # -----------------------------
        # Current Time
        # -----------------------------
        current_clock = datetime.now().strftime("%H:%M:%S")

        # -----------------------------
        # Header Background
        # -----------------------------
        cv2.rectangle(
            frame,
            (0, 0),
            (FRAME_WIDTH, HEADER_HEIGHT),
            DARK_GRAY,
            -1,
        )

        cv2.line(
            frame,
            (0, HEADER_HEIGHT),
            (FRAME_WIDTH, HEADER_HEIGHT),
            LIGHT_GRAY,
            2,
        )

        # =====================================================
        # FPS
        # =====================================================

        fps_text = f"FPS : {round(fps)}"

        cv2.putText(
            frame,
            fps_text,
            FPS_POS,
            FONT,
            1,
            CYAN,
            2,
        )

        # =====================================================
        # TITLE (Centered Automatically)
        # =====================================================

        title = "DriveDiagnose XAI"

        (title_width, _), _ = cv2.getTextSize(
            title,
            FONT,
            1,
            2,
        )

        title_x = (FRAME_WIDTH - title_width) // 2

        cv2.putText(
            frame,
            title,
            (title_x, 45),
            FONT,
            1,
            RED,
            2,
        )

        # =====================================================
        # SUBTITLE
        # =====================================================

        subtitle = "AI Driver Monitoring System"

        (subtitle_width, _), _ = cv2.getTextSize(
            subtitle,
            FONT,
            0.55,
            1,
        )

        subtitle_x = (FRAME_WIDTH - subtitle_width) // 2

        cv2.putText(
            frame,
            subtitle,
            (subtitle_x, 80),
            FONT,
            0.55,
            CYAN,
            1,
        )

        # =====================================================
        # CLOCK (Right Aligned Automatically)
        # =====================================================

        (clock_width, _), _ = cv2.getTextSize(
            current_clock,
            FONT,
            1,
            2,
        )

        clock_x = FRAME_WIDTH - clock_width - 30

        cv2.putText(
            frame,
            current_clock,
            (clock_x, 45),
            FONT,
            1,
            WHITE,
            2,
        )

        # =====================================================
        # STATUS
        # =====================================================

        status = "Driver Status : MONITORING"

        cv2.putText(
            frame,
            status,
            STATUS_POS,
            FONT,
            0.8,
            GREEN,
            2,
        )

        (status_width, status_height), _ = cv2.getTextSize(
            status,
            FONT,
            0.8,
            2,
        )

        circle_x = STATUS_POS[0] + status_width + 20
        circle_y = STATUS_POS[1] - status_height // 2

        cv2.circle(
            frame,
            (circle_x, circle_y),
            8,
            GREEN,
            -1,
        )

        return frame

    def release(self):

        self.cap.release()