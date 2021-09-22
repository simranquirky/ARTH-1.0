
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

