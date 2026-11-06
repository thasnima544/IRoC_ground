import pandas as pd


class CoordinateLookup:

    def __init__(
            self,
            trajectory_file):

        self.trajectory = pd.read_csv(
            trajectory_file
        )

    def nearest_pose(
            self,
            timestamp_ns):

        idx = (

            self.trajectory[
                "timestamp_ns"
            ]

            .sub(timestamp_ns)

            .abs()

            .idxmin()

        )

        return (

            self.trajectory
            .loc[idx]
            .to_dict()

        )