def addMatrix(a, b):
    if(len(a) != len(b)):
        return 0
    else:
        c = [[0 for x in range(len(a))] for y in range(len(a))]
        for i in range(len(a)):
            c[i] = a[i]+b[i]
    return c
def print3x3Matrix(mat):
    c = 0
    for i in range(3):
        for j in range(3):
            print(mat[c],end=' ')
            c+=1
        print('')
       
m1 = [float(x) for x in input('Enter matrix1:').split()]
m2 = [float(x) for x in input('Enter matrix2:').split()]
m3 = addMatrix(m1, m2)
print('The matrices are added as follows:')
print3x3Matrix(m1)
print('+')
print3x3Matrix(m2)
print('=')
print3x3Matrix(m3)          