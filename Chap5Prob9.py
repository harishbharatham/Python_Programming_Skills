import turtle
import math
turtle.penup() 
turtle.goto(-300,0)
turtle.pensize(3)
turtle.color("blue")
turtle.pendown()
for x in range(-300,301):
       turtle.goto(x,50*math.sin((x/100)*2*math.pi))
turtle.penup()
turtle.goto(-300,0)
turtle.color("red")
turtle.pendown()
for x in range(-300,301):
       turtle.goto(x,50*math.cos((x/100)*2*math.pi))
       
turtle.done()
