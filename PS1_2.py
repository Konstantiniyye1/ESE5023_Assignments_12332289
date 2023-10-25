# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 09:11:02 2023

@author: 26576
"""
import numpy as np



M1=np.random.randint(0,51,(5,10))
print(M1)
M2=np.random.randint(0,51,(10,5))
print(M2)


def Matrix_multip(M1,M2):
    if M1.shape[0]!=M2.shape[1] or M1.shape[1]!=M2.shape[0]:
        print("the two matrix can not be multipled following array multiple law")
    else:
        M3=np.zeros((M1.shape[0],M1.shape[0]))
        for i in range(0,M1.shape[0],1):
            for j in range(0,M1.shape[0],1):
                for k in range(0,M1.shape[1],1):
                    M3[i,j]=M3[i,j]+M1[i,k]*M2[k,j]
        print(M3)
        
        
Matrix_multip(M1,M2)
Matrix_multip(M2,M1)


M1=np.random.randint(0,51,(4,10))
print(M1)
M2=np.random.randint(0,51,(10,5))
print(M2)

Matrix_multip(M1,M2)