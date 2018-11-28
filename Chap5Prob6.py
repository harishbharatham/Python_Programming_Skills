y = eval(input('Enter the year:'))
leap = ''
if(y%400 == 0 or y%4 == 0):
    leap = 'leap'
nextday = eval(input('Enter the day(Sunday:0, Monday:1.. :'))
out = ''
def GetWeekday(day):
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

days = [0,31,28,31,30,31,30,31,31,30,31,30]
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
m = 0
for i in days:
    if(i==28 and leap == 'leap'):
        i = i+1
    nextday = nextday+i
    if(nextday > 6):
        nextday = nextday%7
    out = months[m]+' 1, '+str(y)+' is '+GetWeekday(nextday)
    print(out)
    m = m+1   
        
