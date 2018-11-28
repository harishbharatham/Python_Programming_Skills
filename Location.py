class Location:
    def __init__(self, row, column, maxValue):
        self.row = row
        self.column = column
        self.maxValue = maxValue
        
    def locateLargest(self, n, a):
        largest = 0
        index = 0,0
        for i in range(n):
            for j in range(len(a[0])):
                if a[i][j] > largest:
                    largest = a[i][j]
                    index = i,j
        return index
    
 