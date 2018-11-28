pop = 312032486
for i in range(1,6):
    pop = pop + 31536000//7
    pop = pop - 31536000//13
    pop = pop + 31536000//45
    print('In year',i,':',pop)