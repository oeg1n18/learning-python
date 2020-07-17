import numpy as np

x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8,9]])

x.dot(y) #same as np.dot(x, y)

np.dot(x, np.ones(3)) # also matrix multiplication 
x @ np.ones(3) # same as above 


""" numpy.linalg has a standard set of matrix decompositions and things like inverse and determinant.
These are implemeneted under the hood via the same industry standard linear algebra libraies 
used in languages like MATLAB and R, such as BLAS, LAPACK. """

from numpy.linalg import inv,qr 
X = np.random.randn(5,)
mat = X.T.dot(X)

inv(mat) #inverse of matrix
mat.dot(inv(mat)) #will create diagonal matrix with just ones on the diag
q, r = qr(mat) # compute the qr factorisation of the matrix 

""" 
diag -- returns the diag elements of a square matrix as a 1D array 
dot -- matrix mult 
trace -- compute the sum of the diag elements 
det -- compute the determinant 
eig -- compute the eigenvalues and ebenevectors of the square matrix 
inv -- compute the inverse 
pinv -- compute the Moore-Penrose pseudo-inverse of a matrix
qr -- compute the QR decomposition 
svd -- compute the singular value decomposition 
solve -- Ax = b for x, Where A is a Square matrix 
lstsq -- compute the leas-squres solution to Ax = b
"""