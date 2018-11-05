import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
my_img = mpimg.imread("image/guto1.jpg")

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
    return np.uint8(np.sum(roi*mask))

get_default_mask_for_mean()

def get_distance(pixel, w=[1/3,1/3,1/3]):
    r,g,b = pixel[0],pixel[1],pixel[2]
    w0,w1,w2 = w[0],w[1],w[2]
    return ((r**2)*w0 + (g**2)*w1 + (b**2)*w2)**0.5

def convert_RGB2GRAY(img):
    m=img.shape[0]
    n=img.shape[1]
    gray_img = np.zeros((m,n), dtype = np.uint8)
    for i in range(m):
        for j in range(n):
            gray_img[i,j]=get_distance(img[i,j,:],[.6,.3,.1])
    return gray_img

gray_img = convert_RGB2GRAY(my_img)
gray_img

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
        for j in range(1,n-1):
            roi=img[i-1:i+2,j-1:j+2]
            filtered_img[i,j] = apply_mask(roi) 
    return filtered_img

filt_img = get_mean_filter(gray_img)
filt_img

plt.figure(1,figsize=(10,10))

plt.subplot(121)
plt.xticks([]),plt.yticks([])
plt.title("Original")
plt.imshow(my_img)


plt.subplot(122)
plt.title("Grayscale")
plt.xticks([]),plt.yticks([])
plt.imshow(filt_img, cmap="gray")

plt.show()
