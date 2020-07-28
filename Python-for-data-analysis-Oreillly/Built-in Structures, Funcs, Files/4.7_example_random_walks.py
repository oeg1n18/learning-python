
import random 
import matplotlib.pyplot as plt  
import numpy as np

#===================================== Simulating a Random Walk ==============================================================


position = 0
walk = [position] 
steps = 10000 
for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)



#you could argue that 'walk' is simply the cumulative sum of the random steps and could be evaluated as an array expression. 
# np.random can draw 1000 coin flips at once and set these to 1 and -1 
nsteps =  10000
draws = np.random.randint(0, 2, size=nsteps) #
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum() #cumsum is the cumulative sum of each of the steps

# from this we can extract stats like min and max value along the walk's trajectory 
walk.min() #min distance 
walk.max() 




#============= Simulating Many Random Walks at once =========================================================================
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps)) #draws is an array of 5000 walks each walk containing a list size 1000 or 1 or 0
steps = np.where(draws > 0, 1, -1) #alters each walk to -1 or 1 
walks = steps.cumsum(1) 
walks.max()
walks.min()

# Out of these walks lets compute the minimum crossing time to 30 or -30. remember not all walks reach 30 or -30 
# we can check this using any method 
hits30 = (np.abs(walks) >= 30).any(1) #returns boolean array of all the walks that reach 30 (.any() )
hits30.sum() #counts the number that hits 30 or -30

#We can use this boolean array to select out the rows of walks that actually cross the absolute 
# 30 level and call argmax across axis 2 to get the crossing times: 

crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1) #argmax returns the indicy of the max value int he array for all of the walks
print(crossing_times.mean())

