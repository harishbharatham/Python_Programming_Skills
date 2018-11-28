import random
a = random.randint(0,99)
b = random.randint(0,99)
c = eval(input('Enter the sum of '+str(a)+' and '+str(b)+' :'))
if(c == (a+b)):
    print('Correct')
else:
    print('Incorrect')