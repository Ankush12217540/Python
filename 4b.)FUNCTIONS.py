# def keyword
def name_of_function(arg1,arg2):
    '''
    This is where the function's Document String (docstring) goes.
    When you call help() on your function it will be printed out.
    '''
    #  Do stuff here 
    # Return stuff here
    

# Simple example of a function
def say_hello():
    print('hello')
    
# Calling a function with()
say_hello()
    



#Accepting parameter(arguments)
# lets write a function that greets people with their name.
def greeting(name):
    print(f'Hello {name}')
greeting('Ankush')

#  using return 
# example addition function
def add_num(num1, num2):
    return num1+num2
print(add_num(4,5))
# can also save as variable due to return
result=add_num(6,5)
print(result)
# what's happen when we input two strinfg?
st=add_num('one','two')
print(st)

# what is difference between return and print?
''' The return keyword allows you to actually
save the result of the output of a function as 
a variable. The print() function simply displays 
the output to you, but doesn't save it for future
use. Let's explore this in more detail'''

def print_result(a,b):
    print(a+b)
    
def return_result(a,b):
    return a+b

print_result(10,5)

# you won't see any output if you run this in a .py script
x=return_result(19,3)
#Now you will see output
print(x)
# But what happens if we actulally want to save this result for later use ?
my_result=print_result(20,39)
print(type(my_result))
print(type(x))

'''The return keyword allows you to actually save the
result of the output of a function as a variable.
The print() function simply displays the output to 
you, but doesn't save it 
for future use. Let's explore this in more detail
'''
my_result=return_result(20,20)
print(my_result)
print(my_result+my_result)