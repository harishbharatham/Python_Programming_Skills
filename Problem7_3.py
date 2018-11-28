from account import account

account1 = account(1122,20000,4.5)
account1.withdraw(2500)
account1.deposit(3000)
print(account1.GetBalance())