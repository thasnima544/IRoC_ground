from pathlib import Path

from src.features.orb_matcher import (
    ORBMatcher
)

from src.localization.image_retriever import (
    ImageRetriever
)

from src.localization.coordinate_lookup import (
    CoordinateLookup
)

from config import TRAJECTORY_OUTPUT


class SeedLocalizer:

    def __init__(
            self,
            mission_folder):

        self.mission_folder = (
            Path(
                mission_folder
            )
        )

        self.matcher = ORBMatcher()

        self.image_db = (

            ImageRetriever(
                mission_folder
            )

        )

        self.coord_lookup = (

            CoordinateLookup(

                TRAJECTORY_OUTPUT

            )

        )

    def localize(
            self,
            seed_image):

        match = (

            self.matcher
            .match_seed(
                seed_image
            )

        )

        if match is None:

            return {

                "success":
                    False,

                "message":
                    "No match found"

            }

        image_name = (

            match[
                "image_name"
            ]

        )

        timestamp_ns = (

            self.image_db
            .get_timestamp(
                image_name
            )

        )

        pose = (

            self.coord_lookup
            .nearest_pose(
                timestamp_ns
            )

        )

        return {

            "success":
                True,

            "matched_image":
                image_name,

            "timestamp_ns":
                timestamp_ns,

            "score":
                match[
                    "score"
                ],

            "pose":
                pose
        }