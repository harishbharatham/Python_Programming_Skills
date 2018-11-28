import random

num = random.randint(0,9)
num1 = random.randint(0,9)
num2 = random.randint(0, 9)
inputnum = eval(input("Enter a three digit number: "))
d1 = inputnum // 100
d2 = inputnum % 100
d3 = d2 // 10
d4 = d2 % 10
if (num == d1 and num1 == d3 and num2 == d4):
    award = 10000
    print("Exact Match! The award is : $"+ str(award))
elif ((num == d1 and num1 == d4 and num2 == d3) or (num == d3 and num1 == d1 and num2 == d4) or \
      (num == d3 and num1 == d4 and num2 == d1) or (num == d4 and num1 == d1 and num2 == d3) or \
      (num == d4 and num1 == d3 and num2 == d1)):
        award = 3000
        print("Digits Match! The award is : $"+ str(award))
elif (num == d1 or num1 == d1 or num2 == d1 or num == d3 or num1 == d3 or num2 == d3 or num== d4 or \
      num1 == d4 or num2 == d4):
    award = 1000
    print("Digit Match! The award is : $"+ str(award))
else:
    print("no match")