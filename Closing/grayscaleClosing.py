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

# performing closing using dilation followed by erosion
dilation = cv2.dilate(img,kernel,iterations = 1)
erosion = cv2.erode(dilation,kernel,iterations = 1)


# performing closing using its function
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

print(erosion)
print(closing)
print(erosion==closing)

# Conclusion
# Closing is just another way of saying dilation followed by erosion