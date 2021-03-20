import numpy as np
import cv2

# In binary sometimes we express a black pixel and a white pixel as 0 and 1 respectively.
# In the following code 0 denotes a black pixel and 255 denotes a white pixel. Read observations at the bottom to get full idea.

# input image array
img = np.array([[ 1, 1, 0, 0, 0],
                [ 1, 1, 1, 0, 1],
                [ 0, 1, 1, 0, 1],
                [ 0, 1, 1, 0, 1],
                [ 0, 0, 0, 0, 0],
                [ 1, 1, 0, 0, 0]], np.uint8)

# kernel array
kernel = np.array([[1, 1, 0],
                   [1, 1, 0],
                   [1, 1, 0]], np.uint8)

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

# Observations:
# The 0s and 1s in the numpy array 'img' does not denote white and black. 
# It represents the actual pixel value in grayscale range 0-255.
# To output the array in the form of the image will result in an image showing pixel value 1 which appears to be black.
# To get black and white image output, replace 1 with 255 in 'img' array