import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        font = cv2.FONT_HERSHEY_COMPLEX
        strPos = str(x)+', '+str(y)
        cv2.putText(img, strPos, (x,y), font, .5, (0,255,0), 2, cv2.LINE_AA)
        cv2.imshow('Image', img)

img = cv2.imread('data/lena.jpg')
cv2.imshow('Image', img)

cv2.setMouseCallback('Image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()