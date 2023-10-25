# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 09:17:27 2023

@author: 26576
"""
import numpy as np
import matplotlib.pyplot as plt


def Find_expression(a):
    y=np.array(["","+","-"])
    for i in y:
        for j in y:
            for k in y:
                for l in y:
                    for m in y:
                        for n in y:
                            for o in y:
                                for q in y:
                                    z="1"+i+"2"+j+"3"+k+"4"+l+"5"+m+"6"+n+"7"+o+"8"+q+"9"
                                    if eval(z)==a:
                                        print(z+"="+str(a))
                                        
                                        
def Find_expression_count(a):
    y=np.array(["","+","-"])
    count=0
    for i in y:
        for j in y:
            for k in y:
                for l in y:
                    for m in y:
                        for n in y:
                            for o in y:
                                for q in y:
                                    z="1"+i+"2"+j+"3"+k+"4"+l+"5"+m+"6"+n+"7"+o+"8"+q+"9"
                                    if eval(z)==a:
                                        count+=1
    return count


Find_expression(50)
Find_expression(75)

x=np.linspace(1,100,100)
Total_solutions=np.zeros((100))
for i in range(0,100,1):
    Total_solutions[i]=Find_expression_count(i+1)
plt.plot(x,Total_solutions)

print(max(Total_solutions))
print(np.where(Total_solutions==max(Total_solutions)))

print(min(Total_solutions))
print(np.where(Total_solutions==min(Total_solutions)))