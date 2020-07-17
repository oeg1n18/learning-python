import numpy as np
import timeit

""" the numpy.random module supplements the built-in python random with functions 
for efficiently generating whole arrays of sample values from may kinds of probability 
distributions. For example, you can bet a 4x4 array of samples from the standard normal 
distribution using normal """

samples = np.random.normal(size=(4,4))

from random import normalvariate 
N = 1000000
samples = [normalvariate(0,1) for _ in range(N)]
np.random.normal(size=N) # This is over an order of magnitude faster than the above line 

# We say that these are pseudorandom numbers because they are generated by an 
# algorithm wth deterministic behaviour based on the seed of the random number 
# generator. You can change NumPy's random number generation using np.random.seed: 

np.random.seed(1234)

#The data generation function in numpy.random use a global random seed. To avoid the 
# global state you can use numpy.random.RandomState to create a generator isolated
# from the rest

rng = np.random.RandomState(1234)
rng.randn(10) #creates an array of 10 random numbers

"""
seed -- Seed the random number generator 
permutation -- return a random permutation of a sequence. 
shuffle -- Randomly permute a sequence in-place
rand -- Draw sample from a uniform distribution 
randint -- Draw random ints from a given low to high range 
randn -- Draw samples from a normal distribution with mean 0 and sd 1 
binomial -- Draw samples from a beta distribution 
bet -- draw samples from a beta distribution 
chisquare -- Draw samples from a chi-square distribution 
gamma -- draw samples froma gamma distribution 
unifomr -- draw samples from a uniform [0,1) distribution 
"""