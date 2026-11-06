"""
=========================================================
vocabulary_loader.py

COSMIC_GROUND
IRoC-U 2026

ORB Vocabulary Loader

=========================================================
"""

from pathlib import Path

from src.slam.slam_config import VOCABULARY


class VocabularyLoader:

    def __init__(self):

        self.path = Path(VOCABULARY)

    ###########################################################

    def verify(self):

        if not self.path.exists():

            raise FileNotFoundError(

                f"Vocabulary not found:\n{self.path}"

            )

        return True

    ###########################################################

    def get_path(self):

        self.verify()

        return str(self.path)

    ###########################################################

    def size_mb(self):

        self.verify()

        return self.path.stat().st_size / (1024 * 1024)

    ###########################################################

    def info(self):

        self.verify()

        print("\nORB Vocabulary")

        print("-------------------------")

        print(f"Path : {self.path}")

        print(f"Size : {self.size_mb():.2f} MB")


###############################################################

if __name__ == "__main__":

    vocab = VocabularyLoader()

    vocab.info()