import numpy as np
import cv2

filepath = 'Dilation/assets/dilation7x7sample2.jpg'
img = cv2.imread(filepath,0)

# img = np.array([[0,   0,   0, 0,   0],
#                 [0,   0, 255, 0, 255],
#                 [0,   0,   0, 0, 255],
#                 [0,   0, 255, 0,   0],
#                 [0,   0, 255, 0, 255],
#                 [255, 0,   0, 0,   0]], np.uint8)

kernel = np.array([[0, 1, 0, 0, 0],
                   [1, 0, 1, 0, 0],
                   [0, 1, 1, 0, 0],
                   [0, 0, 0, 0, 0],
                   [1, 1, 1, 1, 1]], np.uint8)

dilation = cv2.dilate(img,kernel,iterations = 1)

outpath = 'Dilation/assets/resultDilation.jpg'
cv2.imwrite(outpath,dilation)

##################################################################

# The code automatically creates a padding of '0' around the image

# Input Image (3X5): 
# 1 0 1 0 0
# 1 1 0 0 1 
# 0 0 1 1 0 

# Padded Image for 3X3 kernel:
# 0 0 0 0 0 0 0
# 0 1 0 1 0 0 0
# 0 1 1 0 0 1 0
# 0 0 0 1 1 0 0
# 0 0 0 0 0 0 0

# Padded Image for 5X5 kernel:
# 0 0 0 0 0 0 0 0 0
# 0 0 1 0 1 0 0 0 0
# 0 0 1 1 0 0 1 0 0
# 0 0 0 0 1 1 0 0 0
# 0 0 0 0 0 0 0 0 0

##################################################################