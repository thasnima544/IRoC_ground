"""
=========================================================
orbslam_runner.py

COSMIC_GROUND
IRoC-U 2026

Official ORB-SLAM3 Runner

Author : Team Bitstream
=========================================================
"""

import subprocess
import time
from pathlib import Path

from src.slam.slam_config import (
    MONOCULAR_EXECUTABLE,
    VOCABULARY,
    CAMERA_YAML,
    PRINT_STATUS
)


class ORBSLAMRunner:

    def __init__(self):

        self.process = None

    ###########################################################

    def verify(self):

        if not MONOCULAR_EXECUTABLE.exists():
            raise FileNotFoundError(
                f"ORB executable not found:\n{MONOCULAR_EXECUTABLE}"
            )

        if not VOCABULARY.exists():
            raise FileNotFoundError(
                f"Vocabulary not found:\n{VOCABULARY}"
            )

        if not CAMERA_YAML.exists():
            raise FileNotFoundError(
                f"Camera YAML not found:\n{CAMERA_YAML}"
            )

        return True

    ###########################################################

    def run(self, mission_folder):

        self.verify()

        mission_folder = Path(mission_folder)

        image_folder = mission_folder / "images"

        if not image_folder.exists():

            raise RuntimeError(
                "Mission images folder not found."
            )

        command = [

            str(MONOCULAR_EXECUTABLE),

            str(VOCABULARY),

            str(CAMERA_YAML),

            str(image_folder)

        ]

        if PRINT_STATUS:

            print("\nLaunching ORB-SLAM3...\n")

            print(" ".join(command))

        start = time.time()

        self.process = subprocess.Popen(

            command,

            stdout=subprocess.PIPE,

            stderr=subprocess.STDOUT,

            universal_newlines=True

        )

        output = []

        while True:

            line = self.process.stdout.readline()

            if line == "" and self.process.poll() is not None:

                break

            if line:

                output.append(line.strip())

                if PRINT_STATUS:

                    print(line.strip())

        return_code = self.process.wait()

        elapsed = time.time() - start

        return {

            "success": return_code == 0,

            "return_code": return_code,

            "time": elapsed,

            "console": output,

            "mission_folder": str(mission_folder)

        }

    ###########################################################

    def shutdown(self):

        if self.process:

            self.process.terminate()

    ###########################################################

    def save(self):

        pass