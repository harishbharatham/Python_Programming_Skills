def isMarkovMatrix(m):
    for i in m:
        for j in i:
            if(j < 0):
                return False
    c = 0
    for i in range(len(m)):
        s = 0
        for j in range(len(m)):
            s = s+m[j][i]
        if(s == 1):
            c+=1
    
    if(c == len(m)):
        return True
    else:
        return False

print('Enter a 3-by-3 matrix row by row:')
m1 = [float(x) for x in input().split()]
m2 = [float(x) for x in input().split()]
m3 = [float(x) for x in input().split()]
m = [m1,m2,m3]
print(isMarkovMatrix(m))