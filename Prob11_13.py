def locateLargest(a):
    max = 0
    r_ind = 0
    c_ind = 0
    for i in a:
        for j in i:
            if(j > max):
                max = j
                c_ind = i.index(j)
                r_ind = a.index(i)
    return r_ind,c_ind
    
        
    
n = eval(input('Enter the number of rows in the list:'))
m = []
for i in range(n):
    m1 = [float(x) for x in input('Enter a row:').split()]
    m.append(m1)
print('The location of the largest element is at',locateLargest(m))