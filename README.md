# About the Project
The project is a part of the Series Visualizing the Code with Geekosophers which is designed to give users the ability to visualize different morphological operations which includes- Dilation, Erosion, Opening and Closing.

# Visualising the Code with Geekosophers
<img src="https://firebasestorage.googleapis.com/v0/b/gs-website-20870.appspot.com/o/blog-images%2Fdilation-thumbnail.png?alt=media&token=965741f8-8e38-4782-8cc2-ec16d617d2d2" width="100%" ><img/>
**Brief about the series-** It is an initiative taken by us to bring the world of algorithms closer to the tech enthusiasts by helping them visualise the algorithms. Join us in this journey where we will be covering a wide range of algorithms from Simple Binary search to complex Data Structure and Algorithms. Learn more about the series by clicking [here](https://www.geekosophers.com/blogs/Gu5linHJme9SHp8wblaH).

# Morphological Operations
## 1. Dilation
Dilation is one of the most common morphological operation along with Erosion. Dilation is used to add pixels to the boundary of the input image making the object more visible and fill small voids in the image.
Dilation operator takes two inputs, one is the image and the other one is the structuring element. The structuring element determines the effect of dilation on the input image.

### Key points about Dilation-
1. Dilation is the dual of erosion.
2. Size of input and output image is same.
3. It grows the object and fill any voids in the input image.
4. The nature of thickening is determined by the structuring element.
5. Dilation can be performed on Binary images as well as Grayscale images.

### Blog Post-
Read more about Dilation in the [blog](https://www.geekosophers.com/blogs/CvsGPWNqgPlxW85PB7AH).
### Dilation Animation- 
The interactive animation can be viewed [here](https://animation.geekosophers.com/Dilation/Dilation%20Animation%20Js/index.html).

## 2. Erosion
Erosion is one of the most common morphological operation along with Dilation. Erosion is used to remove pixels from the boundary of the input image shrinking the object.
Erosion operator takes two inputs, one is the image and the other one is the structuring element. The structuring element determines the effect of erosion on the input image.

### Key points about Erosion-
1. Erosion is the dual of dilation.
2. Size of input and output image is same.
3. It shrinks the object in the input image.
4. The nature of thinning(shrinking) is determined by the structuring element.
5. Erosion can be performed on Binary images as well as Grayscale images.

### Blog Post-
Read more about the Erosion in the [blog](https://www.geekosophers.com/blogs/9Ltu5W4s8lKIBHyPnWkp).
### Erosion Animation-
The interactive animation can be viewed [here](https://animation.geekosophers.com/Erosion/Erosion%20Animation%20Js/index.html).

## 3. Opening-
Opening is Erosion followed by Dilation.
The fundamental of opening process has similar effect as erosion which is to remove pixels from the boundary of the input image shrinking the object. Although, it is less destructive than erosion in nature.

### Key points about Opening-
1. Opening is the dual of closing.
2. Size of input and output image is same.
3. It shrinks the object in the input image, same as erosion.
4. The nature of thinning(shrinking) is determined by the structuring element.
5. Opening can be performed on Binary images as well as Grayscale images.

### Blog Post-
Read more about the Opening in the [blog](https://www.geekosophers.com/blogs/gl23OtTd8usFkaXMJrA4).
### Opening Animation-
The interactive animation can be viewed [here](https://animation.geekosophers.com/Opening/Opening%20Animation%20Js/index.html).

## 4. Closing-
Closing is Dilation followed by Erosion.
The fundamental of closing process has similar effect as dilation which is to add pixels to the boundary of the input image making the object more visible and fill small voids in the image. Although, it is less destructive than dilation in nature.

### Key points about Opening-
1. Closing is the dual of opening.
2. Size of input and output image is same.
3. It grows the object and fill any voids in the input image, same as dilation.
4. The nature of thickening is determined by the structuring element.
5. Closing can be performed on Binary images as well as Grayscale images.

### Blog Post-
Read more about the Closing in the [blog](https://www.geekosophers.com/blogs/kun8yQ1X5kY5lqLSHqvK).
### Closing Animation-
The interactive animation can be viewed [here](https://animation.geekosophers.com/Closing/Closing%20Animation%20Js/index.html).

