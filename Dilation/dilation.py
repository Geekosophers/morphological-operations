import numpy as np
import cv2

filepath = 'images/dilation7x7sample2.jpg'
img = cv2.imread(filepath,0)

kernel = arr = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)
# Kernel
# 0 1 0
# 1 1 1
# 0 1 0

dilation = cv2.dilate(img,kernel,iterations = 1)
# The code automatically uses the padding of '0' while dilating the image

outpath = 'images/resultDilation.jpg'
cv2.imwrite(outpath,dilation)