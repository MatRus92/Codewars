def digitize(n):
    li = []
    for i in str(n)[::-1]:
        li.append(int(i))

    return li