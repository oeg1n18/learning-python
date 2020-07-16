
#============================== Reading files ==========================================================

path = 'test.txt'
f = open(path)
for line in f:
    pass 

lines = [x.rstrip for x in open(path)] #removes any trailing characters e.g. spaces

#lines come out of the file wih end-of-line marker e.g. '.' ';' delimiters.
# you must close the file once it is useed releasing the resources back to the 
# operating system 
with open(path) as f:
    lines = [x.rstrip for x in f] # will automaticaly close the file once done


f = open(path)
f.read(10) #reads 10 chars
f2 = open(path, 'rb') #Binary mode 
f2.read(10) #reads 10 binary char

f.tell() #gives you the current position 

import sys 
sys.getdefaultencoding() #reutrns 'utf-8'

#seek changes the file position to the indicated bte in the file: 
f.seek(3)

f.close()
f2.close()

#==================================== Writing files =================================================
with open('tmp.txt', 'w') as handle: 
    handle.writelines(x for x in open(path) if len(x) > 1 )

with open('tmp.txt') as f: 
    lines = f.readlines() #lines is a list with each string of the list representing a line of tmp.txt 
                          #which was wrtten from test.
                
                
