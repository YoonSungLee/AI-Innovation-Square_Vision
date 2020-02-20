import cv2

# callback function : 특정 이벤트가 발생했을 때 운영체제가 자동으로 호출하도록 권한을 주는 함수
def on_mouse(event, x, y, flags, param):
    print(event, x, y, flags, param)

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

cv2.namedWindow('img') # 빈 윈도우 창
cv2.setMouseCallback('img', on_mouse) # callback function 사용

cv2.imshow('img', img)

while True:
    key = cv2.waitKey(30)
    if key==27: break