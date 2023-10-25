# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 09:09:08 2023

@author: 26576
"""

def Print_values(a,b,c):
    if a>b:
        if b>c:
            print(a,b,c)
        else:
            if a>c:
                print(a,c,b)
            else:
                print(c,a,b)
    else:
        if b<c:
            print(c,b,a)
            
            
Print_values(5,8,9)
Print_values(51,82,19)
Print_values(25,48,39)
Print_values(65,48,29)
Print_values(55,68,99)