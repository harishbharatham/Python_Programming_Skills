from stack import Stack
stack=Stack()
num=5
L = []
for i in range(num):
    val=(input("Enter the input:"))
    L.append(val)
L.reverse()
stack.push(L)
while not stack.isEmpty():
    print(stack.pop(),end=" ")
