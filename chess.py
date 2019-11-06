import string
import numpy as np


def create_board():
    return np.array([
        ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR'],
        ['WP']*8] + \
        [['']*8]*4 \
        + [['BP']*8,
        ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],
    ])


def coords_to_tile(x, y):
    assert 0 < x < 8 and 0 < y < 8, 'Invalid coordinates'
    letter = chr(x + ord('a'))
    tile = letter + str(y + 1)
    return tile


def tile_to_coords(tile):
    letter = tile[0].lower()
    x = ord(letter) - ord('a')
    y = int(tile[1]) - 1
    assert 0 <= x < 8 and 0 <= y < 8, 'Invalid tile'
    return x, y


def translate_move():
    pass


def is_legal_move(board, from_tile, to_tile):
    from_x, from_y = tile_to_coords(from_tile)
    to_x, to_y = tile_to_coords(to_tile)

    if not all(0 <= e < 8 for e in (from_x, from_y, to_x, to_y)):
        return False

    tile_value = board[from_y, from_x]
    if not tile_value:
        return False
    color, piece = tile_value

    if piece == 'R':
        if from_x == to_x:
            return np.all(board[to_y:from_y:np.sign(from_y - to_y), from_x] == '')
        elif from_y == to_y:
            return np.all(board[from_y, to_x:from_x:np.sign(from_x - to_x)] == '')
    elif piece == 'N':
        pass
    elif piece == 'B':
        pass
    elif piece == 'Q':
        pass
    elif piece == 'K':
        pass
    elif piece == 'P':
        pass
    else:
        assert False, 'Invalid piece!'
    return False


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
    board[1, 0] = ''
    print_board(board)
    print(is_legal_move(board, 'a1', 'a3'))
