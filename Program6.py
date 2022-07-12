# Scaling and resizing
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('vegeta.jpeg')
hist = cv.calcHist([img], [0], None, [256], [0, 256])

plt.plot(hist)