from config import SQLITE_DB

import sqlite3


class ImageDatabase:

    def __init__(self):

        self.conn = sqlite3.connect(
            SQLITE_DB
        )

        self.cursor = self.conn.cursor()

    def add_image(

            self,

            image_id,

            image_name,

            timestamp_ns,

            image_path,

            descriptor_path):

        self.cursor.execute("""

        INSERT OR REPLACE INTO images(

            image_id,

            image_name,

            timestamp_ns,

            image_path,

            descriptor_path

        )

        VALUES(?,?,?,?,?)

        """, (

            image_id,

            image_name,

            timestamp_ns,

            image_path,

            descriptor_path

        ))

        self.conn.commit()

    def get_image(

            self,

            image_name):

        self.cursor.execute("""

        SELECT *

        FROM images

        WHERE image_name=?

        """,

        (image_name,))

        return self.cursor.fetchone()

    def get_all_images(self):

        self.cursor.execute("""

        SELECT *

        FROM images

        """)

        return self.cursor.fetchall()

    def close(self):

        self.conn.close()