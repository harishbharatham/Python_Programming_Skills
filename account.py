class account():
    def __init__(self, id1=0,balance=100.0,annualInterestRate=0.0):
        self.__id = id1
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
    def getID(self):
        return self.__id
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    def setID(self,id1):
        self.__id = id1
    def setBalance(self, balance):
        self.__balance = balance
    def setAnnualInterestRate(self, anr):
        self.__annualInterestRate = anr        
    def getMonthlyInterestRate(self):
        self.__monthlyinterestrate = round(self.__annualInterestRate/(100*12),3)
        return self.__monthlyinterestrate
    def getMonthlyInterest(self):
        self.__monthlyinterestamount = round(self.__balance*self.__monthlyinterestrate,3)
        return self.__monthlyinterestamount
    def withdraw(self, withdwaramount):
        self.__balance = self.__balance-withdwaramount
    def deposit(self,depositamount):
        self.__balance = self.__balance+depositamount      
    def GetBalance(self):
        return self.__balance
    
class atm(account):
    def __init__(self, id1):
        super().__init__()
        self.__id = id
        
    def mainMenu(self):
        return "Main menu \n1: Check balance \n2: Withdraw \n3: Deposit \n4: Exit"
