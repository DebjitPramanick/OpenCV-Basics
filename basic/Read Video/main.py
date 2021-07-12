import cv2
cap = cv2.VideoCapture(0) # Capture video [ 0 is for device own camera ]
fourcc = cv2.VideoWriter_fourcc(*'XVID') # FourCC Code [ Check website of fourcc ]
out = cv2.VideoWriter('basic/Read Video/output.avi', fourcc, 20.0, (640,480)) # Output of video

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        propWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # More props on website
        
        out.write(frame) # Save output video

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Make video image gray
        cv2.imshow('Video Frame',gray) # Show video

        if cv2.waitKey(1) & 0xFF == ord('q'): # If key pressed is 'q', video will stop
            break
    else: 
        break

cap.release() # Video released from capture
out.release() # Release output video
cv2.destroyAllWindows()