
# SETTING COLOR DOT TO SET THE GAME BOARD AND TOKENS
white_dot = chr(9679)
empty_dot = chr(9675)
begin = '\x1b[1m'
end = '\x1b[39m\x1b[22m'
red = '\x1b[31m'
yellow = '\x1b[33m'
blue = '\x1b[34m'
green = '\x1b[32m'
red_dot = begin + red + chr(9679) + end
r_dash = begin + red + "\u203E" * 3 + end
r_up_dash = begin + red + '  |' + end
r_border = begin + red + "\u203E" * 2 + '|' + end
blue_dot = begin + blue + chr(9679) + end
b_dash = begin + blue + "\u203E" * 3 + end
b_up_dash = begin + blue + '|  ' + end
b_border = begin + blue + '|' + "\u203E" * 2 + end
green_dot = begin + green + chr(9679) + end
g_dash = begin + green + '___' + end
g_up_dash = begin + green + '  |' + end
g_border = begin + green + '__|' + end
yellow_dot = begin + yellow + chr(9679) + end
y_dash = begin + yellow + '___' + end
y_up_dash = begin + yellow + '|  ' + end
y_border = begin + yellow + '|__' + end
empty_red = begin + red + chr(9675) + end
empty_blue = begin + blue + chr(9675) + end
empty_green = begin + green + chr(9675) + end
empty_yellow = begin + yellow + chr(9675) + end

# FUNCTION THAT PRINTS INSTRUCTIONS
def instructions():
    '''This function displays the instructions of the game.'''
    input("\nLet's play Trouble!!!\nThe rules are the following: \n\t-All players roll the dice at the beginning of the game to decide who starts."
          "\n\t-Turns go in a clockwise directions.\n\t-You need to get a six in the dice to get your tokens out of your yard."
          "\n\t-Tokens move in a clockwise direction.\n\t-Rolling a six gives you an extra turn."
          "\n\t-If the token of an opponent lands on your token, your token will return to your yard.\n\t"
          "-You need to roll the exact number needed to enter home to send one of your tokens home."
          "\n\t-Tokens of the same color can't occupie the same spot in the game board."
          "\n\t-The first player to get all their tokens in home wins the game.\nPress enter to continue: \n")
# FUNCTION GIVES COLOR TO NUMBERS
def c_n(string):
    '''This function creates red, yellow, green, and blue one-digit numbers.'''
    if string[0] == 'y':
        num = ' ' + begin + yellow + string[1] + end + ' '
    if string[0] == 'r':
        num = ' ' + begin + red + string[1] + end + ' '
    if string[0] == 'g':
        num = ' ' + begin + green + string[1] + end + ' '
    if string[0] == 'b':
        num = ' ' + begin + blue + string[1] + end + ' '
    return num

import random

# PRINTING DICE ROLL FUNCTION
def dice_print(val):
    """This function takes a value from 1 to 6 and prints it as a dice."""
    if val == 1:
        print('_' * 11)
        print('|         |')
        print('|         |')
        print(f'|    {white_dot}    |')
        print('|         |')
        print('|         |')
        print('\u203E' * 11)
    elif val == 2:
        print('_' * 11)
        print('|         |')
        print(f'|    {white_dot}    |')
        print('|         |')
        print(f'|    {white_dot}    |')
        print('|         |')
        print('\u203E' * 11)
    elif val == 3:
        print('_' * 11)
        print(f'|    {white_dot}    |')
        print('|         |')
        print(f'|    {white_dot}    |')
        print('|         |')
        print(f'|    {white_dot}    |')
        print('\u203E' * 11)
    elif val == 4:
        print('_' * 11)
        print('|         |')
        print(f'|  {white_dot}   {white_dot}  |')
        print('|         |')
        print(f'|  {white_dot}   {white_dot}  |')
        print('|         |')
        print('\u203E' * 11)
    elif val == 5:
        print('_' * 11)
        print('|         |')
        print(f'|  {white_dot}   {white_dot}  |')
        print(f'|    {white_dot}    |')
        print(f'|  {white_dot}   {white_dot}  |')
        print('|         |')
        print('\u203E' * 11)
    elif val == 6:
        print('_' * 11)
        print(f'|  {white_dot}   {white_dot}  |')
        print('|         |')
        print(f'|  {white_dot}   {white_dot}  |')
        print('|         |')
        print(f'|  {white_dot}   {white_dot}  |')
        print('\u203E' * 11)
    print('\n')

# ROLLING DICE FUNCTION
def dice():
    '''This function generates a random number from 1 to six.'''
    value = random.randint(1,6)
    dice_print(value)
    return value

# FUNCTION THAT DETERMINES WHAT TOKEN TO MOVE
def find_token(piece):
    '''This function finds the location of a token in the current game-board.'''
    piece = c_n(piece)
    x = 0
    y = 0
    for i in range(len(table)):
        for j in range(len(table[i])):
            if mut_table[i][j] == piece:
                x = j
                y = i
    return x, y
# CHANGING X AND Y FUNCTION
def X_Y_SHIFTS(dice_val, x, y, token):
            '''This function defines where a token will move depending on its position.'''
            if x == 6 and y == 9:
                x -= 1
                y -= 1
            elif x == 5 and y == 6:
                x += 1
                y -= 1
            elif x == 8 and y == 5:
                x += 1
                y += 1
            elif x == 9 and y == 8:
                x -= 1
                y += 1
            elif (x == 6 and y == 14) or ((y == 8 or y == 7) and x == 0):
                y -= 1
            elif (y == 6 and x == 0) or ((x == 6 or x == 7) and y == 0):
                x += 1
            elif (x == 8 and y == 0) or (x == 14 and (y == 6 or y == 7)):
                y += 1
            elif (x == 14 and y == 8) or ((x == 7 or x == 8) and y == 14):
                x -= 1
            elif x == 6:
                y -= 1
            elif x == 8:
                y += 1
            elif y == 6:
                x += 1
            elif y == 8:
                x -= 1
            return x, y

# MOVING TOKENS
red_track = {' 1 ': 0, ' 2 ': 0, ' 3 ': 0, ' 4 ': 0}
def moving_red():
    '''This function controls everything related to the turn of the red player.'''
    M_value = dice()
    test = False
    if M_value != 6 and (red_track[' 1 '] == 0 or red_track[' 1 '] > 65) and (red_track[' 2 '] == 0 or red_track[' 2 '] > 65) and (red_track[' 3 '] == 0 or red_track[' 3 '] > 65) and (red_track[' 4 '] == 0 or red_track[' 4 '] > 65):
        input('All the tokens are in the yard!\nPress enter to continue: ')
        print('\n')
    elif ((M_value != 6 and red_track[' 1 '] == 0) or red_track[' 1 '] +  M_value > 57) and ((M_value != 6 and red_track[' 2 '] == 0) or red_track[' 2 '] +  M_value > 57) and ((M_value != 6 and red_track[' 3 '] == 0) or red_track[' 3 '] +  M_value > 57) and ((M_value != 6 and red_track[' 4 '] == 0) or red_track[' 4 '] +  M_value > 57):
        input("All the tokens are in the yard or they can't enter home!\nPress enter to continue: ")
        print('\n')
    else:
        while test == False:
            try:
                token = input('What token do you want to move: ')
                while (red_track[' ' + token + ' '] + M_value == red_track[' 1 '] or red_track[' ' + token + ' '] + M_value == red_track[' 2 '] or red_track[' ' + token + ' '] + M_value == red_track[' 3 '] or red_track[' ' + token + ' '] + M_value == red_track[' 4 ']) or (red_track[' ' + token + ' '] == 0 and (red_track[' 1 '] == 1 or red_track[' 2 '] == 1 or red_track[' 3 '] == 1 or red_track[' 4 '] == 1)):
                    token = input("You can't stack two of your tokens in the same spot!\nTry with a different token: ")
                while red_track[' ' + token + ' '] + M_value > 65:
                    token = input('That token has already entered home!\nTry with a different  one: ')
                while red_track[' ' + token + ' '] + M_value > 57:
                    token = input('The number in the dice has to be exactly the same as the number needed to enter home!\nTry with a different token: ')

                if M_value == 6 and red_track[' ' + token + ' '] == 0:
                    red_track[' ' + token + ' '] += 1
                    x, y = find_token('r' + token)
                    mut_table[y][x] = ' ' + empty_red + ' '
                    mut_table[13][6] = c_n('r' + token)
                elif M_value + red_track[' ' + token + ' '] == 57:
                    input('\nThe token entered home!\nPress enter to continue the game: \n')
                    x, y = find_token('r' + token)
                    mut_table[y][x] = table[y][x]
                    red_track[' ' + token + ' '] = 100
                else:
                    while M_value != 6 and red_track[' ' + token + ' '] == 0:
                        token = input('That token is on the yard!\nPick a different one: ')
                    x, y = find_token('r' + token)

                    mut_table[y][x] = table[y][x]
                    for i in range(M_value):
                        if red_track[' ' + token + ' '] < 51:
                            x, y = X_Y_SHIFTS(M_value, x, y, token)
                        else:
                            y -= 1
                        red_track[' ' + token + ' '] += 1

                    mut_table[y][x] = c_n('r' + token)
                test = True
            except:
                print('\nEnter a valid token!\n')
    if M_value == 6:
        print('Red gets a another turn!')
        s_red = True
    else:
        s_red = False
    return s_red




yellow_track = {' 1 ': 0, ' 2 ': 0, ' 3 ': 0, ' 4 ': 0}
def moving_yellow():
    '''This function controls everything related to the turn of the yellow player.'''
    M_value = dice()
    test = False
    if M_value != 6 and (yellow_track[' 1 '] == 0 or yellow_track[' 1 '] > 65) and (yellow_track[' 2 '] == 0 or yellow_track[' 2 '] > 65) and (yellow_track[' 3 '] == 0 or yellow_track[' 3 '] > 65) and (yellow_track[' 4 '] == 0 or yellow_track[' 4 '] > 65):
        input('All the tokens are in the yard!\nPress enter to continue: ')
        print('\n')
    elif ((M_value != 6 and yellow_track[' 1 '] == 0) or yellow_track[' 1 '] +  M_value > 57) and ((M_value != 6 and yellow_track[' 2 '] == 0) or yellow_track[' 2 '] +  M_value > 57) and ((M_value != 6 and yellow_track[' 3 '] == 0) or yellow_track[' 3 '] +  M_value > 57) and ((M_value != 6 and yellow_track[' 4 '] == 0) or yellow_track[' 4 '] +  M_value > 57):
        input("All the tokens are in the yard or they can't enter home!\nPress enter to continue: ")
        print('\n')
    else:
        while test == False:
            try:
                token = input('What token do you want to move: ')
                while (yellow_track[' ' + token + ' '] + M_value == yellow_track[' 1 '] or yellow_track[' ' + token + ' '] + M_value == yellow_track[' 2 '] or yellow_track[' ' + token + ' '] + M_value == yellow_track[' 3 '] or yellow_track[' ' + token + ' '] + M_value == yellow_track[' 4 ']) or (yellow_track[' ' + token + ' '] == 0 and (yellow_track[' 1 '] == 1 or yellow_track[' 2 '] == 1 or yellow_track[' 3 '] == 1 or yellow_track[' 4 '] == 1)):
                    token = input("You can't stack two of your tokens in the same spot!\nTry with a different token: ")
                while yellow_track[' ' + token + ' '] + M_value > 65:
                    token = input('That token has already entered home!\nTry with a different  one: ')
                while yellow_track[' ' + token + ' '] + M_value > 57:
                    token = input('The number in the dice has to be exactly the same as the number needed to enter home!\nTry with a different token: ')

                if M_value == 6 and yellow_track[' ' + token + ' '] == 0:
                    yellow_track[' ' + token + ' '] += 1
                    x, y = find_token('y' + token)
                    mut_table[y][x] = ' ' + empty_yellow + ' '
                    mut_table[1][8] = c_n('y' + token)
                elif M_value + yellow_track[' ' + token + ' '] == 57:
                    input('\nThe token entered home!\nPress enter to continue the game: \n')
                    x, y = find_token('y' + token)
                    mut_table[y][x] = table[y][x]
                    yellow_track[' ' + token + ' '] = 100
                else:
                    while M_value != 6 and yellow_track[' ' + token + ' '] == 0:
                        token = input('That token is on the yard!\nPick a different one: ')
                    x, y = find_token('y' + token)

                    mut_table[y][x] = table[y][x]
                    for i in range(M_value):
                        if yellow_track[' ' + token + ' '] < 51:
                            x, y = X_Y_SHIFTS(M_value, x, y, token)
                        else:
                            y += 1
                        yellow_track[' ' + token + ' '] += 1

                    mut_table[y][x] = c_n('y' + token)
                test = True
            except:
                print('\nEnter a valid token!\n')
    if M_value == 6:
        print('Yellow gets a another turn!')
        s_yellow = True
    else:
        s_yellow = False
    return s_yellow
        

blue_track = {' 1 ': 0, ' 2 ': 0, ' 3 ': 0, ' 4 ': 0}
def moving_blue():
    '''This function controls everything related to the turn of the blue player.'''
    M_value = dice()
    test = False
    if M_value != 6 and (blue_track[' 1 '] == 0 or blue_track[' 1 '] > 65) and (blue_track[' 2 '] == 0 or blue_track[' 2 '] > 65) and (blue_track[' 3 '] == 0 or blue_track[' 3 '] > 65) and (blue_track[' 4 '] == 0 or blue_track[' 4 '] > 65):
        input('All the tokens are in the yard!\nPress enter to continue: ')
        print('\n')
    elif ((M_value != 6 and blue_track[' 1 '] == 0) or blue_track[' 1 '] +  M_value > 57) and ((M_value != 6 and blue_track[' 2 '] == 0) or blue_track[' 2 '] +  M_value > 57) and ((M_value != 6 and blue_track[' 3 '] == 0) or blue_track[' 3 '] +  M_value > 57) and ((M_value != 6 and blue_track[' 4 '] == 0) or blue_track[' 4 '] +  M_value > 57):
        input("All the tokens are in the yard or they can't enter home!\nPress enter to continue: ")
        print('\n')
    else:
        while test == False:
            try:
                token = input('What token do you want to move: ')
                while (blue_track[' ' + token + ' '] + M_value == blue_track[' 1 '] or blue_track[' ' + token + ' '] + M_value == blue_track[' 2 '] or blue_track[' ' + token + ' '] + M_value == blue_track[' 3 '] or blue_track[' ' + token + ' '] + M_value == blue_track[' 4 ']) or (blue_track[' ' + token + ' '] == 0 and (blue_track[' 1 '] == 1 or blue_track[' 2 '] == 1 or blue_track[' 3 '] == 1 or blue_track[' 4 '] == 1)):
                    token = input("You can't stack two of your tokens in the same spot!\nTry with a different token: ")
                while blue_track[' ' + token + ' '] + M_value > 65:
                    token = input('That token has already entered home!\nTry with a different  one: ')
                while blue_track[' ' + token + ' '] + M_value > 57:
                    token = input('The number in the dice has to be exactly the same as the number needed to enter home!\nTry with a different token: ')

                if M_value == 6 and blue_track[' ' + token + ' '] == 0:
                    blue_track[' ' + token + ' '] += 1
                    x, y = find_token('b' + token)
                    mut_table[y][x] = ' ' + empty_blue + ' '
                    mut_table[8][13] = c_n('b' + token)
                elif M_value + blue_track[' ' + token + ' '] == 57:
                    input('\nThe token entered home!\nPress enter to continue the game: \n')
                    x, y = find_token('b' + token)
                    mut_table[y][x] = table[y][x]
                    blue_track[' ' + token + ' '] = 100
                else:
                    while M_value != 6 and blue_track[' ' + token + ' '] == 0:
                        token = input('That token is on the yard!\nPick a different one: ')
                    x, y = find_token('b' + token)

                    mut_table[y][x] = table[y][x]
                    for i in range(M_value):
                        if blue_track[' ' + token + ' '] < 51:
                            x, y = X_Y_SHIFTS(M_value, x, y, token)
                        else:
                            x -= 1
                        blue_track[' ' + token + ' '] += 1

                    mut_table[y][x] = c_n('b' + token)
                test = True
            except:
                print('\nEnter a valid token!\n')
    if M_value == 6:
        print('Blue gets a another turn!')
        s_blue = True
    else:
        s_blue = False
    return s_blue


green_track = {' 1 ': 0, ' 2 ': 0, ' 3 ': 0, ' 4 ': 0}
def moving_green():
    '''This function controls everything related to the turn of the green player.'''
    M_value = dice()
    test = False
    if M_value != 6 and (green_track[' 1 '] == 0 or green_track[' 1 '] > 65) and (green_track[' 2 '] == 0 or green_track[' 2 '] > 65) and (green_track[' 3 '] == 0 or green_track[' 3 '] > 65) and (green_track[' 4 '] == 0 or green_track[' 4 '] > 65):
        input('All the tokens are in the yard!\nPress enter to continue: ')
        print('\n')
    elif ((M_value != 6 and green_track[' 1 '] == 0) or green_track[' 1 '] +  M_value > 57) and ((M_value != 6 and green_track[' 2 '] == 0) or green_track[' 2 '] +  M_value > 57) and ((M_value != 6 and green_track[' 3 '] == 0) or green_track[' 3 '] +  M_value > 57) and ((M_value != 6 and green_track[' 4 '] == 0) or green_track[' 4 '] +  M_value > 57):
        input("All the tokens are in the yard or they can't enter home!\nPress enter to continue: ")
        print('\n')
    else:
        while test == False:
            try:
                token = input('What token do you want to move: ')
                while (green_track[' ' + token + ' '] + M_value == green_track[' 1 '] or green_track[' ' + token + ' '] + M_value == green_track[' 2 '] or green_track[' ' + token + ' '] + M_value == green_track[' 3 '] or green_track[' ' + token + ' '] + M_value == green_track[' 4 ']) or (green_track[' ' + token + ' '] == 0 and (green_track[' 1 '] == 1 or green_track[' 2 '] == 1 or green_track[' 3 '] == 1 or green_track[' 4 '] == 1)):
                    token = input("You can't stack two of your tokens in the same spot!\nTry with a different token: ")
                while green_track[' ' + token + ' '] + M_value > 65:
                    token = input('That token has already entered home!\nTry with a different  one: ')
                while green_track[' ' + token + ' '] + M_value > 57:
                    token = input('The number in the dice has to be exactly the same as the number needed to enter home!\nTry with a different token: ')

                if M_value == 6 and green_track[' ' + token + ' '] == 0:
                    green_track[' ' + token + ' '] += 1
                    x, y = find_token('g' + token)
                    mut_table[y][x] = ' ' + empty_green + ' '
                    mut_table[6][1] = c_n('g' + token)
                elif M_value + green_track[' ' + token + ' '] == 57:
                    input('\nThe token entered home!\nPress enter to continue the game: \n')
                    x, y = find_token('g' + token)
                    mut_table[y][x] = table[y][x]
                    green_track[' ' + token + ' '] = 100
                else:
                    while M_value != 6 and green_track[' ' + token + ' '] == 0:
                        token = input('That token is on the yard!\nPick a different one: ')
                    x, y = find_token('g' + token)

                    mut_table[y][x] = table[y][x]
                    for i in range(M_value):
                        if green_track[' ' + token + ' '] < 51:
                            x, y = X_Y_SHIFTS(M_value, x, y, token)
                        else:
                            x += 1
                        green_track[' ' + token + ' '] += 1

                    mut_table[y][x] = c_n('g' + token)
                test = True
            except:
                print('\nEnter a valid token!\n')
    if M_value == 6:
        print('Green gets a another turn!')
        s_green = True
    else:
        s_green = False
    return s_green

# FUNCTION THAT TAKES TOKENS BACK HOME
def dead_token():
    '''This token takes the tokens that were landed on by a token of a different color and takes them back home.'''
    gtl = [c_n('g1'), c_n('g2'), c_n('g3'), c_n('g4')]
    btl = [c_n('b1'), c_n('b2'), c_n('b3'), c_n('b4')]
    ytl = [c_n('y1'), c_n('y2'), c_n('y3'), c_n('y4')]
    rtl = [c_n('r1'), c_n('r2'), c_n('r3'), c_n('r4')]
    alive = {c_n('g1') : 0, c_n('g2') : 0, c_n('g3') : 0, c_n('g4') : 0, c_n('r1') : 0, c_n('r2') : 0, c_n('r3') : 0, c_n('r4') : 0, c_n('b1') : 0, c_n('b2') : 0, c_n('b3') : 0, c_n('b4') : 0, c_n('y1') : 0, c_n('y2') : 0, c_n('y3') : 0, c_n('y4') : 0}
    count = 0

    for i in range(len(mut_table)):
        for j in gtl:
            if j in mut_table[i]:
                alive[j] += 1

        for j in ytl:
            if j in mut_table[i]:
                alive[j] += 1

        for j in rtl:
            if j in mut_table[i]:
                alive[j] += 1

        for j in btl:
            if j in mut_table[i]:
                alive[j] += 1

    for keys in alive.keys():
        count += 1
        if alive[keys] == 0 and ((count < 5 and green_track[' ' + str(count) + ' '] < 65) or (count > 4 and count < 9 and red_track[' ' + str(count - 4) + ' '] < 65) or (count > 8 and count < 13 and blue_track[' ' + str(count - 8) + ' '] < 65) or (count > 12 and yellow_track[' ' + str(count - 12) + ' '] < 65)):
            if count < 5:
                print('\nGreen player, one of your tokens was sent to your yard!\n')
            elif count < 9:
                print('\nRed player, one of your tokens was sent to your yard!\n')
            elif count < 13:
                print('\nBlue player, one of your tokens was sent to your yard!\n')
            else:
                print('\nYellow player, one of your tokens was sent to your yard!\n')
            if keys == c_n('g1'):
                green_track[' 1 '] = 0
                mut_table[1][1] = keys
            if keys == c_n('g2'):
                green_track[' 2 '] = 0
                mut_table[1][3] = keys
            if keys == c_n('g3'):
                green_track[' 3 '] = 0
                mut_table[3][1] = keys
            if keys == c_n('g4'):
                green_track[' 4 '] = 0
                mut_table[3][3] = keys
            if keys == c_n('y1'):
                yellow_track[' 1 '] = 0
                mut_table[1][-4] = keys
            if keys == c_n('y2'):
                yellow_track[' 2 '] = 0
                mut_table[1][-2] = keys
            if keys == c_n('y3'):
                yellow_track[' 3 '] = 0
                mut_table[3][-4] = keys
            if keys == c_n('y4'):
                yellow_track[' 4 '] = 0
                mut_table[3][-2] = keys
            if keys == c_n('r1'):
                red_track[' 1 '] = 0
                mut_table[-4][1] = keys
            if keys == c_n('r2'):
                red_track[' 2 '] = 0
                mut_table[-4][3] = keys
            if keys == c_n('r3'):
                red_track[' 3 '] = 0
                mut_table[-2][1] = keys
            if keys == c_n('r4'):
                red_track[' 4 '] = 0
                mut_table[-2][3] = keys
            if keys == c_n('b1'):
                blue_track[' 1 '] = 0
                mut_table[-4][-4] = keys
            if keys == c_n('b2'):
                blue_track[' 2 '] = 0
                mut_table[-4][-2] = keys
            if keys == c_n('b3'):
                blue_track[' 3 '] = 0
                mut_table[-2][-4] = keys
            if keys == c_n('b4'):
                blue_track[' 4 '] = 0
                mut_table[-2][-2] = keys


# ORIGINAL AND MUTABLE GAME BOARD
table = [['   ', '   ', '   ', '   ', '   ', g_up_dash, ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', y_up_dash, 
          '   ', '   ', '   ', '   ', '   '], #R1
          ['   ', c_n('g1'), '   ', c_n('g2'), '   ', g_up_dash, ' ' + empty_dot + ' ', ' ' + empty_yellow + ' ', ' ' + empty_yellow + ' ', y_up_dash, 
           '   ', c_n('y1'), '   ', c_n('y2'), '   '], #R2
          ['   ', '   ', '   ', '   ', '   ', g_up_dash, ' ' + empty_dot + ' ', ' ' + empty_yellow + ' ', ' ' + empty_dot + ' ', y_up_dash, 
           '   ', '   ', '   ', '   ', '   '], #R3
          ['   ', c_n('g3'), '   ', c_n('g4'), '   ', g_up_dash, ' ' + empty_dot + ' ', ' ' + empty_yellow + ' ', ' ' + empty_dot + ' ', y_up_dash, 
           '   ', c_n('y3'), '   ', c_n('y4'), '   '], #R4
          ['   ', '   ', '   ', '   ', '   ', g_up_dash, ' ' + empty_dot + ' ', ' ' + empty_yellow + ' ', ' ' + empty_dot + ' ', y_up_dash, 
           '   ', '   ', '   ', '   ', '   '], #R5
          [g_dash, g_dash, g_dash, g_dash, g_dash, g_border, ' ' + empty_dot + ' ', ' ' + empty_yellow + ' ', ' ' + empty_dot + ' ', 
           y_border, y_dash, y_dash, y_dash, y_dash, y_dash], #R6
          [' ' + empty_dot + ' ', ' ' + empty_green + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', 
           '   ', ' ' + empty_yellow + ' ', '   ', 
           ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' '], #R7
           [' ' + empty_dot + ' ', ' ' + empty_green + ' ', ' ' + empty_green + ' ', ' ' + empty_green + ' ', ' ' + empty_green + ' ', ' ' + empty_green + ' ', 
           ' ' + empty_green + ' ', '   ', ' ' + empty_blue + ' ', 
           ' ' + empty_blue + ' ', ' ' + empty_blue + ' ', ' ' + empty_blue + ' ', ' ' + empty_blue + ' ', ' ' + empty_blue + ' ', ' ' + empty_dot + ' '], #R8
           [' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', 
           '   ', ' ' + empty_red + ' ', '   ', 
           ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_blue + ' ', ' ' + empty_dot + ' '], #R9
          [r_dash, r_dash, r_dash, r_dash, r_dash, r_border, ' ' + empty_dot + ' ', ' ' + empty_red + ' ', ' ' + empty_dot + ' ', 
           b_border, b_dash, b_dash, b_dash, b_dash, b_dash], #R10
          ['   ', '   ', '   ', '   ', '   ', r_up_dash, ' ' + empty_dot + ' ', ' ' + empty_red + ' ', ' ' + empty_dot + ' ', b_up_dash, 
           '   ', '   ', '   ', '   ', '   '], #R11
          ['   ', c_n('r1'), '   ', c_n('r2'), '   ', r_up_dash, ' ' + empty_dot + ' ', ' ' + empty_red + ' ', ' ' + empty_dot + ' ', b_up_dash, 
           '   ', c_n('b1'), '   ', c_n('b2'), '   '], #R12
          ['   ', '   ', '   ', '   ', '   ', r_up_dash, ' ' + empty_dot + ' ', ' ' + empty_red + ' ', ' ' + empty_dot + ' ', b_up_dash, 
           '   ', '   ', '   ', '   ', '   '], #R13
          ['   ', c_n('r3'), '   ', c_n('r4'), '   ', r_up_dash, ' ' + empty_red + ' ', ' ' + empty_red + ' ', ' ' + empty_dot + ' ', b_up_dash, 
           '   ', c_n('b3'), '   ', c_n('b4'), '   '], #R14
          ['   ', '   ', '   ', '   ', '   ', r_up_dash, ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', b_up_dash, 
           '   ', '   ', '   ', '   ', '   ']] #R15

mut_table = [['   ', '   ', '   ', '   ', '   ', g_up_dash, ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', y_up_dash, 
          '   ', '   ', '   ', '   ', '   '], #R1
          ['   ', c_n('g1'), '   ', c_n('g2'), '   ', g_up_dash, ' ' + empty_dot + ' ', ' ' + empty_yellow + ' ', ' ' + empty_yellow + ' ', y_up_dash, 
           '   ', c_n('y1'), '   ', c_n('y2'), '   '], #R2
          ['   ', '   ', '   ', '   ', '   ', g_up_dash, ' ' + empty_dot + ' ', ' ' + empty_yellow + ' ', ' ' + empty_dot + ' ', y_up_dash, 
           '   ', '   ', '   ', '   ', '   '], #R3
          ['   ', c_n('g3'), '   ', c_n('g4'), '   ', g_up_dash, ' ' + empty_dot + ' ', ' ' + empty_yellow + ' ', ' ' + empty_dot + ' ', y_up_dash, 
           '   ', c_n('y3'), '   ', c_n('y4'), '   '], #R4
          ['   ', '   ', '   ', '   ', '   ', g_up_dash, ' ' + empty_dot + ' ', ' ' + empty_yellow + ' ', ' ' + empty_dot + ' ', y_up_dash, 
           '   ', '   ', '   ', '   ', '   '], #R5
          [g_dash, g_dash, g_dash, g_dash, g_dash, g_border, ' ' + empty_dot + ' ', ' ' + empty_yellow + ' ', ' ' + empty_dot + ' ', 
           y_border, y_dash, y_dash, y_dash, y_dash, y_dash], #R6
          [' ' + empty_dot + ' ', ' ' + empty_green + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', 
           '   ', ' ' + empty_yellow + ' ', '   ', 
           ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' '], #R7
           [' ' + empty_dot + ' ', ' ' + empty_green + ' ', ' ' + empty_green + ' ', ' ' + empty_green + ' ', ' ' + empty_green + ' ', ' ' + empty_green + ' ', 
           ' ' + empty_green + ' ', '   ', ' ' + empty_blue + ' ', 
           ' ' + empty_blue + ' ', ' ' + empty_blue + ' ', ' ' + empty_blue + ' ', ' ' + empty_blue + ' ', ' ' + empty_blue + ' ', ' ' + empty_dot + ' '], #R8
           [' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', 
           '   ', ' ' + empty_red + ' ', '   ', 
           ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_blue + ' ', ' ' + empty_dot + ' '], #R9
          [r_dash, r_dash, r_dash, r_dash, r_dash, r_border, ' ' + empty_dot + ' ', ' ' + empty_red + ' ', ' ' + empty_dot + ' ', 
           b_border, b_dash, b_dash, b_dash, b_dash, b_dash], #R10
          ['   ', '   ', '   ', '   ', '   ', r_up_dash, ' ' + empty_dot + ' ', ' ' + empty_red + ' ', ' ' + empty_dot + ' ', b_up_dash, 
           '   ', '   ', '   ', '   ', '   '], #R11
          ['   ', c_n('r1'), '   ', c_n('r2'), '   ', r_up_dash, ' ' + empty_dot + ' ', ' ' + empty_red + ' ', ' ' + empty_dot + ' ', b_up_dash, 
           '   ', c_n('b1'), '   ', c_n('b2'), '   '], #R12
          ['   ', '   ', '   ', '   ', '   ', r_up_dash, ' ' + empty_dot + ' ', ' ' + empty_red + ' ', ' ' + empty_dot + ' ', b_up_dash, 
           '   ', '   ', '   ', '   ', '   '], #R13
          ['   ', c_n('r3'), '   ', c_n('r4'), '   ', r_up_dash, ' ' + empty_red + ' ', ' ' + empty_red + ' ', ' ' + empty_dot + ' ', b_up_dash, 
           '   ', c_n('b3'), '   ', c_n('b4'), '   '], #R14
          ['   ', '   ', '   ', '   ', '   ', r_up_dash, ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', ' ' + empty_dot + ' ', b_up_dash, 
           '   ', '   ', '   ', '   ', '   ']] #R15


def game_board(curr_table):
    '''This function takes a in a list and prints the game-board.'''
    for i in range(len(curr_table)):
        print(''.join(curr_table[i]))
    print('\n')

game_winner = False
red_turn = False
red_playing = True
yellow_turn = False
yellow_playing = True
blue_turn = False
green_turn = True
turns = True

winning_list = open('winner_list.txt', 'a')

instructions()
players = input("Let's get started!\nHow many people is going to play(2-4): ")
while players != '2' and players != '3' and players != '4':
    players = input('Enter a valid number of players: ')

if int(players) == 2:
    red_playing = False
    yellow_playing = False
elif int(players) == 3:
    yellow_playing = False

print('\nThe player that gets the highest number starts.')
input('Blue player, press enter to roll the dice: ')
b_s = dice()
input('Green player, press enter to roll the dice: ')
g_s = dice()
if b_s > g_s:
    blue_turn = True
    green_turn = False
if red_playing == True:
    input('Red player, press enter to roll the dice: ')
    r_s = dice()
    if r_s > b_s and r_s > g_s:
        red_turn = True
        blue_turn = False
        green_turn = False
if yellow_playing == True:
    input('Yellow player, press enter to roll the dice: ')
    y_s = dice()
    if y_s > r_s and y_s > g_s and y_s > b_s:
        yellow_turn = True
        red_turn = False
        blue_turn = False
        green_turn = False

while game_winner == False:
    dead_token()
    if red_turn == True:
        if red_playing == True:
            while turns == True:
                game_board(mut_table)
                print('RED TURN')
                turns = moving_red()
        turns = True
        red_turn = False
        green_turn = True
    if red_track[' 1 '] > 65 and red_track[' 2 '] > 65 and red_track[' 3 '] > 65 and red_track[' 4 '] > 65:
        print('\nRed wins!!!\n')
        winner_name = input("Type the name of the winner: ")
        winning_list.write('\nRed -', {winner_name})
        game_winner = True
    dead_token()
    if green_turn == True:
        while turns == True:
            game_board(mut_table)
            print('GREEN TURN')
            turns = moving_green()
        turns = True
        green_turn = False
        yellow_turn = True
    if green_track[' 1 '] > 65 and green_track[' 2 '] > 65 and green_track[' 3 '] > 65 and green_track[' 4 '] > 65:
        print('\nGreen wins!!!\n')
        winner_name = input("Type the name of the winner: ")
        winning_list.write('\nGreen -', {winner_name})
        game_winner = True
    dead_token()
    if yellow_turn == True:
        if yellow_playing == True:
            while turns == True:
                game_board(mut_table)
                print('YELLOW TURN')
                turns = moving_yellow()
        turns = True
        yellow_turn = False
        blue_turn = True
    if yellow_track[' 1 '] > 65 and yellow_track[' 2 '] > 65 and yellow_track[' 3 '] > 65 and yellow_track[' 4 '] > 65:
        print('\nYellow wins!!!\n')
        winner_name = input("Type the name of the winner: ")
        winning_list.write('\nYellow -', {winner_name})
        game_winner = True
    dead_token()
    if blue_turn == True:
        while turns == True:
            game_board(mut_table)
            print('BLUE TURN')
            turns = moving_blue()
        turns = True
        blue_turn = False
        red_turn = True
    if blue_track[' 1 '] > 65 and blue_track[' 2 '] > 65 and blue_track[' 3 '] > 65 and blue_track[' 4 '] > 65:
        print('\nBlue wins!!!\n')
        winner_name = input("Type the name of the winner: ")
        winning_list.write('\nBlue -',  {winner_name})
        game_winner = True
    game_board(mut_table)

    ins_display = input("If you want to see the instructions, type \"yes\": ")
    if ins_display == 'yes':
        instructions()
    exit_string = input("\nIf you don't want to keep playing, type \"no\": ")
    if exit_string == 'no':
        game_winner = True

print("The game has ended!")

winning_list.close()
#