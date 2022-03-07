def validSolution(board):
    rows = [[],[],[],[],[],[],[],[],[]]
    grids = [[],[],[],[],[],[],[],[],[]]
    for i in range(len(board)):
        if len(board[i]) != len(board[i]):
            return False

        iterator = 0
        for j in range(len(board[i])):
            rows[iterator].append(board[i][j])
            iterator += 1

            if i < 3:
                if j < 3:
                    grids[0].append(board[i][j])
                elif 3 <= j < 6:
                    grids[1].append(board[i][j])
                else:
                    grids[2].append(board[i][j])

            if 2 < i < 6:
                if j < 3:
                    grids[3].append(board[i][j])
                elif 3 <= j < 6:
                    grids[4].append(board[i][j])
                else:
                    grids[5].append(board[i][j])


            if 5 < i < 9:
                if j < 3:
                    grids[6].append(board[i][j])
                elif 3 <= j < 6:
                    grids[7].append(board[i][j])
                else:
                    grids[8].append(board[i][j])

    for i in rows:
        if len(i) != len(set(i)):
            return False


    for i in grids:
        if len(i) != len(set(i)):
            return False


    return True


print(validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]))

print(validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]))