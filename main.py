import numpy as np

# we are going to make a 20x10 tetris game board using numpy
board_dim = (20,10)

board = np.zeros(board_dim, dtype=int)

print(board)

I_piece = np.array([[0,0,0,0], [1,1,1,1]])
J_piece = np.array([[1,0,0,0], [1,1,1,0]])
L_piece = np.array([[0,0,1,0], [1,1,1,0]])
O_piece = np.array([[0,1,1,0], [0,1,1,0]])
S_piece = np.array([[0,1,1,0], [1,1,0,0]])
T_piece = np.array([[0,1,0,0], [1,1,1,0]])
Z_piece = np.array([[1,1,0,0],[0,1,1,0]])

print(I_piece)
print(J_piece)
print(L_piece)
print(O_piece)
print(S_piece)
print(T_piece)
print(Z_piece)
