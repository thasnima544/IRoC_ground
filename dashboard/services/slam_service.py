from pathlib import Path
import json
import pandas as pd


class SlamService:

    def __init__(self):

        self.maps_dir = (
            Path("../maps")
        )

    def get_keyframes(self):

        file = (

            self.maps_dir
            /
            "keyframes.json"

        )

        if not file.exists():

            return []

        with open(file) as fp:

            return json.load(fp)

    def get_map_data(self):

        trajectory = (

            Path("../trajectories")
            /
            "trajectory.csv"

        )

        if not trajectory.exists():

            return []

        df = pd.read_csv(
            trajectory
        )

        return df.to_dict(
            orient="records"
        )

    def get_localization_history(self):

        file = (
            Path("../outputs")
            /
            "localization_results.csv"
        )

        if not file.exists():

            return []

        df = pd.read_csv(
            file
        )

        return df.to_dict(
            orient="records"
        )