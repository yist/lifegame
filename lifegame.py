if __name__ == '__main__':
    print('this is life game')
    rows, cols = (10, 10)
    board = []
    for row_index in range(rows):
        temp_row = []
        for col_index in range(cols):
            temp_row.append(0)
        board.append(temp_row)
   
    #print(board)
    board[5][5] = 1
    board[5][6] = 1
    board[6][6] = 1
    for row_index in range(rows):
        #print(row_index)
        for col_index in range(cols):
            print(board[row_index][col_index], end=" ")
        print('')