import random
def printMatrix():
    n=4
    mat = [[0 for x in range(n)] for y in range(n)] 
    for i in range(n):
        for j in range(n):
            mat[i][j] = random.randint(0,1)
    for i in range(n):
        for j in range(n):
            print(mat[i][j],end=' ')
        print('')
    return mat
def addrow(m):
    indexOfMaxRow = 0
    maxRow = sum(m[0])
    for row in range(1, len(m)): 
        if sum(m[row]) > maxRow:
            maxRow = sum(m[row])
            indexOfMaxRow = row
    return indexOfMaxRow
def addcol(m):
    l_col = []
    for i in range(len(m)):
        s = 0
        for j in range(len(m)):
            s = s+m[j][i]
        l_col.append(s)
    return max(l_col)
mat = printMatrix()
print(addrow(mat))
print(addcol(mat))



