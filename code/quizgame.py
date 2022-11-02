'''
Get basic right
'''

print('Welcome to the quiz game!')

s = 0
playing = input('Do you want to play the game? Yes/No  ')

if playing != 'yes':
    quit()

print('Okay, lets play :)')

answer = input('What does CPU stands for? ')
if answer.lower().strip() == 'central processing unit':
    print('correct')
    s +=1
else:
    print('incorrect')

answer = input('What does RAM stands for? ')
if answer.lower().strip() == 'random access memory':
    print('correct')
    s += 1
else:
    print('incorrect')

answer = input('What does k8s stands for? ')
if answer.lower().strip() == 'kubernetes':
    print('correct')
    s += 1
else:
    print('incorrect')

answer = input('What is extension of terraform file? ')
if answer.lower().strip() == 'tf':
    print('correct')
    s += 1
else:
    print('incorrect')

print('Your quiz score is ', s,'Goodbye')
print("You got " + str((s / 4) * 100) + "%.")
