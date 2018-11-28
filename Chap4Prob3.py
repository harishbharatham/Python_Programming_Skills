def weekday(day):
    if(day == 0):
        return 'Sunday'
    elif(day == 1):
        return 'Monday'
    elif(day == 2):
        return 'Tuesday'
    elif(day == 3):
        return 'Wednesday'
    elif(day == 4):
        return 'Thursday'
    elif(day == 5):
        return 'Friday'
    elif(day == 6):
        return 'Saturday'

today = eval(input('Enter today''s day:'))
days = eval(input('Enter the number of days elapsed since today:'))
nextday = today+days
if(nextday > 6):
    nextday = nextday%7
print('Today is',weekday(today),'and the future day is',weekday(nextday))
