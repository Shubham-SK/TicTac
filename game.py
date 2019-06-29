from math import inf as infinity
from random import choice
import platform
import time
from os import system

user = -1
computer = +1
gameState = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


def analyze(state):
    if winner(state, computer):
        outcome = +1
    elif winner(state, user):
        outcome = -1
    else:
        outcome = 0

    return outcome


def winner(state, player):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def endgame(state):
    return winner(state, user) or winner(state, computer)


def availableSpots(state):
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def possibility(x, y):
    if [x, y] in availableSpots(gameState):
        return True
    else:
        return False


def commit(x, y, player):
    if possibility(x, y):
        gameState[x][y] = player
        return True
    else:
        return False


def minimax(state, depth, player):
    if player == computer:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or endgame(state):
        outcome = analyze(state)
        return [-1, -1, outcome]

    for cell in availableSpots(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        outcome = minimax(state, depth - 1, -player)
        state[x][y] = 0
        outcome[0], outcome[1] = x, y

        if player == computer:
            if outcome[2] > best[2]:
                best = outcome  # max value
        else:
            if outcome[2] < best[2]:
                best = outcome  # min value

    return best


def clean():
    rihjt = platform.system().lower()
    if 'windows' in rihjt:
        system('cls')
    else:
        system('clear')


def generateVisual(state, computerDecision, humanDecision):
    chars = {
        -1: humanDecision,
        +1: computerDecision,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def computerTurn(computerDecision, humanDecision):
    depth = len(availableSpots(gameState))
    if depth == 0 or endgame(gameState):
        return

    clean()
    print(f'computer turn [{computerDecision}]')
    generateVisual(gameState, computerDecision, humanDecision)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(gameState, depth, computer)
        x, y = move[0], move[1]

    commit(x, y, computer)
    time.sleep(1)


def userTurn(computerDecision, humanDecision):
    depth = len(availableSpots(gameState))
    if depth == 0 or endgame(gameState):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    clean()
    print(f'user turn [{humanDecision}]')
    generateVisual(gameState, computerDecision, humanDecision)

    while move < 1 or move > 9:
        try:
            move = int(input('Choose number in [1, 9]: '))
            coord = moves[move]
            can_move = commit(coord[0], coord[1], user)

            if not can_move:
                print('Invalid')
                move = -1
        except (EOFError, KeyBoardInterrupt):
            print('exiting')
            exit()
        except (KeyError, ValueError):
            print('Invalid')


def main():
    clean()
    humanDecision = ''  # X or O
    computerDecision = ''  # X or O
    first = ''  # if user is the first

    # user chooses X or O to play
    while humanDecision != 'O' and humanDecision != 'X':
        try:
            print('')
            humanDecision = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('exiting')
            exit()
        except (KeyError, ValueError):
            print('Invalid')

    # Setting computer's choice
    if humanDecision == 'X':
        computerDecision = 'O'
    else:
        computerDecision = 'X'

    # user may start first
    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('exiting')
            exit()
        except (KeyError, ValueError):
            print('Invalid')

    # Main loop of this game
    while len(availableSpots(gameState)) > 0 and not endgame(gameState):
        if first == 'N':
            computerTurn(computerDecision, humanDecision)
            first = ''

        userTurn(computerDecision, humanDecision)
        computerTurn(computerDecision, humanDecision)

    # Game over message
    if winner(gameState, user):
        clean()
        print(f'user turn [{humanDecision}]')
        generateVisual(gameState, computerDecision, humanDecision)
        print('win - this is a problem. I was supposed to win - :(')
    elif winner(gameState, computer):
        clean()
        print(f'computer turn [{computerDecision}]')
        generateVisual(gameState, computerDecision, humanDecision)
        print('loss')
    else:
        clean()
        generateVisual(gameState, computerDecision, humanDecision)
        print('tie')

    quit()


if __name__ == '__main__':
	main()