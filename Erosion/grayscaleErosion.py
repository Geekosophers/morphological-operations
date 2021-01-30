import numpy as np
import cv2

# Comment lines 9 to 12 and uncomment lines 5 and 6 to perform erosion on a real image.
# filepath = 'Erosion/assets/erosion7x7sample2.jpg'
# img = cv2.imread(filepath,0)

# The following code uses a grayscale range 0-255 where 0 represents a black pixel and 255 represents a white pixel.
img = np.array([[3, 4, 8, 1, 7],
                [9, 4, 2, 1, 6],
                [7, 8, 8, 1, 1]], np.uint8)

kernel = np.array([[0, 1, 0],
                   [1, 1, 0],
                   [0, 1, 0]], np.uint8)

erosion = cv2.erode(img,kernel,iterations = 1)

outpath = 'Erosion/assets/resultErosion.jpg'
cv2.imwrite(outpath,erosion)

##################################################################

# The code automatically creates a padding of '0' around the image

# Input Image (3X5):
# 3 4 8 1 7
# 9 4 2 1 6
# 7 8 8 1 1

# Padded Image for 3X3 kernel:
# 1 1 1 1 1 1 1
# 1 3 4 8 1 7 1
# 1 9 4 2 1 6 1
# 1 7 8 8 1 1 1
# 1 1 1 1 1 1 1

# Padded Image for 5X5 kernel:
# 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1
# 1 1 3 4 8 1 7 1 1
# 1 1 9 4 2 1 6 1 1
# 1 1 7 8 8 1 1 1 1
# 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1

##################################################################