import cv2
import numpy as np

img = cv2.imread('data/shapes.jpg')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for cont in contours:
    appx = cv2.approxPolyDP(cont, 0.01*cv2.arcLength(cont, True), True)
    # cv2.drawContours(img, [appx], 0, (0, 0, 0), 5)
    x = appx.ravel()[0]
    y = appx.ravel()[1]
    if len(appx) == 3:
        cv2.putText(img, "Triangle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 13))
    elif len(appx) == 4:
        cv2.putText(img, "Rectangle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 13))
    elif len(appx) == 5:
        cv2.putText(img, "Pentagon", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 13))
    elif len(appx) == 10:
        cv2.putText(img, "Star", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 13))
    else:
        cv2.putText(img, "Circle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 13))

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
