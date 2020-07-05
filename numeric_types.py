#========================== Numeric literals ==================================
1234 #integers
1.23 #Floating-point Numbers
0x9ff #hex
3+4j #complex
set('spam'),{1,2,3,4} #construction forms
x=1
q = bool(x)    #Boolean
y = True
z = False
# casts
int(3.145) #truncates
float(3) #converts integer to float
q = 10/4 #returns 2.5
q = 10//4 #returns 2 truncates the result
#conversions
q = int('100', 8)
q = int('40', 16)
q = int('10000000', 2)
# Math tools
import math
math.pi
math.e
math.sin(2*math.pi/180)
math.sqrt(5)
pow(2,4)
math.floor(2.567) #lowest round to 2

import random
random.random() #random floats, integers,choices, shuffles
random.randint(1, 10) #random int between 1 and 10
suits = ['hearts', 'clubs', 'diamonds', 'spades']
random.shuffle(suits) #pick a random from the lsit

# sets =======================================
# Sets are an unordered collection of unique and immutable objects
# By definition, an item appears only once in a set, no matter how many
# times it is added. Seths have a variety of applications in numeric 
# and database focused work

# for python 2.7 and earlier
x = set('abcde') #each alpha-numeric is a an item in the set
y = set('bdsyx') 
x-y #difference
x|y #union
x & y #intersection
x ^ y #symetric difference (XOR)
x > y #superset
x < y #subset

engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', 'sue'}
'bob' in engineers #returns rue
engineers & managers #who is both engineer and manager
engineers | managers #all people in either catageory 
engineers - managers #engineers who are not managers
managers - engineers #managers who are not engineers
engineers > managers #are all managers engineers? 
{'bob', 'sue'} < engineers #are both engineers?
(managers | engineers) > managers #all people is a superset of managers
managers ^ engineers #who is in one but not in both
(managers | engineers) - (managers ^ engineers) #intersection
