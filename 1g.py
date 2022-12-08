# CREATING TUPLES
t=(1,2,3)
#check len just like a list
print(len(t))
#can also mix object types
t=('one',2)
print(t)
#using indexing just like we did in list
print(t[0])
#slicing just like list
print(t[-1])

# Basic Tuples Methods
#Use .index to enter a value and return the index
print(t.index('one'))
#use .count to count the number of times a value appears
print(t.count('one'))

#IMMUTABILITY
# t[0]='change' ----> ERROR
# t.append('nope')---> ERROR

# Tuples are not often used in programming but are used when immutability 
# is necessary