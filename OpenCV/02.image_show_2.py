# Show image until 'esc' gets pressed
import cv2

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow('img', img)
key = cv2.waitKey()

# ESC의 ASCII Code는 27
while key!=27:
    key = cv2.waitKey()