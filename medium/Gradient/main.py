import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as pl

img = cv2.imread('data/sudoku.png')

# Image gradient methods
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=1) # Laplacian Image Transformation
lap = np.uint8(np.absolute(lap))
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

title = ["Image", "Laplacian", "SobelX", "SobelY", "Sobel Combined"]
images = [img, lap, sobelX, sobelY, sobelCombined]

for i in range(5):
    pl.subplot(2,3,i+1)
    pl.imshow(images[i], 'gray')
    pl.title(title[i])
    pl.xticks([]), pl.yticks([])

pl.show()