def bubbleSort(data):
    IsSorted = False
    while not IsSorted:
        IsSorted = True
        for index in range((len(data) - 1)):
            if data[index] > data[index + 1]:
                IsSorted = False
                temp = data[index]
                data[index] = data[index + 1]
                data[index + 1] = temp
        
nums = [int(x) for x in input('Enter list of numbers:').split()]
bubbleSort(nums)
print(nums)