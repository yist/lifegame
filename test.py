
'''
import time


CURSOR_UP = "\033[1A"
CLEAR = "\x1b[2K"
print("apple")
print("orange")
print("pear")
time.sleep(3)
# clears TWO lines
print(CURSOR_UP + CLEAR + CURSOR_UP + CLEAR, end="")
time.sleep(3)
print("pineapple")

def wipe_board 
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

n_row = 10
n_col = 10
board = [ [0]*n_row for i in range(n_col)]


board[4][5] = 1
board[5][5] = 1
board[5][6] = 1

plt.figure(figsize = (n_row, n_col))
sns.heatmap(board, cmap = 'viridis', vmin = 0, vmax = 1, square=True, linewidths=.5)
plt.show()
