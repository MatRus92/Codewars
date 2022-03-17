def get_real_floor(n):
    if n == 0:
        return 0
    elif n == 15:
        return 13
    elif n < 0:
        return n
    if n > 13:
        return n - 2

    return n - 1