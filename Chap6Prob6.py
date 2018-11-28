#Prime number function
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True
#reverse function for palindrome
def reverse(number):
    rev = ""
    while number!=0:
        rev = rev+str(number%10)
        number= number//10
    return int(rev)
#Palindrome function
def isPalindrome(number):
    if number == reverse(number):
        return True
    else:
        return False
#main logic
mat = [[0 for x in range(10)] for y in range(10)]
prime = []
count = 0
i = 2
while count<100:
    if(isPrime(i) and isPalindrome(i)):
        prime.append(i)
        count=count+1
    i=i+1
a=0
for i in range(10):
    for j in range(10):
        mat[i][j] = prime[a]
        a=a+1
for i in range(10):
    for j in range(10):
        print(format(mat[i][j],'<10'),end=' ')
    print('')

