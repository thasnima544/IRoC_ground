from pathlib import Path
import pandas as pd


class DatasetLoader:

    def __init__(self, mission_folder):

        self.mission_folder = Path(
            mission_folder
        )

    def load(self):

        dataset = {}

        # =====================================
        # Images
        # =====================================

        images_dir = (
            self.mission_folder /
            "images"
        )

        images = []

        image_files = sorted(

    list(images_dir.glob("*.jpg")) +

    list(images_dir.glob("*.png"))

)

        for idx, image_path in enumerate(
            image_files
        ):

            images.append({

                "image_id": idx,

                "image_name":
                    image_path.name,

                "timestamp_ns":
                    idx,

                "image_path":
                    str(image_path)

            })

        dataset["images"] = images

        # =====================================
        # Sensor Logs
        # =====================================

        sensor_file = (

            self.mission_folder /
            "logs" /
            "sensor.csv"

        )

        if sensor_file.exists():

            sensor_df = pd.read_csv(
                sensor_file
            )

            # ---------------------------------
            # Create timestamp_ns if missing
            # ---------------------------------

            if (
                "timestamp_ns"
                not in sensor_df.columns
            ):

                sensor_df[
                    "timestamp_ns"
                ] = range(
                    len(sensor_df)
                )

            # ---------------------------------
            # Create missing columns if needed
            # ---------------------------------

            defaults = {

                "roll": 0,
                "pitch": 0,
                "yaw": 0,

                "acc_x": 0,
                "acc_y": 0,
                "acc_z": 0,

                "gyro_x": 0,
                "gyro_y": 0,
                "gyro_z": 0,

                "flow_x": 0,
                "flow_y": 0,

                "quality": 0,

                "distance": 0

            }

            for col, value in defaults.items():

                if col not in sensor_df.columns:

                    sensor_df[col] = value

            dataset["sensor"] = (
                sensor_df
            )

        else:

            dataset["sensor"] = (
                pd.DataFrame()
            )

        # =====================================
        # ESP
        # =====================================

        dataset["esp"] = (
            pd.DataFrame()
        )

        # =====================================
        # Events
        # =====================================

        dataset["events"] = (
            pd.DataFrame()
        )

        # =====================================
        # Metadata
        # =====================================

        dataset["metadata"] = {}

        print(
            f"\nLoaded "
            f"{len(images)} images"
        )

        print(
            f"Sensor rows: "
            f"{len(dataset['sensor'])}"
        )

        if len(images) > 0:

            print(
                f"First image: "
                f"{images[0]['image_name']}"
            )

        return dataset