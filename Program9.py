#skipy
#blur an image with skipy
#https://docs.scipy.org/doc/scipy/reference/ndimage.html
from scipy import misc,ndimage
from matplotlib import pyplot as plt

face = misc.face()
blurred_face = ndimage.gaussian_filter(face, sigma=3)

fig, ax = plt.subplots(1, 2, figsize=(16, 8))

ax[0].imshow(face)
ax[0].set_title("Original Image")
ax[0].set_xticks([])
ax[0].set_yticks([])


ax[1].imshow(blurred_face)
ax[1].set_title("Blurred Image")
ax[1].set_xticks([])
ax[1].set_yticks([])