import numpy as np

from pathlib import Path

from config import FEATURE_DIR


class FeatureDatabase:

    def __init__(self):

        FEATURE_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

    def store(

            self,

            image_path,

            descriptor_data):

        if descriptor_data is None:

            return

        descriptors = (

            descriptor_data[
                "descriptors"
            ]

        )

        if descriptors is None:

            return

        image_name = (

            Path(
                image_path
            )

            .stem

        )

        save_path = (

            FEATURE_DIR /

            f"{image_name}.npy"

        )

        np.save(

            save_path,

            descriptors

        )

        return save_path

    def load(

            self,

            descriptor_file):

        return np.load(

            descriptor_file,

            allow_pickle=True

        )

    def get_all_descriptors(self):

        return sorted(

            FEATURE_DIR.glob(
                "*.npy"
            )

        )