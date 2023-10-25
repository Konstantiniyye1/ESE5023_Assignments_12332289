# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 09:13:19 2023

@author: 26576
"""

def Pascal_triangle(k):
    x=np.ones((k,k))
    for i in range(2,k,1):
        for j in range(1,i,1):
            x[i,j]=x[i-1,j-1]+x[i-1,j]
    print(x[k-1,:])
    
    
Pascal_triangle(1)
Pascal_triangle(2)
Pascal_triangle(5)
Pascal_triangle(100)
Pascal_triangle(200)