from LinearEquation import LinearEquation

a,b,c,d,e,f = eval(input('Enter a,b,c,d,e,f:'))
eq1 = LinearEquation(a,b,c,d,e,f)
print('Equation Solvable:',eq1.IsSolvable())
print('Solution of X is:',eq1.GetX())
print('Solution of Y is:',eq1.GetY())