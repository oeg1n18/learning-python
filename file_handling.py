#================= File Handling =========================
output = open('data.txt', 'w') #Create output file('w' means write)
input = open('data.txt', 'r') #Create input file ('r' means read)
input = open('data.txt') #same as prior line 'r' is set by defualt

aString = input.read() #Read entire file into a single string
N = 5
aStreag = input.read(N) #Read up to next N characters (or bytes) into a string
aString = input.readline() #Read next line including \n line character
aList = input.readlines() #Read entire file into list of line strings with \n
output.write(aString) #write a string of characters (or bytes) into file
output.writelines(aList) #write all line strings in a list into a file
output.seek(N) #change file position to offset N for next operation
output.flush() # Flush output buffer to disk without closing


x=0
with open('data.txt', 'r') as a_file:
  for line in a_file:
    stripped_line = line.strip()
    print(stripped_line)
    
open('data.bin', 'rb') # python 2.X files (str strings)
print('line iterator')






output.close() #manual close