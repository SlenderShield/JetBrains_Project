import random
# Write your code here
name = input('Enter your name: ')
print('Hello,', name)
answer = {'rock': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
          'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
          'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
          'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
          'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
          'tree': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
          'wolf': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
          'sponge': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
          'paper': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
          'air': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
          'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
          'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
          'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
          'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
          'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf']}
choiced = input().split(',')
if choiced == ['']:
    choiced = ['rock', 'scissors', 'paper']
print("Okay, let's start")


def check(name):
    fils = open('rating.txt', 'r+')
    fils = [value for line in fils for value in line.strip().split()]
    if name in fils:
        rating = fils[fils.index(name) + 1]
    else:
        rating = 0
    return rating


rating = int(check(name))
while True:
    choice = input()
    if choice not in (choiced) and choice not in ('!exit', '!rating'):
        print('Invalid input')
    else:
        # print(f"Sorry, but the computer chose {choices[choice]}")
        com_choice = random.choice(choiced)
        if choice == '!exit':
            print('Bye!')
            exit()
        elif choice == '!rating':
            print(f"Your rating: {rating}")
        elif com_choice in choice:
            print(f"There is a draw ({choice})")
            rating += 50
        elif com_choice not in answer[choice]:
            print(f"Sorry, but the computer chose {com_choice}")
        else:
            print(f"Well done. The computer chose {com_choice} and failed")
            rating += 100
