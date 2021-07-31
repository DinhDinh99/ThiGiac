import cv2
import numpy as np 

# ảnh đen
img = np.zeros((600,800,3))
cv2.imshow("Imgae",img)


img[300:600,100:500]= 255
cv2.imshow(("img"), img)

cv2.waitKey()
