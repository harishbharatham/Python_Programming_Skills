def sumDigits(n):
    s = 0
    while n!=0:
        s = s+n%10
        n = n//10
    return(s)

a = eval(input('Enter a number:'))
print('The sum of digits is',sumDigits(a))