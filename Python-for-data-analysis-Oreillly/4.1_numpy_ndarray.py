
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

 #=================== Arithmetic with NumPy Arrays ========================================

arr = np.array([[1., 2., 3.], [4., 5., 6.]])

arr * arr #each cell of arr is multiplied by itself
arr - arr #each element is now 0
1/arr # creates reciprocal of each cell
arr ** 0.5 #roots each cell

# Arithmetic operations with scalars propagate the scalar argument to each element in the array 
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]]) 
arr2 > arr #returns an np array of true and false

#=================== Basic indexing and slicing ======================================================= 
arr = np.arange(10) #array of 1-10 int64 
arr[5] #returns 5
arr[5:8] #returns array of 5, 6, 7
arr[5:8] = 12 #5,6,7 are all replaced with 12 
arr_slice = arr[5:8] #retuns an array of 12 (array is mutable)
#if you change the vallues in arr_slice, the mutations are reflected in the original

# numpy does this as always creating new copies slows things down. if however you do want 
# want to copy it you can use the following syntax 
arr_new = arr[5:8].copy()

#to make things easier you can access elements using commas 
arr = np.arange(15).reshape((3,5))
arr[0,1] # indexing

#====================== indexing with slices ==========================================================
arr2d = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
                
arr2d[:2] #returns array ([[1,2,3],[4,5,6]])

#===================== Fancy indexing =================================================================
# fancy indexing is a term adopted by numPy to describe indexing using integer arrays
arr = np.empty((8,4))
for i in range(8):
    arr[i] = i
# to select out a subset of the rows in a particular order, you can simply pass a list or ndarray 
# of integers specifiying the desicred order
arr[[4, 3, 0, 6]] # will reutnr row 4 followed by 3 ect 

#========================= Transposin Arrays and Swapping Axes ======================================
arr = np.arange(15).reshape((3,5))
arr.T #transposes the array 

# When doing matrix computations, you may do this very often-for example, when computing the 
# inner matrix product using np.dot 

np.dot(arr.T, arr)
arr = np.arange(16).reshape((2, 2, 4))

# for higher dimensional arrays, transpose will accept a tuple of axis numbers to permutate the axes
arr.transpose((1, 0, 2))

#========================= Fast Element-Wise array functions ========================================
arr = np.arange(10)
np.sqrt(arr) 
np.exp(arr)

x = np.random.randn(8) 
y = np.random.randn(8)

np.maximum(x,y) # cumputed the element-wise maximum and returned the array with the largest element 
 