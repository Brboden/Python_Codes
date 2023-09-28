import random

def getSecretnum(numdigits):
    numbers = list(range(10))
    random.shuffle(numbers)
    secretnum = ''
    for i in range(numdigits):
        secretnum += str(numbers[i])
    return secretnum

def getclues(guess, secretnum):
    if guess == secretnum:
        return 'You got it!'

    clue = []

    for i in range(len(guess)):
        if guess[i] == secretnum[i]:
            clue.append('Fermi')
        elif guess[i] in secretnum:
            clue.append('Pico')
    if len(clue) == 0:
        return 'Bagels'

    clue.sort()
    return ' '.join(clue)

def isOnlydigits(num):
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

def playagain():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')

NUMDIGITS = 3
MAXGUESS = 10

print('I am thinking of a %s-digit number. Try to guess what it is.' %(NUMDIGITS))
print("Here are some clues:")
print("When I say:   That means:")
print("  Pico        One digit is correct but in the wrong position.")
print("  Fermi       One digit is correct and in the right position.")
print("  Bagels      No digit is correct.")

while True:
    secretnum = getSecretnum(NUMDIGITS)
    print('I have thought up a number. You have %s guesses to get it.' %(MAXGUESS))

    numguesses = 1
    while numguesses <= MAXGUESS:
        guess = ''
        while len(guess) != NUMDIGITS or not isOnlydigits(guess):
            print('Guess #%s: ' %(numguesses))
            guess = input()

        clue = getclues(guess, secretnum)
        print(clue)
        numguesses += 1

        if guess == secretnum:
            break
        if numguesses > MAXGUESS:
            print('You ran out of guesses. The answer was %s.' %(secretnum))

    if not playagain():
        break
    











