# Gaussian Functions

import cv2

img = cv2.imread('data/lena.jpg')
lr = cv2.pyrDown(img)
hr = cv2.pyrUp(img)

cv2.imshow("Original", img)
cv2.imshow("Pyrdown", lr)
cv2.imshow("Pyrup", hr)
cv2.waitKey(0)
cv2.destroyAllWindows()