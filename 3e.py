#LIST COMPHERNSION

# grab every letter in string
lst=[x for x in 'word']
print(lst)

# Square numbers in range and turn into list
lst=[x**2 for x in range(0,11)]
print(lst)

# check for even number in a range
lst=[x for x in range(12) if x % 2==0]
print(lst)

# Convert celsius into Fahrenheit
celsius=[0,10,20,20.1,34.5]
print(celsius)
fahrenheit=[((9/5)*temp +32) for temp in celsius]
print(fahrenheit)

# Nested list compherension example
lst=[x**2 for x in [x**2 for x in range(11)]]

'''later on this course we will learn about  generator compherension
After this lecture you should feel comfortable reading and writing
basic list compherension
'''
