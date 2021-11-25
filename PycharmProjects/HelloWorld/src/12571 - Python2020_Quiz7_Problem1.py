import random
seed_value = int(input())
random.seed(seed_value)
while True:
    player = input('rock, paper, scissors?\n')
    choice = random.choice(['rock','paper','scissors'])
    if player == 'quit':
        print('bye!')
        break
    elif player == 'rock':
        if choice == 'rock':
            print("I'm rock, tied!")
        elif choice == 'paper':
            print("I'm paper, you lose!")
        else:
            print("I'm scissors, you win!")
    elif player == 'paper':
        if choice == 'rock':
            print("I'm rock, you win!")
        elif choice == 'paper':
            print("I'm paper, tied!")
        else:
            print("I'm scissors, you lose!")
    elif player == 'scissors':
        if choice == 'rock':
            print("I'm rock, you lose!")
        elif choice == 'paper':
            print("I'm paper, you win!")
        else:
            print("I'm scissors, tied!")
    else:
        print('invalid!')
