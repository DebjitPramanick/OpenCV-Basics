import cv2
import numpy as np

cap = cv2.VideoCapture('data/vtest.avi')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2) # This will find difference between frame1 and frame2
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) # Converting diff into grayscale mode to find contours

    # Make the edges more detectable
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Find contours for moving objects
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)

        # Detect objects is contour area is greater than 700
        if cv2.contourArea(c) < 700:
            continue
        else:
            cv2.rectangle(frame1, (x,y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Video", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()