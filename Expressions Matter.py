def expression_matter(a, b, c):
    first = int(a) * (int(b) + int(c))
    second = int(a) * int(b) * int(c)
    third = int(a) + int(b) * int(c)
    fourth = (int(a) + int(b)) * int(c)
    five = int(a) + int(b) + int(c)

    res = first

    if second > res:
        res = second

    if third > res:
        res = third

    if fourth > res:
        res = fourth

    if five > res:
        res = five

    return res