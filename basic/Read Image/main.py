import cv2

# Read image

img = cv2.imread('data/lena.jpg', -1) # Second argument is flag = -1/0/1

cv2.imshow('Image', img) # To show image
k = cv2.waitKey(delay=0) # Wait to display image for 10 seconds or simply pass 0 to display image for infinity time

if k == 27: # If escape key is pressed image window will be closed
    cv2.destroyAllWindows() # Destroy all windows

elif k == ord('s'):# If s key is pressed image will be saved and window will be closed
    cv2.imwrite('basic/Read Image/lena.png', img) 
    cv2.destroyAllWindows() # Destroy all windows

