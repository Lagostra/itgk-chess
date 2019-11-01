from copy import deepcopy
import string

def create_board():
    return [
        ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR'],
        ['WP']*8] + \
        [['']*8]*4 \
        + [['BP']*8,
        ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],
    ]


def get_piece_symbol(piece_code):
    return {
        'WR': '♖', 'WN': '♘', 'WB': '♗', 'WQ': '♕', 'WK': '♔', 'WP': '♙',
        'BR': '♜', 'BN': '♞', 'BB': '♝', 'BQ': '♛', 'BK': '♚', 'BP': '♟',
        '': '   '
    }[piece_code]


def print_board(board):
    letters = "  " + "".join(s.ljust(3) for s in string.ascii_lowercase[:8])
    print(*letters, sep='')
    for i, row in reversed(list(enumerate(board))):
        print(str(i + 1).ljust(2) + "".join(get_piece_symbol(p).ljust(2) for p in row) + str(i + 1).rjust(2))
    print(*letters, sep='')


if __name__ == '__main__':
    board = create_board()
    print_board(board)