import time
class Time:
        def __init__(self):
            self.__t = round(time.time())
            self.__hour =  ((self.__t//60)// 60)% 24
            self.__minute = (self.__t//60)%60
            self.__second = self.__t%60
            self.currenttime = str(self.__hour)+':'+str(self.__minute)+':'+str(self.__second)
        def GetHours(self):        
            return self.__hour
        def GetMinutes(self):
            return self.__minute
        def GetSeconds(self):
            return self.__second
        def GetTime(self):
            return self.__time 
        def setTime(self, elapseTime):
            sec = elapseTime%60
            mins = elapseTime//60
            mins = mins%60
            hrs = ((elapseTime//60)// 60)% 24
            return(str(hrs)+':'+str(mins)+':'+str(sec))