import cv2

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow('img', img) # winname : 창이름
cv2.waitKey() # 키를 입력받을때까지 무한대기, 숫자 입력값이 있으면 number 밀리세컨드 초 동안 대기(1000=1초)