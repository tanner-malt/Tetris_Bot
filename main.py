import numpy as np

# we are going to make a 20x10 tetris game board using numpy
board_dim = (20,10)
board = np.zeros(board_dim, dtype=int)

# pieces
I_piece = np.array([[0,0,0,0], [1,1,1,1]])
J_piece = np.array([[1,0,0,0], [1,1,1,0]])
L_piece = np.array([[0,0,1,0], [1,1,1,0]])
O_piece = np.array([[0,1,1,0], [0,1,1,0]])
S_piece = np.array([[0,1,1,0], [1,1,0,0]])
T_piece = np.array([[0,1,0,0], [1,1,1,0]])
Z_piece = np.array([[1,1,0,0],[0,1,1,0]])
'''
print(I_piece)
print(J_piece)
print(L_piece)
print(O_piece)
print(S_piece)
print(T_piece)
print(Z_piece)
'''


def rotator(piece: np.ndarray):
    '''
    this function will take a piece and rotate it 90
    '''
    return np.rot90(piece)


def collision_check(board: np.ndarray, piece: np.ndarray, position: tuple = (0,3)):
    '''
    this function will take the board, and pieces and check for collision issues

    board: np.ndarry this is the playing board and remains constant dimension, is where we are doing the checks.
    1's mean the position is occupied, 0 means it is open.
    piece: np.ndarry this is just the type of piece in form of an array, 1 and 0 for if it is true
    position: where the piece is at current state, looks at the top left position within the board, a cordinate. 
    
    Returns True if there is overlap, else returns false
    '''

    # First we need to get the piece dimension so we know how to slice the board:
    pc_height, pc_wid = piece.shape
    row, col = position

    # we need to get the piece with respect to the board, so we slice the board such that:
    piece_to_board = board[row:row+pc_height, col: col+pc_wid]
    
    # next we do element wise matrix multiplication, since everything full is 1, if it is 1, it is occupied space.
    overlap_mask = piece_to_board * piece

    if overlap_mask.any():
        return True
    return False

collision_check(board,I_piece)