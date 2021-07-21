import cv2
import numpy as np
from matplotlib import pyplot as pl

img = cv2.imread('data/smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((2,2), np.uint8)
dilation = cv2.dilate(mask, kernal, iterations=2)
erosion = cv2.erode(mask, kernal, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal) # Opening = Dilation + Erosion
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal) # Closing = Erosion + Dilation
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)

titles = ['Image', 'Mask', 'Dilation(Rm Blacks)', 'Erosion(Rm Blacks)', 'Opening', 'Closing', 'Gradient', 'Tophat']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    pl.subplot(2,4,i+1), pl.imshow(images[i], 'gray')
    pl.title(titles[i])
    pl.xticks([]), pl.yticks([])

pl.show()
