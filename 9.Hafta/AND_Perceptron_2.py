import numpy as np
import matplotlib.pyplot as plt

my_data_x = []
my_data_x.append([0,0])
my_data_x.append([0,1])
my_data_x.append([1,0])
my_data_x.append([1,1])
my_data_x

my_data_y = []
my_data_y.append(0)
my_data_y.append(0)
my_data_y.append(0)
my_data_y.append(1)
my_data_y

x,y = my_data_x, my_data_y
for a,b in zip(x,y):
    print(a,b)
    
--------------------------------------------------------------------------------------
# Yukardaki kodları Funksıyon kullanarak

def get_my_data():
    my_data_x = []
    my_data_x.append([0,0])
    my_data_x.append([0,1])
    my_data_x.append([1,0])
    my_data_x.append([1,1])
    my_data_x
    
    my_data_y = []
    my_data_y.append(0)
    my_data_y.append(0)
    my_data_y.append(0)
    my_data_y.append(1)
    my_data_y
    
    return my_data_x, my_data_y
    
    
    for a,b in zip(my_data_x, my_data_y):
    print(a,b)
