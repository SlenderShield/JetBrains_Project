import random


def replace(let, enc):
    global word
    enc = list(enc)
    i = 0
    while i < len(word):
        if word[i] == let:
            enc[i] = let
        i += 1
    return ''.join(enc)


print('H A N G M A N')
menu = input('Type "play" to play the game, "exit" to quit:')
if menu == 'quit':
    exit()
words = ('python', 'java', 'kotlin', 'javascript')
word = random.choice(words)
encrypted = len(word) * '-'
history = set({})
attempts = 0
win = False
while attempts < 8:
    print('\n' + encrypted)
    if word == encrypted:
        win = True
    letter = input('Input a letter:')
    if len(letter) > 1:
        print('You should input a single letter')
    elif not letter.islower():
        print('It is not an ASCII lowercase letter')
    elif letter in history:
        print('You already typed this letter')
    elif letter not in word:
        print('No such letter in the word')
        attempts += 1

    else:
        encrypted = replace(letter, encrypted)
    history.add(letter)

if win:
    print('You survived!')
else:
    print('You are hanged!')