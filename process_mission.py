"""
=========================================================
process_mission.py

COSMIC_GROUND
IRoC-U 2026

Offline Mission Processing Pipeline

Pipeline

Dataset
    ↓
ORB Features
    ↓
Trajectory
    ↓
ORB-SLAM3
    ↓
Localization
    ↓
Outputs

=========================================================
"""

import time
from pathlib import Path

from config import *

from src.core.dataset_loader import DatasetLoader

from src.database.database_manager import DatabaseManager

from src.features.feature_extractor import FeatureExtractor
from src.features.feature_database import FeatureDatabase

from src.trajectory.trajectory_builder import TrajectoryBuilder

from src.slam.slam_manager import SLAMManager

from src.localization.coordinate_lookup import CoordinateLookup


# =========================================================

def process_dataset(mission_folder):

    mission_folder = Path(mission_folder)

    print("\n" + "=" * 60)
    print("PROCESSING MISSION")
    print("=" * 60)

    print(f"Mission : {mission_folder.name}")

    start = time.time()

    # =====================================================
    # DATASET
    # =====================================================

    loader = DatasetLoader(mission_folder)

    dataset = loader.load()

    print(f"Images : {len(dataset['images'])}")
    print(f"Sensor Samples : {len(dataset['sensor'])}")

    # =====================================================
    # DATABASE
    # =====================================================

    db = DatabaseManager(mission_folder)

    # =====================================================
    # FEATURE EXTRACTION
    # =====================================================

    extractor = FeatureExtractor()

    feature_db = FeatureDatabase()

    print("\nExtracting ORB Features...\n")

    for image in dataset["images"]:

        image_path = image["image_path"]

        descriptor = extractor.extract(image_path)

        if descriptor is not None:

            feature_db.store(
                image_path,
                descriptor
            )

    print("Feature extraction complete.")

    # =====================================================
    # TRAJECTORY
    # =====================================================

    print("\nBuilding Trajectory...")

    trajectory = TrajectoryBuilder().build(
        dataset["sensor"]
    )

    print(f"Trajectory Points : {len(trajectory)}")

    # =====================================================
    # ORB-SLAM3
    # =====================================================

    print("\nLaunching ORB-SLAM3...\n")

    slam = SLAMManager()

    slam_result = slam.run(
        mission_folder
    )

    print("ORB-SLAM3 Finished")

    # =====================================================
    # LOCALIZATION
    # =====================================================

    print("\nRunning Localization...")

    localizer = CoordinateLookup()

    localizer.process(
        mission_folder
    )

    print("Localization Finished")

    # =====================================================
    # FINISHED
    # =====================================================

    elapsed = time.time() - start

    print("\n" + "=" * 60)
    print("MISSION COMPLETE")
    print("=" * 60)

    print(f"Mission : {mission_folder.name}")
    print(f"Processing Time : {elapsed:.2f} sec")

    print("=" * 60)


# =========================================================

def main():

    datasets = sorted(

        DATASETS_DIR.glob(
            "mission_*"
        )

    )

    if len(datasets) == 0:

        print("No datasets found.")

        return

    print("\nAvailable Missions\n")

    for i, ds in enumerate(datasets):

        print(f"[{i}] {ds.name}")

    index = int(

        input("\nSelect Mission : ")

    )

    process_dataset(

        datasets[index]

    )


# =========================================================

if __name__ == "__main__":

    main()