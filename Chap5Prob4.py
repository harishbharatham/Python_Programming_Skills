num = eval(input('Enter the number of lines:'))
s= ''
for i in range(1,num+1):
    s = s+str(i)+' '
    if(i != 1):
        s = str(i)+' '+s
    print(format(s,'^50'))