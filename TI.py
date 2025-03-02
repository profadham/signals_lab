# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np

t =np.arange(0,10,0.01)

x = np.exp(-0.5*t)
xshift = np.exp(-0.5*(t-2))


y1 = 5*x
y2 =5*xshift

y3 = 5*np.exp(-0.5*(t-2))

plt.plot(t,y1,)
plt.plot(t,y2,)
plt.plot(t,y3,'--g')
plt.legend(['y1','y2','y1_shifted'])



plt.ylim((0,5))