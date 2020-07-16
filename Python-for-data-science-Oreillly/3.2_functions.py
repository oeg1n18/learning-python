
#=========================================== Returning Multiple Variables ========================================
def f():
    a = 5 
    b = 6
    c = 7
    return a,b,c

a, b, c= f()

#============================================= Functions Are objects ============================================
# Since Python functions are objects, you can create e.g. lists of functions 
states = ['   Alabama  ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south carolina##', 'West virginia?']

import re

def remove_punctuation(value):
    return re.sub('[!#?]', ' ', value)

clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops): #loops through the cleaning functions applying each one to the strings
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result

# you can use functions as arguments to other functions



#============================================ Anonymous Lambda functions =======================================
#soppose you wanted to sort a collection of strings by the number of distinct letters 
# in each strings
strings = ['foo', 'card', 'bar', 'aaaaaa', 'abab']
# can pass a lambda function to the lists sort method
strings.sort(key=lambda x:len(set(list(x))))


def apply_to_list(some_list, f):
    return[f(x) for x in some_list]

ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2) #short way to define a simple function



#=========================================== Generators ========================================================
# iterating over object is accomplished by the iterator protocol, a generic way to make objects iterable. 
# for example iterating over a dict yields the dict keys:
some_dict = {'a':1, 'b':2, 'c':3}
for key in some_dict:
    print(key) # prints keys

# When you write 'for key in some_dict', the Python interpreter first attempts to create an iteraotr out 
# of some_dict:   A generator is a concise way to construct a new iterable oject. Wheras normal functions
# ececute and return a single result at a time, generators reutrn a sequence of multiple results lazily, 
# pausing after each one until the next one is requested. To create a generator, use the yield keyword 
# instead of reutnr in a function:

def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n ** 2))
    for i in range(1, n + 1):
        yield i ** 2 

gen = squares()

for x in gen:
    print(x, end=' ')

#==================== Generator expressions
# The folowing code blocks do the exact same thing 
gen = (x ** 2 for x in range(100))

def _make_gen():
    for x in range(100):
        yield x ** 2
gen = _make_gen()

# ============================================= itertools module ==============================================
import itertools
first_letter = lambda x: x[0]
names = ['Alan', 'Ollie', 'Mark', 'Nicola', 'Giles', 'Tom']
for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names)) #names is a generator 

""" will print (groups names by first letter)
A ['Alan']
O ['Ollie']
M ['Mark']
N ['Nicola']
G ['Giles']
T ['Tom']
"""

#========================================== Errors and Exception handling =====================================
#float('something') #creates ValueError so can try

def attempt_float(x):
    try:
        return float(x)
    except:
        return x 

#float((1,2)) #will raise Type error

def attempt_float(x):
    try: 
        return float()
    except(TypeError, ValueError):

        return x

f = open('test.txt', 'w')

try:
    write_to_file(f)
except:
    print('failed')
else:
    print('Succeeded')
finally:
    f.close()


