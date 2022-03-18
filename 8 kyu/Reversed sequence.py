def reverse_seq(n):
    ret = []

    for i in range(n + 1):
        if i > 0:
            ret.append(i)

    return ret[::-1]