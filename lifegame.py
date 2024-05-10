def print_board(total_number_rows, total_num_cols):
    for row_index in range(total_number_rows):
        for col_index in range(total_num_cols):
            print(board[row_index][col_index], end=" ")
        print('')


def count_cells(sr, sc):
     for (sr, sc) in [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]:
            if (sr >= 0 and sc >= 0) and (sr < 10 and sc < 10):
                if board[sr][sc] == 1:
                        num_live_cells_counter = num_live_cells_counter + 1

def game_rules(r, c):
      if board[r][c] == 1:
            if num_live_cells_counter > 3 or num_live_cells_counter < 2:
                    board[r][c] = 0
            if num_live_cells_counter == 2 or num_live_cells_counter == 3:
                    board[r][c] = 1
            if board[r][c] == 0:
                if num_live_cells_counter == 3:
                    board[r][c] = 1                 
            print_board(rows, cols)

    

if __name__ == '__main__':
    print('this is life game')
    rows, cols = (10, 10)
    board = []
    for row_index in range(rows):
        temp_row = []
        for col_index in range(cols):
            temp_row.append(0)
        board.append(temp_row)

    print("time = 0")
    board[5][5] = 1
    board[5][6] = 1
    board[6][6] = 1
    print_board(rows, cols)

    print("time = 1")
    for r in range(rows):
        for c in range(cols):
            # Now we check the surrounding cells of the cell at (r, c).
            #
            # The value of the cell at position (r, c) is board[r][c].
            #
            # The surrouding cells are:
            #   board[r-1][c-1]     board[r-1][c]   board[r-1][c+1]
            #   board[r][c-1]                       board[r][c+1]
            #   board[r+1][c-1]     board[r+1][c]   board[r+1][c+1]
            # whenever valid.
            
            num_live_cells_counter = 0

            '''
            # The following works, but it is boring / inefficient.
            # 
            # Check board[r-1][c-1]
            if (r > 0 and c > 0) or (r == 0 and c == 0) or (r == 0 and c > 0) or (r > 0 and c == 0):
                if board[r-1][c-1] == 1:
                    num_live_cells_counter = num_live_cells_counter + 1
                else:
                    pass # Do nothing.

             # Check board[r-1][c]
            if r > 0:
                if board[r-1][c] == 1:
                    num_live_cells_counter = num_live_cells_counter + 1
                else:
                    pass # Do nothing.
            '''

            for (sr, sc) in [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]:
                if (sr >= 0 and sc >= 0) and (sr < 10 and sc < 10):
                    if board[sr][sc] == 1:
                        num_live_cells_counter = num_live_cells_counter + 1
                    else:
                        pass # Do nothing.
            # Apply life game rules 
            if board[r][c] == 1:
                if num_live_cells_counter > 3 or num_live_cells_counter < 2:
                    board[r][c] = 0
                if num_live_cells_counter == 2 or num_live_cells_counter == 3:
                    board[r][c] = 1
            if board[r][c] == 0:
                if num_live_cells_counter == 3:
                    board[r][c] = 1                 
            print_board(rows, cols)
