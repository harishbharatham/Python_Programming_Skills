from Point import point
x1,y1,x2,y2 = eval(input('Enter two points x1, y1, x2, y2:'))
p1 = point(x1,y1)
p2 = point(x2,y2)
print('The distance between the two points is',p1.distance(p2))
if(p1.isNearBy(p2)):
    print('The two points are near each other')
else:
    print('The two points are not near each other')