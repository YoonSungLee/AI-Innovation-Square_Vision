# Opensource Computer Vision library
# C++ 기반 라이브러리
# Python, Java에서도 사용 가능

import cv2

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

print('type(img) =', type(img))
print('img.shape, img.dtype =', img.shape, img.dtype) # OpenCV : (B, G, R)

# uint8 : unsigned integer(부호가 없는 정수형), 픽셀 하나 당 8bit(1byte), 0~255까지의 숫자를 표현