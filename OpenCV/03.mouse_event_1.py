# detect mouse clicks and wheel scroll up and down
import cv2

# callback function : 특정 이벤트가 발생했을 때 운영체제가 자동으로 호출하도록 권한을 주는 함수
def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # 마우스의 왼쪽 버튼이 눌려진 이벤트
        print('Left mouse button down at', x, y)
    elif event == cv2.EVENT_LBUTTONUP:  # 마우스의 왼쪽 버튼이 (눌러지고 나서) 떼어진 이벤트
        print('Left mouse button up at', x, y)
    elif event == cv2.EVENT_LBUTTONDBLCLK:  # 마우스 왼쪽 버튼 더블클릭
        print('Left mouse button double clicked  at', x, y)
    elif event == cv2.EVENT_MOUSEWHEEL: # 마우스 휠
        if flags>0: # 마우스휠을 위로 올릴 때 flags 양수 출력
            print('mouse wheel scrolled up at', x, y)
        else:       # 마우스휠을 아래로 내릴 때 flags 음수 출력
            print('mouse wheel scrolled down at', x, y)


img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

cv2.namedWindow('img')  # 빈 윈도우 창
cv2.setMouseCallback('img', on_mouse)   # callback function 사용

cv2.imshow('img', img)
cv2.waitKey()