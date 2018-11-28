import turtle

def square(x,y,fill_color):
    turtle.penup()
    turtle.goto(x,y) 
    turtle.pendown()
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    for i in range(0,4):
        turtle.forward(60) 
        turtle.right(90) 
    turtle.end_fill()

color = "black" 
x = -250 
y = -250
sqsize = 60 
for i in range(0,8): 
    for j in range(0,8):
        square(x+j*sqsize,y+i*sqsize,color)
        color = 'black' if color == 'white' else 'white' 
    color = 'black' if color == 'white' else 'white' 
    
turtle.done()