import numpy as np
import cv2

# Comment lines 9 to 12 and uncomment lines 5 and 6 to perform dialtion on a real image.
# filepath = 'Dilation/assets/dilation7x7sample2.jpg'
# img = cv2.imread(filepath,0)

# The following code uses a grayscale range 0-255 where 0 represents a black pixel and 255 represents a white pixel.
img = np.array([[3, 4, 8, 1, 7],
                [9, 4, 2, 1, 6],
                [7, 8, 8, 1, 1]], np.uint8)

kernel = np.array([[0, 1, 0],
                   [1, 1, 0],
                   [0, 1, 0]], np.uint8)

dilation = cv2.dilate(img,kernel,iterations = 1)

outpath = 'Dilation/assets/resultDilation.jpg'
cv2.imwrite(outpath,dilation)

##################################################################

# The code automatically creates a padding of '0' around the image

# Input Image (3X5):
# 3 4 8 1 7
# 9 4 2 1 6
# 7 8 8 1 1

# Padded Image for 3X3 kernel:
# 0 0 0 0 0 0 0
# 0 3 4 8 1 7 0
# 0 9 4 2 1 6 0
# 0 7 8 8 1 1 0
# 0 0 0 0 0 0 0

# Padded Image for 5X5 kernel:
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 3 4 8 1 7 0 0
# 0 0 9 4 2 1 6 0 0
# 0 0 7 8 8 1 1 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0

##################################################################