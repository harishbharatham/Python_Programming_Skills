save = eval(input('Enter the monthly saving amount:'))
total = 0
for i in range(6):
    total = (total+save)*(1+5/(100*12))
print('After the sixth month, the account value is',round(total,2))
