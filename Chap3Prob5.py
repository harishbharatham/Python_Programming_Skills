import turtle
turtle.penup()
turtle.goto(-500,0)
c = 7
for i in range(3,9):
    if i == 7:
        continue
    
    angle = 360/i
    side = 450/i
    c = c+7
    clr = "grey"+str(c)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(clr)
    for s in range(i):
        turtle.forward(side)
        turtle.left(angle)
    turtle.penup()
    turtle.end_fill()
    turtle.forward(180)
turtle.done()