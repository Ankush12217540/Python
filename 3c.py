#  WHILE LOOP:

 # simple while loop in action:
 
x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to ',x)
    x+=1
    
x=0
while x<10:
    print('x is currently :',x)
    print('x is still less than 10, adding 1 to ',x)
    x+=1
else:
    print('All Done!')
   
   
    
'''break: Breaks out of the current closest enclosing loop.
continue: Goes to the top of the closest enclosing loop.
pass: Does nothing at all. '''

x=0
while x<10:
    print('x is currently :',x)
    print('x is still less than 10, adding 1 to ',x)
    x+=1
    if x==3:
        print('x==3')
    else:
        print('continuing...')
        continue
    
#Let's put in a break once x ==3 and see if the result makes sense:
    x=0
    while x<10:
        print('x is currently: ',x)
        print('x is still less than 10, adding 1 to x')
        x+=1
        if x==3:
            print('Breaking because x==3')
            break
        else:
            print('continuing...')
            continue