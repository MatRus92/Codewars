def find_missing(sequence):
    pattern = abs(int((sequence[0] - sequence[-1]) / int(len(sequence))))

    if sequence[0] > sequence[-1]:
        pattern = -pattern


    for i in range(len(sequence)):
        if sequence[i+1] - sequence[i]  != pattern:
            if sequence[0] < 0 or sequence[-1] < 0:
                return -(-sequence[i] + -pattern)
            else:
                return sequence[i] + pattern
    return pattern

print(find_missing([1, 2, 3, 4, 6, 7, 8, 9]))
print(find_missing([1, 3, 4, 5, 6, 7, 8, 9]))
print(find_missing([1, 3, 5, 9, 11]))
print(find_missing([1, -2, -5, -8, -11, -17, -20, -23, -26]))