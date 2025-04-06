# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

n = 1000

t,T = np.linspace(0,8,n,retstep=True)

x1 = np.where(t<=4,0,1)
x2 = np.where(np.logical_and(t >= 4, t <= 6), 0, 2)

y = np.convolve(x1, x2, mode='full') * T

ty = np.linspace(0,2*8,n*2-1)

plt.figure()
plt.plot(t, x1, label = "$x_1$")
plt.grid(True)
plt.figure()
plt.plot(t, x2, label = "$x_2$")
plt.grid(True)
plt.figure()
plt.plot(ty, y, label = "$x_1\\star x_2$")
plt.grid(True)

plt.legend(loc='best')

