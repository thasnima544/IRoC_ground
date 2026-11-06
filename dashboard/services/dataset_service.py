from pathlib import Path
import pandas as pd
import json

DATASETS_DIR = Path("../datasets")


class DatasetService:

    def __init__(self):

        self.datasets_dir = (
            DATASETS_DIR
        )

    def get_all_missions(self):

        if not self.datasets_dir.exists():

            return []

        missions = []

        for mission in sorted(

                self.datasets_dir.glob(
                    "mission_*"
                )):

            missions.append({

                "id":
                    mission.name,

                "path":
                    str(mission)

            })

        return missions

    def get_latest_mission(self):

        missions = (
            self.get_all_missions()
        )

        if not missions:

            return None

        return missions[-1]

    def get_dashboard_stats(self):

        latest = (
            self.get_latest_mission()
        )

        if latest is None:

            return {}

        mission = Path(
            latest["path"]
        )

        stats = {}

        try:

            image_index = pd.read_csv(

                mission /
                "image_index.csv"

            )

            stats[
                "image_count"
            ] = len(
                image_index
            )

        except:

            stats[
                "image_count"
            ] = 0

        try:

            sensor = pd.read_csv(

                mission /
                "sensor.csv"

            )

            stats[
                "sensor_count"
            ] = len(sensor)

        except:

            stats[
                "sensor_count"
            ] = 0

        return stats

    def get_mission_details(
            self,
            mission_id):

        mission = (
            self.datasets_dir /
            mission_id
        )

        metadata_file = (

            mission /
            "metadata.json"

        )

        if metadata_file.exists():

            with open(
                    metadata_file
            ) as fp:

                return json.load(fp)

        return {}

    def get_sensor_data(self):

        latest = (
            self.get_latest_mission()
        )

        if latest is None:

            return []

        sensor_file = (

            Path(
                latest["path"]
            )

            /
            "sensor.csv"

        )

        if not sensor_file.exists():

            return []

        df = pd.read_csv(
            sensor_file
        )

        return df.to_dict(
            orient="records"
        )

    def get_battery_data(self):

        latest = (
            self.get_latest_mission()
        )

        if latest is None:

            return []

        esp_file = (

            Path(
                latest["path"]
            )

            /
            "esp_status.csv"

        )

        if not esp_file.exists():

            return []

        df = pd.read_csv(
            esp_file
        )

        return df.to_dict(
            orient="records"
        )