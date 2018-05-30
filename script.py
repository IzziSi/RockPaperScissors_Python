import random
import time

options = ['rock', 'paper', 'scissors']
computer = options[random.randint(0,2)]
print(computer)


player_pick = input('Pick your option: Rock, Paper, Scissors. \n')
while player_pick != options[0] and player_pick != options[1] and player_pick != options[2]:
    player_pick = input('That is not an option, please pick: Rock, Paper, or Scissors. \n')

    
print('You chose ', player_pick, 'is this correct? \n')

confirm = input('Yes or no.\n')

if confirm != 'yes':
    player_pick = input('Pick your option: Rock, Paper, Scissors. \n')
while player_pick != options[0] and player_pick != options[1] and player_pick != options[2]:
    player_pick = input('That is not an option, please pick: Rock, Paper, or Scissors. \n')

print('You chose ' + player_pick + '. \n')

time.sleep(1)
print('Rock...')
time.sleep(3)
print('paper...')
time.sleep(3)
print('scissors...')
time.sleep(3)
print('Shoot! \n\n')
print('Computer picked ' + computer + '. You picked ' + player_pick + '.\n')

if computer == player_pick:
    print('You tied!')
elif computer == 'rock' and player_pick == 'paper':
          print('You win!')
elif computer == 'rock' and player_pick == 'scissors':
    print('You lose!')
elif computer == 'paper' and player_pick == 'rock':
    print('You lose!')
elif computer == 'paper' and player_pick == 'scissors':
    print('You win!')
elif computer == 'scissors' and player_pick == 'rock':
    print('You win!')
elif computer == 'scissors' and player_pick == 'paper':
    print('You lose!')
