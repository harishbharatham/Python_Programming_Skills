def ValidatePassword(s):
    s.strip()
    count = 0
    l1 = list(s)
    for x in l1:
        if x.isdigit():
            count = count+1       
    if(len(s) >= 8 and s.isalnum() and count >= 2):
        return True
    else:
        return False

s = input('Enter your password:')
if(ValidatePassword(s)):
    print('Valid Password')
else:
    print('Invalid Password')