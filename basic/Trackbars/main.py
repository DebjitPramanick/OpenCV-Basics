import cv2
import numpy as np

def callback(x):
    print(x)

img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow("Image")

ref = 1

cv2.createTrackbar('B', 'Image', 0, 255, callback)
cv2.createTrackbar('G', 'Image', 0, 255, callback)
cv2.createTrackbar('R', 'Image', 0, 255, callback)

switch = '0 : OFF\n 1 : ON'
cv2.createTrackbar(switch, 'Image', 0, 1, callback)

while(1):
    cv2.imshow('Image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    b = cv2.getTrackbarPos('B', 'Image')
    g = cv2.getTrackbarPos('G', 'Image')
    r = cv2.getTrackbarPos('R', 'Image')
    s = cv2.getTrackbarPos(switch, 'Image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.waitKey(0)
cv2.destroyAllWindows()