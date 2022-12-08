# FILES

# myfile=open('whoops.txt') --->This will give error as this file is not present in directory

# open the 'test.txt' file
my_file=open('test.txt')
# printing the 'test.txt' file
print(my_file.read())


# This will not print the  'test.txt' file as the cursor will be at the end of the file
print(my_file.read())

# To place the cursor at the begining of the file, use below function
my_file.seek(0)

# Now the file will be printed
print(my_file.read())

# Again the cursor will be at the end of the file, so repeat the same file
print(my_file.read())
my_file.seek(0)

# same as above
print(my_file.read())
my_file.seek(0)

# To read the file line by line use the below function
print(my_file.readlines())
# To read the single line, use the readline intead of readlines in the .readlines() exesion

# It is always a good practise to cloase the file after working with it
my_file.close()



# WRITING TO A FILE

# Add a second  argument to the function,'w' which stands for write.
#  Passing 'W+' lets us read and write to the file
my_file=open('test.txt','w+')
my_file.write('This is a new line')
print(my_file.read())

#  Read the file
my_file.seek(0)
print(my_file.read())

my_file.close()    # always do this when you are done with a file
 
 
 
#   APPENDING TO A FILE
# passing the argument 'a' opens the file and puts the end,so anything written
# is appended .Like 'w+' , 'a' lets us read and write  to a file. if the file does not exist,one will be created.            # taking pointer to the intial point..
my_file=open('test.txt','a+')
my_file.write('\nThis is text being appended to test.txt')
my_file.write('\nAnd another line here.')
my_file.seek(0)
print(my_file.read())
my_file.close()  
  
for line in open('test.txt'):
    print(line)
    
    '''
    1. We could have called the ''line'' object anything
        (see example below)
    2. By not calling .read() on the line , the whole text file was not stored in memory
    3. Notice the indent on the second line for print. This whitespace is required in python
    '''
    
#  Pertaining to the first point above
for asdf in open('test.txt'):
    print(asdf)
    
