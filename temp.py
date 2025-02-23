# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np


def mul(n1,x1,n2,x2):
    min_n = min(min(n1),min(n2))
    max_n = max(max(n1),max(n2))
    n =np.arange(min_n,max_n+1)
    ###################################
    x1n = np.zeros(np.shape(n))
    x1n[(n>=min(n1))&(n<=max(n1))]=x1
    x2n = np.zeros(np.shape(n))
    x2n[(n>=min(n2))&(n<=max(n2))]=x2
    ###################################
    x = x1n*x2n
    return x,n

n1 = np.arange(0,5)
x1 = n1
n2 = np.arange(-2,3)
x2 = np.full(np.shape(n2),2)

x,n = mul(n1,x1,n2,x2)
plt.stem(n, x,use_line_collection='True')
    
