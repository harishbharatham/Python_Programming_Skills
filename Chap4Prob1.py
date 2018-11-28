a,b,c,d,e,f = eval(input('Enter a, b, c, d, e, f:'))
p = (e*d)-(b*f)
q= (a*f)-(e*c)
r = (a*d)-(b*c)
if r == 0:
    print('The equation has no solution')
else:
    print('x is '+str(round(p/r,2))+' and y is '+str(round(q/r,2)))