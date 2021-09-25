import numpy as np
import cv2

img1= cv2.imread("nobita.jpg")
img2= cv2.imread("suzuka.png")

print(img1.shape)
print(img2.shape)
img1=cv2.resize(img1, (169,297))

img=np.hstack((img1,img2))

cv2.imshow("Before", img)
cv2.waitKey()
cv2.destroyAllWindows()

cp1=img1[5:100, 25:120]
img2[5:100, 25:120]=cp1
fp2=img2

img2= cv2.imread("suzuka.png")

cp2=img2[5:100, 25:120]
img1[5:100, 25:120]=cp2
fp1=img1






photo=np.hstack((fp1,fp2))
cv2.imshow("After", photo)
cv2.waitKey()
cv2.destroyAllWindows()
