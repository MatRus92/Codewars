def litres(time):
    return int(round_up(time * 0.5))

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier