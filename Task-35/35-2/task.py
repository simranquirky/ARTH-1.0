import numpy as np
import cv2

img1= cv2.imread("p1.jpg")
img2= cv2.imread("p2.jpg")
img3= cv2.imread("p3.jpg")
img4= cv2.imread("p4.jpg")

cv2.imshow("Image 1", img1)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow("Image 2", img2)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow("Image 3", img3)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow("Image 4", img4)
cv2.waitKey()
cv2.destroyAllWindows()

print("ORIGINAL SHAPE OF IMAGES" )

print(img1.shape)
print(img2.shape)
print(img3.shape)
print(img4.shape)

width, height = 183 , 275
img2=cv2.resize(img2, (width,height))
img3=cv2.resize(img3, (width,height))
img4=cv2.resize(img4, (width,height))

print(" SHAPE OF IMAGES AFTER RESIZING" )
print(img1.shape)
print(img2.shape)
print(img3.shape)
print(img4.shape)

combined=np.hstack((img1,img2,img3,img4))
cv2.imshow("combined images", combined)
cv2.waitKey()
cv2.destroyAllWindows()
