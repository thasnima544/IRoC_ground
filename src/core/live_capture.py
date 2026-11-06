"""
=========================================================
live_capture.py

COSMIC_GROUND
IRoC-U 2026

Live image capture from OV9281 USB Camera.

Author : Team Bitstream
=========================================================
"""

import cv2
from pathlib import Path

from config import (
    CAMERA_INDEX,
    FRAME_WIDTH,
    FRAME_HEIGHT,
    FPS,
    IMAGE_FORMAT,
    IMAGE_PREFIX,
    SHOW_CAMERA
)

from src.telemetry.timestamp_sync import TimestampSync


class LiveCapture:

    def __init__(self, mission_folder):

        self.timestamp = TimestampSync()

        self.mission_folder = Path(mission_folder)

        self.image_folder = self.mission_folder / "images"

        self.image_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        self.cap = cv2.VideoCapture(
            CAMERA_INDEX,
            cv2.CAP_V4L2
        )

        if not self.cap.isOpened():
            raise RuntimeError(
                "Unable to open camera."
            )

        self.cap.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            FRAME_WIDTH
        )

        self.cap.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            FRAME_HEIGHT
        )

        self.cap.set(
            cv2.CAP_PROP_FPS,
            FPS
        )

        self.cap.set(
            cv2.CAP_PROP_BUFFERSIZE,
            1
        )

        print("\nCamera Initialized")

        print(f"Resolution : {FRAME_WIDTH} x {FRAME_HEIGHT}")

        print(f"FPS : {FPS}")

    ############################################################

    def capture(self):

        ret, frame = self.cap.read()

        if not ret:

            return None

        timestamp = self.timestamp.unix()

        filename = self.timestamp.image_name(
            IMAGE_PREFIX,
            IMAGE_FORMAT
        )

        image_path = self.image_folder / filename

        cv2.imwrite(
            str(image_path),
            frame
        )

        if SHOW_CAMERA:

            preview = frame.copy()

            cv2.putText(

                preview,

                filename,

                (20, 35),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.7,

                (0, 255, 0),

                2

            )

            cv2.imshow(
                "COSMIC Camera",
                preview
            )

            cv2.waitKey(1)

        return {

            "timestamp": timestamp,

            "filename": filename,

            "path": image_path,

            "frame": frame

        }

    ############################################################

    def release(self):

        if self.cap is not None:

            self.cap.release()

        cv2.destroyAllWindows()

        print("Camera Released")


#################################################################

if __name__ == "__main__":

    import time

    mission = Path("datasets/test_mission")

    cam = LiveCapture(mission)

    try:

        while True:

            data = cam.capture()

            if data:

                print(

                    f"{data['filename']}"

                    f"   "

                    f"{data['timestamp']}"

                )

            time.sleep(0.10)

    except KeyboardInterrupt:

        cam.release()