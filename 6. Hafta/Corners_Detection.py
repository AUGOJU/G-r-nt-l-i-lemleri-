import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("image/tc.png")

plt.imshow(img)

def get_distance(pixel, w=[1/3, 1/3, 1/3]):
    r,g,b = pixel[0],pixel[1],pixel[2]
    w0,w1,w2 = w[0],w[1],w[2]
    return ((r**2)*w0 + (g**2)*w1 + (b**2)*w2)**0.5
  
def get_average(pixel):
    return (int(pixel[0]) + int(pixel[1]) + int(pixel[2])) / 3

def convert_RGB2GRAY(img, x):
    satir = img.shape[0]
    sutun = img.shape[1]
    gray_img = np.zeros((satir, sutun))
    for i in range(satir):
        for j in range(sutun):
            gray_img[i,j] = get_distance(img[i,j,:], x)
    return gray_img

def convert_RGB2GRAY_Scale(img):
    satir = img.shape[0]
    sutun = img.shape[1]
    gray_scale = np.zeros((satir, sutun))
    for i in range(satir):
        for j in range(sutun):
            gray_scale[i,j] = get_average(img[i,j])
    return gray_scale
  
def convert_GRAY2BW(gray_img, x):
    satir = gray_img.shape[0]
    sutun = gray_img.shape[1]
    bw_img = np.empty((satir, sutun))
    for i in range(satir):
        for j in range(sutun):
            if gray_img[i,j] > x:
                bw_img[i,j] = 1
            else:
                bw_img[i,j] = 0
    return bw_img
  
img.shape

plt.figure(1, figsize = (10,10))

gray_img = convert_RGB2GRAY(img, [.6, .3, .1])
bw_img = convert_GRAY2BW(gray_img, 120)

plt.imshow(gray_img)
plt.xticks([])
plt.yticks([])

plt.imshow(bw_img)
plt.xticks([])
plt.yticks([])

plt.figure(2, figsize = (10,10))

plt.subplot(121)
plt.title("RGB Image")
plt.imshow(img)

plt.subplot(122)
plt.title("BW Image")
plt.imshow(bw_img, cmap = 'gray')
plt.show()

# External Corners
def pixel_compare_1(img_block):
    #my_b = bwimg[i-1,i+1,j-1,j+1]
    s=0
    img_block=img_block.reshape(1,4)
    for i in range(4):
        if(img_block[i].any()==1):
            s=s+2**i
    if s==8 or s==4 or s==2 or s==1:
        return True
    else:
        return False

    
# Internal Corners    
def pixel_compare_2(img_block):
    #my_b = bwimg[i-1,i+1,j-1,j+1]
    img_block=img_block.reshape(1,4)
    s=0
    for i in range(4):
        if(img_block[i]==0):
            s=s+2**i
    if s==8 or s==4 or s==2 or s==1:
        return True
    else:
        return False
    
def count_object(bwimg):
    m=bwimg.shape[0]
    n=bwimg.shape[1]
    exter_corners = 0
    inter_conrers = 0
    for i in range(1,m-1):
        for j in range(1,n-1):
            if(pixel_compare_1(bwimg[i-1:i+1,j-1:j+1])):
                exter_corners+=1
            if (pixel_compare_2(bwimg[i-1:i+1,j-1:j+1])):
                inter_corners+=1
                
    return (exter_corners - inter_corners)/4
  
objects = count_object(gray_img)

