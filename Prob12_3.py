from account import account, atm

for i in range (10):
    accountlist = []
    accountlist.append(account(id1 = i))

def main1():
    print(atmSim.mainMenu())
    choiceInput = eval(input("Enter a choice:" ))
    if choiceInput == 1:
        print(atmSim.GetBalance())
        main1()
    elif choiceInput == 2:
        d = eval(input("Enter amount to withdraw: "))
        atmSim.withdraw(d)
        main1()
    elif choiceInput == 3:
        d = eval(input("Enter amount to deposit: "))
        atmSim.withdraw(d)
        main1()
    else:
        None

idInput = eval(input("Input your ID: "))
atmSim = atm(idInput)
main1()   
    