import random


print('Enter a number to determine a range \n')
print('We will generate a number and you have to guess in less than 3 attempts\n')

range_limit = input('Lets determine the range ')

if range_limit.isdigit():
    range_limit = int(range_limit)
    if int(range_limit) == 0:
        print('range should greater than zero')
        quit()
    else:
        print('Cool! range selected is ',range_limit)
else:
    print('Enter a digit and not alphabet')
    quit()

random_number = random.randint(0, range_limit)

print(random_number)

attempt = 0

while True:
    guess = input('Guess the number ')
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Please type a number')
        continue

    attempt += 1
    if random_number == int(guess):
        print('Bingo')
        break
    elif random_number > int(guess):
        print('Random number is greater than number you have guessed')
    else:
        print('Random number is less than number you have guessed')


if attempt <= 3:
     print('You won')
     print('You completed this in',attempt, 'guesses')
else:
     print('Better luck next time')
     print('You completed this in', attempt, 'guesses')
