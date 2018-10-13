from random import randint

player = input('rock (r), paper (p), or scissors (s)?')
computer = randint(1, 3)

if computer == 1:
    choice = 'r'
elif computer == 2:
    choice = 'p'
else:
    choice = 's'

print(player, 'vs', choice)

if player == choice:
    print('DRAW')
elif player == 'r' and choice == 's':
    print('PLAYER WINS')
elif player == 'r' and choice == 'p':
    print('COMPUTER WINS')
elif player == 'p' and choice == 'r':
    print('PLAYER WINS')
elif player == 'p' and choice == 's':
    print('COMPUTER WINS')

