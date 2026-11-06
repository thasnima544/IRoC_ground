import cv2
import numpy as np

from config import ORB_NFEATURES


class FeatureExtractor:

    def __init__(self):

        self.orb = cv2.ORB_create(
            nfeatures=ORB_NFEATURES
        )

    def extract(self, image_path):

        image = cv2.imread(
            str(image_path),
            cv2.IMREAD_GRAYSCALE
        )

        if image is None:
            return None

        kp, des = self.orb.detectAndCompute(
            image,
            None
        )

        return {

            "keypoints": kp,
            "descriptors": des
        }

    def extract_from_image(
            self,
            image):

        if len(image.shape) == 3:

            image = cv2.cvtColor(

                image,

                cv2.COLOR_BGR2GRAY

            )

        kp, des = self.orb.detectAndCompute(

            image,

            None

        )

        return {

            "keypoints": kp,

            "descriptors": des

        }