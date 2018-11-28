t = 10000
t4 = 0
for i in range(10):
    t = t+(0.05*t)
print('One year tuition after 10 years is',round(t,2))
t4 = t
for i in range(3):
    t = t+(0.05*t)
    t4 = t+t4
print('Four year tuition after 10 years is',round(t4,2))