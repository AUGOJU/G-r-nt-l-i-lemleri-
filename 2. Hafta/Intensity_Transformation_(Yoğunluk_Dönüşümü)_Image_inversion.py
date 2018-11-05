import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('image/guto.jpg')

def fonksiyon(x):
    return 255 - x
    
img2 = np.empty((1600,1200,3), dtype=np.uint8)
rows = img.shape[0]
cols = img.shape[1]
for i in range(rows):
    for j in range (cols):
        img2[i,j] = fonksiyon(img[i,j])

ORIGINAL
-----------
plt.imshow(img)
plt.title('original')

INVERSE
----------
plt.imshow(img2)
plt.title('image inversion')
plt.show()
