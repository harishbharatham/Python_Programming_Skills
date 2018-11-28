def srp(a,b):
    if((a==0 and b==1) or (a==1 and b==0)):
        return 1
    elif((a ==1 and b==2) or (a==2 and b==1)):
        return 2
    elif((a==2 and b==0) or (a==0 and b==2)):
        return 0

import random

count = 0
while(count<2):
    game = ['scissor','rock','paper']
    system = random.randint(0,2)
    user = eval(input('scissor (0), rock (1), paper (2):'))
    if(user<0 or user>2):
        print('Invalid Selection. Try again')
        continue
    elif(user == system):
        print('The computer is '+game[system]+'. You are '+game[user]+'. It is a draw.')
        continue
    c = srp(user, system)
    if(c == user):
        print('The computer is '+game[system]+'. You are '+game[user]+'. You won.')
        count=count+1
    elif(c==system):
        print('The computer is '+game[system]+'. You are '+game[user]+'. You loose.')
        count = count+1
if(count>=2):
    print('Game Over')