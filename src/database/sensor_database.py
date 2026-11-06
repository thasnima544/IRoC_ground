from config import SQLITE_DB

import sqlite3


class SensorDatabase:

    def __init__(self):

        self.conn = sqlite3.connect(
            SQLITE_DB
        )

        self.cursor = self.conn.cursor()

    def add_sensor(

            self,

            row):

        self.cursor.execute("""

        INSERT OR REPLACE INTO sensors(

            timestamp_ns,

            roll,
            pitch,
            yaw,

            rollspeed,
            pitchspeed,
            yawspeed,

            flow_x,
            flow_y,

            flow_comp_m_x,
            flow_comp_m_y,

            flow_quality,

            distance_m,

            battery_voltage,

            battery_remaining

        )

        VALUES(

            ?,?,?,?,?,?,
            ?,?,?,?,?,?,
            ?,?,?

        )

        """, (

            row["timestamp_ns"],

            row["roll"],
            row["pitch"],
            row["yaw"],

            row["rollspeed"],
            row["pitchspeed"],
            row["yawspeed"],

            row["flow_x"],
            row["flow_y"],

            row["flow_comp_m_x"],
            row["flow_comp_m_y"],

            row["flow_quality"],

            row["distance_m"],

            row["battery_voltage"],

            row["battery_remaining"]

        ))

        self.conn.commit()

    def nearest_sensor(

            self,

            timestamp_ns):

        self.cursor.execute("""

        SELECT *

        FROM sensors

        ORDER BY ABS(

            timestamp_ns - ?

        )

        LIMIT 1

        """,

        (timestamp_ns,))

        return self.cursor.fetchone()

    def close(self):

        self.conn.close()