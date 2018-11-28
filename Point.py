class point(object):
    def __init__(self, x=0,y=0):
        self.__x = x
        self.__y = y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setX(self,x):
        self.__x = x
    def setY(self,y):
        self.__y = y
    def distance(self,other):
        return round((abs(self.__x-other.__x)**2+abs(self.__y-other.__y)**2)**0.5,2)
    def isNearBy(self,other):
        if((abs(self.__x-other.__x)**2+abs(self.__y-other.__y)**2)**0.5) < 5:
            return True
        else:
            return False
    def __str__(self):
        return '('+str(self.__x)+','+str(self.__y)+')'
        
        