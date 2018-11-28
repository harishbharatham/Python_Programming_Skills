name = input('Enter employee\'s name:')
hours = eval(input('Enter number of hours worked in a week:'))
payrate = eval(input('Enter hourly pay rate:'))
fedtax = eval(input('Enter federal tax withholding rate:'))
statetax = eval(input('Enter state tax withholding rate:'))
gross = payrate*hours
fedamount = fedtax*gross
stateamount = statetax*gross
fedtax = fedtax*100
statetax = statetax*100

print('Employee Name:',name,'\nHours Worked:',format(hours,'<10.1f'),'\n\
Pay Rate:','$'+str(round(payrate,2)),'\nGross Pay: $'+str(gross),'\n\
Deductions:\n  Federal Withholding ('+str(fedtax)+'%): $'+str(round(fedamount,2)),'\n\
  State Withholding ('+str(statetax)+'%): $'+str(round(stateamount,2)),'\n  Total Deduction:\
 $'+str(round(fedamount+stateamount,2)),'\nNet Pay: $'+str(round(gross-fedamount-stateamount,2)))