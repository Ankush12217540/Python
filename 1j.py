#  TEST of Topics till Taught
a=(60+(10**2)/4*7)-134.75
print(a)

print(4*(6+5))
print(4*6+5)
print(4+6*5)


#square root:
print(100*0.5)

#square
print(10**2)

#string
s='hello'
#print out 'e' using indexing
print(s[1])
#Reversing string using slicing
print(s[::-1])

'''Given string 'hello', give two
methods of producing the letter 'o' using indexing.
'''
s='hello'
#print out 'o'
#mehtod 1:
print(s[-1])
#method 2:
print(s[4])


#LIST
#Build the list[0,0,0] two seperate ways
#method 1:
print([0]*3)
#method 2:
list2=[0,0,0]
print(list2)
#Reassign 'hello' in this list to say 'goodbye' instead:
list3=[1,2,[3,4,'hello']]
print(list3)
list3[2][2]='goodbye'
print(list3)

#sort the list below:
list4=[5,3,4,6,1]

#method 1:
print(sorted(list4))
#method 2:
list4.sort()
print(list4)

#DICTIONARIES
d={'simple_key':'hello'}
#Grab 'hello'
print(d['simple_key'])

d={'k1':{'k2':'hello'}}
#grab hello
print(d['k1']['k2'])
#getting a little trickier
d={'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])


#  what is major difference between Tuples and lists
# ===>Tuoles are immutable
#how do you create tuple?
t=(1,2,3)
print(t)

# What is unique about sets?
# ==>They don't allow for duplicate items
list5=[1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

#BOOLEANS
# Answer before running cell
print(2 > 3)
# Answer before running cell
print(3 <= 2)
# Answer before running cell
print(3 == 2.0)

# Answer before running cell
print(3.0 == 3)

# Answer before running cell
print(4**0.5 != 2)




#TWO NESTED LIST
l_one=[1,2,[3,4]]
l_two=[1,2,{'k1':4}]
#True or False
l_one[2][0] >=l_two[2]['k1']