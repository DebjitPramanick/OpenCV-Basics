import cv2
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as pl


img = cv2.imread("data/gradient.png")
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)

titles = ['Original', 'Binary', 'Binary_INV', 'Trunc', 'Tozero']
images = [img, th1, th2, th3, th4]

for i in range(5):
    pl.subplot(2,3,i+1), pl.imshow(images[i], 'gray')
    pl.title(titles[i])
    pl.xticks([]), pl.yticks([])

pl.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
