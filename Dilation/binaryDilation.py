import numpy as np
import cv2

# Comment lines 10 to 15 and uncomment lines 5 and 6 to perform dialtion on a real image.
# filepath = 'Dilation/assets/dilation7x7sample2.jpg'
# img = cv2.imread(filepath,0)

# In binary sometimes we express a black pixel and a white pixel as 0 and 1 respectively.
# In the following code 0 denotes a black pixel and 255 denotes a white pixel.
img = np.array([[0,   0,   0, 0,   0],
                [0,   0, 255, 0, 255],
                [0,   0,   0, 0, 255],
                [0,   0, 255, 0,   0],
                [0,   0, 255, 0, 255],
                [255, 0,   0, 0,   0]], np.uint8)

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
# 0 0 0 0 0 0 0 0 0
# 0 0 1 0 1 0 0 0 0
# 0 0 1 1 0 0 1 0 0
# 0 0 0 0 1 1 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0

##################################################################