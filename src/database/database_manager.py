"""
=========================================================
database_manager.py

COSMIC_GROUND
IRoC-U 2026

Mission Database Manager

Creates

mission.db

Stores

Images
Telemetry
Mission Events

Exports CSV automatically.

Author : Team Bitstream
=========================================================
"""

import csv
import sqlite3
from pathlib import Path

from config import (
    SQLITE_DB,
    SENSOR_HEADERS,
    IMAGE_HEADERS,
    SENSOR_FILE,
    IMAGE_INDEX_FILE,
)


class DatabaseManager:

    def __init__(self, mission_folder):

        self.mission_folder = Path(mission_folder)

        self.sensor_csv = self.mission_folder / SENSOR_FILE

        self.image_csv = self.mission_folder / IMAGE_INDEX_FILE

        self.connection = sqlite3.connect(SQLITE_DB)

        self.cursor = self.connection.cursor()

        self.create_tables()

        self.create_csv()

    ############################################################

    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS images(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp REAL,

            image_name TEXT UNIQUE

        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS telemetry(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp REAL,

            image_name TEXT,

            roll REAL,

            pitch REAL,

            yaw REAL,

            flow_comp_m_x REAL,

            flow_comp_m_y REAL,

            flow_rate_x REAL,

            flow_rate_y REAL,

            flow_x REAL,

            flow_y REAL,

            ground_distance REAL,

            quality INTEGER,

            sensor_id INTEGER

        )

        """)

        self.connection.commit()

    ############################################################

    def create_csv(self):

        if not self.sensor_csv.exists():

            with open(

                self.sensor_csv,

                "w",

                newline=""

            ) as file:

                writer = csv.writer(file)

                writer.writerow(SENSOR_HEADERS)

        if not self.image_csv.exists():

            with open(

                self.image_csv,

                "w",

                newline=""

            ) as file:

                writer = csv.writer(file)

                writer.writerow(IMAGE_HEADERS)

    ############################################################

    def save_image(

        self,

        timestamp,

        image_name

    ):

        self.cursor.execute(

            """

            INSERT INTO images(

                timestamp,

                image_name

            )

            VALUES(?,?)

            """,

            (

                timestamp,

                image_name

            )

        )

        self.connection.commit()

        with open(

            self.image_csv,

            "a",

            newline=""

        ) as file:

            writer = csv.writer(file)

            writer.writerow([

                timestamp,

                image_name

            ])

    ############################################################

    def save_telemetry(

        self,

        data,

        image_name

    ):

        row = [

            data["timestamp"],

            image_name,

            data["roll"],

            data["pitch"],

            data["yaw"],

            data["flow_comp_m_x"],

            data["flow_comp_m_y"],

            data["flow_rate_x"],

            data["flow_rate_y"],

            data["flow_x"],

            data["flow_y"],

            data["ground_distance"],

            data["quality"],

            data["sensor_id"]

        ]

        self.cursor.execute("""

        INSERT INTO telemetry(

            timestamp,

            image_name,

            roll,

            pitch,

            yaw,

            flow_comp_m_x,

            flow_comp_m_y,

            flow_rate_x,

            flow_rate_y,

            flow_x,

            flow_y,

            ground_distance,

            quality,

            sensor_id

        )

        VALUES(

            ?,?,?,?,?,?,?,?,?,?,?,?,?,?

        )

        """, row)

        self.connection.commit()

        with open(

            self.sensor_csv,

            "a",

            newline=""

        ) as file:

            writer = csv.writer(file)

            writer.writerow(row)

    ############################################################

    def close(self):

        self.connection.close()


############################################################

if __name__ == "__main__":

    db = DatabaseManager(

        "datasets/test_mission"

    )

    db.save_image(

        100.15,

        "img_001.png"

    )

    db.save_telemetry(

        {

            "timestamp":100.15,

            "roll":0.10,

            "pitch":0.20,

            "yaw":1.50,

            "flow_comp_m_x":0.01,

            "flow_comp_m_y":0.02,

            "flow_rate_x":0.00,

            "flow_rate_y":0.00,

            "flow_x":5,

            "flow_y":2,

            "ground_distance":1.75,

            "quality":255,

            "sensor_id":0

        },

        "img_001.png"

    )

    db.close()

    print("Database Test Complete.")