def array_madness(a, b):
    first = 0
    second = 0

    for x in a:
        first += x ** 2

    for y in b:
        second += y ** 3

    if first > second:
        return True
    return False