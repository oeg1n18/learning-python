
import numpy as np

arr = np.arange(10)
np.save('exampledata/some_array', arr)
# will be saved with .npy extnesion 
np.load('exampledata/some_array.npy')
np.savez('exampledata/array_archive.npz', a=arr, b=arr)
# when loading an .npz file, you get back a dict-like object that loads the individual arrays lazily 
arch = np.load('exampledata/array_archive.npz')
arch['b'] # is array([0,1,2,3.....9])
