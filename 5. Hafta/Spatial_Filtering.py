import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
my_img = mpimg.imread("image/guto.jpg")

mask0 = np.array([1,1,1,1,1,1,1,1,1]).reshape(3,3)
mask0

mask1 =mask0/9
mask1

mask2 = np.random.randint(20,size=9).reshape(3,3)
mask2

def get_default_mask_for_mean():
    return np.array([1,1,1,1,1,1,1,1,1]).reshape(3,3)/9

def apply_mask(roi):
    mask = get_default_mask_for_mean()
    return sum(sum(roi*mask))
  
get_default_mask_for_mean()

apply_mask(roi)

roi=my_img[2-1:2+2,3-1:3+2]
apply_mask(roi)

def get_median(roi):
    s_1 = roi.reshape(1,9)
    s_1.sort()
    return s_1[1,4]
  
def get_mean_filter(img):
    m=img.shape[0]
    n=img.shape[1]
    filtered_img = np.zeros((m,n),dtype=np.uint8)
    for i in range(1,m-1):
        for j in range(1,n):
            roi=img[i-1:i+2,j-1:j+2]
            filtered_img[i,j] = get_median(roi) #apply_mask(roi) 
    return filtered_img
  
filt_img = get_mean_filter(my_img)

plt.figure(1,figsize=(10,10))

plt.subplot(121)
plt.xticks([]),plt.yticks([])
plt.title("Original")
plt.imshow(my_img)


plt.subplot(122)
plt.title("Grayscale")
plt.xticks([]),plt.yticks([])
plt.imshow(filt_img)

plt.show()

