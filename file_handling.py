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

#========================== Pandas =======================================================

#pandas is a popular library for data management 
import pandas as pd 
print(pd.__version__)
csv_path = 'file1.csv'
df=pd.read_csv(csv_path) #df stands for data frame
print('Data frame 1 (df)')
print(df.head()) # examines first 5 rows of data frame
print('\n', '\n', '\n')

#process for loading an excel file is similar
xlsx_path='file2.xls'
df2 = pd.read_excel(xlsx_path)
print ("Data frame 2 (df2)")
print(df2.head())
print('\n', '\n', '\n')

#to create a new dataframe of just a column(s)
print('Data frame 3 (df3)')
df3 = df2[['Segment', 'Gross Sales']]
print(df3.head())
print('\n', '\n', '\n')


#There are three ways to select data from a datafram in Pandas:loc, iloc, and lx
# Ioc is primarily label based; when two argumets are used, you use column headers and row 
# indexs to select the data you want. ioc can also take an integer as a row or column number 
# e.g.
print('Using ioc')
cell = df2.loc[0, 'Gross Sales'] #selected cell from row 0 col 'Gross sales' in df2
print('Data frame 2 (cell)')
print(cell)
print('\n', '\n')


#iloc is integer-based. You use column numbers and row numbers to get rows or columns at 
# particular positions in the data e.g. 
cell2 = df2.iloc[0,0]
print('cell [0][0] from df2')
print(cell2)
print('\n', '\n')


#Creating a new datafame with loc slicing. 
#you can also slice data frames and assign the values to a new data frame using column
# names. The code assigns the first three rows and all columns in between to the columns
# named Segment and Poduct. The reuslt is a new data frame Z with the corresponding values
Z = df2.loc[0:2, 'Segment':'Product']
print('sliced df2 using loc')
print(Z)
print('\n', '\n')

#Creating a new dataframe with iloc slicing
# in this example, we assign the first two rows and first three columns to the variable Z. 
# The result is a dataframe comprised of the selected rows and columns
Z = df2.iloc[0:2, 0:3]
print(Z)
print('\n', '\n')

#============================= Working with Data and Saving Data =========================
#should you have repeated values in a single column and want to know a column of the unique
#values you can use the unique() method. 
Z = df2['Segment'].unique()
print('Using .unique() to get all of the unique items in a particular column')
print(Z)
print('\n', '\n')
