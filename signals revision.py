import numpy as np
import matplotlib.pyplot as plt
arr = np.array([1,2,3])
a = np.linspace(2,10,num = 5,endpoint = True,retstep =True)#default num = 50
a2 = np.arange(2,10,3)
a3= np.ones(5)
a4 = np.ones((2,2),dtype=int)
a5 = np.zeros((2,3),dtype =int)
a6 = np.eye(2, dtype = int) #identity matrix
a7 = np.eye(4,k=1,dtype=int) #k is the shift of the diagonals with ones
a8 = np.full((4,5),10)
print(a4)
a4 = np.reshape(a4,(4,1))
a4 = np.reshape(a4,4)
a4 = np.reshape(a4,(-1,2))
a4 = np.reshape(a4,(-1,2),order='F') #fills column wise instead of row wise
print(a4)
print(np.shape(a4))

x = np.array([[1,2,3,4],[5,6,7,8]])
b = np.repeat(x,2)
c = np.repeat(x,2,axis=1) #repeats each element in a row
d = np.repeat(x,2,axis=0) #repeats each row

print(x)
print(b)
print(c)
print(d)

'''
a.flatten() moves row by row
a.flatten('F') moves col by col
'''