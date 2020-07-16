
import numpy as np 
data = np.random.randn(2,3) #returns a 2/3 array with random numbers 
data * 10 #multiplies all elements in the array by 10 
data + data #each cell has been added to itself

data.shape #returns the dimension of the array
data.dtype #returns the data type of the array

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1) # creates a np array 

data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2) # creates 2d np array
arr2.ndim # retruns number of dimensions
arr2.shape # returns a tuple (2,4)

np.zeros(10) # returns 1d array with 10 zeros
np.zeros((2,3,2)) # returns 3d array filled with 0's 

""" Numpy Array functions 
array -- convert input data to ndarray 
asarray -- convert input to ndarray, but do not copy if the input is already an ndarray 
arange -- like the built-in range but returns an ndarray instead of a list 
one -- produce an array of all 1s with the given shape and dtype
ones_like -- produces a ones array of the same shape and dtype 
zeros -- like ones and ones_like but creates ndarray of 0's 
zeros_like
empty -- create new arrays by allocating new memory, but do not populate with any values like ones ane zeros
empyt_like 
full -- produce an array of the given shape and dtype with all values set to the indictes "fill value"
full_like -- full_like takes another array and produces a filled array of the same shape and dtype
eye, identity -- create a NXN identity matrix
"""

#==================== Data Types for ndarrays =========================================================
arr1 = np.array([1,2,3], dtype=np.float64)
arr2 = np.array([1,2,3], dtype=np.int32)

#cast an array from one data type to another using astype 
arr = np.array([1,2,3,4,5]) #dtype = int64
float_arrr = arr.astype(np.float64) #casts to float64

numeric_strings = np.array(['1.23', '-0.54', '344.0'], dtype=np.string_)
numeric_strings.astype(float) #returns array of float64 
""" its important to be cautious when using the numpy.string_ types, as string
 data in Numpy is fized size and may truncate input without warning. Pandas has 
 more intuitive out of the box behaviour for non-numeric data"""

 