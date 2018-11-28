n = eval(input('Enter an integer:'))
a = ""
while n!=0:
    a = a+str(n%10)
    n = n//10
print('The reversed number is',a)
