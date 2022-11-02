import random

user_score = 0
pc_score = 0

options = ['rock', 'paper', 'scissor']

while True:
    pc_pick = random.randint(0, 2)
    user_pick = input('Chose rock, paper, scissor or r,p,s / q to quit  ')
    pc_check = options[pc_pick]
    print('computer picked', pc_check, 'number is ', pc_pick)
    if user_pick.lower().strip() == 'q':
        print('Quiting the game!')
        break

    if (user_pick == 'rock' or user_pick == 'r') and options[pc_pick] == 'scissor':
        print('User won')
        user_score += 1

    elif (user_pick == 'paper' or user_pick == 'p') and options[pc_pick] == 'rock':
        print('User won')
        user_score += 1

    elif (user_pick == 'scissor' or user_pick == 's') and options[pc_pick] == 'paper':
        print('User won')
        user_score += 1

    elif user_pick == options[pc_pick]:
        print('Draw Tie!')

    else:
        print('PC won')
        pc_score += 1

if user_score > pc_score:
    print('User won', user_score, '>>> computer won', pc_score)
else:
    print('User won', user_score, '<<< computer won', pc_score)
