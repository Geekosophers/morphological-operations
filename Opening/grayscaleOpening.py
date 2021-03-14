import numpy as np
import cv2

# input image array
img = np.array([[3, 4, 8, 1, 7],
                [9, 4, 2, 1, 6],
                [7, 8, 8, 1, 1]], np.uint8)

# kernel array
kernel = np.array([[0, 1, 0],
                   [1, 1, 0],
                   [0, 1, 0]], np.uint8)

# performing opening using erosion followed by dilation
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(erosion,kernel,iterations = 1)

# performing opening using its function
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

print(dilation)
print(opening)
print(dilation==opening)

# Conclusion
# Opening is just another way of saying erosion followed by dialtion