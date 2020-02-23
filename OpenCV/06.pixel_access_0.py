import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)
img[240,320] = (0,255,0) # (0,255,0) == 0,255,0
img[240,322] = [0,0,255] # pixel에 값을 넣을 때는 튜플, 리스트 모두 가능

cv2.imshow('img', img)
cv2.waitKey()