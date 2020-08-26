import numpy as np
import cv2

img = cv2.imread('dilation7x7sample2.jpg',0)

kernel = arr = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)
# Kernel
# 0 1 0
# 1 1 1
# 0 1 0

dilation = cv2.dilate(img,kernel,iterations = 1)
# The code automatically uses the padding of '0' while dilating the image

cv2.imwrite('resultDilation.jpg',dilation)