n = eval(input(('Enter the number of students:')))
marks = []
x = 0
for i in range(n):
    x = eval(input('Enter the marks of student number '+str(i+1)+':'))
    marks.append(x)
max1 = max(marks)
print('first highest:',max1)
marks.remove(max1)
max1 = max(marks)
print('second highest:',max1)