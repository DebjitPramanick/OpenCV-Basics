import cv2
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as pl


img = cv2.imread('data/lena.jpg', -1)
cv2.imshow('Image' ,img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

pl.imshow(img)
# pl.xticks([]), pl.yticks([]) # To hide x and y axis 
pl.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
