import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as pl

img = cv2.imread('data/messi5.jpg', 0)
canny = cv2.Canny(img, 100, 200)

title = ["Image", "Canny"]
images = [img, canny]

for i in range(2):
    pl.subplot(1,2,i+1)
    pl.imshow(images[i], 'gray')
    pl.title(title[i])
    pl.xticks([]), pl.yticks([])

pl.show()