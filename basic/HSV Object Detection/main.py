import cv2
import numpy as np

def callback(x):
    print(x)

cap = cv2.VideoCapture(0)

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", 'Tracking', 0, 255, callback) # Lower Hue
cv2.createTrackbar("LS", 'Tracking', 0, 255, callback) # Lower Saturation
cv2.createTrackbar("LV", 'Tracking', 0, 255, callback) # Lower Value
cv2.createTrackbar("UH", 'Tracking', 255, 255, callback) # Upper Hue
cv2.createTrackbar("US", 'Tracking', 255, 255, callback) # Upper Saturation
cv2.createTrackbar("UV", 'Tracking', 255, 255, callback) # Upper Value

while(1):
    # img = cv2.imread("data/smarties.png") # For image reading

    _, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(img, img, mask=mask)


    cv2.imshow('Image', img)
    cv2.imshow('Mask', mask)
    cv2.imshow('Res', res)
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()