import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('image/guto.jpg')

def get_distance(pixel,w=[1/3,1/3,1/3]):
    r,g,b = pixel[0],pixel[1],pixel[2]
    w0,w1,w2 = w[0],w[1],w[2]
    return ((r**2)*w0+(g**2)*w1+(b**2)*w2)**0.5
    
my_RGB = [1,2,3]
gray_level = get_distance(my_RGB,[0.6,0.3,0.1])
# gray_level = get_distance(my_RGB) -> boyle de yazilabilir
print(gray_level)

def convert_RGB2GRAY(img):
    m=img.shape[0]
    n=img.shape[1]
    gray_img = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            gray_img[i,j]=get_distance(img[i,j,:],[.6,.3,.1])
    return gray_img

#### Convert A Grayscale Image into Black White Image ####
def convert_GRAY2BW(grayimg,threshold):
    m=grayimg.shape[0]
    n=grayimg.shape[1]
    img_bw = np.empty((m,n))
    for i in range(m):
        for j in range(n):
            if grayimg[i,j] > threshold:
                img_bw[i,j]=1
            else:
                img_bw[i,j]=0
    return img_bw
    
    
plt.figure(1,figsize=(10,10))

plt.subplot(221)
plt.xticks([]),plt.yticks([])
plt.imshow(img)

gray_level_img = convert_RGB2GRAY(img)

plt.subplot(222)
plt.imshow(gray_level_img,cmap='gray')
plt.xticks([]),plt.yticks([])

plt.subplot(223)
plt.xticks([]),plt.yticks([])
plt.imshow(gray_level_img, cmap='gray')

plt.subplot(224)
plt.imshow(convert_GRAY2BW(gray_level_img,120), cmap='gray')
plt.xticks([]),plt.yticks([])

plt.show()
