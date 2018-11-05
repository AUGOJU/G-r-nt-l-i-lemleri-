import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

def matris_create_28_by_28_with_0_1():
    my_matris = np.zeros((28,28))
    for i in range(28):
        for j in range(28):
            my_matris[i,j] = random.randint(0,1)
    return my_matris

m = matris_create_28_by_28_with_0_1()
m

def matris_create_28_with_0_1(matrix_a):
    m = matrix_a.shape[0]
    n = matrix_a.shape[1]
    x_min = m
    x_max = 0
    y_min = n
    y_max = 0
    for i in range(m):
        for j in range(n):
            if(matrix_a[i,j] == 1 and x_min > i):
                x_min = i
            if(matrix_a[i,j] == 1 and x_max < i):
                x_max = i
            if(matrix_a[i,j] == 1 and y_min > j):
                y_min = j
            if(matrix_a[i,j] == 1 and y_max < j):
                y_max = j
    return (x_min, x_max, y_min, y_max)

matris_create_28_with_0_1(m)

def get_similarity(character_a, character_b):
    m = character_a.shape[0]
    n = character_a.shape[1]
    my_similarity = 0
    for i in range(m):
        for j in range(n):
            my_similarity = my_similarity+character_a[i,j]*character_b[i,j]
    return my_similarity

c_1 = matris_create_28_by_28_with_0_1()
c_2 = matris_create_28_by_28_with_0_1()
get_similarity(c_1, c_2)

def get_similarity_for_100_char(kac_char = 100):
    chars = []
    for i in range(kac_char):
        new_char = matris_create_28_by_28_with_0_1()
        chars.append(new_char)
    for i in range(kac_char):
        benzerlik = get_similarity(chars[0], chars[i])
        print("0 -- " + str(i) + " ", benzerlik)
        
c_1 = matris_create_28_by_28_with_0_1()
c_2 = matris_create_28_by_28_with_0_1()
get_similarity(c_1, c_2)
get_similarity_for_100_char(10)
