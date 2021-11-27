import random
while True:
    vibor = ['paper', 'rock', 'scissors']

    computer = random.choice(vibor)
    player = None

    while player not in vibor:

        player = input('select you position ( paper, rock, scissors ): ').lower()

    if player == computer:

        print('computer: '+computer)
        print('player: '+player)
        print('Nichya')
    elif player == 'rock':
       if computer == 'paper':
           print('computer: '+ computer)
           print('player: ' + player)
           print('You loose!')
       if computer == 'scissors':
           print('computer: '+ computer)
           print('player: ' + player)
           print('You win!')
    elif player == 'scissors':
       if computer == 'paper':
           print('computer: '+ computer)
           print('player: ' + player)
           print('You win!')
       if computer == 'rock':
           print('computer: '+ computer)
           print('player: ' + player)
           print('You loose!')
    elif player == 'paper':
       if computer == 'rock':
           print('computer: '+ computer)
           print('player: ' + player)
           print('You win!')
       if computer == 'scissors':
           print('computer: '+ computer)
           print('player: ' + player)
           print('You loose!')


    play_again = input('New katka (Yes/No): ').lower()

    if play_again !='yes':
        break
print('buy, buy')

