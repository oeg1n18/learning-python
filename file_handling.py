#================= File Handling =========================
# Data read from a file always comes back to your script as a string
# you will have to convert it to a different type of python object 
# if a string is not what you need. Python does not add any formatting
# ad does not convert objects to strings automatically when you write 
# data to a file.

## loop through each line of the file
with open('data.txt', 'r') as a_file:
  for line in a_file:
    stripped_line = line.strip()
    print(stripped_line)

output = open('data.txt', 'w') #Create output file('w' means write)
input = open('data.txt', 'r') #Create input file ('r' means read)

aString = input.read() #Read entire file into a single string
N = 1
aString = input.read(N) #Read up to next N characters (or bytes) into a string
aString = input.readline() #Read next line including \n line character
aList = input.readlines() #Read entire file into list of line strings with \n
output.write('Hello World\n'
             'Hello world\n'
             'Hello world') #write a string of characters (or bytes) into file

output.writelines(aList) #write all line strings in a list into a file
output.seek(N) #change file position to offset N for next operation
output.flush() # Flush output buffer to disk without closing

output.close() #manual close