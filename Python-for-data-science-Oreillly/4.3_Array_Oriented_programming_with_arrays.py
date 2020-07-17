
""" Numpy arrays enables you to express many kinds of data processing in concise expressions that 
might otherwise require writing loops. This practice of replacing loops is called vectorization. 
It may be 2 or more orders of magnitude faster than pure Python equivalents. """

#==================================== Array Oriented Programming =================================
import numpy as np 
points = np.arange(-5, 5, 0.01) # 10000 equally spaced points 
# saay you wanted to evaluate the function sqrt(x^2 + y^2)
xs, ys = np.meshgrid(points, points) 
# The np.meshgrid function takes two 1d arrays and produces two 2D matrices 
# corresponding to all pairs(x, y) in the two arrays: (coordinates) 
# xs is the same as ys.T 
z = np.sqrt(xs ** 2 + ys ** 2) 
# will complete the operation for every element in the arrays 

print('Xs matrix\n', xs)
print('Yx matrix\n', ys)


# creating a visualisation. 
import matplotlib.pyplot as plt 
plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
plt.title("image plot of sqrt(x^2 = y^2 for a grid of values")
#plt.show()

#========================= Expressing Conditional Logic as Array operations =======================
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5]) 
cond = np.array([True, False, True, True, False]) 

#Suppose we wanted to take a value from xarr whenever the corresponding value in cond is True 
# and otherwise take the value of yarr 
result = np.where(cond, xarr, yarr) # returns array([1.1, 2.2., 1.3, 1.4, 2.5])
# The second and third arguments to np.where dont need to be arrays; they can be scalars. 
# A typical use in data analysis is to produce a new array fo values based on another array. 
# e.g. suppose you havd a matrix of randomly generated data and you wanted to replace all 
# positive values with 2 and negative with -2 

arr = np.random.randn(4, 4) 
arr > 0 # returns array of true when an element is above 0 
np.where(arr > 0, 2, -2)

#======================== Mathematical and Statistical Methods ====================================

arr = np.random.randn(5, 4) 
arr.mean() 
np.mean(arr) #pretty much same as above 
arr.sum()
arr.mean(axis=0) #computes the mean over specific aixis 
arr.sum(axis=0) 


# ========================= Metods for Boolean Arrays ============================================
arr = np.random.randn9100) 
(arr > 0 ).sum() #number of positive values 

bools = np.array([False, False, True, False])
bools.any() #tests if one or more is true 
bools.all() # tests if every value is true 

#========================= Sorting ===============================================================
arr = np.random.randn(6) 
arr.sort() #returns array of smallest to largest 

arr = np.random.randn(5,3) 
arr.sort(1) # will sort the first row 


#=========================== Unique and other Set logic =========================================
names = np.array9['Bob', 'Joe', 'will', 'Bob', 'will', 'Joe', 'Joe'])
np.unique(names) #returns an array of just the unique arrays 

