import random

choices = ['rock', 'paper', 'scissors']

while True:
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input('rock, paper or scissors ?: ')
        player = player.lower()


    def show_result():
        if player == computer:
            print('Player - ',player)
            print('Computer - ',computer)
            print('Tie!')
        elif player == 'rock':
            if computer == 'paper':
                print('Player - ',player)
                print('Computer - ',computer)
                print('You lose!')
            else:
                print('Player - ',player)
                print('Computer - ',computer)
                print('You Win!')
        elif player == 'paper':
            if computer == 'scissors':
                print('Player - ',player)
                print('Computer - ',computer)
                print('You lose!')
            else:
                print('Player - ',player)
                print('Computer - ',computer)
                print('You Win!')
        elif player == 'scissors':
            if computer == 'rock':
                print('Player - ',player)
                print('Computer - ',computer)
                print('You lose!')
            else:
                print('Player - ',player)
                print('Computer - ',computer)
                print('You Win!')
    show_result()
    play_again = input("Want to play again ? (yes or no): ")
    play_again = play_again.lower() 
    if play_again!= 'yes':
        break

print('Byeeeeeeeeee!')