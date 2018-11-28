def FindSubstring(a,b):
    if(b.find(a) != -1):
        return True
    else:
        return False
    
s1 = input('Enter the string 1:')
s2 = input('Enter the string 2:')
print(FindSubstring(s1, s2))