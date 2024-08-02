

board =    {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
print('')

def printBoard(theBoard):
    print(f"{theBoard['top-L']} |{theBoard['top-M']}|{theBoard['top-R']}\n"
          f"--+-+--\n"
          f"{theBoard['mid-L']} |{theBoard['mid-M']}|{theBoard['mid-R']}\n"
          f"--+-+--\n"
          f"{theBoard['low-L']} |{theBoard['low-M']}|{theBoard['low-R']}\n")

turn = 'X'

for i in range(9):
    printBoard(board)
    print('Ruch gracza X, w który polu stawiasz znak?')
    move = input('')
    board[move] = turn
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'
    if board['']

printBoard(board)