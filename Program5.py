# Scaling and resizing
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("pics/goku.jpeg")
# Splitting the BGR values from the image
b, g, r = cv.split(img)

zeros = np.zeros(img.shape[:2], dtype="uint8")

fig, ax = plt.subplots(1, 3, figsize=(16, 8))
fig.tight_layout()

red = cv.merge([r, zeros, zeros])
green = cv.merge([zeros, g, zeros])
blue = cv.merge([zeros, zeros, b])

ax[0].imshow(red)
ax[0].set_title("Red")

ax[1].imshow(green)
ax[1].set_title("Green")

ax[2].imshow(blue)
ax[2].set_title("Blue")

plt.show()