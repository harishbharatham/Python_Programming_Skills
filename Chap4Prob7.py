import random
rank = random.randint(0,13)
if rank == 0:
    rank = 'A'
if rank == 11:
    rank = 'Jack'
elif rank == 12:
    rank = 'Queen'
elif rank == 13:
    rank = 'King'
    
suit = random.randint(1,4)
if suit == 1:
    suit = 'Clubs'
elif suit == 2:
    suit = 'Diamonds'
elif suit == 3:
    suit = 'Hearts'
elif suit == 4:
    suit = 'Spades'
print('The card you picked is the '+str(rank)+' of '+suit)