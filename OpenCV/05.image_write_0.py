# image write
import cv2
import numpy as np

img = np.zeros((640, 480, 3), dtype=np.uint8)
cv2.imshow('img', img)
cv2.waitKey()
cv2.imwrite('img.png', img)

img = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('cat_grayscale.jpg', img)