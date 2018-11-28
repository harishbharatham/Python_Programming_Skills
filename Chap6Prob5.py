import random
def printMatrix(n):
    mat = [[0 for x in range(n)] for y in range(n)] 
    for i in range(n):
        for j in range(n):
            mat[i][j] = random.randint(0,1)
    for i in range(n):
        for j in range(n):
            print(mat[i][j],end=' ')
        print('')
        
printMatrix(eval(input('Enter n:')))

