# CONSTRUCTING A DICTONARY

# Make a dictonary with {} and : to signify a key and a value
my_dict={'key':'value1','key2':'value2'}

#Call values by their key
print(my_dict['key2'])
my_dict={'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
print(my_dict['key3'])
#can call an index on that value
print(my_dict['key3'][0])
#we  affect the value of a keys as well. for instances
my_dict['key1']=my_dict['key1']-123
print(my_dict['key1'])
print(my_dict)
# Set the object equal to itself minus 123
my_dict['key1'] -=123
print(my_dict['key1'])

#creating a new dictonary
d={}
#creating a new ket through assignment
d['animal']='Dog'
d['answer']=42
print(d)

#NESTING WITH DICTONARIES
# Dictonaries nested inside a dictonary nested inside a dictonary
d={'key1':{'nestkey':{'subnestkey':'value'}}}
#keep calling keys
print(d['key1']['nestkey']['subnestkey'])

#A few Dictionary Methods
#create a typical dictionary
d={'key1':1,'key2':2,'key3':3}
#method to return a list of all keys 
print(d.keys())
print(d.values())
#method to return tuples of all items (we'll learn abot=ut tuples soon)
print(d.items())