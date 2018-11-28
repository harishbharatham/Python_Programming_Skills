list1 = list()
list2 = list()

def sumOfDoubleEvenPlace(num):
    summ = 0
    for i in range(1, (len(list1))):
        d = 2 * list1[i]
        if d > 9:
            t = getDigit(d)
            summ = summ + t
        else:
            summ = summ + d
        i = i + 2
    return summ

def getDigit(d):
    a = d % 10
    b = d // 10
    t = a + b
    return t

def sumOfOddPlace(num):
    summ = 0
    y = getSize(num)
    for i in range(y):
        summ = summ + list1[i]
        i = i + 2
    return summ
    
def prefixMatched(num, d):
    k = 1
    b = 0
    a = 0
    if d > 9:
        k = 2
        a = d % 10
        b = d // 10
    res = getPrefix(num, k)
    if d == res[0]:
        return True
    elif (b == res[0] and a == res[1]):
        return True
    else:
        return False
    
def getSize(num):
    d = len(str(num))
    return d
               
def getPrefix(num, k):
    x = 0
    y = getSize(num)
    if k > (y - 1):
        return num
    else:
        for i in range(k):
            list2.insert(i, list1[(y - 1) - x])
            x = x + 1
    return list2

def isValid(num):
    s = sumOfDoubleEvenPlace(num)
    s1 = sumOfOddPlace(num)
    s3 = getSize(num)
    if (s3 > 12 and s3 < 17) and ((s + s1) % 10 == 0) and (prefixMatched(num, 4) or prefixMatched(num, 5) \
                                                        or prefixMatched(num, 37) or prefixMatched(num, 6)):
        return True
    else:
        return False
    

num = eval(input("Enter Credit Card number: "))
number = num
y = getSize(num)
for i in range(y):
    if number > 0:
        list1.insert(i, number % 10)
        number = number // 10
if isValid(num):
    print("The card number is valid")
else:
    print("The card number is invalid")

