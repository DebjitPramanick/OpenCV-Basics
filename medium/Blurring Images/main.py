import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as pl

img = cv2.imread('data/water.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # As matplotlib reads images in RGB format

kernel = np.ones((5,5), np.float)/25
dst = cv2.filter2D(img, -1, kernel) # Homogeneous filter applied
blur = cv2.blur(img, (15,15)) # Blurring picture
gblur = cv2.GaussianBlur(img, (25,25), 0) # Gaussian Blurring
median = cv2.medianBlur(img,45) # Media blur
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75) # Edge is kept sharpe

title = ["Image", "2D Convolution", "Blur", "GBlur", "MBlur", "BFilter"]
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(6):
    pl.subplot(2,3,i+1)
    pl.imshow(images[i], 'gray')
    pl.title(title[i])
    pl.xticks([]), pl.yticks([])

pl.show()