import cv2

img = cv2.imread('data/lena.jpg', 1)


img = cv2.line(img, (0,0), (255,230), (255,0,0), 3) # Creates a line
img = cv2.arrowedLine(img, (0,100), (200,160), (255,0,0), 3) # Creates an arrowed line
img = cv2.rectangle(img, (120,120), (280,280), (0,0,255), 4) # Creates a hollow rectangle
img = cv2.rectangle(img, (220,290), (360,360), (0,0,255), -1) # Creates a solid rectangle
img = cv2.circle(img, (290, 40), 40, (0,255,0), -1) # Creates a solid circle
img = cv2.putText(img, 'OpenCV', (0, 400), cv2.FONT_HERSHEY_COMPLEX, 2, (255,255,255), 6, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()