#Assign a list to an variable named my_list
my_list=[1,2,3]
print(my_list)
my_list=['A string', 23,100.232,'o']
print(len(my_list))

# Indexing and Slicing
my_list=['one','two','three',4,5]
print(my_list[0])
print(my_list[1:])
print(my_list[:3])
print(my_list + ['New Item'])
print(my_list)

# Reassign
my_list=my_list + ['add new item permanently']
print(my_list)

#make the list doubel
print(my_list*2)
#Again doubling not permanent
print(my_list)


#BASIC LIST METHODS

#Create a new list
list1=[1,2,3]

# Apped
list1.append('append me!')
print(list1)

#Pop off the 0 indexed item
list1.pop(0)
print(list1)

#Assign the popped element, -->remember default popped index is -1
popped_item=list1.pop()
print(popped_item)
print(list1)

'''It should be noted that lists indexing will 
return an error if there is no element at that index'''
 # list1[100]  ---> This will give error
 
'''we can also use the sort method and the reverse
 methods to also effects our list'''
 
 
new_list=['a','e','x','b','c']
print(new_list)


 #use reverse to reverse order(this is permanent!)
new_list.reverse()
print(new_list)

# use sort to sort the list ( in this case alphabetical order, 
# but for numbers its accending order)
new_list.sort()
print(new_list)

# NESTING LIST

# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]
# Make a list of lists to form a matrix
matrix=[lst_1,lst_2,lst_3]
print(matrix)
#Grab first item of the first in the matrix object
print(matrix[0])
 #Grab first item of the first item in the matrix object
print(matrix[0][0])



# LIST COMPREHENSIONS

# Build  a list comprehension by deconstructing a for loop within a[]
first_col=[row[0] for row in matrix]
print(first_col)