"""
=========================================================
frame_manager.py

COSMIC_GROUND
IRoC-U 2026

Frame Manager

Loads images from a mission in timestamp order.

Author : Team Bitstream
=========================================================
"""

import cv2
import pandas as pd
from pathlib import Path

from config import IMAGE_INDEX_FILE


class FrameManager:

    def __init__(self, mission_folder):

        self.mission_folder = Path(mission_folder)

        self.image_folder = self.mission_folder / "images"

        self.index_file = self.mission_folder / IMAGE_INDEX_FILE

        self.frames = []

    ###########################################################

    def load(self):

        if not self.index_file.exists():

            raise FileNotFoundError(

                self.index_file

            )

        table = pd.read_csv(

            self.index_file

        )

        table = table.sort_values(

            "timestamp"

        )

        self.frames = []

        for _, row in table.iterrows():

            image_path = self.image_folder / row["image_name"]

            self.frames.append({

                "timestamp": row["timestamp"],

                "image_name": row["image_name"],

                "image_path": image_path

            })

        return self.frames

    ###########################################################

    def images(self):

        if len(self.frames) == 0:

            self.load()

        for frame in self.frames:

            image = cv2.imread(

                str(frame["image_path"]),

                cv2.IMREAD_GRAYSCALE

            )

            if image is None:

                continue

            yield {

                "timestamp": frame["timestamp"],

                "image_name": frame["image_name"],

                "image": image

            }

    ###########################################################

    def count(self):

        if len(self.frames) == 0:

            self.load()

        return len(self.frames)