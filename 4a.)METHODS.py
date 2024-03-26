#  METHODS

# creatig a simple list
lst=[1,2,3,4,5]
print(lst)


''' The methods for a list are:
1.append;  2.count   3.extend   4.insert   5.pop   6.remove   7. reverse   8.sort
'''

# append() allows us to add element to the end of a list:
lst.append(6). 
print(lst) 

#count() --> check how many times 2 shows us in the list
# i.e, It calculate total occurence of a given element of List.
List=[1,2,3,1,2,1,2,1]
print("Total number of 2 in the the given list is: ",lst.count(2))



# insert()--> insert an element at the specified position.
'''syntax: ==> list.insert(<position, element)
 note: position mention should be  within the range of list, as 
 in this case betweem 0 and 4, elsewise throw index error'''
list=['Mathematics','Chemistry','1997',2000]
# Insert at index 2 value 10087
list.insert(2,10087)
print(list) 



# extend()==>Add content to List2 to end of List1
# syntax: List1.extend(List2)
List1=[1,2,3]
List2=[2,3,4,5]
# Add List2 to List1 now
List1.extend(List2)
print(List1)
# Add List1 to List2 now
List2.extend(List1)
print(List2)



'''sum()===>Calculates the sum of all the elements of the List. 
Syntax:  sum(List)     '''
List=[1,2,3,4,5]
print("The Sum of the list :",List,"is: ",sum(List))
# The sum is calculated only for numeric values, elsewise throws TypeError.
List=['gfg','abc',3]
#print(sum(List))===>Will throw error



# index()==> Return the index of the first occurence.
# The srart and End are not necessary parameter
# syntax: list.index(element, start, end)
List=[1,2,3,1,2,1,2,3,2,1]
print(List.index(2))
print(List.index(3,4,8))

# Min()==>Calculates minimum of all the elements of List.

#pop()--> Removes and returns the last value from the List or the given index value.
# Deletion of List Elements
''' To Delete one or more elements, i.e.
 remove an element, many built-in functions can be
 used, such as pop() & remove() and keywords such as del '''
list=[2.3,4.445, 3, 5.33, 1.054,2.50]
print(list.pop())

# del()  --> Element to be deleted is mentioned using list name index
#syntax:    del list[index]
list=[2.3, 4.445, 3, 5.33, 1.054, 2.5]
del list[0]
print(list)

# remove()--->Removes a given object from the List. 
# syntax:  list.remove(element)
list=[2.3,4.445,3,5.33,1.054,2.5]
list.ramove(3)


# max()	Calculates maximum of all the elements of List
