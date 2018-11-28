a = eval(input('Enter first number:'))
b = eval(input('Enter second number:'))
min1 = 0
gcd = 1
if(a > b):
    min1 = b
else:
    min1 = a

for i in range(1, min1):
    if(a%i == 0 and b%i == 0):
        gcd = i

print('The GCD of two numbers is:'+str(gcd))
