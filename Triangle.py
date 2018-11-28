from GeometricObject import GeometricObject
class Triangle(GeometricObject):
    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
    def getSide1(self):
        return self.__side1
    def setSide1(self,side1):
        self.__side1 = side1
    def getSide2(self):
        return self.__side2
    def setSide2(self,side2):
        self.__side2 = side2
    def getSide3(self):
        return self.__side3
    def setSide3(self,side3):
        self.__side3 = side3
    def getArea(self):
        p = (self.__side1+self.__side2+self.__side3)/2
        a = (p*(p-self.__side1)*(p-self.__side2)*(p-self.__side3))**0.5
        return round(a,2)
    def getPerimeter(self):
        p = (self.__side1+self.__side2+self.__side3)
        return round(p,2)
    def printTriangle(self):
        print(self.__str__()+"Triangle: side1 = "+str(self.__side1)+" side2 = "+\
              str(self.__side2) + " side3 = " + str(self.__side3))
        
class TriangleError(Exception):
    def __inti__(self):
        pass    
            
            
            