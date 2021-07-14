import cv2

img = cv2.imread('data/messi5.jpg')
img2 = cv2.imread('data/opencv-logo.png')

# Resize images to make them of same size

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# mergedImg = cv2.add(img2, img)
mergedImg = cv2.addWeighted(img, .2, img2, .9, 0)

cv2.imshow('Image', mergedImg)

cv2.waitKey(0)
cv2.destroyAllWindows()