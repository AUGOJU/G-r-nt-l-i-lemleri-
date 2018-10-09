# G-r-nt-l-i-lemleri-
Görüntülü işlemi dersinde yaptimiz örnekleri

import numpy as np
import matplotlib.pyplot as  plt
import matplotlib.image as mpimg

img = mpimg.imread("Data/kerim.png")
print("ndimension : ",img.ndim)
print("shape : ",img.shape)

# red
print("Red Min: ")
print(img[..., 0].min())
print("Red Max: ")
print(img[..., 0].max())

# green
print("Green Min: ")
print(img[..., 1].min())
print("Green Max: ")
print(img[..., 1].max())

# blue
print("Blue Min: ")
print(img[..., 2].min())
print("Blue Max: ")
print(img[..., 2].max())

plt.imshow(img)

-------
ndimension :  3
shape :  (384, 512, 4)
Red Min: 
0.0
Red Max: 
1.0
Green Min: 
0.0
Green Max: 
0.99215686
Blue Min: 
0.0
Blue Max: 
1.0

<matplotlib.image.AxesImage at 0x225186b0550>
-------------------------------------------------------

def myfunction_1(img):
    import numpy as np
    import matplotlib.pyplot as  plt
    import matplotlib.image as mpimg

   
    print("ndimension : ",img.ndim)
    print("shape : ",img.shape)

    # red
    print("Red Min: ")
    print(img[..., 0].min())
    print("Red Max: ")
    print(img[..., 0].max())

    # green
    print("Green Min: ")
    print(img[..., 1].min())
    print("Green Max: ")
    print(img[..., 1].max())

    # blue
    print("Blue Min: ")
    print(img[..., 2].min())
    print("Blue Max: ")
    print(img[..., 2].max())

    plt.imshow(img)
--------------
img = mpimg.imread("Data/kerim.png")
myfunction_1()
--------------
ndimension :  3
shape :  (384, 512, 4)
Red Min: 
0.0
Red Max: 
1.0
Green Min: 
0.0
Green Max: 
0.99215686
Blue Min: 
0.0
Blue Max: 
1.0
-------------------------------------------------------

def myfunction_1():
    import numpy as np
    import matplotlib.pyplot as  plt
    import matplotlib.image as mpimg
    
    img = mpimg.imread("Data/kerim.png")
   
    print("ndimension : ",img.ndim)
    print("shape : ",img.shape)

    # red
    print("Red Min: ")
    print(img[..., 0].min())
    print("Red Max: ")
    print(img[..., 0].max())

    # green
    print("Green Min: ")
    print(img[..., 1].min())
    print("Green Max: ")
    print(img[..., 1].max())

    # blue
    print("Blue Min: ")
    print(img[..., 2].min())
    print("Blue Max: ")
    print(img[..., 2].max())

    plt.imshow(img)
-------------
myfunction_1()
-------------
ndimension :  3
shape :  (384, 512, 4)
Red Min: 
0.0
Red Max: 
1.0
Green Min: 
0.0
Green Max: 
0.99215686
Blue Min: 
0.0
Blue Max: 
1.0
