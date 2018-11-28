class LinearEquation:
    def __init__(self, a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def Geta(self):
        return self.__a
    def Getb(self):
        return self.__b
    def Getc(self):
        return self.__c
    def Getd(self):
        return self.__d
    def Gete(self):
        return self.__e
    def Getf(self):
        return self.__f
    def Seta(self, a):
        self.__a = a
    def Setb(self, b):
        self.__b = b
    def Setc(self, c):
        self.__c = c
    def Setd(self,d):
        self.__d = d
    def Sete(self,e):
        self.__e = e
    def Setf(self,f):
        self.__f = f    
    def IsSolvable(self):
        if(self.__a*self.__d - self.__b*self.__c != 0):
            return True
        else:
            return False
    def GetX(self):
        if(self.IsSolvable()):
            return (self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d - self.__b*self.__c)
        else:
            return('X Not solvable')
    def GetY(self):
        if(self.IsSolvable()):
            return (self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d - self.__b*self.__c)
        else:
            return('Y Not solvable')                