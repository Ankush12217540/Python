# FOR LOOPS

list1=[1,2,3,4,5,6,7,8,9,10]
for num in list1:
    print(num)
    
# MODULO
print(17%5)

# 3 remainder 1
print(10 % 3)

# 2 Remainder 4
print(18%7)

# 2 no ramainder 
print(4%2)

print('Printing only even number from the list1')
for num in list1:
    if num% 2==0:
        print(num)
        
print('We could also put else statement in there')
for num in list1:
    if num%2==0:
        print(num)
    else:
        print('Odd Number')



# Creating a For loop that sums up the list:    
# Start sum at zero
list_sum=0
for num in list1:
    list_sum=list_sum + num
print(list_sum)


# Start sum at zero:
list_sum=0
for num in list1:
    list_sum+=num
print(list_sum)


''' we have used for loops lists ,how about with string?
Remember strings are a sequence so when we iterate through 
through them we will be accessing each items in that strindg
'''
for letters in 'This is a string':
    print(letters)
    
    
# using for loop with  tuple:
tup=(1,2,3,4,5)
for t in tup:
    print(t)
    
list2=[(2,4),(6,8),(10,12)]
for tup in list2:
    print(tup)

# now unpacking!
for (t1,t2) in list2:
    print(t1)
    
# using dictionary with for loops:
d={'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)
    
# Create a dictionary view object:
d.items()
print(d)

# Dictionary Unpacking:
for k,v in d.items():
    print(k)
    print(v)
    
'''if you want to obtain a true list of keys,values or
key/value tuples, you can cast the views as a list:'''
print(list(d.keys()))

'''
Remember that dictionary are unordered, and keys values come back in arbitary order.
you can obtain a sorted list using sorted()'''
print(sorted(d.values()))