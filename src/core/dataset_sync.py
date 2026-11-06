import pandas as pd


class DatasetSynchronizer:

    def __init__(self):

        pass

    def nearest_sensor(
            self,
            image_ts,
            sensor_df):

        idx = (

            sensor_df[
                "timestamp_ns"
            ]

            .sub(image_ts)

            .abs()

            .idxmin()

        )

        return sensor_df.loc[idx]

    def synchronize(
            self,
            images,
            sensor_df):

        synced = []

        if sensor_df.empty:

            return synced

        for img in images:

            sensor = (

                self.nearest_sensor(

                    img[
                        "timestamp_ns"
                    ],

                    sensor_df

                )

            )

            synced.append({

                "image":

                    img,

                "sensor":

                    sensor.to_dict()

            })

        return synced