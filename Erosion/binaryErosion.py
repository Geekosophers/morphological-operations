import numpy as np
import cv2

# Comment lines 10 to 15 and uncomment lines 5 and 6 to perform erosion on a real image.
# filepath = 'Erosion/assets/erosion7x7sample2.jpg'
# img = cv2.imread(filepath,0)

# In binary sometimes we express a black pixel and a white pixel as 0 and 1 respectively.
# In the following code 0 denotes a black pixel and 255 denotes a white pixel. Read observations at the bottom to get full idea.
img = np.array([[ 1, 1, 0, 0, 0],
                [ 1, 1, 1, 0, 1],
                [ 0, 1, 1, 0, 1],
                [ 0, 1, 1, 0, 1],
                [ 0, 0, 0, 0, 0],
                [ 1, 1, 0, 0, 0]], np.uint8)

kernel = np.array([[1, 1, 0],
                   [1, 1, 0],
                   [1, 1, 0]], np.uint8)

erosion = cv2.erode(img,kernel,iterations = 1)

outpath = 'Erosion/assets/resultErosion.jpg'
cv2.imwrite(outpath,erosion)

##################################################################

# The code automatically creates a padding of '1' around the image

# Input Image (3X5): 
# 1 0 1 0 0
# 1 1 0 0 1 
# 0 0 1 1 0 

# Padded Image for 3X3 kernel:
# 1 1 1 1 1 1 1
# 1 1 0 1 0 0 1
# 1 1 1 0 0 1 1
# 1 0 0 1 1 0 1
# 1 1 1 1 1 1 1

# Padded Image for 5X5 kernel:
# 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1
# 1 1 1 0 1 0 0 1 1
# 1 1 1 1 0 0 1 1 1
# 1 1 0 0 1 1 0 1 1
# 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1

# Observations:
# The 0s and 1s in the numpy array 'img' does not denote white and black. 
# It represents the actual pixel value in grayscale range 0-255.
# To output the array in the form of the image will result in an image showing pixel value 1 which appears to be black.
# To get black and white image output, replace 1 with 255 in 'img' array

##################################################################