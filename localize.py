import cv2
import os

SEED = "seed_image.png"
IMAGE_DIR = "datasets/mission_003/images"

orb = cv2.ORB_create(2000)

seed = cv2.imread(SEED, 0)

kp1, des1 = orb.detectAndCompute(
    seed,
    None
)

bf = cv2.BFMatcher(
    cv2.NORM_HAMMING,
    crossCheck=True
)

best_score = 0
best_image = None

for file in os.listdir(IMAGE_DIR):

    path = os.path.join(
        IMAGE_DIR,
        file
    )

    img = cv2.imread(
        path,
        0
    )

    if img is None:
        continue

    kp2, des2 = orb.detectAndCompute(
        img,
        None
    )

    if des2 is None:
        continue

    matches = bf.match(
        des1,
        des2
    )

    score = len(matches)

    if score > best_score:

        best_score = score
        best_image = file

print(
    "BEST:",
    best_image,
    "MATCHES:",
    best_score
)