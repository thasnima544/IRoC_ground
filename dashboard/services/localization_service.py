from pathlib import Path

from src.localization.seed_localizer import (
    SeedLocalizer
)


class LocalizationService:

    def __init__(self):

        self.datasets_dir = (
            Path("../datasets")
        )

    def get_latest_mission(self):

        missions = sorted(

            self.datasets_dir.glob(
                "mission_*"
            )

        )

        if not missions:

            return None

        return missions[-1]

    def localize(
            self,
            seed_image):

        mission = (
            self.get_latest_mission()
        )

        if mission is None:

            return {

                "success":
                    False,

                "message":
                    "No mission dataset"

            }

        localizer = (

            SeedLocalizer(
                mission
            )

        )

        result = (

            localizer.localize(
                seed_image
            )

        )

        return result