import turtle
import math
turtle.penup() 
turtle.goto(-15,225)
turtle.pensize(3)
turtle.pendown()
for x in range(-15,16):
       turtle.goto(x,math.pow(x, 2))
turtle.done()
