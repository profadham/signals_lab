# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

np.array([1,2,3])
np.arange(2)
np.arange(1,10,2,dtype = int) #start, end+1, step

np.linspace(2.0,3.0,num=5) #3.0 is included
#5 numbers between 2.0, 3.0 inclusive

np.linspace(2.0,3.0,num=5,endpoint = False,retstep=True) #3.0 not included
#returns step
#default num=50

np.ones(5, dtype = int) #5 ones, default is float
np.ones((2,5)) #rows,cols

np.zeros(5)

np.eye(5) #identity matrix 5x5
np.eye(5,k=2) #shift diagonal 2

np.ful((2,2),10) #2x2 matrix filled with 10s

np.full((2,2),[1,2])

np.shape(np.eye(3)) #returns dimensions of the matrix

############################

a=np.array([[1,2,3],[4,5,6]])
np.reshape(a,6,order='f') #[6,5,4,3,2,1]
np.reshape(a,(3,-1))
"""
[
 [1,2]
 [3,4]
 [5,6]
 ]
""" 
a.flatten('f') #[6,5,4,3,2,1]
np.repeat(a,2,axis = 0) #axis = 0 for row and 1 for column
"""
[
 [1,2,3]
 [1,2,3]
 [4,5,6]
 [4,5,6]
 ]
"""
np.repeat(a,2) #[1,1,2,2,3,3,4,4,5,5,6,6] flatten then rpeat

