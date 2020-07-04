

# ========= Numbers =======================================================
x = 123  #ints
y = 1.234 #floats

import math
print('pi value', 'math.pi')
print('square route of 85', math.sqrt(85))

import random
print('random number', 'random.random()')
x = random.choice([1,2,3,4])




#========= Strings ==================================================
# Strings are imutable objects You cannot re-assign them only create new ones
# you can however create a new one and assign it to the same name python
# cleans up old objects as you go


S = 'spam' #string decleration
print('string length', len(S)) #string length
y = S[0] #the first item in S, indexing by zero based position
z = S[-1] #last item in the end in s 'm'
S[1:3] # slice of S
S + 'xyz' #Concatenation
S * 8 #repetition

S = 'Spam'
S.find('pa') #returns the nuber if instances
S.replace('pa', 'XYZ') #Replaces all occurances of pa with xyz
#S still reamins as 'Spam'
line = 'aaa,bbb,ccc,dd\n'
line.split(',') # split on a delimiter
S.upper() #uppercase
S.lower() #lowercase
S.isalpha() #reutrns ture for alfphanumeric. Same for isdigit ect
line.rstrip() #remove Whitespace characters on the right side
line.rstrip().split(',') #combine two operations

'%s, eggs, and %s' % ('spam', 'SPAM') #formatting for all python version





# ============ Lists ==========================================================
# they are mutable unlike strings and can contain a number of different object
# types

L = [123, 'spam', 1.23] #decleration
len(L) #returns length
L[0] #indexing
L[:-1] # slicing a list returns a new Lists
l + [4,5,6] #concat/repeat makes new lists too

# Type specific operations
L.append('NI') #Growing: add object to the append
L.pop(2) #Shrinking: delete an item in the middle

M - ['bb', 'aa', 'cc']
M.sort() #sorts them into alphabecital order
M.reverse() #reverses the order
#Nesting
M = [[1,2,3]
     [4,5,6]
     [7,8,9]]
M[1] #Geet row 2
M[1][2] #get row 2, then get item 3 within Growing

#Comprehensions
col2 = [row[1] for row in M]  #collects items in column 2
diag = [M[i][i] for i in [0,1,2]] #Collect a diagonal from matrix





#================== Dictonary ================================================
# Store obejcts by key instead of relative position. They are not indexable

D = {'food': 'Spam', 'quantity':4, 'color':'pink'}
D['food'] #reutns Spam
D['quantity'] += 1 #adds 1 to quantity value

D['name'] = 'Bob' #create keys by assignment
if not 'f' in D:
    print('missing') #checking if f exisits in the Dictonary

# Dicts do not have any order. If we want to print them back in an order.
D = {'1':1, 'b':2, 'c': 3}
Ks = list(D.keys()) #converts to list
Ks.sort() #sorted keys list
for key in Ks:
     print(key, '=>', D[key]) # prints a => 1
                             #        b => 2
                             #        c => 3
# alternatively
for key in sorted(D):
    print(key, '=>', D[key])  # prins same as above.



#==================== Tuples =================================================
# Fairly similar to a list but are immutable.
T = (1,2,3,4)
len(T) #returns number of items
T + (5,6) #Concatenation
T[4] #indexing
T.index(4), #returns 3 as 4 appears at index 3
T.count(4) # 4 appears once
# cannot .append(**) a Tuples


#====================== Files ================================================
# Can be used to read and write text memos, audio clips, Excel documents, saved
# email messages, and whatever else you have on your machine
f = open('data.txt', '2')
f.write('Hello ')
f.write('World')
f.close()
