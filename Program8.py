#https://scikit-image.org/
#astro
#“Active contour models are defined for image segmentation based on the curve flow, curvature,
# and contour to obtain the exact target region or segment in the image.”

import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data
from skimage.filters import gaussian
from skimage.segmentation import active_contour

img = data.astronaut()

# Data for circular boundary
s = np.linspace(0, 2 * np.pi, 400)
x = 220 + 100 * np.cos(s)
y = 100 + 100 * np.sin(s)
init = np.array([x, y]).T

# formation of the active contour
cntr = active_contour(gaussian(img, 3), init, alpha=0.015, beta=10, gamma=0.001)
fig, ax = plt.subplots(1, 2, figsize=(7, 7))
ax[0].imshow(img, cmap=plt.cm.gray)
ax[0].set_title("Original Image")

ax[1].imshow(img, cmap=plt.cm.gray)
# circular boundary
ax[1].plot(init[:, 0], init[:, 1], '--r', lw=3)
ax[1].plot(cntr[:, 0], cntr[:, 1], '-b', lw=3)
ax[1].set_title("Active Contour Image")