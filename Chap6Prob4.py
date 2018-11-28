def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True # number is prime
count = 0
for i in range(2,10000):
    if(isPrime(i)):
        count=count+1;
print(count)