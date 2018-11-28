'''
(Turtle: draw points, rectangles, and circles) Use the functions defined in Listing
6.14 to write a program that displays a rectangle centered at (-75, 0) with width
and height 100 and a circle centered at (50, 0) with radius 50. Fill 10 random
points inside the rectangle and 10 inside the circle, as shown in Figure 6.11c.'''
import turtle
def rectangle(center, width, height):
    turtle.penup()
    turtle.goto(center)
    turtle.penup()
    turtle.forward(width/2)
    turtle.right(90)
    turtle.forward(height/2)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    #turtle.done()

def circle(start, radius):
    turtle.penup()
    turtle.goto(start)
    turtle.pendown()
    turtle.circle(radius)
    #turtle.done()
import random

def random_rectangle():
    for i in range(1, 11):
        x = random.randint(-124, -26)
        y = random.randint(-49, 49)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pensize(2)
        turtle.dot()
    #turtle.done()
   
def random_circle():   
    count = 0      
    while count< 10:
        x = random.randint(30, 70)
        y = random.randint(-35, 25)
        if (x**2+y**2)**0.5 < 50:       
            turtle.penup()
            turtle.goto(x, y)
            turtle.pensize(2)
            turtle.dot()
            count+=1
    turtle.done()
        
rectangle((-75, 0), 100, 100)
circle((0, 0), 50)
random_rectangle()
random_circle()

    
    
    
