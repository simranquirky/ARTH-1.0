# What is An Image?
An image is defined as a two-dimensional function, F(x,y), where x and y are spatial coordinates, and the amplitude of F at any pair of coordinates (x,y) is called the intensity of that image at that point. When x,y, and amplitude values of F are finite, we call it an image.

In other words, an image can be defined by a two-dimensional array specifically arranged in rows and columns.
## Types of an images
- BINARY IMAGE– The binary image as its name suggests, contains only two-pixel elements i.e 0 & 1, where 0 refers to black and 1 refers to white. This image is also known as Monochrome.
- BLACK AND WHITE IMAGE– The image which consists of the only black and white color is called BLACK AND WHITE IMAGE.
- 8-bit COLOR FORMAT– It is the most famous image format. It has 256 different shades of colors in it and is commonly known as Grayscale Image. In this format, 0 stands for Black, and 255 stands for white, and 127 stands for gray.
- 16-bit COLOR FORMAT– It is a color image format. It has 65,536 different colors in it. It is also known as High Color Format. In this format, the distribution of color is not as same as the Grayscale image.

## What is Image Processing

Both Image Processing algorithms and Computer Vision (CV) algorithms take an image as input; however, in image processing, the output is also an image, whereas in computer vision the output can be some features/information about the image.


## Why do we need Image Processing?

The data that we collect or generate is mostly raw, i.e. it is not fit to be used in applications directly due to several possible reasons. Therefore, we need to analyze it first, perform the necessary pre-processing, and then use it.

For instance, let’s assume that we were trying to build a cat classifier. Our program would take an image as input and then tell us whether the image contains a cat or not. The first step for building this classifier would be to collect hundreds of cat pictures.

One common issue is that all the pictures we have scraped would not be of the same size/dimensions, so before feeding them to the model for training, we would need to resize/pre-process them all to a standard size.

This is just one of many reasons why image processing is essential to any computer vision application.
## What is OpenCV
OpenCV (Open Source Computer Vision Library) is a library of programming functions mainly aimed at real-time computer vision. Originally developed by Intel. The library is cross-platform and free for use. OpenCV features GPU acceleration for real-time operations.

OpenCV is written in C++ and its primary interface is in C++, but it still retains a less comprehensive though extensive older C interface. All of the new developments and algorithms appear in the C++ interface. There are bindings in Python, Java, and MATLAB/OCTAVE.

OpenCV-Python makes use of Numpy, which is a highly optimized library for numerical operations with a MATLAB-style syntax. All the OpenCV array structures are converted to and from Numpy arrays. This also makes it easier to integrate with other libraries that use Numpy such as SciPy and Matplot

### Prerequisites
Before going any further, let’s discuss what you need to know to follow this tutorial with ease. Firstly, you should have some basic programming knowledge in Python.
Secondly, you should know what machine learning is and the basics of how it works. As a bonus, it would help if you have had any exposure to, or basic knowledge of, Open CV before going on with this tutorial. But this is not required.

One thing you should know to follow this tutorial is how exactly an image is represented in memory. Each image is represented by a set of pixels i.e. a matrix of pixel values.
For a grayscale image, the pixel values range from 0 to 255 and they represent the intensity of that pixel. For instance, if you have an image of 20 x 20 dimensions, it would be represented by a matrix of 20x20 (a total of 400-pixel values).

If you are dealing with a colored image, you should know that it would have three channels — Red, Green, and Blue (RGB). Therefore, there would be three such matrices for a single image.

### Installation of Python OpenCV
Note: Since we are going to use OpenCV via Python, it is an implicit requirement that you already have Python (version 3) already installed on your workstation.
Windows
`$ pip install opencv-python`
# Creating a Custom Image by Using Python Code OpenCV

Our output will look like:
![Screenshot (495)](https://user-images.githubusercontent.com/60690997/134287709-2495aabb-566a-40e2-9d33-7530bb39d4d6.png)


## Step1:
Importing Important Python Libraries like Numpy and OpenCV

`import numpy as np`

`import cv2`

## Step 2:
Creating a Numpy Array with zeros.
The ones() function is used to get a new array of given shape and type, filled with ones.
This will give us a white background for the black background you can use zeros() function.


`img=np.ones((550, 770, 3))`

## Step 3: 

Defining the colors

`black=(0,0,0)`

`red=(0,0,255)`

`green=(0,255,0)`

## Step4:

Now, this is where our actual custom image is created using geometric functions in OpenCV like line and rectangle with color, coordinates, and thickness specified.

`cv2.rectangle(img, (480,250), (100,450),green,8)`

`cv2.rectangle(img, (580,150), (200,350),green,8)`

`cv2.line( img, (100,450),(200,350),green,8)`

`cv2.line( img, (480,250),(580,150),green,8)`

`cv2.line( img, (100,250),(200,150),green,8)`

`cv2.line( img, (480,450),(580,350),green,8)`


## Step 5:

Defining other values.

`start_point=(40,100)`

`font_thickness=5`

`font_size=3`

`font=cv2.FONT_HERSHEY_SIMPLEX`


## Step 6:
Now final step is to show the image using imshow() function in OpenCV with a putText() function using cv2.FONT_HERSHEY_SIMPLEX

`cv2.putText(img,'ARTH-TASK',start_point,font,font_size,red,font_thickness)`

`cv2.imshow('window-photo',img)`

`cv2.waitKey(0)`

`cv2.destroyAllWindows()`

