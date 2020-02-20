# bgr -> rgb using slicing [start:stop:step]
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)

plt.imshow(img[:,:,::-1], interpolation='bicubic') # interpolation : 부드럽게
plt.xticks([])
plt.yticks([])
plt.show()