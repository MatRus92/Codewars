def between(a,b):
    returned = []
    if a < b:
        for i in range(a,b + 1):
            returned.append(i)

    return returned