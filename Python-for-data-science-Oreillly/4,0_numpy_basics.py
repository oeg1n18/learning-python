

#==================================== Arrays and Vectorized Computation =========================
# Numpy is a library for array and vectorized computation. It stores the array in a contigous 
# block of memory. independant of other buil in python objects. Numpy operatons perfrom 
# computations on entire arrays without the need ofr Python for loops 
# To give an idea of perfromance differences 

import numpy as np 
my_arr = np.arange(1000000)
my_list = list(range(1000000))
# lets multiply each sequence by 2:
print(' ---------------- numpy array ---------------')
#%time for _ in range(10): my_arr2 = my_arr * 2 #works with ipython terminal
print(' -----------------Python List ---------------')
#%time for _ in range(10): my_list2 = [x * 2 for x in my_list] works with ipython terminal

