"""
=========================================================
camera_loader.py

COSMIC_GROUND
IRoC-U 2026

Camera Calibration Loader

Loads ORB-SLAM3 camera.yaml

=========================================================
"""

from pathlib import Path
import cv2

from src.slam.slam_config import CAMERA_YAML


class CameraLoader:

    def __init__(self):

        self.yaml_path = Path(CAMERA_YAML)

        self.parameters = {}

    ###########################################################

    def verify(self):

        if not self.yaml_path.exists():

            raise FileNotFoundError(

                f"Camera YAML not found:\n{self.yaml_path}"

            )

        return True

    ###########################################################

    def load(self):

        self.verify()

        fs = cv2.FileStorage(

            str(self.yaml_path),

            cv2.FILE_STORAGE_READ

        )

        if not fs.isOpened():

            raise RuntimeError(

                "Unable to open camera.yaml"

            )

        self.parameters = {

            "Camera.fx": fs.getNode("Camera.fx").real(),

            "Camera.fy": fs.getNode("Camera.fy").real(),

            "Camera.cx": fs.getNode("Camera.cx").real(),

            "Camera.cy": fs.getNode("Camera.cy").real(),

            "Camera.k1": fs.getNode("Camera.k1").real(),

            "Camera.k2": fs.getNode("Camera.k2").real(),

            "Camera.p1": fs.getNode("Camera.p1").real(),

            "Camera.p2": fs.getNode("Camera.p2").real(),

            "Camera.k3": fs.getNode("Camera.k3").real(),

            "Camera.width": int(

                fs.getNode("Camera.width").real()

            ),

            "Camera.height": int(

                fs.getNode("Camera.height").real()

            ),

            "Camera.fps": fs.getNode("Camera.fps").real()

        }

        fs.release()

        return self.parameters

    ###########################################################

    def print(self):

        if len(self.parameters) == 0:

            self.load()

        print("\nCamera Parameters\n")

        for key, value in self.parameters.items():

            print(f"{key} : {value}")


###############################################################

if __name__ == "__main__":

    camera = CameraLoader()

    camera.load()

    camera.print()