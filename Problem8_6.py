def countLetters(s):
    l1 = list(s)
    c = 0
    for x in l1:
        c+=1
    return c

s1 = input('Enter the string:')
print(countLetters(s1))