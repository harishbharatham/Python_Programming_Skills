x1,y1,x2,y2 = eval(input('Enter the endpoints of the first line segment:'))
x3,y3,x4,y4 = eval(input('Enter the endpoints of the second line segment:'))

a = y1-y2
b = x2-x1
e = x2*y1-x1*y2
c = y3-y4
d = x4-x3
f = x4*y3-x2*y4

from LinearEquation import LinearEquation

l = LinearEquation(a,b,c,d,e,f)

if l.IsSolvable():
    print('The intersection point is ', l.GetX(), l.GetY())
else:
    print('The equation has no solution')
    


