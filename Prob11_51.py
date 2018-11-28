a = input('Enter students names and scores separated by comma')
b = list(a.split(','))
mat1 = []
while b != []:
    mat1.append(b[:2])
    b = b[2:]
print(mat1)

mat1.sort(key=lambda x:x[1])

print(mat1)

