import cv2
import numpy as np

img = cv2.imread("data/gradient.png")
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)

cv2.imshow("Image", img)
cv2.imshow("Threshold", th1)
cv2.imshow("Threshold2", th2)
cv2.imshow("Threshold3", th3)
cv2.imshow("Threshold4", th4)

cv2.waitKey(0)
cv2.destroyAllWindows()
