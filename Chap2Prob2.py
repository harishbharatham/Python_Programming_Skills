n = eval(input('Enter a number between 0 and 1000:'))
sum = 0
for i in range(3):
    temp = n%10
    n = n//10
    sum = sum + temp
print('The sum of the digits is',str(sum))