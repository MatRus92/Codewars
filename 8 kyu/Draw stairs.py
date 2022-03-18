def draw_stairs(n):
    returned = ''
    for i in range(n):

        if i != n - 1:
            returned += (' ' * i) + 'I' +'\n'
        else:
            returned += (' ' * i) + 'I'

    return returned