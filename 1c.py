#singel word
a='hello'
print(a)

#Entire Phrase
a='This is also a string'
print(a)

#We can also use doubles quote
a="String built with doubles quote"
print(a)

#Be careful with doubles quote
#  a='I'm using single quote, but this wil create an error'  --->Syntax error
a="Now I'm ready to use single quotes inside a string!"
print(a)

# we can use print statement to print a string
print('Hellow world1')
print('Hellow world 2')
print('use \n to print a new line')
print('\n')
print('See what i mean?')


#stirng Basics
print(len('Hellow world'))

s='Helllow World'
print(s)
#Show first element(in this case a letter)
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])
print(s[6])
print(s[7])
print(s[8])
print(s[9])
print(s[10])
print(s[11])
print(s[12])


#Grab everything past the first term all the way to the length of which is lens(s)
print(s[1:])

#Note that there is no change to the original s
print(s)

#Grab everything UP to 3rd index
print(s[:3])

#OBSEVING: lower limit is included but upper limit is not included while indexing

#Everything
print(s[:])

#Last letter (one index behind 0 so it loops backs around)
print(s[-1])

#Grab Everything but the last letter
print(s[:-1])

#Grab everything but go in steps of 1
print(s[::1])

#Grab Everything,but go in step size of 2
print(s[::2])

#we can use this to print string backwards
print(s[::-1])

# STRING PROPERTIES

#Let's try to change the first letter to 'x'
#   s[0]='x'  ---->This will give error because we can't do, change the item assignment!
#something we can do is to concentrate the strings!
print(s)

#concntrate stings!
s=s + ' concentrate me! '
print(s)

# we can use multiplication symbol to create repetetion!
letter='z'
print(letter*10)

# BASIC BUILT IN STRING METHODS
print(s)

# Upper Case a String
print(s.upper())

#lower case
print(s.lower())

# Split a string by blank space ( this is the default)
print(s.split())

#Split by a specific element ( doesn't include the element that was split on)
print(s.split('w'))

# PRINT FORMATTING METHOD

# .format method
print('Insert another string with curly bracket:{}'.format('The inserted string'))