year = eval(input('Enter year: (e.g., 2008):'))
month = eval(input('Enter month: 1-12:'))
if(month == 1):
    month_of_year = 13 
    year = year-1
elif(month == 2):
    month_of_year = 14
    year = year-1
else:
    month_of_year = month
date = eval(input('Enter the day of the month: 1-31:'))
days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day = (date + (26*(month_of_year+1)//10) + year%100 + (year%100//4) + (year/100//4) + 5*(year/100))%7
print('Day of the week is ', days[int(day)])