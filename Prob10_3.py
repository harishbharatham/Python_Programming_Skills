l1 = eval(input('Enter integers between 1 and 100:'))
s1 = set(l1)
for x in s1:
    count = 0
    t = 'times'
    for y in l1:
        if x==y:
            count = count+1
    if(count==1):
        t = 'time'
    print(x,'occurs',count,t)