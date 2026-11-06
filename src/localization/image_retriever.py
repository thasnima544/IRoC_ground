import pandas as pd
from pathlib import Path

from config import IMAGE_INDEX_FILE


class ImageRetriever:

    def __init__(self, mission_folder):

        self.mission_folder = Path(
            mission_folder
        )

        self.image_index = pd.read_csv(

            self.mission_folder /
            IMAGE_INDEX_FILE

        )

    def get_image_record(
            self,
            image_name):

        row = self.image_index[

            self.image_index[
                "image_name"
            ]

            ==

            image_name

        ]

        if len(row) == 0:

            return None

        return row.iloc[0].to_dict()

    def get_timestamp(
            self,
            image_name):

        record = self.get_image_record(
            image_name
        )

        if record is None:

            return None

        return record[
            "timestamp_ns"
        ]