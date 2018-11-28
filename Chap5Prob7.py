s = 0
num = []
for n in range(1, 10000):
    s= 0
    for x in range(1,n):
        if n % x == 0:
            s += x
    if(s == n):
        num.append(n)
for i in num:
    print(i)