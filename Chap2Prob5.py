w = eval(input('Enter weight in pounds:'))
h = eval(input('Enter height in inches:'))
w = 0.45359237*w
h = 0.0254*h
bmi = w/(h*h)
print('BMI is',round(bmi,4))