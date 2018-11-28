subt,grat = eval(input('Enter the subtotal and a gratuity rate:'))
grat = (grat/100)*subt
subt = grat+subt
print('The gratuity is',str(round(grat,2)),'and the total is',str(round(subt,2)))
