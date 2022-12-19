# USEFYL OPERATORE


# Range
print(list(range(0,11)))
''' Notice how 11 is not included up to but nor including 11, just like slice notation'''
print(list(range(0,12)))

# Third parameter is step size!
# step size just means how big of a jump/ leap/step you take from starting 
#number to get to the next number.
print(list(range(0,11,2)))
print(list(range(0,101,10)))

# Enumerate  --> it is useful function to use with for loops. lets imagine the following situation
index_count=0
for letter in 'abcde':
    print("At index{} the letter is {}".format(index_count,letter))
    index_count +=1

'''Keeping track of how many loops you've gone through is so common, 
that enumerate was created so you don't need to worry about creating
and updating this index_count or loop_count variabl
'''
# Notice the tuple unpacking!
for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))


# ZIP
''' Notice the format enumerates actually raturns , let's lets take a look by
transformaing it to a list()'''
print(list(enumerate('abcde')))

# You can use the zip() finction to quickly create a list of tuples by "zipping" up together two list:
mylist1=[1,2,3,4,5]
mylist2=['a','b','c','d','e']

#This one is also a generator! we will explain this later, but for now let's transform it to list
print(list(zip(mylist1,mylist2)))

#To use the generator ,we could just use  a for loop
for item1,item2 in zip(mylist1,mylist2):
    print('For this tuple,first item was {} and second item was {}'.format(item1,item2))
    
# IN OPERATOR
''' We've already seen the 'in' keyword during the for loop, but we can use it to quickly check if an object is in a list'''
print('x' in ['x','y','z'])
# NOT IN
print('x' not in ['x','y','z'])

# MAX AND MIN==>check the minimum or maximum of a list with these functions.
mylist=[10,20,30,40,100]
print(min(mylist))
print(max(mylist))

# RANDOM
''' Python comes with a built in random library. There are a lot of functions included in this random library
so we will show you only two useful functuons for now'''

from random import shuffle
# This shuffle the list "in-place" meaning it wont return aythiing ,instead it will effect the list passed
print(shuffle(mylist))

from random import randint
# Return random integer in range [a,b], uncliding both end points
print(randint(0,100))

# INPUT
input('Enter something into this box')
