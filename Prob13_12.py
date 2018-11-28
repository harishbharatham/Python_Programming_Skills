from Triangle import Triangle, TriangleError
import sys
s1,s2,s3 = eval(input('Enter the three sides of a triangle:'))
t1 = Triangle(s1,s2,s3)
try:
    if((s1+s2 < s3) or (s2+s3 < s1) or (s3+s1 < s2)):
        raise TriangleError
except TriangleError:
    print('The sides do not form a triangle')
    sys.exit()
t1.setColor(input('Enter the color of the triangle:'))
t1.setFilled(bool(eval(input('Enter 1 if the triangle is to be filled else 0:'))))

print('The area of the triangle is', t1.getArea())
print('The perimeter of the triangle is', t1.getPerimeter())
print('The color of the triangle is', t1.getColor())
print('Is the triangle filled:', str(t1.isFilled()))


