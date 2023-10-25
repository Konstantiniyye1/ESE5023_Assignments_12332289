# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 09:16:40 2023

@author: 26576
"""

def least_moves(x):
    n=0
    while x>1:
        if x%2==1:
            x=(x-1)/2
            n=n+2
        else:
            x=x/2
            n=n+1
    print(n)



least_moves(2)
least_moves(3)
least_moves(5)
least_moves(245)
least_moves(1543)
