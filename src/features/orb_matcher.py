import cv2
import numpy as np

from pathlib import Path

from src.features.feature_extractor import (
    FeatureExtractor
)

from src.features.feature_database import (
    FeatureDatabase
)

from config import MATCH_RATIO
from config import MIN_MATCH_COUNT


class ORBMatcher:

    def __init__(self):

        self.extractor = (
            FeatureExtractor()
        )

        self.feature_db = (
            FeatureDatabase()
        )

        self.matcher = cv2.BFMatcher(
            cv2.NORM_HAMMING,
            crossCheck=False
        )

    def match_seed(

            self,

            seed_image_path):

        seed = cv2.imread(
            str(seed_image_path),
            cv2.IMREAD_GRAYSCALE
        )

        if seed is None:

            raise Exception(
                "Seed image not found"
            )

        seed = cv2.resize(

            seed,

            (640, 640)

        )

        seed_features = (

            self.extractor
            .extract_from_image(
                seed
            )

        )

        seed_des = (

            seed_features[
                "descriptors"
            ]

        )

        if seed_des is None:

            return None

        best_score = 0

        best_match = None

        descriptor_files = (

            self.feature_db
            .get_all_descriptors()

        )

        for desc_file in descriptor_files:

            try:

                db_des = (

                    self.feature_db
                    .load(
                        desc_file
                    )

                )

                if db_des is None:

                    continue

                matches = (

                    self.matcher
                    .knnMatch(

                        seed_des,

                        db_des,

                        k=2

                    )

                )

                good = []

                for m, n in matches:

                    if (

                        m.distance

                        <

                        MATCH_RATIO
                        * n.distance

                    ):

                        good.append(m)

                score = len(good)

                if score > best_score:

                    best_score = score

                    best_match = {

                        "image_name":

                            desc_file
                            .stem + ".jpg",

                        "score":

                            score,

                        "descriptor":

                            str(
                                desc_file
                            )

                    }

            except Exception:

                continue

        if best_match is None:

            return None

        if (

            best_match[
                "score"
            ]

            <

            MIN_MATCH_COUNT

        ):

            return None

        return best_match