def gcd(m, n):
    if(m%n == 0):
        return n
    else:
        return gcd(n,m%n)

m = eval(input('Enter number1:'))
n = eval(input('Enter number2:'))
print('The GCD is',gcd(m,n))