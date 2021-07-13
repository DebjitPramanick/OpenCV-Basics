import cv2
import datetime
cap = cv2.VideoCapture(0) # Capture video [ 0 is for device own camera ]
cap.set(3, 600)
cap.set(4, 700)

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        text = 'Width: '+ str(cap.get(3)) + 'Height: ' + str(cap.get(4))
        dateText = str(datetime.datetime.now())
        frame = cv2.putText(frame, dateText, (100,400), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 2, cv2.LINE_AA)
        cv2.imshow('Video Frame',frame) # Show video
        if cv2.waitKey(1) & 0xFF == ord('q'): # If key pressed is 'q', video will stop
            break
    else: 
        break

cap.release() # Video released from capture
cv2.destroyAllWindows()