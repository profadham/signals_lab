# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np

t =np.arange(0,10,0.01)

x1 = np.cos(10*np.pi*t)
x2 = np.exp(-0.5*t)


a = 2
b = 1.25

x3 = a*x1 + b*x2

y1 = 5*x1
y2 = 5*x2
y3 = 5*x3

y_act = 5*y1 + 5*y2


plt.subplot(2,1,1)
plt.plot(t,y3)
plt.subplot(2,1,2)
plt.plot(t,y_act)
#plt.stem(x2, t,use_line_collection='True')