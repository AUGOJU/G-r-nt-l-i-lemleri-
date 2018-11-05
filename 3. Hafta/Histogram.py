import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img0 = mpimg.imread('image/guto.jpg')
img1 = mpimg.imread('image/guto1.jpg')

imgplot0 = plt.imshow(img0)
plt.colorbar(imgplot0)
plt.show()

infra_red = plt.imshow(img0[...,0],cmap='hot')
plt.colorbar(infra_red)
plt.show()

grayimg = plt.imshow(img1,cmap='gray')
plt.colorbar(grayimg)
plt.show()

spectral =  plt.imshow(img1,cmap='nipy_spectral')
plt.colorbar(spectral)
plt.show()

fig, axes = plt.subplots(2,2)
fig.set_figwidth(10)
fig.set_figheight(10)

ax1 = axes[0,0]
ax2 = axes[0,1]
ax3 = axes[1,0]
ax4 = axes[1,1]

imgplot0 = ax1.imshow(img0)
fig.colorbar(imgplot0,ax=ax1)
ax1.set_xticks([]),ax1.set_yticks([])
ax2.hist(img0.ravel(), bins=256, range=(0,255))

imgplot1 = ax3.imshow(img1,cmap='gray')
fig.colorbar(imgplot1,ax=ax3)
ax3.set_xticks([]),ax3.set_yticks([])
ax4.hist(img1.ravel(), bins=256, range=(0.0,1.0),fc='k')

plt.suptitle('Histograms')
plt.show()
