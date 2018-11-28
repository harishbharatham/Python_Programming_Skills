from Location import Location
n = eval(input('Enter the number of rows in the list:'))
a = [[i for i in eval(input('Enter a row with comma:'))] for i in range(n)]   
m = 0       
          
l = Location(n, a, 0)
print('Largest location is ', l.locateLargest(n,a))