"""
=========================================================
mission_manager.py

COSMIC_GROUND
IRoC-U 2026

Mission Manager

Loads a completed mission dataset,
synchronizes timestamps,
prepares data for localization,
ORB feature extraction,
and ORB-SLAM3.

Author : Team Bitstream
=========================================================
"""

from pathlib import Path

from src.core.dataset_loader import DatasetLoader
from src.core.dataset_sync import DatasetSynchronizer


class MissionManager:

    def __init__(self, mission_folder):

        self.mission_folder = Path(mission_folder)

        self.loader = DatasetLoader(self.mission_folder)

        self.sync = DatasetSynchronizer()

        self.dataset = None

        self.synced_dataset = None

    ###########################################################

    def load(self):

        print("\nLoading Mission Dataset...")

        self.dataset = self.loader.load()

        return self.dataset

    ###########################################################

    def synchronize(self):

        if self.dataset is None:
            raise RuntimeError(
                "Dataset not loaded."
            )

        print("Synchronizing Images and Telemetry...")

        self.synced_dataset = self.sync.synchronize(

            self.dataset["images"],

            self.dataset["sensor"]

        )

        return self.synced_dataset

    ###########################################################

    def get_images(self):

        if self.synced_dataset is None:
            return []

        return self.synced_dataset

    ###########################################################

    def get_metadata(self):

        return self.dataset.get(
            "metadata",
            {}
        )

    ###########################################################

    def get_sensor(self):

        return self.dataset.get(
            "sensor",
            []
        )

    ###########################################################

    def get_events(self):

        return self.dataset.get(
            "events",
            []
        )

    ###########################################################

    def get_esp(self):

        return self.dataset.get(
            "esp",
            []
        )

    ###########################################################

    def summary(self):

        if self.dataset is None:
            return

        print()

        print("=" * 60)

        print("MISSION SUMMARY")

        print("=" * 60)

        print(
            f"Mission Folder : {self.mission_folder}"
        )

        print(
            f"Images         : {len(self.dataset['images'])}"
        )

        print(
            f"Sensor Samples : {len(self.dataset['sensor'])}"
        )

        print(
            f"ESP Samples    : {len(self.dataset['esp'])}"
        )

        print(
            f"Mission Events : {len(self.dataset['events'])}"
        )

        metadata = self.dataset.get(
            "metadata",
            {}
        )

        if metadata:

            print()

            for key, value in metadata.items():

                print(
                    f"{key} : {value}"
                )

        print("=" * 60)

    ###########################################################

    def ready(self):

        return (
            self.dataset is not None
            and
            self.synced_dataset is not None
        )


###############################################################

if __name__ == "__main__":

    mission = MissionManager(
        "datasets/mission_001"
    )

    mission.load()

    mission.synchronize()

    mission.summary()