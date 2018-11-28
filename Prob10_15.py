def isSorted(lst):
    l1 = []
    l2 = list(lst)
    for i in range(0,len(lst)):
        m = min(lst)
        l1.append(m)
        lst.remove(m)
    if(l1 == l2):
        return True
    else:
        return False

l = [int(x) for x in input('Enter list:').split()]
if(isSorted(l)):
    print('The list is already sorted')
else:
    print('The list is not sorted')
