 # "STATEMENT " ASSESSMENT SOLUTIONS
 
 
 
''' Q.)Use for .split(), and if you create  a Statement that will print
        out words that start with 's':   '''
#ANSWER
st= 'Print only the word that start with s in this sentence'
for word in st.split():
    if word[0]=='s':
        print(word)
 
''' Q.) Use range() to print() all the even number from 0 to 10. '''
#ANSWER:
print(list(range(0,11,2)))


'''Q.) Use list compherension to create a list of all numbers 
    beteween 1 to 50 that are divisible by 3.'''
#ANSWER:
lst=[x for x in range(1,51) if x%3==0]
print(lst)



'''Q.) Go through the string below and if the length
     of a word is even print "even!" '''
#ANNWER:
st='Print every word in this sentence that has even number of letters '
for word in st.split():
    if len(word)%2==0:
        print(word+" <--- has an even length!")
        

''' Q.) Write a program that prints the integers from 1 to 100. 
        But for multiples of three print "Fizz" instead of the number,
        and for the multiples of five print "Buzz". For numbers which
       are multiples of both three and five print "FizzBuzz"  '''
#ANSWER:
for number in list(range(1,101)):
    if (number%3==0 and number%5==0):
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)
        
'''Q.) Use a list Comprehension to create a list for the first letters
       of every word in the string'''
#ANSWER: 
st='Create a list of the first letters of every word in this string '
lst=[x[0] for x in st.split()]
print(lst)