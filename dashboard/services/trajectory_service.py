from pathlib import Path
import pandas as pd


class TrajectoryService:

    def __init__(self):

        self.trajectory_file = (
            Path("../trajectories")
            /
            "trajectory.csv"
        )

    def get_trajectory(self):

        if not (

            self.trajectory_file
            .exists()

        ):

            return []

        df = pd.read_csv(
            self.trajectory_file
        )

        return df.to_dict(
            orient="records"
        )

    def get_statistics(self):

        if not (

            self.trajectory_file
            .exists()

        ):

            return {}

        df = pd.read_csv(
            self.trajectory_file
        )

        return {

            "points":
                len(df),

            "max_x":
                float(
                    df["x"].max()
                ),

            "max_y":
                float(
                    df["y"].max()
                ),

            "max_z":
                float(
                    df["z"].max()
                )

        }