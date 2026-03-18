## Numpy

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))


## 2D array 

import numpy as np
a = np.array([4,6,7,8])
b = np.array([5,8,9,10])

print(a+b)
print(a*b)

## Array Properties

arr = np.array([10,20,30,40,50])

print(arr.size)
print(arr.dtype)
print(arr.sum())
print(arr.mean())

## 2D array 

arr = np.array([[1,2,3,4,5],
                [2,5,6,7,8,]])
print(arr)
print(arr.shape)

## Task 1:
## create two numpy array 

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a+b)
print(a*b)

## Task 2:
## create Array print mean ,sum , max ,min

arr = np.array([5,10,15,20,25])
print(arr.mean())
print(arr.sum())
print(arr.max())
print(arr.max())

## Task 3 (Mini Challenge):

arr =np.array([[80, 90, 70],
 [60, 75, 85],
 [88, 92, 79]])

print(arr.shape)
print(np.average(arr))