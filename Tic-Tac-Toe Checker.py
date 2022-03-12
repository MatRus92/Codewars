def is_solved(board):
    columns = [[], [], []]
    diagonals = [[],[]]

    for i in range(len(board)):
        row = board[i]

        # win row
        if all_equal(row):
            return row[0]

        diagonals[0].append(board[i][i])
        diagonals[1].append(board[::-1][i][i])

        for j in range(len(row)):
            columns[j].append(row[j])

    # win column
    for i in range(len(columns)):
        row = columns[i]
        if all_equal(row):
            return row[0]

    # win diagonal
    for i in range(len(diagonals)):
        row = diagonals[i]
        if all_equal(row):
            return row[0]

    # not yet finished
    if 0 in board[0] or 0 in board[1] or 0 in board[2]:
        return -1

    # cats game
    return 0

def all_equal(lst):
    if 0 not in lst:
        return lst[:-1] == lst[1:]

print(is_solved(
    [
        [0,1,1],
        [2,0,2],
        [2,1,0]
    ]))

print(is_solved(
    [
        [2, 0, 1],
        [2, 1, 2],
        [2, 1, 0]
    ]))
print(is_solved(
    [
        [0, 0, 1],
        [0, 1, 2],
        [2, 1, 0]
    ]))

print(is_solved(
    [
        [0, 0, 2],
        [0, 1, 2],
        [2, 1, 2]
    ]))

print(is_solved(
    [
        [1, 1, 1],
        [0, 2, 2],
        [0, 0, 0]
    ]))

print(is_solved(
    [
        [2, 1, 2],
        [2, 1, 1],
        [1, 1, 2]
    ]))

print(is_solved(
    [
        [2, 1, 2],
        [2, 1, 1],
        [1, 2, 1]
    ]))