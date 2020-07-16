
import numpy as np
a=np.array([0,1,2,3,4])
type(a) #returns numpy.ndarray
#as the data in the numpy.ndarry is all of one type then it is 
a.dtype #returns dtype('int32')
a.size #returns 5
a.ndim #returns the number of dimensions or rank of array
print(a.shape) # returns a tuple of the size of the array in each dimention (col, row)


#============== indexing and slicing ===============
c=np.array([20,1,2,3,4])
c[0] = 100 #sets first value in array to 100
d = c[1:4] #slicing availible.

#============== Basic Operations ==================
#vector addition 
u=np.array([1,0])
v=np.array([0,1])
z = u + v #vector addition z = array([1,1] this would not be so simple using regular array's
z = u - v #vector subtraction

#vector multiplication with a scalar
z = 2*u #only requires one line of code.
u = np.array([1,2])
v = np.array([3,2])
z = u*v #hattenberg product
result = np.dot(u,v) #returns the dot product of u and v
z = u+1 # scalar addition. Adds to all values in the array (broadcasting)
mean_a=a.mean() #returns the average of all the elements in the array
max_b = a.max() #returns largest value int he array
np.pi # returns pi
np.linspace(-2,2,num=5) #returns a evenly spaced array from -2 - 2 in 5 steps

#=============== Ploting sine wave ==========================
x = np.linspace(0,2*np.pi,100)
y=np.sin(x)
import matplotlib.pyplot as plt 
plt.plot(x,y) #plots the graph
plt.show()

#============== Numpy in 2d 
a = [[11,12,13,14], [21,22,23],[31,32,33]]
A = np.array(a)
A.ndim(a) #ndim obtains the number of dimensions (rank of an array) in this case it is 2
A.shape #returns a tuple returns (3,3) (num of nested arrays, number of items per list)
A.size #returns 9, the number of elements

B = np.array(a)
Y = A + B #matrix addition
Y = 2*Y #multiplying matrix by a scalar
H = A * B #hattemard product
C = np.dot(A,B) # dot product matrix multiplication


