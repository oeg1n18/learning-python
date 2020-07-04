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
