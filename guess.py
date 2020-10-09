import random

database = open('database000.txt','w')
name = input('What is your name? ').title()
print('Welcome,',name)
database.write(name)
database.write('\nNumber of wins: ')
print('Please specify a and b. We\'ll generate a random number between them.')
a = input('a: ')
b = input('b: ')
num = int(random.randrange(int(a),int(b)))

def numGuess():

    guess = 5
    win = 0
    condition = True
    while condition:
        user_input = int(input("Please enter an integer: "))
        if user_input == num:
            print('Correct! You win.')
            win = win + 1
            database.write(str(win))
            answer = input('Do you want to play again? (Y/N) ')
            if answer.lower() == 'y':
                pass
                guess = 5
            elif answer.lower() == 'n':
                exit(0)
        elif user_input < num:
            print('It\'s larger!')
            guess = guess - 1
            if guess == 0:
                print('Game over.')
                database.write(str(win))
                exit(0)
            else:
                print('You have {0} more guesses.'.format(guess))

        elif user_input > num:
            print('It\'s smaller!')
            guess = guess - 1
            if guess == 0:
                print('Game over.')
                database.write(str(win))
                exit(0)
            else:
                print('You have {0} more guesses.'.format(guess))

        else:
            print('Try again!')
            guess = guess - 1
            if guess == 0:
                print('Game over.')
                database.write(str(win))
                exit(0)
            else:
                print('You have {0} more guesses.'.format(guess))



print(numGuess())

