import numpy as np
import matplotlib.pyplot as plt

def my_product_two_dim_with_threshold(a,b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
    
def get_my_data():
    my_data_x = []
    my_data_x.append([1,0,0])
    my_data_x.append([1,0,1])
    my_data_x.append([1,1,0])
    my_data_x.append([1,1,1])
    my_data_x
    
    my_data_y = []
    my_data_y.append(0)
    my_data_y.append(0)
    my_data_y.append(0)
    my_data_y.append(1)
    my_data_y
    
    return my_data_x, my_data_y
    
x,y = get_my_data()
for a,b in zip(x,y):
    print(a,b)
    
def get_parameters():
    w = []
    w.append(3)
    w.append(2)
    w.append(1)
    w
    learning_rate = 1
    epoch = 100
    
    return w, learning_rate, epoch
   
get_parameters()

w, learning_rate, epoch = get_parameters()
samples, output = get_my_data()

samples

output

for i in range(2):
    error = "hata_yok"
    s = -1
    print("******************************************************")
    for each_sample,d in zip(samples, output):
        s = s + 1
        print("ağırlık: ", w)
        print("örnek: ", each_sample)
        print("gercek output: ", d)
        #print(my_product_two_dim_with_threshold(w, each_sample))
        
        u = my_product_two_dim_with_threshold(w, each_sample)
        
        if(u > 0):
            y = 1
        else:
            y = 0
        print("Tahmin çıktı: ", y)
        print("")
        
        if(y != d): # error var
            for s in range(3):
                w[s] = w[s] - learning_rate*(y-d)*each_sample[s]
            error = "hata var"
    if(error == "hata_yok"):
        print("hata yok", i)
        break 

print(w)
