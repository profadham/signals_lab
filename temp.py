# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np

#n = np.arange(-5,5)
#x = np.reshape([n==0],np.shape(n))
#x = n-2==0
#plt.stem(n, x,use_line_collection='True',markerfmt = 'rx',label='lab2',linefmt='r--')

n = np.arange(-25,25)
x = np.exp(12j*n)*(n>=0)
y = np.real(x)
z = np.imag(x)
plt.subplot(2,1,1) #2,1 2 rows and 1 column
plt.stem(n, y,use_line_collection='True')
plt.subplot(2,1,2)
plt.stem(n,z,use_line_collection='True')
plt.legend() #makes the label appear