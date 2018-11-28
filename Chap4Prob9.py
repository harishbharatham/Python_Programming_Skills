import turtle
x1,y1,r1 = eval(input('Enter circle1''s center x-, y-coordinates, and radius:'))
x2,y2,r2 = eval(input('Enter circle2''s center x-, y-coordinates, and radius:'))
d = ((x2-x1)**2+(y2-y1)**2)**0.5
s = ''
if d <=abs(r1-r2):
    if(r1 >= r2):
        s ='circle2 is inside circle1'
    else:
        s ='circle1 is inside circle2'
elif d <= (r1+r2):
    s ='circle2 overlaps circle1'
elif (d>r1+r2):
    s ='circle2 does not overlap circle1'
turtle.penup()
turtle.goto(x1,y1)
turtle.write('('+str(x1)+','+str(y1)+')',font=12)
turtle.forward(r1)
turtle.left(90)
turtle.pendown()
turtle.circle(r1)
turtle.penup()
turtle.goto(x2,y2)
turtle.write('('+str(x2)+','+str(y2)+')',font=12)
turtle.forward(r2)
turtle.left(90)
turtle.pendown()
turtle.circle(r2)
turtle.write(s,font=16)
turtle.done()

