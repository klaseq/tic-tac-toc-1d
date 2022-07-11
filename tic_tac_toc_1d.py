from random import randrange

def evalaute(field):
    if 'xxx' in field:
        return 'x'
    elif 'ooo' in field:
        return 'o'
    elif '-' not in field:
        return '!'
    else:
        return '-'

def move(field, position, symbol):
    return field[:position] + symbol + field[position + 1:]

def player_move(play_field):
    while True:
        position_number = int(input('witch field do you want to play? (from 0): '))
        if position_number >= 0 and position_number < len(play_field) and play_field[position_number] == '-':
            return move(play_field, position_number, 'x')
        else:
            print('wrong field')

def computer_move(play_field):
    while True:
        position_number = randrange(len(play_field))
        if play_field[position_number] == '-':
            return move(play_field, position_number, 'o')

def tic_tac_toc():
    
    field = 20 * '-'
    
    while True:
        print(field)
        field = player_move(field)
        print(field)
        if evalaute(field) != '-':
            break
        
        field = computer_move(field)
        if evalaute(field) != '-':
            break
    
    print(field)
    if evalaute(field) == '!':
        print('draw!')
    elif evalaute(field) == 'x':
        print('you win!')
    elif evalaute(field) == 'o':
        print('you lose!')

tic_tac_toc()