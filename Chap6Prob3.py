def displaySortedNumbers(num1, num2, num3):
    n = [num1,num2,num3]
    m1 = max(n)
    sort1=[]
    sort1.append(m1)
    n.remove(m1)
    m1 = max(n)
    sort1.append(m1)
    n.remove(m1)
    sort1.append(n[0])
    return sort1

a,b,c = eval(input('Enter three numbers:'))
for i in displaySortedNumbers(a, b, c):
    print(i)