matrix1 = [float(x) for x in input('Enter matrix1:').split()]
matrix2 = [float(x) for x in input('Enter matrix2:').split()]  

mat1 = []
while matrix1 != []:
    mat1.append(matrix1[:3])
    matrix1 = matrix1[3:]
print(mat1)
mat2 = []
while matrix2 != []:
    mat2.append(matrix2[:3])
    matrix2 = matrix2[3:]
result = [[0 for x in range(3)] for y in range(3)]

def multiplyMatrix(X, Y):
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][0]*Y[0][j] + X[i][1]*Y[1][j] + X[i][2]*Y[2][j]
    return (result)  
      
def printMatrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end =' ')
        print()

             
m3 = multiplyMatrix(mat1, mat2)

printMatrix(mat1)
print('+')
printMatrix(mat2)
print('=')
printMatrix(m3)

