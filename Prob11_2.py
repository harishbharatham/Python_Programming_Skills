def sumMajorDiagonal(m):
    s = 0
    i = 0
    j = 0
    for x in range(len(m)):
        s = s+m[i][j]
        i+=1
        j+=1
    return round(s,2)

m1 = [float(x) for x in input('Enter a 4-by-4 matrix row for row 1:').split()]
m2 = [float(x) for x in input('Enter a 4-by-4 matrix row for row 2:').split()]
m3 = [float(x) for x in input('Enter a 4-by-4 matrix row for row 3:').split()]
m4 = [float(x) for x in input('Enter a 4-by-4 matrix row for row 4:').split()]
m = [m1,m2,m3,m4]
print('Sum of the elements in the major diagonal is',sumMajorDiagonal(m))