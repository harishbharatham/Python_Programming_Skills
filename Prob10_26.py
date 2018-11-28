def isSorted(lst):
    l1 = []
    for i in range(0,len(lst)):
        m = min(lst)
        l1.append(m)
        lst.remove(m)
    return l1
def merge(list1, list2):
    l3 = list1+list2
    l3 = isSorted(l3)
    return l3
lst1 = [int(x) for x in input('Enter list1:').split()]
lst2 = [int(x) for x in input('Enter list2:').split()]
lst3 =merge(lst1, lst2)
print('The merged list is',end=' ')
for i in lst3:
    print(i,end=' ')