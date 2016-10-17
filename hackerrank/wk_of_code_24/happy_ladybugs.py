import sys
from collections import Counter

def happy_or_not(board, visualize=False):
    c = Counter(board)
    n = len(board)
    if visualize:
        print c
    if '_' in board:
        for cell_content, freq in c.items():
            if cell_content == '_':
                continue
            if freq < 2:
                return 'NO'
        return 'YES'
    else:
        for i in range(n):
            if n>1 and (board[0] != board[1] or board[n-1] != board[n-2]):
                return 'NO'                
            elif board[i-1] != board[i] and board[i] != board[i+1]:
                return 'NO'    
        return 'YES'

