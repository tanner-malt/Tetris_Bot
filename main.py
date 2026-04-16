import numpy as np
import random 
import os
import time

# we are going to make a 20x10 tetris game board using numpy
board_dim = (20,10)

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
class piece:
    def __init__(self, piece_type: str):
        if piece_type == 'I':
            self.piece = I_piece
        elif piece_type == 'J':
            self.piece = J_piece
        elif piece_type == 'L':
            self.piece = L_piece
        elif piece_type == 'O':
            self.piece = O_piece
        elif piece_type == 'S':
            self.piece = S_piece
        elif piece_type == 'T':
            self.piece = T_piece
        elif piece_type == 'Z':
            self.piece = Z_piece
        else:
            raise ValueError('Invalid piece type')
        self.position = (0, 3)

    def rotator(self):
        '''
        this function will take a piece and rotate it 90
        '''
        return np.rot90(self.piece)
    
    def move_left(self):
        '''
        this function will take a piece and move it left by one unit
        '''
        row, col = self.position
        return (row, col-1)
    
    def move_right(self):
        '''
        this function will take a piece and move it right by one unit
        '''
        row, col = self.position
        return (row, col+1)
    
    def move_down(self):
        '''
        this function will take a piece and move it down by one unit
        '''
        row, col = self.position
        return (row+1, col)


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

    # check bounds — treat out-of-bounds as a collision
    if row + pc_height > board.shape[0] or col < 0 or col + pc_wid > board.shape[1] or row < 0:
        return True

    # we need to get the piece with respect to the board, so we slice the board such that:
    piece_to_board = board[row:row+pc_height, col: col+pc_wid]
    
    # next we do element wise matrix multiplication, since everything full is 1, if it is 1, it is occupied space.
    overlap_mask = piece_to_board * piece

    if overlap_mask.any():
        return True
    return False

def spawn_piece(board: np.ndarray):
    '''
    This function spawns a piece at 0,3, we also can check for collision here, if there is a collision, then the game is over.
    ''' 
    pieces = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']
    piece_type = random.choice(pieces)
    new_piece = piece(piece_type)
    if collision_check(board, new_piece.piece):
        print('Game Over')
        return None
    return new_piece


def advance_piece(board: np.ndarray, piece: piece):
    '''
    This function will advance the piece down by one unit, if there is a collision, then we will add the piece to the board and spawn a new piece.
    '''
    new_position = piece.move_down()
    if collision_check(board, piece.piece, new_position):
        # add the piece to the board
        row, col = piece.position
        pc_height, pc_wid = piece.piece.shape
        board[row:row+pc_height, col:col+pc_wid] += piece.piece
        # spawn a new piece
        return spawn_piece(board)
    else:
        # move the piece down
        piece.position = new_position
        return piece
    

def clear_lines(board: np.ndarray):
    '''
    This function will check for any full lines after a piece locks if there is a full line we will clear it and move the lines above down by one unit.
    '''
    full_lines = np.where(board.sum(axis=1) == board.shape[1])[0]
    if len(full_lines) == 0:
        return board, 0
    keep = np.where(board.sum(axis=1) < board.shape[1])[0]
    new_board = np.zeros_like(board)
    new_board[len(full_lines):] = board[keep]
    board[:] = new_board
    return board, len(full_lines)

def render_board(board: np.ndarray):
    '''
    This function will render the board in the terminal, we will use # for occupied space and . for empty space.
    '''
    for row in board:
        line = ''.join(['#' if cell else '.' for cell in row])
        print(line)


def main():
    board = np.zeros(board_dim, dtype=int)
    current_piece = spawn_piece(board)
    while current_piece is not None:
        os.system('cls' if os.name == 'nt' else 'clear')
        render_board(board)
        time.sleep(0.5)  # Adjust the speed of the game here
        current_piece = advance_piece(board, current_piece)
        board, lines_cleared = clear_lines(board)

main()