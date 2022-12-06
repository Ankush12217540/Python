#   There are three ways to perform string formatting.
#   1. The oldest method involves placeholder using the midulo % character
#   2. An improved technique uses the .format() string method.
#   3. The  newest method introduced with python 3.6 uses formatted string litetral , called f-string



#  FORMATTIG=NG WITH PLACEHOLDER
print("I'm going to inject %s here." %'something')
print("i'm going to inject %s text here, and %s text here."%('some','more'))
x,y='some','more'
print("I'm going to inject %s text here, and %s text here."%(x,y))

#Format conversion method : %s and %r
# %r and repr()--> delver the sting representation of the objects,including quotation marksamd character
print('He said his name was %s.' %'Fred')
print('He said his name was %r.'%'Fred')

# \t insert a tab into a sting
print('I once caught  a fish %s.'%'this \tbig')
print(' I once caught a fish %r.'%'this \tbig')


# &s and %d operatr
print('I wrote %s programs today.' %3.75)
print('I wrote %d programs today.' %3.75)


# PADDING AND PRECISION OF FLOATING POINT NUMBERS
print('Floating point numbers: %5.2f' %(3.17454))
print('Floating point numbers: %1.0f' %(13.144))
print('Floating point number: %1.5f' %(13.144))
print('Floating point numbers: %10.2f' %(13.144))

#  MULTIPLE FORMATTING
print('First: %s, Second: %5.2f,Third: %r' %('hi!', 3.1415,'bye!'))

#FORMATTING WITH THE .format() METHOD
print('This is a string with an {}'.format('insert'))

# There are several advantages of .format() over the %s placeholder method

#   1.) Inserted object can be called by index position:
print('The {2}, {1},{0}'.format('fox', 'brown','quick'))

#   2.) Inserted objects can be assigned keywords:
print('First Object: {a}, Second Object: {b}, Third Object:  {c}'.format(a=1,b='Two',c=12.3))

#    3.) Inserted object can be reused, avoiding duplication:
print('A %s saved is a %s earned.' %('penny','penny'))
# vs
print('A {p} saved is {p} earned.'.format(p='penny'))


#ALIGNMENT, PADDING AND PRECISION WITH .format()
print('{0:8} | {1:9}'.format('Fruit','Quantity'))
print('{0:8} | {1:9}'.format('Apples',3.))
print('{0:8} | {1:9}'.format('Oranges',10))

#passing optional <,^,> to set a left, center or right alignment:
print('{0:=<8} | {1:-^8}  |  {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8}  |  {2:.>8}'.format(11,22,33))

print('This is my ten-character, two-decimal number: %10.2f' %13.579)
print('This is my ten-character, two-decimal number: {0:10.2f}'.format(13.579))


# FORMATTED STRING LIETERALS (f-string)

name='Fred'
print(f"He said his name is {name}.")

# Float formatting follows "result: {value:{width}.precission}}"
num = 23.45678
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")


#If this becomes important, you can always use .format() method syntax inside an f-string:
num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:10.4f}")
