import cv2
import numpy as np

mat0 = np.uint8([[130, 140], [150, 160]])
mat1 = np.uint8([[100, 100], [100, 100]])
mat2 = np.uint8([[145, 145], [145, 145]])

print('mat0');print(mat0)
print('mat1');print(mat1)
print('mat2');print(mat2)

print('mat0+mat1')
print(mat0+mat1)
# [[230 240]
#  [250   4]]
# uint8이 255까지의 값을 표현하므로 260은 overflow가 발생하여 0부터 다시 시작

print('cv2.add(mat0, mat1)')
print(cv2.add(mat0, mat1))
# [[230 240]
#  [250 255]]
# OpenCV 함수의 add는 255가 벗어나면 255로 고정(이미지 덧셈 최적화)

print('mat0-mat2')
print(mat0-mat2)
# [[241 251]
#  [  5  15]]
# underflow가 발생하여 255부터 다시 시작

print('cv2.subtract(mat0, mat2)')
print(cv2.subtract(mat0, mat2))
# [[ 0  0]
#  [ 5 15]]
# OpenCV 함수의 subtract는 0을 벗어나면 0으로 고정(이미지 뺄셈 최적화)

# 가중치가 있는 덧셈
# alpha + beta = 1로 설정하면 가중치가 있는 평균 구현 가능
# src1과 src2는 같은 shape 요구
# src1*alpha + src2*beta + gamma
print('cv2.addWeighted(mat0, 0.7, mat1, 0.3, 0)')
print(cv2.addWeighted(mat0, 0.7, mat1, 0.3, 0))