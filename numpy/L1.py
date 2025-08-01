#numerical python - fundamental package for scientific computing in python

import numpy as np

arr=np.array([4,5,6])
print(arr)

a2=np.array([[4,5,6],[1,2,3]])
print(a2)
print(a2.shape)

a2.shape=(3,2)
print(a2)


arr_zerp=np.zeros((4,5))
print(arr_zerp)

print(np.arange(10,20,2))

print(np.linspace(100,200,11))

print(np.full((4,5),5))


#Mathematical operations
a5=np.array([1,2,3])
a6=np.array([5,6,7])
a7=np.array([1,2,3])

print(np.equal(a5,a7))

print(np.array_equal(a5,a7))

print(np.sum(a5))

a8=[[1,2],[8,9]]
print(np.sum(a8))

print(np.sum(a8,axis=0))
print(np.sum(a8,axis=1))

#sub,multiply,divide,sin,cos,tan,sqrt,exp,log,min,median,min,max, std, array1 + array2

#slicing & indexing

arr1=np.array([1,2,3,4,5])
arr2=np.array([[1,2,3],[4,5,6]])

print(arr1[1:4])
print(arr1[-2])

print(arr2[0][1:])

print(arr2[:][1:])