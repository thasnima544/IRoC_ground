import cv2

img = cv2.imread("obstacle.png")

img128 = cv2.resize(
    img,
    (128,128)
)

cv2.imwrite(
    "seed_image.png",
    img128
)