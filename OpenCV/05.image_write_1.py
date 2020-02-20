# read color image as gray and save it as jpg
import cv2
import numpy as np

img = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('img', img)
cv2.waitKey()
cv2.imwrite('cat-gray.jpg', img)