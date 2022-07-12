#A colored image consists of 3 color channels where a gray image only consists of 1 Color channel which carries intensity information for each pixel showing the image as black-and-white.

#The following code separates each color channel:

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('goku.jpeg')
b, g, r = cv.split(img)

fig, ax = plt.subplots(1, 3, figsize=(16, 8))
fig.tight_layout()

ax[0].imshow(cv.cvtColor(r, cv.COLOR_BGR2RGB))
ax[0].set_title("Red")

ax[1].imshow(cv.cvtColor(g, cv.COLOR_BGR2RGB))
ax[1].set_title("Green")

ax[2].imshow(cv.cvtColor(b, cv.COLOR_BGR2RGB))
ax[2].set_title("Blue")