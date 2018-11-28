def prefix(s1, s2):
    l1 = list(s1)
    l2 = list(s2)
    l3 = ''
    l = min(len(l1),len(l2))
    for x in range(0,l):
        if l1[x] == l2[x]:
            l3 =l3+str(l1[x])
        elif l1[x] != l2[x]:
            break
    return l3

s1 = input('Enter the string 1:')
s2 = input('Enter the string 2:')
s3 = prefix(s1, s2)       
if(s3 == ''):
    print('No Match')
else:
    print(s3)