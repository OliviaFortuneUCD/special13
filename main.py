#OpenCV is an open-source library that was developed by Intel in the year 2000. It is mostly used in computer vision tasks
#such as object detection, face detection, face recognition, image segmentation, etc but also contains a lot of useful functions that you may need in ML.

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('goku.jpeg')
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

fig, ax = plt.subplots(1, 2, figsize=(16, 8))
fig.tight_layout()

ax[0].imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
ax[0].set_title("Original")

ax[1].imshow(cv.cvtColor(gray_image, cv.COLOR_BGR2RGB))
ax[1].set_title("Grayscale")
plt.show()