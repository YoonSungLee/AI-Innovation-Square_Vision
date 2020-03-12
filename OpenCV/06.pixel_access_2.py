# split each channel
# OpenCV는 3차원의 이미지는 컬러로 인식하지만, 2차원의 이미지는 흑백으로 인식한다.
# 따라서 3차원의 이미지에서 R이 포함되어 있는 이미지를 따로 가져와서 cv2.imshow한다고 해도 흑백으로 표현한다.
import cv2

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

b, g, r = cv2.split(img)    # 이미지 분리

cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
cv2.waitKey()