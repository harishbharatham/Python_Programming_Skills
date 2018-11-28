def mean(x):
    return round((sum(x)/len(x)),2)
def deviation(x):
    m = mean(x)
    sd = 0
    l = len(x)-1
    for i in x:
        sd = sd+(i-m)**2
    sd = (sd/l)**0.5
    return round(sd,5)
l1 = [float(x) for x in input('Enter numbers:').split()]
l1 = list(l1)
print(mean(l1))
print(deviation(l1))