# Return the reversal of an integer, e.g. reverse(456) returns # 654
def reverse(number):
    rev = ""
    while number!=0:
        rev = rev+str(number%10)
        number= number//10
    return int(rev)

# Return true if number is a palindrome
def isPalindrome(number):
    if number == reverse(number):
        return True
    else:
        return False
    
n = eval(input('Enter an integer:'))
print('The reversed number is',reverse(n))
print(isPalindrome(n))
